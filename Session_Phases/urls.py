from django.urls import path
from . import views

app_name = 'session_phases'

urlpatterns = [
    path('sessao/<int:number>', views.session_presentation),
    path('', views.dashboard_presentation)
]
