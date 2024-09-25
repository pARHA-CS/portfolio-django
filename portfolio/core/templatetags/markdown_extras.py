import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    # Utilisation de la bibliothèque Markdown pour convertir le texte
    return mark_safe(markdown.markdown(text, extensions=['fenced_code', 'codehilite']))