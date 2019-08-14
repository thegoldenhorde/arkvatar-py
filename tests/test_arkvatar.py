import pytest
import secrets
import arkvatar


class TestArkvatar(object):
    @pytest.mark.asyncio
    async def test_verify_success(self):
        identifier = f"{''.join(secrets.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g']) for _ in range(9))}@gmail.com"
        verification = await arkvatar.verify(identifier)
        assert type(verification) == dict
        assert verification['data'] == 'Email'

    @pytest.mark.asyncio
    async def test_verify_failure(self):
        identifier = "azerty"
        verification = await arkvatar.verify(identifier)
        assert type(verification) == dict
        assert verification['error'] == 'Invalid identifier format.'

    @pytest.mark.asyncio
    async def test_show(self):
        identifier = "ALhWkv1uGfujoVdRRiaFzrKzCwJvPkz7hi"
        verification = await arkvatar.show(identifier)
        assert type(verification) == dict
        assert 'url' in verification

    @pytest.mark.asyncio
    async def test_store(self):
        identifier = f"{''.join(secrets.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g']) for _ in range(9))}@gmail.com"
        verification = await arkvatar.store("Email", identifier)
        assert type(verification) == dict
        assert verification['data'] == f"https://arkvatar.com/arkvatar/{identifier}"

    @pytest.mark.asyncio
    async def test_store_failure(self):
        identifier = "azerty"
        verification = await arkvatar.store("Email", identifier)
        assert type(verification) == dict
        assert 'error' in verification
