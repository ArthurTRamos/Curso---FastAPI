from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):

    # Trabalhamos com um tempo de mentira
    with mock_db_time(model=User) as time:
        new_user = User(username='test', email='test@test', password='secret')

        # Adiciona o user a comunicação entre o BD e o Python
        session.add(new_user)

        # Transmite, de verdade, as operações feitas ao banco
        session.commit()

        # scalar Converte o que vem do BD em objeto Python
        user = session.scalar(select(User).where(User.username == 'test'))

        assert asdict(user) == {
            'id': 1,
            'username': 'test',
            'email': 'test@test',
            'password': 'secret',
            'created_at': time,
        }
