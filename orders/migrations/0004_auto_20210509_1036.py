# Generated by Django 3.2.2 on 2021-05-09 10:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210509_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fcdf32e8-5b4c-4bc3-8e6b-b605d8879447'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='communication',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f1fe6d22-6ba9-4aae-8ac7-24359f6ae799'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3fbae896-7234-4e22-9e83-c03696756ce3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contactpoint',
            name='id',
            field=models.UUIDField(default=uuid.UUID('137bf5b0-bbc7-4b7a-923a-b48075d5b386'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='humanname',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5ace790a-b1b7-4ff4-aeb2-edce91ec1743'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(default=uuid.UUID('500bf1f2-67dc-483e-afdc-789f1a510100'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='managingorganization',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2bb078fc-96d5-4bb5-a3e3-379855c07d67'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='managingorganizationcontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8ad8e3ee-60f8-48d8-934e-5b087ab1fbc1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('721fca83-7299-4249-8a81-e808fad4cbb3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patientcontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b0842a6e-1b30-4d02-8f9f-1b2df3c40c9f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5cf6be23-d47f-49a3-8b20-388d60228cf3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7c26a44-da26-4d04-9bce-c49c873dbad5'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='practitionerrole',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6d89a3a6-43c7-442c-9e2e-ab0e61cc79e9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e110de41-dd7e-454c-8f9a-8324a8d10e66'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ca781ccc-a744-4f71-bc49-5c34fb35eee9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2ff90ea9-ee25-46b3-a18d-fd58310d68aa'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='DiagnosticOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('fe94aa6b-651c-4f58-bc60-265ceb9980ee'), editable=False, primary_key=True, serialize=False)),
                ('orderNum', models.CharField(max_length=16)),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.practitioner')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.patient')),
            ],
        ),
    ]
