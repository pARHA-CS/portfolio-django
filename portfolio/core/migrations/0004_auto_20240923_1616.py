from django.db import migrations
from django.utils.text import slugify

def generate_unique_slugs(apps, schema_editor):
    RecentWork = apps.get_model('core', 'RecentWork')  # Assurez-vous que 'core' est le nom de votre application
    for work in RecentWork.objects.all():
        if not work.slug:  # Si un slug n'existe pas
            base_slug = slugify(work.title)
            slug = base_slug
            num = 1
            # Vérifie l'unicité du slug et ajoute un suffixe s'il est en conflit
            while RecentWork.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
            work.slug = slug
            work.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recentwork_slug'),  # Remplace par le numéro de la migration précédente
    ]

    operations = [
        migrations.RunPython(generate_unique_slugs),
    ]
