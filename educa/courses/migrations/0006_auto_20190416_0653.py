# Generated by Django 2.2 on 2019-04-16 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='video',
            name='created',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='updated',
        ),
        migrations.AddField(
            model_name='video',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', to='courses.Module'),
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='name', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='www.baidu.com', max_length=200),
        ),
    ]
