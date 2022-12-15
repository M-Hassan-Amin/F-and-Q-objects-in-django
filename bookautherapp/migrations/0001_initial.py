# Generated by Django 4.1.4 on 2022-12-15 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=40)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('published', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookautherapp.author')),
            ],
        ),
    ]