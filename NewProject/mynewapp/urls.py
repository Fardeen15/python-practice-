from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'students', views.StudentView)
routers.register(r'studentsClass', views.StudentClassView)

urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_frameWork')),
    url(r"^posts/$", views.PostApi.as_view()),
    url(r"^CreateUser/$", views.CreateUser.as_view()),
    url(r"^LoginDjangoUser/$", views.LoginDjangoUser.as_view()),
    url(r"^CreateNewDjangoUser/$", views.CreateNewDjangoUser.as_view())
]
