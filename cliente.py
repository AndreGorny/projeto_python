class Cliente:

    def __init__(self, nome: str, cpf: str,
                 sexo: str, nascimento: str,
                 email: str, telefone: str,
                 cartao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone
        self.cartao = cartao
