# Generated by Django 4.2.3 on 2023-09-12 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sReg', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=50)),
                ('studentAge', models.IntegerField(default=18)),
                ('studentEmail', models.EmailField(max_length=254, unique=True)),
                ('studentAddress', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='receipe.department')),
                ('studentId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='receipe.studentreg')),
            ],
            options={
                'verbose_name': 'student',
                'ordering': ['studentName'],
            },
        ),
        migrations.CreateModel(
            name='receipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='receipe/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='studentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rank', models.IntegerField()),
                ('date_of_report', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentresult', to='receipe.student')),
            ],
            options={
                'unique_together': {('student', 'Rank')},
            },
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
