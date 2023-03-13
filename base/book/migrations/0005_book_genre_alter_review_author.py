# Generated by Django 4.1.7 on 2023-03-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Art', 'Art'), ("Children's", 'Children'), ('Classic', 'Classic'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller'), ('Biography', 'Biography'), ('Christian', 'Christian'), ('Science', 'Science'), ('Self Help', 'Self Help')], default='Art', max_length=40),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.TextField(default='Anoymous'),
        ),
    ]
