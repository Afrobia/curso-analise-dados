preco_cenoura= 4.5
preco_oleo= 12
preco_fermento= 15
preco_leite= 5
preco_acucar= 6
preco_ovos= 14

def soma_ingredientes(tem_cenoura, tem_acucar, tem_oleo, tem_fermento, tem_leite, tem_ovos):
    soma = 0
    if tem_cenoura:
        soma += preco_cenoura
    if tem_acucar:
        soma += preco_acucar
    if tem_oleo:
        soma += preco_oleo
    if tem_fermento:
        soma += preco_fermento
    if tem_leite:
        soma += preco_leite
    if tem_ovos:
        soma += preco_ovos
    return soma

total = soma_ingredientes(True, True, True, True, True, True)

print("O preço total dos ingredientes é: ", total)