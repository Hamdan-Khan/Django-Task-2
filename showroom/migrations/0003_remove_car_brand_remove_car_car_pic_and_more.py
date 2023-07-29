# Generated by Django 4.2.3 on 2023-07-26 14:46

from django.db import migrations, models
import django.db.models.deletion
import showroom.models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0002_alter_engine_chasis_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_pic',
        ),
        migrations.RemoveField(
            model_name='car',
            name='engine',
        ),
        migrations.RemoveField(
            model_name='car',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('car_pic', models.ImageField(upload_to=showroom.models.car_path)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='showroom.brand')),
                ('engine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='engine', to='showroom.engine')),
                ('feature', models.ManyToManyField(related_name='feature', to='showroom.feature')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='showroom.carmodel'),
            preserve_default=False,
        ),
    ]
