# Generated by Django 5.1.2 on 2024-11-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Event Name')),
                ('date', models.DateField(verbose_name='Event Date')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('total_regular_tickets', models.PositiveIntegerField(verbose_name='Total Regular Tickets')),
                ('total_vip_tickets', models.PositiveIntegerField(verbose_name='Total VIP Tickets')),
                ('available_regular_tickets', models.PositiveIntegerField(verbose_name='Available Regular Tickets')),
                ('available_vip_tickets', models.PositiveIntegerField(verbose_name='Available VIP Tickets')),
                ('regular_ticket_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Regular Ticket Price')),
                ('vip_ticket_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='VIP Ticket Price')),
                ('early_bird_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Early Bird Price')),
                ('early_bird_deadline', models.DateTimeField(verbose_name='Early Bird Deadline')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]
