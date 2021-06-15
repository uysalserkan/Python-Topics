from django.http import response
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Makale
from main.api.serializers import MakaleSerializer


@api_view(["GET", "POST"])
def makale_list_create_api_view(request):
    """
    Request e göre oluşturulmuş makaleleri GET veya POST olarka işleriz.
    """

    if request.method == "GET":
        # Makaleleri görmek istiyoruz.
        makaleler = Makale.objects.filter(aktif=True)
        # nesnelerden oluşan bir query set
        serialized = MakaleSerializer(makaleler, many=True)
        # Birden fazla query içerebilir
        return Response(serialized.data)

    elif request.method == "POST":
        serialized = MakaleSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return response(status=status.HTTP_400_BAD_REQUEST)
