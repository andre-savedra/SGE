# Generated by Django 5.0.3 on 2024-05-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_chatbot_done_chatbot_message_alter_chatbot_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelogs',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='filelogs',
            name='response',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='filelogs',
            name='row',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
