from django.urls import path

from authorization.presentation.views.login import LoginView
from authorization.presentation.views.logout import LogoutView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
