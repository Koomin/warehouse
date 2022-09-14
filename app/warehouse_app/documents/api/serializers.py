from rest_framework import serializers

from documents.models import DocumentType, DocumentGroup, Document, DocumentItem
from products.models import Product
from stores.models import Store


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['uuid', 'optima_id', 'optima_class', 'details_id', 'short_name', 'name', 'numbering', 'type_id',
                  'is_active']


class DocumentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentGroup
        fields = ['uuid', 'optima_id', 'document_type', 'name', ]


class DocumentSerializer(serializers.ModelSerializer):
    document_type = serializers.SlugRelatedField(slug_field='uuid', queryset=DocumentType.objects.all(), required=False)
    document_type_name = serializers.CharField(source='document_type.short_name', allow_null=True, required=False)
    destination_store = serializers.SlugRelatedField(slug_field='uuid', queryset=Store.objects.all(), required=True)
    destination_store_name = serializers.CharField(source='destination_store.short_name', allow_null=True,
                                                   required=False)
    source_store_name = serializers.CharField(source='source_store.short_name', allow_null=True, required=False)
    source_store = serializers.SlugRelatedField(slug_field='uuid', queryset=Store.objects.all())
    document_group_name = serializers.CharField(source='document_group.name', required=False)
    document_group = serializers.SlugRelatedField(slug_field='uuid', queryset=DocumentGroup.objects.all(),
                                                  allow_null=True, required=False)
    document_date = serializers.DateTimeField(format='%d-%m-%Y', required=False)
    document_creation_date = serializers.DateTimeField(format='%d-%m-%Y', required=False)

    class Meta:
        model = Document
        fields = ['uuid', 'optima_id', 'document_type', 'document_type_name', 'optima_full_number', 'value_net',
                  'value_gross', 'source_store', 'source_store_name', 'destination_store', 'destination_store_name',
                  'document_group', 'document_group_name', 'exported', 'document_date', 'document_creation_date']


class DocumentItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_value = serializers.DecimalField(source='product.value', max_digits=12, decimal_places=2, read_only=True)
    product_retail_value = serializers.DecimalField(source='product.retail_value', max_digits=12, decimal_places=2,
                                                    read_only=True)
    product_unit = serializers.CharField(source='product.unit.short_name', required=False, read_only=True)
    product = serializers.SlugRelatedField(slug_field='uuid', queryset=Product.objects.all())
    document = serializers.SlugRelatedField(slug_field='uuid', queryset=Document.objects.all())

    class Meta:
        model = DocumentItem
        fields = ['uuid', 'optima_id', 'document', 'product', 'product_name', 'product_value', 'product_retail_value',
                  'product_unit', 'quantity', 'net_price', 'gross_price']
