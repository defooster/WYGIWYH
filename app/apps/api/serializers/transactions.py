from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import Account
from apps.api.fields.transactions import TransactionTagField, TransactionCategoryField
from apps.api.serializers.accounts import AccountSerializer
from apps.transactions.models import (
    Transaction,
    TransactionCategory,
    TransactionTag,
    InstallmentPlan,
)


# Create serializers for other related models as needed
class TransactionCategorySerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = TransactionCategory
        fields = "__all__"


class TransactionTagSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = TransactionTag
        fields = "__all__"


class InstallmentPlanSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = InstallmentPlan
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    category = TransactionCategoryField(required=False)
    tags = TransactionTagField(required=False)

    exchanged_amount = serializers.SerializerMethodField()

    # For read operations (GET)
    account = AccountSerializer(read_only=True)

    # For write operations (POST, PUT, PATCH)
    account_id = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), source="account", write_only=True
    )

    reference_date = serializers.DateField(
        required=False, input_formats=["iso-8601", "%Y-%m"]
    )

    permission_classes = [IsAuthenticated]

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = [
            "id",
            "installment_plan",
            "recurring_transaction",
            "installment_id",
        ]

    def validate(self, data):
        if "date" in data and "reference_date" not in data:
            data["reference_date"] = data["date"].replace(day=1)
        elif "reference_date" in data:
            data["reference_date"] = data["reference_date"].replace(day=1)
        else:
            raise serializers.ValidationError(
                _("Either 'date' or 'reference_date' must be provided.")
            )
        return data

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        transaction = Transaction.objects.create(**validated_data)
        transaction.tags.set(tags)
        return transaction

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if tags is not None:
            instance.tags.set(tags)
        return instance

    @staticmethod
    def get_exchanged_amount(obj):
        return obj.exchanged_amount()
