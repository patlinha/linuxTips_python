# aqui coeça o escopo global
nome = "Global"
numero = 1
flag = True

def funcao():
#aqui começa o escopo local

    def funcao_interna():
        #aqui começa o escopo local da funcao_interna
        nome = "Interna"
        print(nome)
        return nome
        #aqui termina o escopo local da funcao_interna   
        
    nome = "Local"
    print("Print locals(): ",locals())
    print(nome)
    return nome
#aqui termina o escopo local

funcao()

print("#"*30)
print("print globals(): ",globals()) #imprime todas as variáveis globais
print("#"*30)
print(globals()["nome"]) #é equivalente a :
print(nome)


