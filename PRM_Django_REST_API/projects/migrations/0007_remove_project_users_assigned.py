# Generated by Django 4.0.1 on 2022-01-11 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_alter_risk_project"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="users_assigned",
        ),
    ]
