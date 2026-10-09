from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_gateway_requires_identity_and_capability():
    body={"command_id":"c1","device_id":"d1","type":"collect_inventory","payload":{}}
    assert c.post("/v1/gateway/commands",json=body).status_code==401
    assert c.post("/v1/gateway/commands",headers={"x-service-identity":"control-server"},json=body).status_code==202
    assert "collect_inventory" in c.get("/v1/gateway/capabilities").json()["commands"]
