# Generated by Django 4.2.13 on 2024-06-11 06:19

from django.db import migrations
from crawl.utils import load_initial_brief_data

class Migration(migrations.Migration):

    dependencies = [
        ("crawl", "0001_initial"),
    ]

    operations = [migrations.RunPython(load_initial_brief_data)]
