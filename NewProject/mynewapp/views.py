from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import StudentSerializer, StudentClassSerializer, NewUserSerializer
from django.contrib.auth import authenticate, login, logout
from .models import Student, StudentClass
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from pyrebase import pyrebase

config = {
    "apiKey": "AIzaSyCiN4aF04dvyMgwMFu-lOqMMXBQcXUvkfE",
    "authDomain": "campusrecruitment-system.firebaseapp.com",
    "databaseURL": "https://campusrecruitment-system.firebaseio.com",
    "projectId": "campusrecruitment-system",
    "storageBucket": "campusrecruitment-system.appspot.com",
    "messagingSenderId": "619734899398",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentClassView(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer


class PostApi(APIView):
    def post(self, request):
        username = self.request.data['username']
        r = requests.get(
            "http://api.msg91.com/api/sendotp.php?authkey=344496AzdzXjgqMWUf5f86d63aP1&mobile=00{}&otp_length=6".format(username))
        return Response(r.json())


class CreateUser(APIView):

    def post(self, request):
        email = self.request.data['email']
        password = self.request.data['password']
        image = self.request.data['image']
        r = {
            "email": email,
            "password": password
        }
        storage = firebase.storage()
        imagePut = storage.child("images/example").put(image)
        print(imagePut)
        user = auth.create_user_with_email_and_password(email, password)
        return Response(user)


class CreateNewDjangoUser(APIView):

    def post(self, request):
        firstname = self.request.data['firstname']
        lastname = self.request.data['lastname']
        email = self.request.data['email']
        username = self.request.data['username']
        password1 = self.request.data['password']
        user = User.objects.create(
            username=username, email=email, first_name=firstname, last_name=lastname, password=password1)
        profile = NewUserSerializer(user)
        return JsonResponse({"User": profile.data})


class LoginDjangoUser(APIView):

    def post(self, request):
        # if request.method == 'POST':
        # if User.is_anonymous:
        #     print(self.request.user)
        #     # profile = NewUserSerializer(self.request.user)
        #     # print(profile)
        #     return Response("you are already login")
        # else:
        username = self.request.data['username']
        password1 = self.request.data['password']
        user = authenticate(username=username, password=password1)
        print(user)
        if user is not None:
            login(self.request, user)
            profile = NewUserSerializer(user)
            return JsonResponse({"User": profile.data})
        else:
            return Response("user not exists")
