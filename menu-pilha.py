#Alunos = Luiz Henrique Del Poso Vilalva, João Carlos (Bahia)

def vazia(pilha):
    return len(pilha) == 0

def empilhar(pilha, item):
    pilha.append(item)

def desempilhar(pilha):
    if vazia(pilha):
        return "pilha vazia!"
    return pilha.pop()


while True:
    print("1 - abrir o arquivo")
    print("0 - sair")
    op = int(input())
    if op == 0:
        break
    elif op == 1:
        nomearq = input("Entre com o nome do arquivo e extensão:")
        arquivo = open(nomearq, 'r', encoding='utf-8')
        print(arquivo.read())
        arquivo.close()

        pilha_desfazer = []
        pilha_refazer = []
        versao_atual = ""  
        while True:
            print("1 - Adicionar texto")
            print("2 - Substituir palavra no texto")
            print("3 - Remover palavra do texto")
            print("4 - Remover texto todo")
            print("5 - Desfazer")
            print("6 - Refazer")
            print("0 - sair")
            op = int(input(">>"))
            if op == 0:
                break
            elif op == 1:
                print("Digite o texto a ser inserido:")
                novo_texto = input(">>")
                arquivo = open(nomearq, 'a', encoding="utf-8")
                arquivo.write(' ' + novo_texto)
                arquivo.close()
                versao_anterior = versao_atual 
                versao_atual = versao_atual + ' ' + novo_texto
                empilhar(pilha_desfazer, versao_anterior)
                pilha_refazer = [] 
            elif op == 2:
                palavra = input("Digite a palavra que deseja substituir:")
                sub = input("Digite a nova palavra:")
                arquivo = open(nomearq, 'r', encoding="utf-8")
                versao_atual = arquivo.read()
                arquivo.close()
                versao_anterior = versao_atual 
                versao_atual = versao_atual.replace(palavra, sub)
                arquivo = open(nomearq, 'w', encoding='utf-8')
                arquivo.write(versao_atual)
                arquivo.close()
                empilhar(pilha_desfazer, versao_anterior)
                pilha_refazer = [] 
            elif op == 3:
                palavra = input("Digite a palavra que deseja remover:")
                arquivo = open(nomearq, 'r', encoding="utf-8")
                versao_atual = arquivo.read()
                arquivo.close()
                versao_anterior = versao_atual 
                versao_atual = versao_atual.replace(palavra, "")
                arquivo = open(nomearq, "w", encoding='utf-8')
                arquivo.write(versao_atual)
                arquivo.close()
                empilhar(pilha_desfazer, versao_anterior)
                pilha_refazer = [] 
            elif op == 4:
                arquivo = open(nomearq, 'w', encoding='utf-8')
                arquivo.close()
                versao_anterior = versao_atual  
                versao_atual = ""
                empilhar(pilha_desfazer, versao_anterior)
                pilha_refazer = []  
            elif op == 5:
                versao_anterior = desempilhar(pilha_desfazer)
                if versao_anterior == "pilha vazia!":
                    print("Nada para desfazer!")
                else:
                    pilha_refazer.append(versao_atual)
                    versao_atual = versao_anterior
                    arquivo = open(nomearq, 'w', encoding='utf-8')
                    arquivo.write(versao_atual)
                    arquivo.close()
                    print("Desfeito com sucesso. Texto anterior:", versao_anterior)
            elif op == 6:
                versao_refeito = desempilhar(pilha_refazer)
                if versao_refeito == "pilha vazia!":
                    print("Nada para refazer!")
                else:
                    pilha_desfazer.append(versao_atual)
                    versao_atual = versao_refeito
                    arquivo = open(nomearq, 'w', encoding='utf-8')
                    arquivo.write(versao_atual)
                    arquivo.close()
                    print("Refato com sucesso. Texto refato:", versao_refeito)
