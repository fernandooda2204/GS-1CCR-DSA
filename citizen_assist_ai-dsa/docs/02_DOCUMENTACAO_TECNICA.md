# Documentação técnica — Citizen Assist AI

**Disciplina:** Data Structures and Algorithms (DSA) • **Turma:** 1CC-FEV  
**Atividade:** Global Solution 2026.2 — Citizen Tech  
**Integrantes:** [PREENCHER NOMES E RMs]  
**Data dos testes:** [PREENCHER DATA DE EXECUÇÃO LOCAL]  
**Ambiente de entrega:** [PREENCHER VERSÃO DO PYTHON E SISTEMA OPERACIONAL]

## 1. Problema e recorte

O Citizen Assist AI organiza informações úteis ao cidadão. Nosso recorte é **informações de serviços de saúde**. O protótipo ajuda a localizar registros locais de exemplo, classificados por título e categoria, sem integrar uma API governamental. Os dados pré-carregados são **inteiramente fictícios e demonstrativos**, portanto não devem ser tratados como informação oficial.

## 2. Objetivo e funcionalidades

Permitir cadastrar, consultar por ID, pesquisar por título/categoria, atualizar, excluir, ordenar e analisar registros. Há tratamento de lista vazia, IDs repetidos, entradas inválidas e consultas sem resultado.

## 3. Modelo de registro

Classe `Registro` (em `registro.py`): `identificador` (inteiro positivo e único), `titulo`, `categoria`, `descricao`, `requisitos`, `local` (strings não vazias na interface). Exemplo: 30 / Vacinação de rotina / Prevenção / Informações sobre vacinação / Documento de identificação / Unidade de saúde.

## 4. Lista encadeada própria

`No` tem `registro` e referência `proximo`. `ListaEncadeada` mantém `cabeca`, `cauda`, `tamanho`. Os cadastros não são armazenados em uma lista Python. Percorrer começa em `cabeca`, segue `proximo` e termina em `None`.

Representação antes de ordenar o conjunto demonstrativo:

```text
cabeça -> [30] -> [10] -> [50] -> [20] -> [40] -> [15] -> None
```

**Inserção:** novo nó vai ao final, ajustando `cauda`; quando vazia, `cabeca` e `cauda` apontam para o mesmo nó.  
**Remoção:** encontra o ID e religa `anterior.proximo`; atualiza `cabeca` quando remove o primeiro e `cauda` quando remove o último.  
**Integridade:** `validar_integridade` verifica tamanho, cauda, término da cadeia e ciclos, para testes.

## 5. Busca linear

`busca_linear` percorre cada nó e testa se o termo aparece no título ou na categoria, ignorando diferenças entre maiúsculas/minúsculas. Retorna zero ou vários resultados. Busca por ID também é linear. O menu impede pesquisas em branco e apresenta aviso quando não encontra correspondência.

## 6. Ordenação implementada: Merge Sort

A implementação divide a cadeia em metades usando duas referências (`lento` e `rapido`), ordena cada metade recursivamente e as mescla em ordem **religando os nós originais**. Ela não usa `sorted` nem `list.sort`. A chave é título ou categoria com desempate pelo ID. Depois da mesclagem, a lista atualiza `cabeca` e `cauda`.

Exemplo de IDs em sequência de títulos após o Merge Sort: **50, 40, 10, 20, 15, 30**, pois os títulos são Aferição, Apoio, Consulta, Orientação, Saúde bucal, Vacinação. O algoritmo implementado é verificável em `algoritmos.py`.

## 7. Menu interativo

| Opção | Operação | Validação principal |
|---|---|---|
| 1 | Cadastro | ID positivo e sem duplicidade; textos obrigatórios |
| 2 | Consulta ID | ID inválido ou ausente |
| 3 | Pesquisa | Escolha de campo e termo não vazio |
| 4 | Atualização | ID existente; Enter mantém valor |
| 5 | Exclusão | ID existente; exige confirmação |
| 6 | Ordenação | Lista não vazia; critério 1 ou 2 |
| 7 | Análise | Total, categorias, IDs e integridade |
| 8 | Encerramento | Encerra o laço do menu |

## 8. Indicadores

`len(lista)` mostra o total de registros em O(1). `categorias()` percorre os nós e cria uma contagem temporária por categoria. Essa estrutura auxiliar **não substitui a lista encadeada** exigida.

## 9. Tratamento de erros

- ID digitado com letras, 0 ou número negativo: repete solicitação.
- ID já cadastrado: recusa antes da criação do registro.
- ID inexistente: informa ausência sem alterar a estrutura.
- Lista vazia: análise segura e ordenação com aviso.
- Opção de menu ou critério inválido: aviso e retorno ao menu.
- Campo textual vazio no cadastro: solicita novamente.

## 10. Estratégia de testes

A validação foi feita em três frentes, cobrindo os quatro grupos exigidos pelo enunciado: casos normais, registros inexistentes, entradas inválidas e operações com lista vazia.

1. **Testes unitários (`unittest`, 26 casos):** cadastro, percurso, duplicidade, consulta, atualização, remoção na cabeça/meio/cauda, remoção de único, lista vazia, pesquisa, ordenação, preservação dos nós, contagens, ciclo e demonstração.
2. **Roteiro automático (`--roteiro`):** reproduz o fluxo completo de operações sem digitação.
3. **Sessões do menu interativo:** exercitam a validação de entradas digitadas (opção inválida, ID com letras/zero/negativo, critério inválido, termo em branco) e o comportamento com lista vazia.

Para repetir:

```bash
python -m unittest discover -s testes -v
python testes/roteiro_testes.py
python main.py --roteiro
```

As sessões do menu podem ser repetidas com `python main.py` (lista vazia) e `python main.py --demo`, digitando as entradas registradas em `testes/evidencias/sessao_menu.txt`.

## 11. Análise de complexidade (Big-O)

Considere `n` como o número de registros e `k` como o custo de comparação de textos.

| Operação | Tempo | Memória auxiliar | Justificativa |
|---|---|---|---|
| Inserção física no fim | O(1) | O(1) por nó | Referência direta à cauda |
| Cadastro com ID único | O(n) | O(1), além do novo nó | Busca por duplicidade antes de inserir |
| Percurso completo | O(n) | O(1) | Visita cada nó uma vez |
| Consulta por ID | O(n) | O(1) | Busca linear; melhor caso O(1) |
| Pesquisa por texto | O(n·k) | O(r) para resultados | Examina até n registros, devolve r resultados |
| Atualização por ID | O(n) | O(1) | Busca linear; alteração é O(1) |
| Remoção por ID | O(n) | O(1) | Precisa achar nó e predecessor |
| Total de registros | O(1) | O(1) | `tamanho` é mantido nas operações |
| Total por categoria | O(n) esperado | O(c) | Percorre os nós e conta c categorias em dicionário auxiliar |
| Merge Sort da cadeia | O(n log n) | O(log n) pilha | Divide e mescla nós; não copia os registros |

Na pesquisa, o custo de criar `casefold` e buscar substring pode variar com o tamanho da string; O(n·k) é uma aproximação útil, sendo `k` esse custo. Para o Merge Sort, as comparações de texto também têm custo variável; O(n log n) conta comparações de chaves quando tratadas como custo constante.

**Por que Merge Sort?** Adequa-se à divisão e reconexão de listas encadeadas, com limite O(n log n) em casos comuns, sem precisar de acesso por índice.  
**Por que não busca binária?** Ela depende de acesso eficiente ao meio em sequência ordenada; a lista encadeada deste projeto não oferece acesso aleatório O(1), e a consulta por ID ocorre independentemente da ordenação atual.

## 12. Evidências de teste

Arquivos de evidência, com a saída real das execuções:

- `testes/evidencias/testes_unitarios.txt`: execução dos 26 testes de `unittest` (todos com resultado `ok`).
- `testes/evidencias/saida_roteiro.txt`: saída do roteiro automático (`python main.py --roteiro`).
- `testes/evidencias/sessao_menu.txt`: sessões do menu interativo com lista vazia e com entradas inválidas.

Nas tabelas abaixo, a coluna **Fonte** indica onde o resultado observado pode ser conferido: **R** = roteiro (número do passo), **M-A** = sessão do menu com lista vazia, **M-B** = sessão do menu com entradas inválidas, **U** = teste unitário.

### 12.1 Casos normais

| # | Caso | Entrada | Resultado esperado | Resultado observado | Fonte |
|---:|---|---|---|---|---|
| 1 | Cadastro de vários registros | IDs 30, 10, 50, 20, 40, 15 | Nós ligados na ordem de inserção | `cabeça -> [30] -> [10] -> [50] -> [20] -> [40] -> [15] -> None` | R 2 |
| 2 | Consulta por ID existente | ID 10 | Exibir "Consulta básica" | `Consulta básica` | R 4 |
| 3 | Pesquisa por categoria | Categoria "atendimento" (minúsculas) | IDs 10 e 15, ignorando maiúsculas | `[10, 15]` | R 6 |
| 4 | Pesquisa por título | Título "CONSULTA" | IDs 10 e 20 | `ok` | U `test_busca_por_titulo` |
| 5 | Atualização | ID 20, novo título "Orientação nutricional atualizada" | Retornar sucesso e manter o ID | `True`; o título novo aparece com ID 20 após a ordenação | R 8 e 11 |
| 6 | Remoção | ID 50 | Nó removido e cadeia religada | `True`; cadeia `[30] -> [10] -> [20] -> [40] -> [15]` | R 9 e 10 |
| 7 | Ordenação por título (Merge Sort) | Critério título | Ordem alfabética: 40, 10, 20, 15, 30 | `[(40, 'Apoio psicológico'), (10, 'Consulta básica'), (20, 'Orientação nutricional atualizada'), (15, 'Saúde bucal'), (30, 'Vacinação de rotina')]` | R 11 |
| 8 | Ordenação por categoria | Critério categoria | Agrupado por categoria, desempate por ID | `ok` | U `test_merge_sort_categoria` |
| 9 | Ordenação de lista grande | 127 registros em ordem decrescente | IDs 1 a 127 em ordem, mesmos nós | `ok` | U `test_merge_sort_grande` |
| 10 | Indicadores | Análise após as operações | Total 5; contagem por categoria; integridade OK | `Total de registros: 5`; Acolhimento 1, Atendimento 2, Orientação 1, Prevenção 1; `Integridade da lista: OK` | R 12 |
| 11 | Exclusão cancelada | ID 10, resposta `n` | Registro mantido | `Exclusão cancelada.` | M-B |

### 12.2 Registros inexistentes

| # | Caso | Entrada | Resultado esperado | Resultado observado | Fonte |
|---:|---|---|---|---|---|
| 12 | Consulta inexistente | ID 999 | Informar ausência sem erro | Roteiro: `None`; menu: `Registro não encontrado.` | R 5; M-B |
| 13 | Pesquisa sem resultado | Termo "inexistente" / "xyz" | Zero resultados | Roteiro: `[]`; menu: `Nenhum resultado encontrado.` | R 7; M-B |
| 14 | ID duplicado | Cadastro do ID 30 já existente | Cadastro recusado | Roteiro: `Recusada`; menu: `ID duplicado: cadastro recusado.` | R 3; M-B |
| 15 | Remoção inexistente | ID 9 em lista com ID 1 | Retornar falso, tamanho mantido | `ok` | U `test_remocao_inexistente` |
| 16 | Atualização inexistente | ID 99 | Retornar falso | `ok` | U `test_atualizar_inexistente` |

### 12.3 Entradas inválidas

| # | Caso | Entrada | Resultado esperado | Resultado observado | Fonte |
|---:|---|---|---|---|---|
| 17 | Opção de menu inválida | `9`, `abc`, Enter vazio | Aviso e retorno ao menu | `Opção inválida. Escolha de 1 a 8.` (nos três casos) | M-B |
| 18 | ID não numérico, zero ou negativo | `abc`, `0`, `-5` | Pedir o ID novamente | `ID inválido. Digite um número inteiro positivo.` (nos três casos) | M-B |
| 19 | Critério de pesquisa inválido | `x` | Aviso e retorno ao menu | `Critério inválido.` | M-B |
| 20 | Critério de ordenação inválido | `3` | Aviso e retorno ao menu | `Critério inválido.` | M-B |
| 21 | Termo de pesquisa em branco | Apenas espaços | Pedir o termo novamente | `Campo obrigatório. Tente novamente.` | M-B |
| 22 | Pesquisa em branco (função) | `busca_linear(lista, '  ')` | `ValueError` | `ok` | U `test_busca_vazia` |
| 23 | Campo inexistente (função) | Campo `local` na busca e na ordenação | `ValueError` | `ok` | U `test_campo_invalido` |

### 12.4 Operações com lista vazia

| # | Caso | Entrada | Resultado esperado | Resultado observado | Fonte |
|---:|---|---|---|---|---|
| 24 | Análise | Opção 7 | Total 0, cadeia vazia, integridade OK | `Total de registros: 0`; `cabeça -> None`; `Integridade da lista: OK` | R 1; M-A |
| 25 | Ordenação pelo menu | Opção 6 | Aviso de lista vazia | `Lista vazia. Não há registros para ordenar.` | M-A |
| 26 | Consulta, atualização e exclusão | Opções 2, 4 e 5 | Informar ausência sem erro | `Registro não encontrado.` (nas três opções) | M-A |
| 27 | Pesquisa | Opção 3, termo "Consulta" | Zero resultados | `Nenhum resultado encontrado.` | M-A |
| 28 | Remoção (função) | `remover(1)` | Retornar falso, lista íntegra | `ok` | U `test_remocao_lista_vazia` |
| 29 | Merge Sort (função) | Lista vazia | Sem erro, lista íntegra | `ok` | U `test_merge_sort_vazio` |

**Resumo:** todos os 29 casos tiveram resultado observado igual ao esperado.

## 13. Limitações e extensões

O sistema não conserva dados após encerrar e não verifica a atualização real de serviços. Persistência em arquivo, filtros adicionais e interfaces gráficas seriam extensões opcionais; não são necessárias para o objetivo de DSA.

## 14. Atendimento à rubrica (10 pontos)

| Critério do enunciado | Onde verificar | Peso |
|---|---|---:|
| Funcionamento, CRUD, menu, validação | `main.py`, testes | 3,0 |
| Lista encadeada e uso de Python | `lista_encadeada.py` | 3,0 |
| Busca e ordenação próprias | `algoritmos.py` | 2,0 |
| Organização, documentação e Big-O | `README.md`, este documento | 1,0 |
| Evidências e demonstração | `testes/evidencias/`, seção 12, `docs/03_APRESENTACAO.md` | 1,0 |
