import pytest
import datetime

from core.models import Patient


@pytest.mark.django_db
def test_patient_model():
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

    assert patient.created_at
    assert str(patient) == patient.name
