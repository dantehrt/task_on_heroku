# Generated by Django 2.1.4 on 2019-01-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_order', models.IntegerField()),
                ('task_type', models.CharField(max_length=1)),
                ('image_url', models.CharField(max_length=3)),
                ('task_condition', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.CharField(max_length=200)),
                ('assignment_id', models.CharField(max_length=200)),
                ('accept_time', models.DateTimeField()),
                ('submit_time', models.DateTimeField()),
                ('work_time', models.IntegerField()),
                ('input_task_order', models.IntegerField()),
                ('input_task_type', models.CharField(max_length=1)),
                ('input_image_url', models.CharField(max_length=3)),
                ('input_task_condition', models.CharField(max_length=1)),
                ('answer_annotation_data', models.TextField(blank=True)),
                ('answer_text_box1', models.CharField(blank=True, max_length=200)),
                ('answer_text_box3', models.CharField(blank=True, max_length=200)),
                ('answer_text_box4', models.CharField(blank=True, max_length=200)),
                ('answer_text_box2', models.CharField(blank=True, max_length=200)),
                ('answer_text_box5', models.CharField(blank=True, max_length=200)),
                ('answer_comments', models.TextField(blank=True)),
                ('approve', models.CharField(blank=True, max_length=200)),
                ('reject', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.CharField(max_length=200)),
                ('assignment_id', models.CharField(max_length=200)),
                ('number_of_completed_tasks', models.IntegerField()),
                ('task_condition', models.CharField(max_length=1)),
                ('submit_time', models.DateTimeField()),
            ],
        ),
    ]
