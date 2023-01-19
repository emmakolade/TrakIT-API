from .serializers import RegisterSerializer
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response


# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        # sends data to the serilizer, then validate
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # this runs a method called create

        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)
