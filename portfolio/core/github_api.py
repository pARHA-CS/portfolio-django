import requests
import base64
import markdown
import re

def get_github_readme(owner, repo):
    """Récupère le README depuis l'API GitHub et convertit le Markdown en HTML."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    response = requests.get(url)
    if response.status_code == 200:
        readme_data = response.json()
        # Le contenu est encodé en base64, donc on doit le décoder
        readme_content = base64.b64decode(readme_data['content']).decode('utf-8')

        # Convertir le Markdown en HTML avec les bonnes extensions
        html_content = markdown.markdown(
            readme_content,
            extensions=[
                'fenced_code',  # Blocs de code avec triple backticks
                'codehilite',   # Coloration syntaxique
                'tables',       # Support des tableaux en Markdown
                'nl2br',        # Convertir les sauts de ligne en <br />
                'toc'           # Table des matières (facultatif)
            ]
        )

        # Corriger les chemins d'images relatifs
        html_content = fix_relative_image_urls(html_content, owner, repo)

        # Activer les blocs Mermaid
        html_content = add_mermaid_support(html_content)

        return html_content
    return None

def fix_relative_image_urls(html_content, owner, repo, branch="master"):
    """Remplace les URLs d'images relatives par des URLs absolues pointant vers GitHub."""
    base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/"
    # Corrige les chemins relatifs pour les images
    html_content = re.sub(r'src="([^http][^"]+)"', f'src="{base_url}\\1"', html_content)

    return html_content


def add_mermaid_support(html_content):
    """
    Ajoute le support pour les blocs Mermaid en remplaçant les blocs de code Mermaid
    par des divs avec la classe 'mermaid'.
    """
    # Regex pour trouver les blocs Mermaid dans le Markdown
    html_content = re.sub(
        r'<pre><code class="language-mermaid">([^<]+)</code></pre>',  # Rechercher les blocs Mermaid
        r'<div class="mermaid">\1</div>',  # Remplacer par des divs Mermaid
        html_content
    )
    return html_content
