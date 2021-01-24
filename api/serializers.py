from rest_framework.serializers import ModelSerializer
from portal.models import CardData


class CardDataModelSerializer(ModelSerializer):
    class Meta:
        model = CardData
        fields = '__all__'