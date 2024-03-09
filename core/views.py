from rest_framework import permissions, viewsets

from . import models, serializers


class WaasUserViewSet(viewsets.ModelViewSet):
    queryset = models.WassUser.objects.all()
    serializer_class = serializers.WassUserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class WaasOrganizationViewsSet(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.WaasOrganizationSerializer
    # permission_classes = [permissions.IsAuthenticated]


class WaasRoleViewSet(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.WaasRoleSerializer
    # permission_classes = [permissions.IsAuthenticated]


class WaasBillingViewSet(viewsets.ModelViewSet):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.WaasBillingSerializer
    # permission_classes = [permissions.IsAuthenticated]
