import requests
import base64

def get_github_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    response = requests.get(url)
    if response.status_code == 200:
        readme_data = response.json()
        # Le contenu est encodé en base64, donc on doit le décoder
        readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
        return readme_content
    return None
