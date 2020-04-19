from django.urls import path, include
from login_api import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view()),
     path('', include(router.urls)),

]
