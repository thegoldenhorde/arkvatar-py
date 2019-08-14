import pytest
from arkvatar.client import Client


class TestClient(object):
    @pytest.mark.asyncio
    async def test_get_success(self):
        client = Client()
        request = await client.get('https://jsonplaceholder.typicode.com/todos/1')
        assert type(request) == dict
        assert request['id'] == 1

    @pytest.mark.asyncio
    async def test_post(self):
        client = Client()
        request = await client.post('https://httpbin.org/post')
        assert type(request) == dict
        assert len(request) >= 0
