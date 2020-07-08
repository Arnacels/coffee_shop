from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateBoughtCoffeeSerializer, BoughtCoffeeSerializer, CoffeeSerializer
from .models import Coffee, BoughtCoffee


class CoffeeListView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer


class BoughtCoffeeListView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = BoughtCoffee.objects.all()
    serializer_class = BoughtCoffeeSerializer


class CreateBoughtCoffeeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CreateBoughtCoffeeSerializer(data=request.data)
        if serializer.is_valid():
            check = serializer.save()
            check.save()
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response('no coffee or no user' ,status=status.HTTP_400_BAD_REQUEST)
