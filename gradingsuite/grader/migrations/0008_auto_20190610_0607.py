# Generated by Django 2.2.1 on 2019-06-10 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0007_rubricitem_optional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rubricitem',
            name='earned_points',
        ),
        migrations.CreateModel(
            name='GradedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_points', models.IntegerField()),
                ('rubric_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grader.RubricItem')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grader.Submission')),
            ],
        ),
    ]
