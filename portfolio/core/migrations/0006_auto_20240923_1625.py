from django.db import migrations
from django.utils.text import slugify

def generate_unique_slugs(apps, schema_editor):
    RecentWork = apps.get_model('core', 'RecentWork')  # Utilise le nom correct de ton app
    for work in RecentWork.objects.all():
        if not work.slug or RecentWork.objects.filter(slug=work.slug).count() > 1:
            base_slug = slugify(work.title)
            slug = base_slug
            num = 1
            while RecentWork.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
            work.slug = slug
            work.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recentwork_slug'),  # Modifie cette dépendance pour refléter la migration précédente
    ]

    operations = [
        migrations.RunPython(generate_unique_slugs),
    ]
