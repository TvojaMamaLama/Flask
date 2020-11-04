from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


from .models import Investor, Qualification
from .serializer import InvestorSerializer, QualificationSerializer


class CreateInvestorView(APIView):
    '''Создание инвестора'''
    parser_classes = [FormParser, MultiPartParser, JSONParser]

    def post(self, request):
        serializer = InvestorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class RulesView(APIView):
    '''Подтверждение принятия правил'''

    def post(self, request):
        try:
            investor = Investor.objects.get(id=request.data['id'])
            investor.platform_rules = True
            investor.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)


class AddQualificationView(APIView):
    '''Добавление квалификации'''

    def post(self, request):
        try:
            investor = Investor.objects.get(id=request.data['id'])
            qualifications = Qualification.objects.filter(status__in=request.data['qualifications'])
            investor.qualification.add(*qualifications)
            investor.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class GetQualificationView(APIView):
    '''Получение квалификации'''

    def get(self, request, investorId):
        try:
            investor = Investor.objects.get(id=investorId)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QualificationSerializer(investor.qualification.all(), many=True)
        return Response(serializer.data)
