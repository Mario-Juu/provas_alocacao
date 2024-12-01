#  Trabalho 2 de Algoritmos
## Descrição
O projeto consiste no desenvolvimento de algoritmos para resolver um problema de alocação de provas baseado na coloração de grafos. A tarefa é atribuir o menor número possível de tipos de prova a mesas dispostas em uma sala de aula, de forma que nenhuma mesa adjacente tenha o mesmo tipo de prova. 

## Tecnologias
O projeto foi desenvolvido em Python devido à sua simplicidade, ampla disponibilidade de bibliotecas para manipulação de grafos (como networkx), e facilidade de integração com algoritmos personalizados.

## Como usar
1. Abra o CMD 
2. Confira se o Python está instalado
```
python --version
```
3. Confira se o pip está configurado.
```
pip --version 
```
4. Instale o networkx.
```
pip install networx
```
5. Execute o arquivo .py seguindo o seguinte padrão:
```
aloca_provas.py <numero_do_algoritmo> <caminho_das_salas)/sala<numero_da_sala>.txt
```


## Algoritmo 4

Afim de melhorar a eficiência dos algoritmos para esse problema de coloração de grafos, decidimos adotar como estratégia alterar o sistema de pontuação para um sistema de saturação (uma forma diferente de "pontuar"), usando o algoritmo DSatur como base.
O DSatur (Degree of Saturation) é um algoritmo clássico para coloração de grafos que funciona muito bem para resolver problemas como esse, onde desejamos minimizar o número de cores utilizadas. Ele utiliza o conceito de saturação, que mede o número de cores distintas já atribuídas aos vizinhos de um vértice.
### Explicação do Algoritmo DSatur

#### Saturação:

A saturação de um vértice é o número de cores distintas já atribuídas aos seus vizinhos.
Quanto maior a saturação, maior a chance de um vértice estar próximo de um conflito de cores.

#### Seleção de Vértices:

Em cada iteração, escolhemos o vértice com maior saturação.
Se houver empate, escolhemos o vértice com maior grau (número de vizinhos).

#### Atribuição de Cores:

Para o vértice escolhido, atribuímos a menor cor que não foi usada pelos seus vizinhos.

#### Atualização da Saturação:

Após atribuir uma cor a um vértice, atualizamos a saturação de todos os seus vizinhos não coloridos.


## Conclusão 
Afim de ter uma análise relacionada a eficiência dos algoritmos, segue a tabela com as devidas comparações: 

|    | Sala             |  Alg 1  |  Alg 2  |  Alg 3  |  Alg 4  |  alg5  |
|:--:|:-----------------|:-------:|:-------:|:-------:|:-------:|:------:|
| 0  | salas/sala1.txt  |   11    |   11    |   11    |   10    |   10   |
| 1  | salas/sala2.txt  |   12    |   12    |   11    |    9    |   9    |
| 2  | salas/sala3.txt  |   12    |   12    |   10    |   10    |   6    |
| 3  | salas/sala4.txt  |   14    |   14    |   12    |   12    |   12   |
| 4  | salas/sala5.txt  |   18    |   19    |   19    |   17    |   17   |
| 5  | salas/sala6.txt  |   18    |   18    |   19    |   16    |   17   |
| 7  | salas/sala8.txt  |   26    |   27    |   26    |   24    |   24   |
| 8  | salas/sala9.txt  |   26    |   26    |   25    |   25    |   25   |
| 9  | salas/sala10.txt |   25    |   26    |   25    |   25    |   25   |
| 10 | salas/sala11.txt |   29    |   31    |   31    |   29    |   29   |
| 11 | salas/sala12.txt |   30    |   31    |   31    |   28    |   29   |

Média:

|    | Sala             |  Alg 1  |  Alg 2  |  Alg 3  |  Alg 4  |  alg5  |
|:--:|:-----------------|:-------:|:-------:|:-------:|:-------:|:------:|
| 0  | Melhor Média  |   21.3    |   22.2    |   21.9    |   20.4    |   20.4   |


### Resumo dos Dados
#### Algoritmo 4 (DSatur):

Mostrou-se mais eficiente ou equivalente ao alg5 em 10 de 12 instâncias.
Reduziu significativamente o número de tipos de prova em casos como sala2 (9 contra 12 de outros algoritmos) e sala6 (16 contra 18-19).

#### Algoritmos 1, 2 e 3:

Tiveram desempenhos semelhantes em diversas salas, especialmente em grafos menos densos (e.g., sala1 e sala9).
O Algoritmo 3 frequentemente supera os Algoritmos 1 e 2, especialmente em grafos de maior densidade (e.g., sala7).

#### alg5:

Em geral, obteve soluções semelhantes ou ligeiramente melhores que o DSatur.
Ficou empatado ou levemente atrás do DSatur em casos como sala11 e sala12.

#### Casos com Melhores Resultados para DSatur (Algoritmo 4):

sala2: Redução de 3-4 tipos de prova em comparação aos Algoritmos 1, 2 e 3.

sala6: Redução consistente de 2-3 tipos de prova.

sala8: Reduziu em 2 tipos de prova, comparado ao Algoritmo 1.

#### Casos com Empate (ou Próximos):

Em grafos muito densos (sala10, sala11), os algoritmos DSatur e alg5 mostraram desempenhos semelhantes.
O DSatur demonstra eficiência equivalente ao alg5 na maioria das situações.

#### Algoritmos Mais Simples (1, 2 e 3):

Para grafos menos densos (sala1, sala3), as diferenças são menos marcantes.
No entanto, os algoritmos 2 e 3 são superados por DSatur e alg5 em grafos mais complexos.

#### Conclusão
O Algoritmo 4 (DSatur) foi a solução mais eficiente desenvolvida no projeto, demonstrando desempenho competitivo com o algoritmo alg5. Ele é particularmente vantajoso em grafos densos e estruturas complexas, onde a escolha dinâmica de vértices por saturação evita conflitos e reduz o número total de tipos de prova.

A simplicidade de implementação e eficiência computacional fazem do DSatur uma escolha recomendada para o problema, enquanto os algoritmos mais simples podem ser úteis para casos menores ou menos complexos.
