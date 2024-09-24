from django.urls import path
from .views import SignupView, SigninView

urlpatterns = [
    path('signUp/', SignupView.as_view(), name='signup'),
    path('signIn/', SigninView.as_view(), name='signin'),
]
