from dataclasses import dataclass
from typing import List


@dataclass
class Cliente:
    cd_cliente: int
    nm_cliente: str
    nr_cpf: str
    dt_nascimento: str
    nm_email: str
    nr_telefone: str
    qt_pontos: float


@dataclass
class Premio:
    cd_premio: int
    nm_premio: str
    vl_pontos: float


@dataclass
class Empresa:
    cd_empresa: int
    nm_empresa: str
    nm_razao_social: str
    nr_cnpj: str
    vl_tx_conversao: float
    cd_premios: List[Premio]
