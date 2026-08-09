import app


class FakeCursor:
    def execute(self, query):
        pass

    def close(self):
        pass


class FakeConnection:
    def cursor(self):
        return FakeCursor()


def test_health():
    app.conn = FakeConnection()

    client = app.app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["database"] == "connected"
