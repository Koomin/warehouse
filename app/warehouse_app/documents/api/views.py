from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from documents.models import Document, DocumentItem, DocumentType
from documents.api.serializers import DocumentSerializer, DocumentItemSerializer, DocumentTypeSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'

    @action(detail=True, methods=['get'])
    def type(self, request, uuid=None):
        documents = Document.objects.filter(document_type__uuid=uuid)
        if documents:
            serializer = self.get_serializer(documents, many=True)
            return Response(serializer.data)


class DocumentItemViewSet(viewsets.ModelViewSet):
    queryset = DocumentItem.objects.all()
    serializer_class = DocumentItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'

    @action(detail=True, methods=['get'])
    def document(self, request, uuid=None):
        document_items = DocumentItem.objects.filter(document__uuid=uuid)
        if document_items:
            serializer = self.get_serializer(document_items, many=True)
            return Response(serializer.data)


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.filter(is_active=True).distinct('optima_id')
    serializer_class = DocumentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'
