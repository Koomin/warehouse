from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from documents.models import Document, DocumentItem, DocumentType
from documents.api.serializers import DocumentSerializer, DocumentItemSerializer, DocumentTypeSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-document_date')
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'

    @action(detail=True, methods=['get'])
    def type(self, request, uuid=None):
        documents = self.queryset.filter(document_type__uuid=uuid)
        if documents:
            serializer = self.get_serializer(documents, many=True)
            return Response(serializer.data)


class DocumentItemViewSet(viewsets.ModelViewSet):
    queryset = DocumentItem.objects.all()
    serializer_class = DocumentItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        document_uuid = serializer.data[0].get('document')
        document = Document.objects.get(uuid=document_uuid)
        document.save_to_optima()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'])
    def document(self, request, uuid=None):
        document_items = DocumentItem.objects.filter(document__uuid=uuid)
        if document_items:
            serializer = self.get_serializer(document_items, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def store(self, request, uuid=None):
        document_items = DocumentItem.objects.filter(document__source_store__uuid=uuid)
        if document_items:
            serializer = self.get_serializer(document_items, many=True)
            return Response(serializer.data)


class OrderViewSet(DocumentViewSet):
    queryset = Document.objects.filter(~Q(issued=True, realized=True),
                                       document_type__short_name__in=['CUK', 'PIEK']).order_by('-document_date')

    @action(detail=True, methods=['get'])
    def type(self, request, uuid=None):
        documents = self.queryset.filter(document_type__uuid=uuid)
        if documents:
            serializer = self.get_serializer(documents, many=True)
            return Response(serializer.data)


class OrderItemViewSet(DocumentItemViewSet):
    queryset = DocumentItem.objects.filter(~Q(document__issued=True, document__realized=True),
                                           document__document_type__short_name__in=['CUK', 'PIEK']).order_by(
        '-document__document_date')


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.filter(is_active=True).distinct('optima_id')
    serializer_class = DocumentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'
