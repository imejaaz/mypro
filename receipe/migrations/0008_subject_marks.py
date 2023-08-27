# Generated by Django 4.2.3 on 2023-08-25 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0007_alter_student_department_alter_student_studentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(blank=None)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipe.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipe.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
