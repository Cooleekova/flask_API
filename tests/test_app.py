import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    test_app = app({'TESTING': True, 'DATABASE': db_path})

    with test_app.test_client() as client:

        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_get_user(client, user_id):
    rv = client.get('/users/<int:user_id>')
    json_data = rv.get_json()
    assert json_data['username']

