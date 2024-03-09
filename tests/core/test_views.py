import pytest

from core import models

# Only one global marker (most commonly used)
pytestmark = pytest.mark.unit
# Several global markers


@pytest.mark.unit
def test_something():
    billings = models.Billing.objects.all()
