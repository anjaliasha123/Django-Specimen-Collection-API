# Generated by Django 4.1.7 on 2025-01-10 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('herp', '0001_initial'),
        ('research_article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='specimen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='herp.specieslocation'),
        ),
    ]
