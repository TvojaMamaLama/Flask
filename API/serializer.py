from rest_framework import serializers


from .models import Investor, Qualification


class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = ('status', 'description')


class InvestorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investor
        exclude = ('qualification',)
