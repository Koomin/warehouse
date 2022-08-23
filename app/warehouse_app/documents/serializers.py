from rest_framework import serializers

from documents.models import DocumentType, DocumentGroup, Document, DocumentItem


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'optima_id', 'optima_class', 'details_id', 'short_name', 'name', 'numbering', 'type_id',
                  'is_active']


class DocumentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentGroup
        fields = ['id', 'optima_id', 'document_type', 'name', ]


class DocumentSerializer(serializers.ModelSerializer):
    document_type = serializers.CharField(source='document_type.short_name')
    document_type_id = serializers.IntegerField(source='document_type.id')
    destination_store = serializers.CharField(source='destination_store.short_name', allow_null=True, required=False)
    destination_store_id = serializers.IntegerField(source='destination_store.id', allow_null=True, required=False)
    source_store = serializers.CharField(source='source_store.short_name', allow_null=True, required=False)
    source_store_id = serializers.IntegerField(source='source_store.id', allow_null=True, required=False)

    class Meta:
        model = Document
        fields = ['id', 'optima_id', 'document_type', 'document_type_id', 'optima_full_number', 'value_net',
                  'value_gross', 'source_store', 'source_store_id', 'destination_store', 'destination_store_id',
                  'document_group', 'exported', ]


class DocumentItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    product_id = serializers.IntegerField(source='product.id')

    class Meta:
        model = DocumentItem
        fields = ['id', 'optima_id', 'document', 'product', 'product_id', 'quantity', 'net_price', 'gross_price',]
