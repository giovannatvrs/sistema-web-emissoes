from fastapi.testclient import TestClient
from app.models import Emissao
from datetime import date


def test_get_emissao_not_found(client: TestClient):
    response = client.get("/emissoes/9999")
    assert response.status_code == 404
    assert response.json() == {"detail":"Emissão não encontrada"}

def test_get_emissao_by_id(client: TestClient, db_session):
    emissao = Emissao(data=date(2025, 1, 1), tipo="CRI", emissor="Emissor", valor=1222000.00, link="https://www.teste.com")

    db_session.add(emissao)
    db_session.commit()
    db_session.refresh(emissao)
    response = client.get(f"/emissoes/{emissao.id}")
    assert response.status_code == 200
    response = response.json()
    assert response["id"] == emissao.id
    assert response["data"] == emissao.data.isoformat()
    assert response["tipo"] == emissao.tipo
    assert response["emissor"] == emissao.emissor
    assert response["valor"] == str(emissao.valor)
    assert response["link"] == emissao.link
