from django.urls import path
from .views import HomeTemplateView, project_detail

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('projets/<slug:slug>/', project_detail, name='project_detail'),
]