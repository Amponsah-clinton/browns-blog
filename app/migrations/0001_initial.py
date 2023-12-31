# Generated by Django 4.2 on 2023-07-25 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('snippet', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('link', models.CharField(blank=True, max_length=2000, null=True)),
                ('post_ategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
