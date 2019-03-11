from django.urls import path, include
from django.views.generic import TemplateView

from . import views


app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('teste/', TemplateView.as_view(template_name='teste.html'), name='teste'),
]
