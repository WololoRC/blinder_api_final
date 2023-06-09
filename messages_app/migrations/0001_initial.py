# Generated by Django 4.2.2 on 2023-06-13 20:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0004_blockedusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='profiles.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('messages', models.ManyToManyField(related_name='messages', to='messages_app.message')),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to='profiles.profile')),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to='profiles.profile')),
            ],
        ),
    ]
