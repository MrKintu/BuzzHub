# Generated by Django 5.0b1 on 2023-11-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authy", "0011_profile_d_o_e_profile_doc_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="doc_name",
            new_name="doc_id",
        ),
        migrations.AddField(
            model_name="profile",
            name="id_document",
            field=models.ImageField(
                default="default.jpg", null=True, upload_to="id_document"
            ),
        ),
    ]
