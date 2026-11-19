"""Testes automáticos da estrutura e algoritmos (unittest da biblioteca padrão)."""
import unittest
from registro import Registro
from lista_encadeada import ListaEncadeada
from algoritmos import busca_linear, ordenar_merge_sort
from main import popular_demo


def criar(identificador, titulo='Serviço', categoria='Saúde'):
    return Registro(identificador, titulo, categoria, 'Descrição', 'Documento', 'Unidade')


class TesteLista(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeada()

    def test_inicialmente_vazia(self):
        self.assertEqual(len(self.lista), 0)
        self.assertIsNone(self.lista.buscar_id(1))
        self.assertTrue(self.lista.validar_integridade())

    def test_insercao_e_percurso(self):
        for numero in (30, 10, 50):
            self.assertTrue(self.lista.cadastrar(criar(numero)))
        self.assertEqual([r.identificador for r in self.lista], [30, 10, 50])
        self.assertEqual(self.lista.cabeca.registro.identificador, 30)
        self.assertEqual(self.lista.cauda.registro.identificador, 50)
        self.assertTrue(self.lista.validar_integridade())

    def test_id_duplicado_recusado(self):
        self.lista.cadastrar(criar(10))
        self.assertFalse(self.lista.cadastrar(criar(10, 'Outro')))
        self.assertEqual(len(self.lista), 1)

    def test_remocao_lista_vazia(self):
        self.assertFalse(self.lista.remover(1))
        self.assertTrue(self.lista.validar_integridade())

    def test_remocao_inexistente(self):
        self.lista.cadastrar(criar(1))
        self.assertFalse(self.lista.remover(9))
        self.assertEqual(len(self.lista), 1)

    def test_remocao_primeiro(self):
        for x in (1, 2, 3):
            self.lista.cadastrar(criar(x))
        self.assertTrue(self.lista.remover(1))
        self.assertEqual([r.identificador for r in self.lista], [2, 3])
        self.assertTrue(self.lista.validar_integridade())

    def test_remocao_meio(self):
        for x in (1, 2, 3):
            self.lista.cadastrar(criar(x))
        self.assertTrue(self.lista.remover(2))
        self.assertEqual([r.identificador for r in self.lista], [1, 3])
        self.assertTrue(self.lista.validar_integridade())

    def test_remocao_ultimo(self):
        for x in (1, 2, 3):
            self.lista.cadastrar(criar(x))
        self.assertTrue(self.lista.remover(3))
        self.assertEqual([r.identificador for r in self.lista], [1, 2])
        self.assertEqual(self.lista.cauda.registro.identificador, 2)
        self.assertTrue(self.lista.validar_integridade())

    def test_remocao_unico_e_reinsercao(self):
        self.lista.cadastrar(criar(1))
        self.assertTrue(self.lista.remover(1))
        self.assertIsNone(self.lista.cabeca)
        self.assertIsNone(self.lista.cauda)
        self.assertTrue(self.lista.cadastrar(criar(2)))
        self.assertTrue(self.lista.validar_integridade())

    def test_atualizar_existente(self):
        self.lista.cadastrar(criar(1))
        self.assertTrue(self.lista.atualizar(1, 'Novo', 'Categoria', 'Desc', 'Req', 'Local'))
        self.assertEqual(self.lista.buscar_id(1).titulo, 'Novo')
        self.assertEqual(self.lista.buscar_id(1).local, 'Local')

    def test_atualizar_inexistente(self):
        self.assertFalse(self.lista.atualizar(99, 'A', 'B', 'C', 'D', 'E'))

    def test_contagem_categorias(self):
        self.lista.cadastrar(criar(1, categoria='A'))
        self.lista.cadastrar(criar(2, categoria='B'))
        self.lista.cadastrar(criar(3, categoria='A'))
        self.assertEqual(self.lista.categorias(), {'A': 2, 'B': 1})

    def test_cadeia_ids_vazia(self):
        self.assertEqual(self.lista.cadeia_ids(), 'cabeça -> None')

    def test_integridade_ciclo_detectado(self):
        self.lista.cadastrar(criar(1))
        self.lista.cauda.proximo = self.lista.cabeca
        self.assertFalse(self.lista.validar_integridade())


class TesteAlgoritmos(unittest.TestCase):
    def setUp(self):
        self.lista = ListaEncadeada()
        self.lista.cadastrar(criar(30, 'Vacinação', 'Prevenção'))
        self.lista.cadastrar(criar(10, 'Consulta', 'Atendimento'))
        self.lista.cadastrar(criar(50, 'Aferição', 'Prevenção'))
        self.lista.cadastrar(criar(20, 'Consulta avançada', 'Atendimento'))

    def test_busca_por_titulo(self):
        self.assertEqual([r.identificador for r in busca_linear(self.lista, 'CONSULTA')], [10, 20])

    def test_busca_por_categoria(self):
        self.assertEqual([r.identificador for r in busca_linear(self.lista, 'prevenção', 'categoria')], [30, 50])

    def test_busca_inexistente(self):
        self.assertEqual(busca_linear(self.lista, 'abc'), [])

    def test_busca_vazia(self):
        with self.assertRaises(ValueError):
            busca_linear(self.lista, '  ')

    def test_campo_invalido(self):
        with self.assertRaises(ValueError):
            busca_linear(self.lista, 'teste', 'local')
        with self.assertRaises(ValueError):
            ordenar_merge_sort(self.lista, 'local')

    def test_merge_sort_titulo(self):
        nodos_antes = {id(no) for no in capturar_nos(self.lista)}
        ordenar_merge_sort(self.lista, 'titulo')
        self.assertEqual([r.identificador for r in self.lista], [50, 10, 20, 30])
        self.assertEqual(nodos_antes, {id(no) for no in capturar_nos(self.lista)})
        self.assertTrue(self.lista.validar_integridade())

    def test_merge_sort_categoria(self):
        ordenar_merge_sort(self.lista, 'categoria')
        self.assertEqual([r.identificador for r in self.lista], [10, 20, 30, 50])
        self.assertTrue(self.lista.validar_integridade())

    def test_merge_sort_id_desempata(self):
        self.lista.cadastrar(criar(5, 'consulta'))
        ordenar_merge_sort(self.lista, 'titulo')
        self.assertEqual([r.identificador for r in self.lista], [50, 5, 10, 20, 30])

    def test_merge_sort_vazio(self):
        vazia = ListaEncadeada()
        ordenar_merge_sort(vazia)
        self.assertTrue(vazia.validar_integridade())

    def test_merge_sort_unico(self):
        unica = ListaEncadeada()
        unica.cadastrar(criar(1))
        ordenar_merge_sort(unica)
        self.assertEqual([r.identificador for r in unica], [1])
        self.assertTrue(unica.validar_integridade())

    def test_merge_sort_grande(self):
        lista = ListaEncadeada()
        for i in range(127, 0, -1):
            lista.cadastrar(criar(i, f'Título {i:03d}'))
        ordenar_merge_sort(lista)
        self.assertEqual([r.identificador for r in lista], list(range(1, 128)))
        self.assertTrue(lista.validar_integridade())

    def test_demo_seis_registros(self):
        lista = ListaEncadeada()
        popular_demo(lista)
        self.assertEqual([r.identificador for r in lista], [30, 10, 50, 20, 40, 15])
        self.assertTrue(lista.validar_integridade())


def capturar_nos(lista):
    atual = lista.cabeca
    while atual is not None:
        yield atual
        atual = atual.proximo


if __name__ == '__main__':
    unittest.main()
