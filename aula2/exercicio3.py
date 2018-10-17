# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:37:14 2018

@author: Juliene Vargens
"""

'--------exercicio 3--------------'
#
preco_livro=24.95
desconto=(preco_livro)*0.04
print(desconto)
preco_livro_c_d= preco_livro-desconto
print(preco_livro_c_d)
custo_envio_primeiro=3.00
custo_envio_segundo=0.75
total= ((preco_livro_c_d+custo_envio_primeiro+((custo_envio_segundo+preco_livro_c_d)*59))
print(total)