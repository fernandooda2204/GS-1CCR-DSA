"""Lista simplesmente encadeada implementada com nós e referências explícitas.

Não utiliza list, dict nem sort/sorted como armazenamento/ordenação dos registros.
"""
from __future__ import annotations
from typing import Iterator, Optional
from registro import Registro


class No:
    def __init__(self, registro: Registro, proximo: Optional['No'] = None):
        self.registro = registro
        self.proximo = proximo


class ListaEncadeada:
    def __init__(self):
        self.cabeca: Optional[No] = None
        self.cauda: Optional[No] = None
        self.tamanho = 0

    def __len__(self) -> int:
        return self.tamanho

    def __iter__(self) -> Iterator[Registro]:
        atual = self.cabeca
        while atual is not None:
            yield atual.registro
            atual = atual.proximo

    def inserir(self, registro: Registro) -> bool:
        """Anexa um nó no fim em O(1); duplicidade é responsabilidade do cadastro."""
        novo = No(registro)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            assert self.cauda is not None
            self.cauda.proximo = novo
        self.cauda = novo
        self.tamanho += 1
        return True

    def buscar_id(self, identificador: int) -> Optional[Registro]:
        for registro in self:
            if registro.identificador == identificador:
                return registro
        return None

    def cadastrar(self, registro: Registro) -> bool:
        """Valida ID único por busca linear: O(n) + inserção física O(1)."""
        if self.buscar_id(registro.identificador) is not None:
            return False
        return self.inserir(registro)

    def remover(self, identificador: int) -> bool:
        anterior = None
        atual = self.cabeca
        while atual is not None:
            if atual.registro.identificador == identificador:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if self.cauda is atual:
                    self.cauda = anterior
                self.tamanho -= 1
                atual.proximo = None
                return True
            anterior, atual = atual, atual.proximo
        return False

    def atualizar(self, identificador: int, titulo: str, categoria: str,
                  descricao: str, requisitos: str, local: str) -> bool:
        registro = self.buscar_id(identificador)
        if registro is None:
            return False
        registro.titulo = titulo
        registro.categoria = categoria
        registro.descricao = descricao
        registro.requisitos = requisitos
        registro.local = local
        return True

    def cadeia_ids(self) -> str:
        partes = []  # Usada somente para apresentação, não guarda registros.
        atual = self.cabeca
        while atual is not None:
            partes.append(f"[{atual.registro.identificador}]")
            atual = atual.proximo
        return "cabeça -> " + (" -> ".join(partes) + " -> " if partes else "") + "None"

    def categorias(self) -> dict[str, int]:
        """Agregação auxiliar; os dados principais permanecem na lista encadeada."""
        contagem: dict[str, int] = {}
        for registro in self:
            categoria = registro.categoria
            contagem[categoria] = contagem.get(categoria, 0) + 1
        return contagem

    def validar_integridade(self) -> bool:
        """Verificação de invariantes útil aos testes, incluindo ausência de ciclo."""
        lento, rapido = self.cabeca, self.cabeca
        while rapido is not None and rapido.proximo is not None:
            lento = lento.proximo
            rapido = rapido.proximo.proximo
            if lento is rapido:
                return False
        atual, quantidade, ultimo = self.cabeca, 0, None
        while atual is not None:
            quantidade += 1
            ultimo, atual = atual, atual.proximo
        return (quantidade == self.tamanho and ultimo is self.cauda
                and (self.tamanho != 0 or self.cabeca is None and self.cauda is None)
                and (self.cauda is None or self.cauda.proximo is None))
