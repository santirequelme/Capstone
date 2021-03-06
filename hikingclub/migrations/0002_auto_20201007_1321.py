# Generated by Django 3.1.1 on 2020-10-07 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hikingclub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiking',
            name='mapUrl',
        ),
        migrations.AddField(
            model_name='hiking',
            name='map_url',
            field=models.URLField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='hiking',
            name='short_description',
            field=models.CharField(blank=True, max_length=170),
        ),
        migrations.AlterField(
            model_name='hiking',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='hiking',
            name='level',
            field=models.CharField(blank=True, choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Strenuous', 'Strenuous'), ('Very difficult', 'Very difficult')], default='Select level', max_length=64),
        ),
        migrations.AlterField(
            model_name='hiking',
            name='location',
            field=models.CharField(blank=True, choices=[('San Martin de los Andes', 'San Martin de los Andes'), ('Bariloche', 'Bariloche'), ('Torres del Paine', 'Torres del Paine'), ('El Chalten', 'El Chalten'), ('El Bolson', 'El Bolson'), ('El Calafate', 'El Calafate')], default='Select location', max_length=64),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hike', models.CharField(blank=True, max_length=120)),
                ('name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('date', models.DateField()),
                ('phone', models.CharField(max_length=64)),
                ('book_number', models.CharField(max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
