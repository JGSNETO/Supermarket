# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:21:05 2022

@author: Jose Gomes
"""

from typing import List, Dict
from time import sleep

from models.produto import Produto
from models.helper import formata_float_str_moeda

#Produtos serão uma lista
produtos: List[Produto] = []
#Lista de produtos e quantidade por isso uma lista de dicionário
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    
    menu()
    
def menu() -> None:
    print('*****************************************')
    print('********************Menu*****************')
    
    print('Seleciona uma oção abaixo:')
    print('1-Cadastrar produto')
    print('2-Listar produto')
    print('3-Comprar produto')
    print('4-Visualizar carrinho')
    print('5-Fechar pedido')
    print('6-Sair do sistema')
    
    opcao: int = int(input('Escolha a opção'))
    
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()
        
def cadastrar_produto() -> None:
    print('Cadastro de produto: ')
    print('')
    
    nome: str = str(input('Informe o nome do produto'))
    preco: float = float(input('Informe o preço do produto'))
    
    #Instanciando objeto produto
    produto: Produto = Produto(nome, preco)
    #Adicionando na lista
    produtos.append(produto)
    
    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)
    menu()

def listar_produtos() -> None:
    #Só faz sentido se tiver produto
    if len(produtos) >0:
        print('Listagem de produtos')
        print('---------------')
        for produto in produtos:
            print(produto)
            print('')
            
    else:
        print('Ainda não existem produtos cadastrados')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) >0:
        print('Informe o código do produto que deseja adicionar ao carrinho.')
        print('-----------------------------------')
        for produto in produtos:
            print(produto)
            print('---------------------')
            sleep(1)
        
        codigo: int = int(input('Digite o código: '))
        produto: Produto = pega_produto_codigo(codigo)
        
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    #Pego o valor em um dicionário usando get passando o produto
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f' O produto {produto.nome} agora possui {quant + 1 } unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                
                if not tem_no_carrinho:
                    prod ={produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho')
                    sleep(2)
                    menu()
                     
            else:
                item ={produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado no carrinho')
                sleep(2)
                menu()
        else:
            print(f'O produto com o codigo {codigo} não foi encontrado')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender')
    
    sleep(2)
    menu()
    

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('----------------')
                sleep(1)
                
    else:
        print('Ainda não existem produtos no carrinho')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor: float = 0
        
        print('Produtos do carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor += dados[0].preco * dados[1]
                print('------------------------')
                sleep(1)
        
        print(f'A sua fatura é {formata_float_str_moeda(valor)}')
        carrinho.clear()
        sleep(5)
        menu()
            
    else:
        print('Carrinho vazio')

def pega_produto_codigo(codigo:int) -> Produto:
    p: Produto = None
    
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
            
    return p
if __name__ == '__main__':
    main()
    
#Visualizar carrinho
#Comprar produtos