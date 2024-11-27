from sys import argv
import sys

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

# Executando no terminal 
# exemplo: python soma_ingredientes.py Sim Sim Sim Sim Sim Sim

if __name__ == '__main__':
    terminal_tem_cenoura = sys.argv[1] == "Sim"
    terminal_tem_acucar = sys.argv[2] == "Sim"
    terminal_tem_oleo = sys.argv[3] == "Sim"
    terminal_tem_fermento = sys.argv[4] == "Sim"
    terminal_tem_leite = sys.argv[5] == "Sim"
    terminal_tem_ovos = sys.argv[6] == "Sim"  

    total = soma_ingredientes(terminal_tem_cenoura, terminal_tem_acucar, terminal_tem_oleo, terminal_tem_fermento, terminal_tem_leite, terminal_tem_ovos)      
    
    print("Executando soma_ingredientes.py")
    print("O preço total dos ingredientes é: ", total)
    print("Fim do programa soma_ingredientes.py")