# Generated by Django 4.1.6 on 2023-02-06 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="manager",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="Home.employee",
            ),
        ),
    ]