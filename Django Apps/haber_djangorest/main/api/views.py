from django.http import response
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Makale, Authors
from main.api.serializers import MakaleSerializer, AuthorSerializer

# importing APIView
from rest_framework.views import APIView

# get instance module
from rest_framework.generics import get_object_or_404

# Class based


class AuthorsListCreateAPIView(APIView):
    """
    Yazarları gösterebileceğimiz ve yeni yazar oluşturabileceğimiz alanı yaratıyoruz.
    """

    def get(self, request):
        authors = Authors.objects.all()

        # context request ile linkleme işleminde karşılaştığımız hatayı çözüyoruz..
        serialized = AuthorSerializer(
            authors,
            many=True,
            context={"request": request},
        )
        return Response(serialized.data)

    def post(self, request):
        serialized = AuthorSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serialized.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class MakaleListCreateAPIView(APIView):
    """
    Aşağıda oluşturmuş olduğumuz fonksiyonu class olarak yazıyoruz.
    """

    def get(self, request):
        makaleler = Makale.objects.filter(aktif=True)
        serialized = MakaleSerializer(
            makaleler,
            many=True,
        )
        return Response(serialized.data)

    def post(self, request):
        serialized = MakaleSerializer(
            data=request.data
        )  # buradaki data işaretlemesini unutma xd
        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serialized.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class MakaleDetailAPIView(APIView):
    """
    Aşağıda oluşturduğumuz fonksiyonun class hali.
    """

    def get_object(self, id):
        return get_object_or_404(Makale, pk=id)

    def get(self, request, id):
        makale = self.get_object(id=id)
        serialized = MakaleSerializer(makale)
        return Response(serialized.data)

    def put(self, request, id):
        makale = self.get_object(id=id)
        serialized = MakaleSerializer(makale, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)

        return Response(
            serialized.errors,  # update yaparken karşılaştığımız hatanın neden kaynaklandığını söyleyecek.
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, id):
        makale = self.get_object(pk=id)
        makale.delete()

        return Response(
            {
                "errors": {
                    "code": 204,
                    "message": f"({id}) ID numarasına sahip olan makale silindi.. [Class]",
                }
            },
            status=status.HTTP_204_NO_CONTENT,
        )


# Function Based Methods
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
            return Response(
                serialized.data,
                status=status.HTTP_201_CREATED,
            )
        return response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def makale_detail_api_view(request, id):
    """
    Request ile eğer bir makale var ise (aktif veya değil fark etmez)
    bu makaleye erişip üzerinde değişiklikler yapabilmeliyiz.
    """

    try:
        makale_inst = Makale.objects.get(pk=id)
    except Makale.DoesNotExist:
        return Response(
            {
                "errors": {
                    "code": 404,
                    "message": f"Böyle bir id ({id}) ile ilgili makale bulunamadı.. Lütfen kontrol edip tekrar deneyiniz..",
                }
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        serialized = MakaleSerializer(makale_inst)
        return Response(serialized.data)

    elif request.method == "PUT":
        serialized = MakaleSerializer(makale_inst, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(
            {
                "errors": {
                    "code": 400,
                    "message": f"Değiştirmek istediğiniz {id}'li makalede bir hata meydana geldi. Lütfen girdilerinizi kontrol edip tekrar deneyiniz..",
                }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    elif request.method == "DELETE":
        makale_inst.delete()
        return Response(
            {
                "complete": {
                    "code": 202,
                    "message": f"{id} id numarasına sahip makale database üzerinden kaldırıldı..",
                }
            },
            status=status.HTTP_202_ACCEPTED,
        )
