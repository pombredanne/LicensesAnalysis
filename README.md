Duas abordagens existem.

A primeira é fazer crawling na árvore toda.
O impacto negativo desta abordagem é a demora em percorrer toda a árvore de cada pacote.
Muitos pacotes serão visitados repetidas vezes.
Maior número de requisições deverá ser feito.
Sua programação é fácil.
O impacto positivo é ter a árvore completa de um pacote em cada laço. Isto significa que por mais que sua composição demore, o estado do dados serão sempre consistentes.
Sua árvore pode ser gravada em um banco de dados não relacional.
Um JSON pode ser mantido em disco contendo toda a árvore.
Adotando NoSQL ou JSON em disco, para montar a matriz de dependência um processamento deverá ser feito sobre todos os nós da árvore de dependências.
Uma matriz de dependências pode ser mantida em disco ou em memória sob o mesmo algoritmo e análise aplicado à segunda abordagem.

A segunda abordagem é fazer crawling linear da lista de pacotes.
O impacto positivo é a velocidade em coletar as consistências e não 
Seu impacto negativo é ter consistência no grafo apenas quando todas as dependências forem coletadas.

Uma lista de adjacências ajuda em. perde em.
Uma matriz de adjacências ajuda em. perde em.
Uma árvore de dependências.
Uma lista de dependências.

lista de adjacências pode ser mantida em SQL, disco e memória.
Suas vantagens são: paralelismo, tolerância a falhas, consistência, facilidade no desenvolvimento, interface definida e amigável, disponibilidade, recorte de dados, linguagem de seleção e índices.
Seus drawbacks são: velocidade de inserção.
Pode ser utilizada como um meio para o formato final ou um formato final.