from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Teste com 3 etapas (AAA):
    - A: Arrange (configuração)
    - A: Act (chamar o bloco a ser testado - System under test)
    - A: Assert (garanta que A é A)
    """

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK


def test_helloworld_retorna_html(client):
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


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'email': 'alice@example.com', 'username': 'alice'}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }
