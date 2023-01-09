# O-jogo-da-vida

## [Link](https://davidsatag.github.io/O-jogo-da-vida/) do Jogo da Vida em vue

## O jogo da vida de Conway
O **Jogo da Vida** (um exemplo de autômato celular) é jogado em uma grade retangular bidimensional infinita de células. Cada célula pode estar viva ou morta. O status de cada célula muda a cada turno do jogo (também chamado de geração), dependendo do status dos 8 vizinhos dessa célula. Vizinhos de uma célula são células que tocam essa célula, seja horizontal, vertical ou diagonal dessa célula.

O padrão inicial é a primeira geração. A segunda geração evolui da aplicação das regras simultaneamente a todas as células do tabuleiro de jogo, ou seja, nascimentos e mortes acontecem simultaneamente. Depois, as regras são aplicadas iterativamente para criar as gerações futuras. Para cada geração do jogo, o status de uma célula na próxima geração é determinado por um conjunto de regras. Estas regras simples são as seguintes:

- Se a célula estiver viva, ela permanecerá viva se tiver 2 ou 3 vizinhos vivos
- Se a célula estiver morta, ela ganha vida apenas no caso de ter 3 vizinhos vivos

## Como rodar os projetos
### Python
*No diretório jdvpython digitar:*
- python3 -m jdv

### Vue
*No diretório jdvvue*
- npm install
- npm run build
- npm run serve

