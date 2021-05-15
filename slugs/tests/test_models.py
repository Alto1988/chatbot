import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_message_created():
    obj = mixer.blend('slugs.Messages')
    assert obj.message is not None


# def test_message_fail():
#     obj = mixer.blend('slugs.Messages')
#     assert obj.message is None


def test_groups_created():
    obj = mixer.blend('slugs.Groups')
    assert obj.pk is not None


def test_module_created():
    obj = mixer.blend('slugs.Module')
    assert obj.pk is not None
