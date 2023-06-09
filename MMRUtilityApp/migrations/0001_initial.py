# Generated by Django 4.2.2 on 2023-06-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MMRmodel",
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
                ("cms_contract_id", models.CharField(max_length=5)),
                ("run_date", models.DateField()),
                ("pay_proc_period", models.IntegerField(max_length=6)),
                ("hic_no", models.CharField(max_length=12)),
                ("mbr_last_name", models.CharField(max_length=7)),
                ("mbr_first_init", models.CharField(max_length=1)),
                ("gender", models.CharField(max_length=1)),
                ("mbr_dob", models.DateField()),
                ("age_group", models.CharField(max_length=4)),
            ],
        ),
    ]
