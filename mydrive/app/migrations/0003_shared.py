# Generated by Django 3.0.3 on 2020-03-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='shared',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.files')),
                ('sharedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_holder', to='app.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='app.user')),
            ],
        ),
    ]