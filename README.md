# Cadastro de Imóveis

Atividade N3 de Estrutura de Dados e Organização de Arquivos (Unifasipe).

Acadêmico: João Gabriel Catani Cortonezi

## O que é

Um sistema de cadastro de imóveis feito em Python, que roda no terminal. Pelo menu dá para incluir, alterar, excluir, pesquisar e listar imóveis. Os dados ficam salvos no arquivo `imoveis.json`, então não se perdem quando o programa fecha.

## Como rodar

Precisa ter o Python 3 instalado. Não precisa instalar mais nada, o programa usa só a biblioteca `json`, que já vem com o Python.

Abra o terminal dentro da pasta do projeto e rode:

```
python cadastro.py
```

## O que cada opção do menu faz

- **1 - Incluir imóvel:** pede o título, o bairro e o preço. O código é gerado pelo programa (o código do último imóvel + 1).
- **2 - Listar imóveis:** mostra todos os imóveis na ordem em que foram cadastrados.
- **3 - Excluir imóveis:** pede o código e remove o imóvel.
- **4 - Alterar informações dos imóveis:** pede o código e qual campo alterar (título, bairro ou preço).
- **5 - Pesquisar por termo:** procura o texto digitado no título e no bairro. Aceita um pedaço da palavra e não diferencia maiúsculas de minúsculas.
- **6 - Listar por preço:** lista ordenada do mais barato para o mais caro.
- **7 - Listar por bairro:** lista ordenada pelo bairro, em ordem alfabética.
- **0 - Sair:** fecha o programa.

## Como os dados são guardados

O `imoveis.json` guarda uma lista de imóveis. Cada imóvel tem 4 campos:

```json
{
    "codigo": 1,
    "titulo": "Casa com 3 quartos",
    "bairro": "Jardim Imperial",
    "preco": 450000
}
```

O programa lê esse arquivo ao abrir (`json.load`) e grava de novo (`json.dump`) toda vez que um imóvel é incluído, alterado ou excluído.
