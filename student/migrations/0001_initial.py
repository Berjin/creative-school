# Generated by Django 3.0.8 on 2020-08-03 18:33

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
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ManagementContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('important', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('standard', models.ManyToManyField(to='student.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Day')),
                ('period1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='1+', to='student.Subject')),
                ('period2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='2+', to='student.Subject')),
                ('period3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='3+', to='student.Subject')),
                ('period4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='4+', to='student.Subject')),
                ('period5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='5+', to='student.Subject')),
                ('period6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='6+', to='student.Subject')),
                ('period7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='7+', to='student.Subject')),
                ('period8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='8+', to='student.Subject')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('standard', models.ManyToManyField(to='student.Standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pics')),
                ('admission_number', models.IntegerField()),
                ('roll_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('blood_group', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('EMIS_number', models.BigIntegerField()),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Standard')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
                ('video', models.FileField(blank=True, upload_to='video')),
                ('datetime', models.DateField(auto_now=True)),
                ('standard', models.ManyToManyField(to='student.Standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Teachers')),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('deadline', models.DateField()),
                ('standard', models.ManyToManyField(to='student.Standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=True)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Standard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
