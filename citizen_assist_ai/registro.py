"""Modelo de um serviço público informativo (dados locais, fictícios)."""
from dataclasses import dataclass


@dataclass
class Registro:
    identificador: int
    titulo: str
    categoria: str
    descricao: str
    requisitos: str
    local: str

    def __str__(self) -> str:
        return (f"ID: {self.identificador} | {self.titulo}\n"
                f"Categoria: {self.categoria}\n"
                f"Descrição: {self.descricao}\n"
                f"Requisitos: {self.requisitos}\nLocal: {self.local}")
