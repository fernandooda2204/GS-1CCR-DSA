"""Busca linear e Merge Sort sobre os próprios nós encadeados."""
from typing import Optional
from lista_encadeada import ListaEncadeada, No
from registro import Registro


def busca_linear(lista: ListaEncadeada, termo: str, campo: str = 'titulo') -> list[Registro]:
    """Pesquisa case-insensitive de substring: O(n * k), k = custo da comparação."""
    if campo not in ('titulo', 'categoria'):
        raise ValueError('Campo inválido: escolha titulo ou categoria.')
    termo = termo.casefold().strip()
    if not termo:
        raise ValueError('A pesquisa não pode estar vazia.')
    resultados = []
    for registro in lista:
        if termo in getattr(registro, campo).casefold():
            resultados.append(registro)
    return resultados


def _chave(no: No, campo: str) -> tuple[str, int]:
    return (getattr(no.registro, campo).casefold(), no.registro.identificador)


def _dividir(inicio: No) -> tuple[No, Optional[No]]:
    lento, rapido = inicio, inicio.proximo
    while rapido is not None and rapido.proximo is not None:
        lento = lento.proximo
        rapido = rapido.proximo.proximo
    segunda = lento.proximo
    lento.proximo = None
    return inicio, segunda


def _mesclar(a: Optional[No], b: Optional[No], campo: str) -> tuple[No, No]:
    """Mescla duas sequências ordenadas sem criar nós de Registro."""
    cabeca = cauda = None
    while a is not None or b is not None:
        if b is None or (a is not None and _chave(a, campo) <= _chave(b, campo)):
            escolhido, a = a, a.proximo
        else:
            escolhido, b = b, b.proximo
        escolhido.proximo = None
        if cabeca is None:
            cabeca = escolhido
        else:
            cauda.proximo = escolhido
        cauda = escolhido
    return cabeca, cauda


def _merge_sort(inicio: Optional[No], campo: str) -> tuple[Optional[No], Optional[No]]:
    if inicio is None or inicio.proximo is None:
        return inicio, inicio
    esquerda, direita = _dividir(inicio)
    esquerda, _ = _merge_sort(esquerda, campo)
    direita, _ = _merge_sort(direita, campo)
    return _mesclar(esquerda, direita, campo)


def ordenar_merge_sort(lista: ListaEncadeada, campo: str = 'titulo') -> None:
    """Ordena a lista IN PLACE, religando os nós: O(n log n) tempo, O(log n) pilha."""
    if campo not in ('titulo', 'categoria'):
        raise ValueError('Campo inválido: escolha titulo ou categoria.')
    lista.cabeca, lista.cauda = _merge_sort(lista.cabeca, campo)
