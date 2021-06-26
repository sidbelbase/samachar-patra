from django.urls import path

from .views import ConfirmSignup, SubscribeView

urlpatterns = [
    path('subscribe', SubscribeView.as_view(), name='subscribe'),
    path('confirm/<token>/', ConfirmSignup.as_view(), name='confirm_signup')
]
