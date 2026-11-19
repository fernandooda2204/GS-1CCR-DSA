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

Testes unitários com `unittest` verificam cadastro, percurso, duplicidade, consulta, atualização, remoção na cabeça/meio/cauda, remoção de único, lista vazia, pesquisa, ordenação, preservação dos nós, contagens, ciclo e demonstração. Um roteiro adicional reproduz operações e salva as evidências em `testes/evidencias/`.

Para repetir:

```bash
python -m unittest discover -s testes -v
python testes/roteiro_testes.py
python main.py --roteiro
```

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

As evidências automatizadas estão em:

- `testes/evidencias/testes_unitarios.txt`: execução real dos testes de `unittest` neste pacote.
- `testes/evidencias/saida_roteiro.txt`: demonstração reproduzível da busca, duplicidade, atualização, remoção, ordenação e análise.

| Caso | Entrada | Resultado esperado | Resultado observado |
|---|---|---|---|
| Cadastro normal | IDs 30,10,50 | Cadeia preserva sequência | Conferir saída do roteiro |
| ID duplicado | Cadastro de ID 30 duas vezes | Segundo registro recusado | Conferir saída do roteiro |
| Consulta existente | ID 10 | Exibe Consulta básica | Conferir saída do roteiro |
| Consulta inexistente | ID 999 | Não encontrado | Conferir saída do roteiro |
| Pesquisa | Categoria Atendimento | IDs 10 e 15 | Conferir saída do roteiro |
| Pesquisa inexistente | Termo inexistente | Zero resultados | Conferir saída do roteiro |
| Atualização | ID 20 | Dados modificados | Conferir saída do roteiro |
| Remoção | ID 50 | Nó removido, cadeia íntegra | Conferir saída do roteiro |
| Ordenação | Campo título | Títulos em ordem alfabética | Conferir saída do roteiro |
| Lista vazia | Remoção / Merge Sort | Sem erro e vazia | Testes unitários |
| Entrada inválida | Busca em branco ou campo inválido | Rejeição segura | Testes unitários |

**Observação:** a tabela acima é um guia de leitura dos testes. Substitua por resultados e capturas obtidos no computador de entrega, se o professor exigir evidência local. A validade do resultado observado deve ser verificada pela execução, não apenas pelo texto da tabela.

## 13. Limitações e extensões

O sistema não conserva dados após encerrar e não verifica a atualização real de serviços. Persistência em arquivo, filtros adicionais e interfaces gráficas seriam extensões opcionais; não são necessárias para o objetivo de DSA.

## 14. Atendimento à rubrica (10 pontos)

| Critério do enunciado | Onde verificar | Peso |
|---|---|---:|
| Funcionamento, CRUD, menu, validação | `main.py`, testes | 3,0 |
| Lista encadeada e uso de Python | `lista_encadeada.py` | 3,0 |
| Busca e ordenação próprias | `algoritmos.py` | 2,0 |
| Organização, documentação e Big-O | `README.md`, este documento | 1,0 |
| Evidências e demonstração | `testes/evidencias/`, roteiro oral | 1,0 |

A tabela mapeia requisitos para componentes, **não garante nota**: a avaliação depende da execução, dos critérios do professor e da apresentação.
