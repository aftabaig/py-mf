from rest_framework import serializers

# models
from models import Branch
from models import Contact
from models import Deal
from models import DealBranch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal


class DealBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealBranch