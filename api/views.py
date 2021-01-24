from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from portal.models import CardData
from api.serializers import CardDataModelSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class CardDataModelViewSet(ModelViewSet):
    queryset = CardData.objects.all()
    serializer_class = CardDataModelSerializer
    authentication_classes = [CsrfExemptSessionAuthentication, ]
