from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(default='SENT', max_length=10),
            preserve_default=False,
        ),
    ]
