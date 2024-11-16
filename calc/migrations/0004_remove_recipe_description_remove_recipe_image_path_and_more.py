# Generated by Django 5.1 on 2024-09-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_question_recipe_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='image_path',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='name',
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
    ]
