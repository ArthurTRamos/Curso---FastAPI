from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Teste com 3 etapas (AAA):
    - A: Arrange (configuração)
    - A: Act (chamar o bloco a ser testado - System under test)
    - A: Assert (garanta que A é A)
    """

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK


def test_helloworld_retorna_html():
    client = TestClient(app)

    response = client.get('/helloworld')

    assert (
        response.text
        == """
        <html>
            <head>
                <title> Hello World! </title>
            </head>
            <body>
                <h1> Hello World </h1>
            </body>
        </html>
        """
    )
    assert response.status_code == HTTPStatus.OK
