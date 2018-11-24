import falcon
from falcon import testing
import msgpack
import pytest


from jadeapi.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)

def test_list_images(client):

    doc = {
            'images':[
                {
                    'herf':'images/lemon.png'
                    }
                ]
            }

    response = client.simulate_get('/images')
    result_doc = msgpack.unpackb(response.content, encoding='utf-8')

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK
