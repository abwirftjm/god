# Generated by Django 5.1.1 on 2024-09-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_company_disqualified_company_massmail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='massmail',
            field=models.BooleanField(default=True, help_text='Mailing list recipient.', verbose_name='Mass mailing'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='massmail',
            field=models.BooleanField(default=True, help_text='Mailing list recipient.', verbose_name='Mass mailing'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='massmail',
            field=models.BooleanField(default=True, help_text='Mailing list recipient.', verbose_name='Mass mailing'),
        ),
    ]
