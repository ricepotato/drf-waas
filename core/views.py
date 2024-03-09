from rest_framework import viewsets

from . import models, serializers


class WaasUserViewSet(viewsets.ModelViewSet):
    queryset = models.WassUser.objects.all()
    serializer_class = serializers.WassUserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # can update only name, profile, password
        self.serializer_class = serializers.WaasUserUpdateSerializer
        return super().update(request, *args, **kwargs)


class WaasOrganizationViewsSet(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.WaasOrganizationSerializer
    # permission_classes = [permissions.IsAuthenticated]


class WaasRoleViewSet(viewsets.ModelViewSet):
    queryset = models.Role.objects.prefetch_related("user", "organization")
    # queryset = models.Role.objects.all()
    serializer_class = serializers.WaasRoleListSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["name", "organization", "user"]


class WaasBillingViewSet(viewsets.ModelViewSet):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.WaasBillingSerializer
    # permission_classes = [permissions.IsAuthenticated]
