from django.urls import path
from .views import HomeTemplateView, project_detail, project_list

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('projets/', project_list, name='project_list'),
    path('projets/<slug:slug>/', project_detail, name='project_detail'),
]