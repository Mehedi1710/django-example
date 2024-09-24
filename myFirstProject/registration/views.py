from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django.http import HttpResponse
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
          
        
class UserByEmailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        email = self.kwargs['email']
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise NotFound("User not found.")
        
# class UserByEmailView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     lookup_field = 'email'

#     def get_queryset(self):
#         return User.objects.all()

#     def get_object(self):
#         email = self.kwargs.get('email')
#         return get_object_or_404(User, email=email)

class UserFindByEmail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        email = self.request.query_params.get('email')

        if email:
            return self.queryset.filter(email=email)
        return self.queryset
    
    
class UserFindById(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)