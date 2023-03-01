from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    cpf: str
    sexo: str
    nascimento: str
    email: str
    telefone: str
    cartao: str
    saldo: str  # integer?
    senha: str
    endereco: object
