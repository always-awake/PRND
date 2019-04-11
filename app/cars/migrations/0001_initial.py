# Generated by Django 2.2 on 2019-04-11 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('year', models.DateField()),
                ('fuel_type', models.CharField(choices=[('lpg', 'LPG'), ('휘발유', 'Gasoline'), ('디젤', 'Diesel'), ('하이브리드', 'Hybrid'), ('전기', 'Electric'), ('바이퓨얼', 'Bifuel')], max_length=80, null=True)),
                ('transmission_type', models.CharField(choices=[('오토', 'Auto'), ('수동', 'Manual')], max_length=80, null=True)),
                ('color', models.CharField(max_length=30, null=True)),
                ('mileage', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('ongoing', 'Ongoing'), ('end', 'End')], default='waiting', max_length=80, null=True)),
                ('auction_start_time', models.DateTimeField(blank=True, null=True)),
                ('auction_end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-auction_start_time'],
            },
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kind_name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='cars.Brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model_name', models.CharField(max_length=50)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.Kind')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='cars/2019-04-11')),
                ('represent', models.BooleanField(default=False, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cars.Car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.Model'),
        ),
    ]
