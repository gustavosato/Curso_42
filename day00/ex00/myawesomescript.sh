# #!/bin/sh

#curl -sI $1: Estamos usando o curl para fazer uma requisição HTTP para o bit.ly descrito.
#grep -i "location: ": O comando grep é usado para filtrar as linhas de saída do comando curl e encontrar aquela que contém a palavra "location:"  -i torna a pesquisa case-insensitive
#cut -d" " -f2: O comando cut` é usado para extrair a segunda coluna de texto da saída do comando anterior, utilizando o espaço em branco como delimitador.

curl -sI $1 | grep -i "Location" | cut -d' ' -f2