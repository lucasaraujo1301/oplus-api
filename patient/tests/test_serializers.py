import pytest
import datetime
from rest_framework.utils import json
from rest_framework.utils.encoders import JSONEncoder

from patient.serializers import PatientSerializer


@pytest.mark.django_db
def test_valid_patient_serializer():
    valid_serializer_data = {
        'name': 'Lucas Araujo',
        'cpf': '123.456.789-10',
        'gender': 'male',
        'birth_date': '2022-03-31'
    }

    serializer = PatientSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert json.loads(json.dumps(serializer.validated_data, cls=JSONEncoder)) == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_movie_serializer():
    invalid_serializer_data = {
        'name': 'Lucas Araujo',
        'cpf': '123.456.789-10',
        'gender': 'male',
    }

    serializer = PatientSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {'birth_date': ['This field is required.']}
