# Generated by Django 3.2.2 on 2021-05-09 06:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('aee17b4c-70dd-48fb-bdb7-f07bb71051fe'), editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=1)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-binary'), ('T', 'Transgendered'), ('U', 'Unknown'), ('O', 'Others')], max_length=1)),
                ('birthDate', models.DateField(verbose_name='date of birth')),
                ('deceasedDate', models.DateField(verbose_name='deceased date')),
                ('maritalStatus', models.CharField(choices=[('A', 'Annulled'), ('D', 'Divorced'), ('I', 'Interlocutary'), ('L', 'Legally Separated'), ('M', 'Married|'), ('P', 'Polygamous'), ('N', 'Never Married'), ('O', 'Domestic Partner'), ('U', 'Unmarried'), ('W', 'Widowed'), ('U', 'Unknown')], max_length=1, verbose_name='marital status')),
                ('ethnicity', models.CharField(choices=[('ML', 'Malay'), ('CH', 'Chinese'), ('IN', 'Indian'), ('IB', 'Iban'), ('KM', 'Kadazan Murut'), ('IM', 'West Malaysia indigenous'), ('IS', 'Other East Malaysia indigenous'), ('EA', 'East Asian'), ('HI', 'Hispanic'), ('PI', 'Pacific Islander'), ('AR', 'Arab'), ('PE', 'Persian'), ('UN', 'Unspecified')], max_length=2)),
                ('religion', models.CharField(max_length=2)),
                ('photo', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='HumanName',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('aa0b7725-76f6-4aa2-b511-d3301c124da0'), editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100, verbose_name='full name')),
                ('family', models.CharField(max_length=60, null=True, verbose_name='family or last name')),
                ('given', models.CharField(max_length=60, null=True, verbose_name='given or first name')),
                ('middle', models.CharField(max_length=60, null=True, verbose_name='middle name')),
                ('prefix', models.CharField(max_length=20, null=True, verbose_name='salutations or honorifics')),
                ('suffix', models.CharField(max_length=20, null=True)),
                ('use', models.CharField(choices=[('US', 'usual'), ('OF', 'official'), ('TM', 'temporary'), ('NN', 'nickname'), ('AN', 'anonymous'), ('OL', 'old'), ('MA', 'maiden')], max_length=2)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.person')),
            ],
        ),
    ]