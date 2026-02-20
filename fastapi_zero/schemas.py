from pydantic import BaseModel


class Message(BaseModel):
    # Define que chave será 'message' e o valor, uma string
    message: str
