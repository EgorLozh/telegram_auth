from authorization.presentation.views.registration import RegistrationView
from django.urls import path

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
]
