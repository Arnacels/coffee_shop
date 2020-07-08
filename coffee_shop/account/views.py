from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateUserSerializer, AllUsersSerializer, CreateCardSerializer
from .models import Users, DiscountCard


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                try:
                    user.first_name = request.data['first_name']
                except KeyError:
                    pass
                try:
                    user.last_name = request.data['last_name']
                except KeyError:
                    pass
                try:
                    user.phone = request.data['phone']
                except KeyError:
                    pass
                user.save()
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = AllUsersSerializer

    def get_queryset(self):
        for item in Users.objects.exclude(username='admin'):
            print(item)
            item.check_my_bonus()
        return Users.objects.all()


class CreateCard(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CreateCardSerializer(data=request.data)
        if serializer.is_valid():
            card = serializer.save()
            card.save()
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)

