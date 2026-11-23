import json

with open("imoveis.json", "r", encoding="utf-8") as arquivo:
    imoveis = json.load(arquivo)

def mostrar(imovel):
    print("COD:",imovel["codigo"], "Título:",imovel["titulo"], "Bairro:",imovel["bairro"], "Valor:",imovel["preco"])
    
def carregar():
    for imovel in imoveis:
        mostrar(imovel)

def salvar():
    with open("imoveis.json", "w", encoding="utf-8") as arquivo:
        json.dump(imoveis, arquivo, ensure_ascii=False, indent=4)

def incluir():
    if len(imoveis) == 0:
        codigo = 1
    else:
        codigo = imoveis[-1]["codigo"] + 1

    titulo = input("Qual o titulo do anuncio do imóvel?:")
    bairro = input("Qual o bairro do imóvel?:")
    preco = float(input("Qual o preço do imóvel?:"))
    
    imoveis.append({
        "codigo": codigo,
        "titulo": titulo,
        "bairro": bairro,
        "preco": preco
    })

    salvar()

def excluir():
    codigo = int(input("Qual o código do imóvel para excluir?:"))

    for imovel in imoveis:
        if imovel["codigo"] == codigo:
            imoveis.remove(imovel)
            salvar()
            print("Imóvel excluido")
            return
    print("Imóvel não encontrado")

def alterar():
    codigo = int(input("Qual o código do imóvel que vamos alterar?:"))

    for imovel in imoveis:

        if imovel["codigo"] == codigo:
            print("1 - Título")
            print("2 - Bairro")
            print("3 - Preço")
            campoAlterado = input("Qual campo deseja alterar?:")

            if campoAlterado == "1":
                imovel["titulo"] = input("Qual o novo Título do Imóvel?:")
            elif campoAlterado == "2":
                imovel["bairro"] = input("Qual o novo Bairro do Imóvel?:")
            elif campoAlterado == "3":
                imovel["preco"] = float(input("Qual o novo Preço do Imóvel?:"))
            else:
                print("Opção não encontrada.")
                return
            salvar()
            print("Imóvel alterado.")
            return
        
    print("Imóvel não encontrado.")

def pesquisar():
    termo = input("Digite o texto para pesquisar:").lower()
    achou = False

    for imovel in imoveis:
        if termo in imovel["titulo"].lower() or termo in imovel["bairro"].lower():
            mostrar(imovel)
            achou = True

    if achou == False:
        print("Nenhum imóvel encontrado.")

def pega_preco(imovel):
    return imovel["preco"]

def listar_por_preco():
    ordenados = sorted(imoveis, key=pega_preco)
    for imovel in ordenados:
        mostrar(imovel)

def pega_bairro(imovel):
    return imovel["bairro"]

def listar_por_bairro():
    ordenados = sorted(imoveis, key=pega_bairro)
    for imovel in ordenados:
        mostrar(imovel)

while True:
    print()
    print("1 - Incluir imóvel")
    print("2 - Listar imóveis")
    print("3 - Excluir imóveis")
    print("4 - Alterar informações dos imóveis")
    print("5 - Pesquisar por termo")
    print("6 - Listar por preço")
    print("7 - Listar por bairro")
    print("0 - Sair")
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        incluir()
    elif opcao == "2":
        carregar()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        alterar()
    elif opcao == "5":
        pesquisar()
    elif opcao == "6":
        listar_por_preco()
    elif opcao == "7":
        listar_por_bairro()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")