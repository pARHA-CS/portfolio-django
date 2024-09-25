from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import About, Service, RecentWork, Client
import requests
import base64
from .github_api import get_github_readme

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return  context
    
def project_detail(request, slug):
    project = get_object_or_404(RecentWork, slug=slug)
    
    # Si le projet a un dépôt GitHub associé
    readme_content = None
    if project.github_repo:
        owner, repo = project.github_repo.split('/')
        readme_content = get_github_readme(owner, repo)
    
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'readme': readme_content,
    })

def project_list(request):
    works = RecentWork.objects.all()  # Récupère tous les projets
    return render(request, 'projects/project_list_copy.html', {'works': works})


def get_github_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    response = requests.get(url)
    if response.status_code == 200:
        readme_data = response.json()
        # Le contenu est encodé en base64, donc on doit le décoder
        readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
        return readme_content
    return None

def show_readme(request, owner, repo):
    readme_content = get_github_readme(owner, repo)
    return render(request, 'projects/show_readme.html', {'readme': readme_content})

