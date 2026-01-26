from fastapi.testclient import TestClient
from app.models import Emissao
from datetime import date

def test_listar_emissoes_com_filtro_tipo(client: TestClient, db_session):
    db_session.add(Emissao(data=date(2026, 1, 26), tipo="CRI", emissor="Emissor 1", valor=100, link="http://teste.com"))
    db_session.add(Emissao(data=date(2026, 1, 26), tipo="CRA", emissor="Emissor 2", valor=200, link="http://teste.com"))
    db_session.commit()

    response = client.get("/emissoes?tipo=CRI")
    assert response.status_code == 200
    dados = response.json()
    assert dados["total"] == 1
    assert dados["emissoes"][0]["tipo"] == "CRI"

def test_listar_emissoes_ordenacao_valor(client: TestClient, db_session):
    db_session.add(Emissao(data=date(2026, 1, 26), tipo="CRI", emissor="Emissor 1", valor=100.01, link="http://teste.com"))
    db_session.add(Emissao(data=date(2026, 1, 26), tipo="CRI", emissor="Emissor 2", valor=100, link="http://teste.com"))
    db_session.commit()

    response = client.get("/emissoes?sort_by=valor&order=asc")
    dados = response.json()
    assert float(dados["emissoes"][0]["valor"]) == 100
    assert float(dados["emissoes"][1]["valor"]) == 100.01

def test_listar_emissoes_filtro_data(client: TestClient, db_session):
    db_session.add(Emissao(data=date(2025, 1, 2), tipo="CRI", emissor="Emissor 1", valor=100, link="http://teste.com"))
    db_session.add(Emissao(data=date(2025, 1, 1), tipo="CRI", emissor="Emissor 2", valor=100, link="http://teste.com"))
    db_session.commit()

    response = client.get("/emissoes?final_date=2025-01-01")
    dados = response.json()
    assert dados["total"] == 1
    assert dados["emissoes"][0]["emissor"] == "Emissor 2"


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
    assert response["link"].rstrip('/') == emissao.link.rstrip('/')

def test_put_emissor_by_id(client: TestClient, db_session):
    emissao = Emissao(data=date(2025, 1, 1), tipo="CRI", emissor="Emissor", valor=1222000.00,
                      link="https://www.teste.com")

    db_session.add(emissao)
    db_session.commit()
    db_session.refresh(emissao)
    payload = {
        "tipo": "CRA",
        "emissor": "Empresa",
        "valor": 100000000.00,
        "link": "https://jgp.com.br",
        "data": "2025-02-12"
    }
    response = client.put(f"/emissoes/{emissao.id}", json=payload)
    assert response.status_code == 200


def test_put_emissao_not_found(client: TestClient):
    exemplo = {
        "tipo": "CRI",
        "emissor": "Teste",
        "valor": "1222000.00",
        "link": "https://teste.com",
        "data": "2025-01-01"
    }
    response = client.put("/emissoes/9999", json=exemplo)
    assert response.status_code == 404
    assert response.json() == {"detail":"Emissão não encontrada"}

def test_put_emissao_tipo_vazio(client: TestClient):
    exemplo = {
        "tipo": "",
        "emissor": "Teste",
        "valor": "1222000.00",
        "link": "https://teste.com",
        "data": "2025-01-01"
    }
    response = client.put("/emissoes/9999", json=exemplo)
    assert response.status_code == 422

def test_put_valor_negativo(client: TestClient):
    payload = {
        "tipo": "CRI",
        "emissor": "Empresa S.A",
        "valor": -100.00,
        "link": "https://jgp.com.br",
        "data": "2025-01-01"
    }
    response = client.put("/emissoes/1", json=payload)
    assert response.status_code == 422

def test_put_emissor_vazio(client: TestClient):
    payload = {
        "tipo": "CRI",
        "emissor": "",
        "valor": 100000000.00,
        "link": "https://jgp.com.br",
        "data": "2025-01-01"
    }
    response = client.put("/emissoes/2", json=payload)
    assert response.status_code == 422

def test_put_data_invalida(client: TestClient, db_session):
    emissao = Emissao(data=date(2025, 1, 1), tipo="CRI", emissor="Emissor", valor=1222000.00,
                      link="https://www.teste.com")

    db_session.add(emissao)
    db_session.commit()
    db_session.refresh(emissao)
    payload = {
        "tipo": "CRI",
        "emissor": "Emissor",
        "valor": 100000000.00,
        "link": "https://jgp.com.br",
        "data": "2026-01-27"
    }
    response = client.put(f"/emissoes/{emissao.id}", json=payload)
    assert response.status_code == 422

def test_put_link_invalido(client: TestClient, db_session):
    emissao = Emissao(data=date(2025, 1, 1), tipo="CRI", emissor="Emissor", valor=1222000.00,
                      link="https://www.teste.com")

    db_session.add(emissao)
    db_session.commit()
    db_session.refresh(emissao)
    payload = {
        "tipo": "CRI",
        "emissor": "Emissor",
        "valor": 100000000.00,
        "link": 'teste',
        "data": "2026-01-27"
    }
    response = client.put(f"/emissoes/{emissao.id}", json=payload)
    assert response.status_code == 422

def test_get_estatisticas(client: TestClient, db_session):
    response = client.get("/stats")
    assert response.status_code == 200
