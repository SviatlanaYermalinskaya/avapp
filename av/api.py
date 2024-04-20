from rest_framework import viewsets, permissions
from av.models import Brand
from av.serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BrandSerializer
    