from django.urls import path
from .views import HomeTemplateView, project_detail, project_list, show_readme

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('projets/', project_list, name='project_list'),
    path('projets/<slug:slug>/', project_detail, name='project_detail'),
    path('readme/<str:owner>/<str:repo>/', show_readme, name='show_readme'),
]