# Generated by Django 3.1.3 on 2020-11-22 09:38

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_dur', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('c_trainer', models.CharField(max_length=100)),
                ('exp', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='enquariform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobiles', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('cources', multiselectfield.db.fields.MultiSelectField(choices=[('python', 'PYTHON'), ('django', 'DJANGO'), ('ui', 'UI'), ('flask', 'FLASK'), ('java', 'JAVA')], max_length=27)),
                ('trainer', multiselectfield.db.fields.MultiSelectField(choices=[('narayana', 'NARAYANA'), ('srinivas', 'SRINIVAS'), ('rubi', 'RUBI'), ('rachna', 'RACHNA'), ('mohit', 'MOHIT')], max_length=35)),
                ('shift', multiselectfield.db.fields.MultiSelectField(choices=[('morning', 'MORNING'), ('evening', 'EVENING'), ('night', 'NIGHT')], max_length=21)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('ameerpet', 'AMEERPET'), ('secundrabaad', 'SECANDRABAAD'), ('hyd', 'HYD'), ('begumpet', 'BEGUMPET')], max_length=34)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('salary', models.IntegerField()),
                ('qualification', multiselectfield.db.fields.MultiSelectField(choices=[('ba', 'BA'), ('be', 'BE'), ('bsc', 'BSC'), ('bcom', 'BCOM'), ('c-cat', 'C-CAT')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('iname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('cname', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('telugu', models.IntegerField()),
                ('hindi', models.IntegerField()),
                ('english', models.IntegerField()),
                ('math', models.IntegerField()),
            ],
        ),
    ]