# Citizen Assist AI — Global Solution 2026.2 (DSA)

Protótipo de terminal em **Python 3.8+**, sem dependências externas, para catalogar informações **fictícias** de serviços de saúde. 

## Execução

No terminal, dentro da pasta `citizen_assist_ai`:

```bash
python main.py
python main.py --demo
python main.py --roteiro
python -m unittest discover -s testes -v
python testes/roteiro_testes.py
```

No Windows, `py` pode substituir `python`. `--demo` inicia o **menu interativo** com seis cadastros fictícios. `--roteiro` produz uma **demonstração automática**. Os dados existem apenas durante a execução; não há persistência em disco.

## Menu

1. Cadastrar registro (verifica ID único)
2. Consultar por ID
3. Pesquisar por título ou categoria, com busca linear
4. Atualizar campos de um registro
5. Excluir registro (com confirmação)
6. Ordenar por título ou categoria com Merge Sort sobre os nós
7. Analisar total, quantidade por categoria, cadeia encadeada e integridade
8. Encerrar

## Estrutura

```text
citizen_assist_ai/
├── main.py
├── registro.py
├── lista_encadeada.py
├── algoritmos.py
├── README.md
├── docs/
│   ├── 02_DOCUMENTACAO_TECNICA.md
│   └── 03_APRESENTACAO.md
└── testes/
    ├── test_estrutura.py
    ├── roteiro_testes.py
    └── evidencias/
        ├── testes_unitarios.txt
        └── saida_roteiro.txt
```

## Validação

- IDs devem ser inteiros positivos e únicos.
- Campos obrigatórios não aceitam texto em branco no cadastro.
- Menu e critério de busca/ordenação rejeitam opções desconhecidas.
- Operações em registros inexistentes são tratadas e não quebram a lista.
- Atualizar preserva o ID; os nós são ligados explicitamente por `proximo`.

## Documentação

Consulte `docs/02_DOCUMENTACAO_TECNICA.md` para modelo, análise Big-O e evidências; e `docs/03_APRESENTACAO.md` para roteiro oral e perguntas.

**Antes da entrega:** preencher nomes e RM e atualizar informações do ambiente de execução. Confirme com o professor se a entrega deve ser em ZIP, GitHub ou PDF.
