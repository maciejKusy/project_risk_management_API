# Generated by Django 4.0.1 on 2022-01-10 19:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0003_alter_risk_background_alter_risk_priority_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="risk",
            name="user_assigned",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
