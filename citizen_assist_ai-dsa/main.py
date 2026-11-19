"""Citizen Assist AI: catálogo demonstrativo de serviços de saúde.

Execução: python main.py           (base vazia)
         python main.py --demo    (base fictícia preenchida)
         python main.py --roteiro (demonstração não interativa)
"""
import argparse
from algoritmos import busca_linear, ordenar_merge_sort
from lista_encadeada import ListaEncadeada
from registro import Registro


EXEMPLOS = (
    (30, 'Vacinação de rotina', 'Prevenção', 'Informações sobre vacinação.', 'Documento de identificação', 'Unidade de saúde'),
    (10, 'Consulta básica', 'Atendimento', 'Orientação para consulta inicial.', 'Documento de identificação', 'Unidade de saúde'),
    (50, 'Aferição de pressão', 'Prevenção', 'Informação sobre acompanhamento.', 'Consultar unidade', 'Unidade de saúde'),
    (20, 'Orientação nutricional', 'Orientação', 'Informações sobre hábitos alimentares.', 'Consultar unidade', 'Serviço de referência'),
    (40, 'Apoio psicológico', 'Acolhimento', 'Informações sobre serviços de acolhimento.', 'Consultar unidade', 'Rede de atenção'),
    (15, 'Saúde bucal', 'Atendimento', 'Informações de atendimento odontológico.', 'Consultar unidade', 'Unidade de saúde'),
)


def popular_demo(lista: ListaEncadeada) -> None:
    for valores in EXEMPLOS:
        lista.cadastrar(Registro(*valores))


def ler_texto(rotulo: str, padrao: str = '') -> str:
    while True:
        resposta = input(f'{rotulo}' + (f' [{padrao}]' if padrao else '') + ': ').strip()
        if resposta:
            return resposta
        if padrao:
            return padrao
        print('Campo obrigatório. Tente novamente.')


def ler_id() -> int:
    while True:
        bruto = input('Identificador (inteiro positivo): ').strip()
        if bruto.isdecimal() and int(bruto) > 0:
            return int(bruto)
        print('ID inválido. Digite um número inteiro positivo.')


def exibir(registro: Registro) -> None:
    print('\n' + str(registro) + '\n' + '-' * 45)


def acao_cadastrar(lista: ListaEncadeada) -> None:
    identificador = ler_id()
    if lista.buscar_id(identificador) is not None:
        print('ID duplicado: cadastro recusado.')
        return
    registro = Registro(identificador, ler_texto('Título'), ler_texto('Categoria'),
                        ler_texto('Descrição'), ler_texto('Requisitos'), ler_texto('Local'))
    lista.cadastrar(registro)
    print('Registro cadastrado.')


def acao_consultar(lista: ListaEncadeada) -> None:
    registro = lista.buscar_id(ler_id())
    if registro is None:
        print('Registro não encontrado.')
    else:
        exibir(registro)


def acao_pesquisar(lista: ListaEncadeada) -> None:
    campo = input('Pesquisar por 1-Título ou 2-Categoria: ').strip()
    if campo not in ('1', '2'):
        print('Critério inválido.')
        return
    termo = ler_texto('Termo de pesquisa')
    encontrados = busca_linear(lista, termo, 'titulo' if campo == '1' else 'categoria')
    if not encontrados:
        print('Nenhum resultado encontrado.')
    for registro in encontrados:
        exibir(registro)
    if encontrados:
        print(f'{len(encontrados)} registro(s) encontrado(s).')


def acao_atualizar(lista: ListaEncadeada) -> None:
    registro = lista.buscar_id(ler_id())
    if registro is None:
        print('Registro não encontrado.')
        return
    print('Pressione Enter para manter o valor atual.')
    titulo = ler_texto('Título', registro.titulo)
    categoria = ler_texto('Categoria', registro.categoria)
    descricao = ler_texto('Descrição', registro.descricao)
    requisitos = ler_texto('Requisitos', registro.requisitos)
    local = ler_texto('Local', registro.local)
    lista.atualizar(registro.identificador, titulo, categoria, descricao, requisitos, local)
    print('Registro atualizado.')


def acao_excluir(lista: ListaEncadeada) -> None:
    identificador = ler_id()
    registro = lista.buscar_id(identificador)
    if registro is None:
        print('Registro não encontrado.')
        return
    confirmacao = input(f'Confirma a exclusão de {registro.titulo}? (s/N): ').strip().lower()
    if confirmacao == 's':
        lista.remover(identificador)
        print('Registro excluído.')
    else:
        print('Exclusão cancelada.')


def acao_ordenar(lista: ListaEncadeada) -> None:
    if not len(lista):
        print('Lista vazia. Não há registros para ordenar.')
        return
    escolha = input('Ordenar por 1-Título ou 2-Categoria: ').strip()
    if escolha not in ('1', '2'):
        print('Critério inválido.')
        return
    ordenar_merge_sort(lista, 'titulo' if escolha == '1' else 'categoria')
    print('Lista ordenada com Merge Sort:')
    for registro in lista:
        print(f'{registro.identificador:>3} | {registro.categoria} | {registro.titulo}')


def acao_analisar(lista: ListaEncadeada) -> None:
    print(f'Total de registros: {len(lista)}')
    print('Quantidade por categoria:')
    if len(lista) == 0:
        print('  (nenhuma)')
    else:
        for categoria, quantidade in lista.categorias().items():
            print(f'  {categoria}: {quantidade}')
    print('Representação da estrutura:', lista.cadeia_ids())
    print('Integridade da lista:', 'OK' if lista.validar_integridade() else 'FALHA')


def roteiro_automatico() -> None:
    """Saída reproduzível para demonstrar operações sem depender de digitação."""
    lista = ListaEncadeada()
    print('1. Lista inicialmente vazia:')
    acao_analisar(lista)
    popular_demo(lista)
    print('\n2. Cadastro de seis registros (IDs 30, 10, 50, 20, 40, 15):')
    print(lista.cadeia_ids())
    print('\n3. Tentativa de ID duplicado (30):', 'Recusada' if not lista.cadastrar(Registro(*EXEMPLOS[0])) else 'ERRO')
    print('\n4. Consulta existente (10):', lista.buscar_id(10).titulo)
    print('5. Consulta inexistente (999):', lista.buscar_id(999))
    print('6. Busca linear pela categoria Atendimento:', [r.identificador for r in busca_linear(lista, 'atendimento', 'categoria')])
    print('7. Busca sem resultados:', busca_linear(lista, 'inexistente'))
    print('8. Atualização do ID 20:', lista.atualizar(20, 'Orientação nutricional atualizada', 'Orientação', 'Novo texto', 'Consultar unidade', 'Serviço de referência'))
    print('9. Remoção do ID 50:', lista.remover(50))
    print('10. Antes da ordenação:', lista.cadeia_ids())
    ordenar_merge_sort(lista, 'titulo')
    print('11. Depois do Merge Sort por título:', [(r.identificador, r.titulo) for r in lista])
    print('12. Indicadores e integridade:')
    acao_analisar(lista)


def executar(lista: ListaEncadeada) -> None:
    opcoes = {
        '1': acao_cadastrar, '2': acao_consultar, '3': acao_pesquisar,
        '4': acao_atualizar, '5': acao_excluir, '6': acao_ordenar,
        '7': acao_analisar,
    }
    while True:
        print('\n=== CITIZEN ASSIST AI | SAÚDE ===')
        print('1-Cadastrar | 2-Consultar ID | 3-Pesquisar | 4-Atualizar')
        print('5-Excluir   | 6-Ordenar      | 7-Analisar   | 8-Sair')
        try:
            opcao = input('Escolha uma opção: ').strip()
            if opcao == '8':
                print('Sistema encerrado.')
                break
            acao = opcoes.get(opcao)
            if acao is None:
                print('Opção inválida. Escolha de 1 a 8.')
            else:
                acao(lista)
        except (EOFError, KeyboardInterrupt):
            print('\nSistema encerrado.')
            break


def main() -> None:
    parser = argparse.ArgumentParser(description='Citizen Assist AI: serviços de saúde (dados fictícios)')
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument('--demo', action='store_true', help='Abre o menu preenchido com registros fictícios')
    grupo.add_argument('--roteiro', action='store_true', help='Roda demonstração automática, sem entrada')
    args = parser.parse_args()
    if args.roteiro:
        roteiro_automatico()
        return
    lista = ListaEncadeada()
    if args.demo:
        popular_demo(lista)
        print('Demonstração: seis registros fictícios carregados.')
    executar(lista)


if __name__ == '__main__':
    main()
