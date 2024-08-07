# Generated by Django 5.0.6 on 2024-07-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_applyjob_file_alter_joblisting_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='about',
            field=models.TextField(default='Information about the company is not available.'),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='category',
            field=models.CharField(choices=[('IT', 'IT'), ('Graphic Design', 'Graphic Design'), ('Banking', 'Banking'), ('Sales', 'Sales'), ('HR', 'HR'), ('Accounting', 'Accounting')], max_length=30),
        ),
    ]
