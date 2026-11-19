# Roteiro de apresentação — Citizen Assist AI

**Duração sugerida:** 10 a 12 minutos.  
**Integrantes:** [PREENCHER NOMES E RMs]  
**Demonstração interativa:** `python main.py --demo`  
**Demonstração automática:** `python main.py --roteiro`

## Divisão sugerida

| Pessoa | Tema | Tempo |
|---|---|---|
| 1 | Contexto, recorte e registros | 2 min |
| 2 | Estrutura da lista encadeada, inserção e remoção | 3 min |
| 3 | Busca linear e Merge Sort | 3 min |
| 4 | Menu, Big-O, testes e demonstração | 3 min |

## Sequência de slides ou fala

**1. Problema (1 min):** O cidadão precisa localizar informações de serviços de saúde. Escolhemos simular um catálogo de informações demonstrativas, sem APIs externas, para focar em estruturas de dados e algoritmos.

**2. Modelo (1 min):** Cada registro contém ID único, título, categoria, descrição, requisitos e local. O ID permite consulta, atualização e exclusão.

**3. Estrutura própria (2 min):** A classe `No` guarda um registro e uma referência `proximo`. `ListaEncadeada` mantém cabeça, cauda e tamanho. Ao inserir no fim, conectamos o próximo nó à cauda; ao remover, ligamos o predecessor ao sucessor, tratando cabeça e cauda separadamente.

**4. Algoritmos (2 min):** Para busca, percorremos os nós e comparamos texto. Para ordenar, usamos Merge Sort com divisão da cadeia em duas metades, ordenação recursiva e mesclagem. Não usamos `sorted()` nos registros.

**5. Big-O (1 min):** Inserção física é O(1); cadastro com verificação de unicidade é O(n); busca e remoção são O(n); Merge Sort realiza O(n log n) comparações e usa O(log n) na pilha recursiva, desconsiderando tamanho das strings.

**6. Validação e demo (3 min):** Mostrar o menu, uma consulta, um caso de duplicidade, uma pesquisa, uma remoção, uma ordenação e os indicadores. Apresentar a saída dos testes unitários.

**7. Fechamento (1 min):** Comentar que dados são fictícios e persistência é uma melhoria possível. Mostrar que a funcionalidade principal está nos nós e algoritmos implementados.

## Demonstração interativa em 11 passos

Abra `python main.py --demo`, depois:

| Passo | No menu | O que fazer e explicar |
|---:|---|---|
| 1 | 7 | Mostre 6 registros e `cabeça -> [30] -> [10] -> ...` |
| 2 | 2 | Consulte ID 10; exibe Consulta básica |
| 3 | 2 | Consulte ID 999; mostra não encontrado |
| 4 | 1 | Tente cadastrar ID 30; cadastro duplicado recusado |
| 5 | 3 | Pesquise categoria Atendimento; encontra IDs 10 e 15 |
| 6 | 3 | Pesquise título inexistente; mostra zero resultados |
| 7 | 4 | Atualize ID 20; altere o título e mantenha demais campos com Enter |
| 8 | 5 | Exclua ID 50, confirmando com `s` |
| 9 | 7 | Confira que o tamanho virou 5 e a cadeia está íntegra |
| 10 | 6 | Ordene por título, mostre o Merge Sort |
| 11 | 7 e 8 | Reexiba cadeia ordenada, indicadores e encerre |

**Alternativa segura para demo:** `python main.py --roteiro` apresenta o fluxo completo sem necessidade de digitar.

## 22 perguntas para ensaiar

1. **Por que criar um catálogo de saúde?** É um recorte viável para aplicar operações de DSA a informações úteis ao cidadão.
2. **Os dados são oficiais?** Não, são registros fictícios para demonstrar a estrutura.
3. **Por que Python?** Permite representar nós por objetos e referências explícitas.
4. **O que é um nó?** Objeto que guarda um registro e a referência ao próximo nó.
5. **O que é cabeça?** Referência ao primeiro nó, ou `None` se vazio.
6. **O que é cauda?** Referência ao último nó, usada para inserir no fim diretamente.
7. **Como inserir na lista vazia?** Atribuímos o novo nó à cabeça e à cauda.
8. **Como inserir no fim?** Fazemos `cauda.proximo = novo` e atualizamos a cauda.
9. **Como remover a cabeça?** Fazemos a cabeça apontar para o segundo nó; se for o único, limpamos a cauda.
10. **Como remover um nó do meio?** Ligamos o anterior ao sucessor do removido.
11. **Como remover a cauda?** Ligamos o anterior a `None` e o definimos como nova cauda.
12. **Como impedir IDs duplicados?** Buscamos o ID antes de criar o novo nó.
13. **Por que a inserção é O(1), mas o cadastro é O(n)?** A inserção usa a cauda; a verificação de ID percorre a lista.
14. **Como funciona a busca linear?** Visita os nós sequencialmente até encontrar ou esgotar a lista.
15. **Por que não busca binária?** O acesso ao meio da lista encadeada não é constante e a lista pode estar desordenada.
16. **Por que Merge Sort?** Ele divide e intercala nós com custo O(n log n) de comparações e sem precisar de acesso por índice.
17. **Como o Merge Sort divide a lista?** Usa ponteiros lento e rápido para descobrir a metade e separar a cadeia.
18. **A ordenação cria novos registros?** Não; ela reconecta os nós existentes.
19. **Qual é o custo da remoção?** O(n), devido à busca pelo nó e seu predecessor.
20. **Como lidamos com lista vazia?** Consultas retornam ausência; análises são seguras e a ordenação avisa.
21. **Como testamos integridade?** Conferindo cabeça, cauda, tamanho, último `proximo` e ciclos.
22. **Que melhoria futura faria sentido?** Persistir os registros em arquivo e conectar dados reais somente depois de validar fontes e atualização.

## Recomendações de demonstração

- Não decorem apenas as falas: mostrem em `lista_encadeada.py` a inserção e a remoção.
- Expliquem o uso de `proximo` em `algoritmos.py` durante a mesclagem.
- Executem `python -m unittest discover -s testes -v` antes de apresentar.
- Mostrem a diferença entre **cadastro O(n)** e **inserção física O(1)**.
