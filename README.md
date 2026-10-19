# Black Book Tutory

Pagina de download do Black Book Tutory, em tres partes.
Cada parte abre na noite da sua live e fecha as 10h do dia seguinte.

## Como funciona

A pagina nao tem servidor. O nome do arquivo de cada PDF e derivado da
palavra-chave anunciada ao vivo, por SHA-256 do sal mais a palavra
normalizada. Quem nao ouviu a palavra nao consegue montar a URL, e o
codigo-fonte da pagina nao revela nenhuma delas.

Isso esconde o arquivo, nao protege o arquivo. Quem recebeu a palavra
pode repassar o link. Para controle de acesso de verdade seria preciso
um servidor que valide quem baixa.

## Publicar os PDFs de cada noite

    python3 gerar-chave.py "tabuleiro"

O script imprime o nome que o arquivo precisa ter. Renomeie o PDF para
esse nome, coloque em `pdfs/` e faca um novo deploy.

## Janela de cada parte

| Parte | Abre            | Fecha           |
|-------|-----------------|-----------------|
| 1     | 20/10 as 20h    | 21/10 as 10h    |
| 2     | 21/10 as 20h    | 22/10 as 10h    |
| 3     | 22/10 as 17h    | 23/10 as 10h    |

As datas ficam no bloco `PARTES` no inicio do script em `index.html`.

## Antes da primeira live

A Parte 1 esta com `forcar:'aberto'` para dar para testar o fluxo
inteiro na URL publicada. Tire essa chave do objeto da Parte 1 em
`index.html` quando quiser que ela respeite o horario real.
