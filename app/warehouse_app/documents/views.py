from rest_framework import viewsets, status
from rest_framework import permissions

from documents.models import Document, DocumentItem
from documents.serializers import DocumentSerializer, DocumentItemSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = []


class DocumentItemViewSet(viewsets.ModelViewSet):
    queryset = DocumentItem.objects.all()
    serializer_class = DocumentItemSerializer
    permission_classes = []
