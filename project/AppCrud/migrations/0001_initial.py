# Generated by Django 4.2.4 on 2023-12-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Student_name", models.CharField(max_length=20, null=True)),
                ("Department", models.CharField(max_length=20, null=True)),
                ("Phone", models.CharField(max_length=20, null=True)),
                ("Joinat", models.DateTimeField(auto_now_add=True)),
                (
                    "Profile_img",
                    models.ImageField(blank=True, null=True, upload_to="ProfileImg"),
                ),
            ],
        ),
    ]