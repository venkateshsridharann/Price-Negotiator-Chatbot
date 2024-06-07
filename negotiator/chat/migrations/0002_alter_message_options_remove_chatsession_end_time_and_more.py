# Generated by Django 5.0.6 on 2024-06-06 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('frontapp', '0002_product_category_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['timestamp']},
        ),
        migrations.RemoveField(
            model_name='chatsession',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='chatsession',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='chatsession',
            name='user',
        ),
        migrations.AddField(
            model_name='chatsession',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chatsession',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='chat_sessions', to='frontapp.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(default=''),
        ),
    ]