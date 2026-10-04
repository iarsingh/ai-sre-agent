from fastapi.testclient import TestClient
from sreagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'should we ship', **{'payload': {'burn': 3}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["recommend"] == "freeze"
    refused = client.post("/agent/run", json={"goal": 'deploy to production'}).json()
    assert refused["refused"] is True
