|  Method  |           Step           |     NPM     |     CRAN    |  RUBY GEMS  |
|:--------:|:------------------------:|:-----------:|:-----------:|:-----------:|
| Crawling |           Fetch Packages |      OK     |      OK     |      OK     |
| Crawling |             Create Index |      OK     | Unnecessary |      OK     |
| Crawling |       Get Adjacency List |      OK     |      OK     |      OK     |
| Offline  | Get Package Distribution |      OK     |      OK     |             |
| Manually |       Normalize Licenses |      OK     |      OK     |             |
| Manually |       Normalize Versions |      OK     |      OK     |             |
| Offline  | Get Package Distribution |      OK     |      OK     |             |
| Offline  |      Get Irregular Edges |      OK     |      OK     |             |
| Offline  |               Get Impact |      OK     |      OK     |             |

```json
{
  "name@version1": {
    "index": 0,
    "package": "name",
    "version": "version1",
    "regularityRate": 1.0,
    "globalRegularityRate": 0.75,
    "license": [
      "mit",
      "gpl 3"
    ],
    "dependencies": [
      {
        "package": "name@version2",
        "isRegular": true
      },
      {
        "package": "name@version3",
        "isRegular": null
      }
    ]
  }
```

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
O impacto positivo é a velocidade em coletar as dependenências e visitar apenas uma vez cada nó.
Seu impacto negativo é ter consistência no grafo apenas quando todas as dependências forem coletadas. Fissuras na coleta gerarão grafos que não condizem com o mundo real em alguns vértices.

Manter todos os dados em arquivos no disco implicam em buscar em arquivos, seu acesso é O(n). Seu desempenho pode ser mais lento que uma base de dados. Recursos tecnológicos não precisam ser robustos.
Manter todos os dados em memória implicam em possuir recursos tecnológicos.
Ambos os casos implicam em abrir mão dos benefícios de um gerenciador de dados.
Ambos os casos são vantajosos pela escrita num formato final.
Manter todos os dados em uma base de dados relacional permite paralelismo, tolerância a falhas, consistência, facilidade no desenvolvimento, interface definida e amigável, disponibilidade, recorte de dados, linguagem de seleção e índices.
Com algum cuidado não-relacionais também podem fornecer tais benefícios.
Seus drawbacks são: velocidade de inserção.

Uma lista de adjacências contém menos informações. Seu navegar pelos vértices não é feito em tempo constante.
SQL, NoSQL, disco e RAM
Pode ser utilizada como um meio para o formato final ou um formato final.

Uma matriz de adjacências navega facilmente pelos vértices. Garantir sua consistência é mais trabalhoso.
disco e RAM

Uma árvore de dependências contém dados redundantes mas mapeamento fiel ao mundo real e tempo constante para acessá-la.
NoSQL, disco e RAM

Uma lista de dependências contém dados redundantes e profundidade zero em cada árvore. Não é possível rastrear o momento em que as licenças foram violadas.
SQL, NoSQL, disco e RAM

![Pipeline](https://github.com/rmeloca/LicensesAnalysis/blob/master/PipelineLicencesAnalysis.png)
