import pytest
import datetime

from core.models import Patient
from django.contrib.auth import get_user_model


@pytest.mark.freeze_time(datetime.date.today())
@pytest.mark.django_db
def test_patient_model():
    """Test to create a new patient"""
    patient = Patient(
        name='Teste',
        gender='female',
        cpf='123.456.789-10',
        birth_date=datetime.date.today()
    )

    patient.save()
    assert patient.name == 'Teste'
    assert patient.gender == 'female'
    assert patient.cpf == '123.456.789-10'
    assert patient.birth_date == datetime.date.today()
    assert patient.birth_date_formate() == datetime.date.today().strftime('%d/%m/%Y')

    assert patient.created_at.strftime('%d/%m/%Y %H:%M:%S %f') == datetime.datetime.now().strftime(
        '%d/%m/%Y %H:%M:%S %f')
    assert str(patient) == patient.name


@pytest.mark.django_db
def test_new_user_with_email_successful():
    """Test to create a new user with an email is successful"""
    email = 'est@b.com'
    password = 'test123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )

    assert user.email == email
    assert user.check_password(password)


@pytest.mark.django_db
def test_new_user_with_email_normalized():
    """Test to create a new user with an email normalized"""
    email = 'test@GB.com'
    user = get_user_model().objects.create_user(
        email=email,
        password='test123'
    )

    assert user.email == email.lower()


@pytest.mark.django_db
def test_new_user_invalid_email():
    """Test creating user with no email raises error"""
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(email=None, password='test123')


@pytest.mark.django_db
def test_new_super_user():
    """Test creating a new superuser"""
    user = get_user_model().objects.create_superuser(
        email='test@b.com',
        password='test123'
    )

    assert user.is_superuser
    assert user.is_staff
