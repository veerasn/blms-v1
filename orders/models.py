from django.db import models
import uuid

SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown'),
)

GENDER = (
    ('M', 'Male',),
    ('F', 'Female'),
    ('N', 'Non-binary'),
    ('T', 'Transgendered'),
    ('U', 'Unknown'),
    ('O', 'Others')
)

MARITAL_STATUS = (
    ('A', 'Annulled'),
    ('D', 'Divorced'),
    ('I', 'Interlocutary'),
    ('L', 'Legally Separated'),
    ('M', 'Married|'),
    ('P', 'Polygamous'),
    ('N', 'Never Married'),
    ('O', 'Domestic Partner'),
    ('U', 'Unmarried'),
    ('W', 'Widowed'),
    ('U', 'Unknown')
)

ETHNICITY = (
    ('ML', 'Malay'),
    ('CH', 'Chinese'),
    ('IN', 'Indian'),
    ('IB', 'Iban'),
    ('KM', 'Kadazan Murut'),
    ('IM', 'West Malaysia indigenous'),
    ('IS', 'Other East Malaysia indigenous'),
    ('EA', 'East Asian'),
    ('HI', 'Hispanic'),
    ('PI', 'Pacific Islander'),
    ('AR', 'Arab'),
    ('PE', 'Persian'),
    ('UN', 'Unspecified')
)

RELIGION = (
    ('IS', 'Islam'),
    ('BD', 'Buddhist'),
    ('TA', 'Taoist'),
    ('CH', 'Christian'),
    ('HI', 'Hindu'),
    ('AG', 'Agnostic')
)

NAME_USE = (
    ('US', 'usual'),
    ('OF', 'official'),
    ('TM', 'temporary'),
    ('NN', 'nickname'),
    ('AN', 'anonymous'),
    ('OL', 'old'),
    ('MA', 'maiden')
)

ADDRESS_USE = (
    ('H', 'home'),
    ('W', 'work'),
    ('T', 'temporary'),
    ('O', 'old'),
    ('B', 'billing')
)

ADDRESS_TYPE = (
    ('PO', 'postal'),
    ('PH', 'physical'),
    ('BO', 'both')
)

CONTACT_POINT_SYS = (
    ('phone', 'phone'),
    ('fax', 'fax'),
    ('email', 'E-mail'),
    ('url', 'url'),
    ('sms', 'sms')
)

ORGANIZATION_TYPE = (
    ('prov', 'healthcare provider'),
    ('dept', 'hospital department'),
    ('team', 'organizational team'),
    ('govt', 'government'),
    ('ins', 'insurance company'),
    ('edu', 'educational institution'),
    ('reli', 'religious institution'),
    ('crs', 'clinical research sponsor'),
    ('cg', 'community group'),
    ('bus', 'non-healthcare business or corporation'),
    ('other', 'other')
)

ORGANIZATION_CONTACT_PURPOSE = (
    ('bill', 'billing'),
    ('admin', 'administrative enquiries'),
    ('hr', 'human resources'),
    ('payor', 'insurance claims and payments'),
    ('patif', 'patient information'),
    ('press', 'press enquiries')
)


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=1)
    sex = models.CharField(max_length=1, choices=SEX)
    gender = models.CharField(max_length=1, choices=GENDER)
    birthDate = models.DateField('date of birth')
    deceasedDate = models.DateField('deceased date', null=True)
    maritalStatus = models.CharField('marital status', max_length=1, choices=MARITAL_STATUS)
    ethnicity = models.CharField(max_length=2, choices=ETHNICITY)
    religion = models.CharField(max_length=2, )
    photo = models.BinaryField(null=True)


class HumanName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    text = models.CharField('full name', max_length=100)
    family = models.CharField('family or last name', max_length=60, null=True)
    given = models.CharField('given or first name', max_length=60, null=True)
    middle = models.CharField('middle name', max_length=60, null=True)
    prefix = models.CharField('salutations or honorifics', max_length=20, null=True)
    suffix = models.CharField(max_length=20, null=True)
    use = models.CharField(max_length=2, choices=NAME_USE)


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    use = models.CharField(max_length=1, choices=ADDRESS_USE)
    type = models.CharField(max_length=2, choices=ADDRESS_TYPE)
    text = models.CharField('address', max_length=255)
    city = models.CharField(max_length=5)
    district = models.CharField(max_length=5)
    state = models.CharField(max_length=5)
    postalCode = models.CharField('post code', max_length=5)
    country = models.CharField(max_length=2, default='MY')


class Communication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    language = models.CharField(max_length=3)
    preferred = models.BooleanField(default=0)


class ContactPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    system = models.CharField(max_length=5, choices=CONTACT_POINT_SYS)
    value = models.CharField(max_length=255)
    use = models.CharField(max_length=1, choices=ADDRESS_USE)
    type = models.CharField(max_length=2, choices=ADDRESS_TYPE)
    rank = models.PositiveSmallIntegerField()


class ManagingOrganization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=1)
    type = models.CharField(max_length=5, choices=ORGANIZATION_TYPE)
    name = models.CharField(max_length=255)
    telecom = models.ForeignKey(ContactPoint, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class ManagingOrganizationContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=1)
    contact = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    managingOrganization = models.ForeignKey(ManagingOrganization, on_delete=models.DO_NOTHING)
    purpose = models.CharField(max_length=5, choices=ORGANIZATION_CONTACT_PURPOSE)


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    managingOrganization = models.ForeignKey(ManagingOrganization, on_delete=models.DO_NOTHING)


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    relationship = models.CharField(max_length=5)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)


class PatientContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=1)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=12)
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=1)


class Specialty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=12)
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=1)


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=12)
    text = models.CharField(max_length=255)
    active = models.BooleanField(default=1)


class Qualification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=12)
    text = models.CharField(max_length=255)


class PractitionerRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    managingOrganization = models.ForeignKey(ManagingOrganization, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    specialty = models.ForeignKey(Specialty, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=1)


class Practitioner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    practitionerRole = models.ForeignKey(PractitionerRole, on_delete=models.DO_NOTHING)
    qualification = models.ForeignKey(Qualification, on_delete=models.DO_NOTHING)


class DiagnosticOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderNum = models.CharField(max_length=16)
    subject = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    orderer = models.ForeignKey(Practitioner, on_delete=models.DO_NOTHING)
