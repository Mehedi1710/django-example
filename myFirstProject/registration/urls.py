from django.urls import path, include
from .views import UserList, UserByEmailView
from rest_framework.routers import DefaultRouter
from .views import UserFindByEmail, UserFindById, UserViewSet

router = DefaultRouter()

router.register('users', UserFindByEmail, basename='user')
router.register('byid', UserFindById, basename='userid')
router.register('id', UserViewSet, basename='id')

urlpatterns = [
    path('signup/', UserList.as_view()),
    path('find/<str:email>/', UserByEmailView.as_view(), name='user-by-email'),
    path('', include(router.urls))
]