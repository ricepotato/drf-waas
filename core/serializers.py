from rest_framework import serializers

from . import models


class WassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WassUser
        fields = "__all__"


class WaasUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WassUser
        fields = "__all__"
        read_only_fields = ["email"]


class WaasOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = "__all__"


class WaasRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"


class WaasRoleListSerializer(serializers.ModelSerializer):
    user = WassUserSerializer(many=False, read_only=True)
    organization = WaasOrganizationSerializer(many=False, read_only=True)

    class Meta:
        model = models.Role
        fields = "__all__"
        # fields = ["name", "user", "organization"]


class WaasBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Billing
        fields = "__all__"
