from rest_framework import serializers

from documents.models import DocumentType, DocumentGroup, Document, DocumentItem


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
    document_type = serializers.CharField(source='document_type.short_name')
    document_type_uuid = serializers.IntegerField(source='document_type.uuid')
    destination_store = serializers.CharField(source='destination_store.short_name', allow_null=True, required=False)
    destination_store_uuid = serializers.IntegerField(source='destination_store.uuid', allow_null=True, required=False)
    source_store = serializers.CharField(source='source_store.short_name', allow_null=True, required=False)
    source_store_uuid = serializers.IntegerField(source='source_store.uuid', allow_null=True, required=False)
    document_group = serializers.CharField(source='document_group.name', required=False)
    document_group_uuid = serializers.IntegerField(source='document_group.uuid', required=False)

    class Meta:
        model = Document
        fields = ['uuid', 'optima_id', 'document_type', 'document_type_uuid', 'optima_full_number', 'value_net',
                  'value_gross', 'source_store', 'source_store_uuid', 'destination_store', 'destination_store_uuid',
                  'document_group', 'document_group_uuid', 'exported', ]


class DocumentItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    product_uuid = serializers.IntegerField(source='product.uuid')
    product_value = serializers.DecimalField(source='product.value', max_digits=12, decimal_places=2)
    product_retail_value = serializers.DecimalField(source='product.retail_value', max_digits=12, decimal_places=2)
    product_unit = serializers.CharField(source='product.unit.short_name', required=False)

    class Meta:
        model = DocumentItem
        fields = ['uuid', 'optima_id', 'document', 'product', 'product_uuid', 'product_value', 'product_retail_value',
                  'product_unit', 'quantity', 'net_price', 'gross_price']
