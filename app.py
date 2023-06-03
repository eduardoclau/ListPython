# Versão em código simples, com funções

from typing import List

filaNormal: List[str] = []
filaPrioritaria: List[str] = []


def andarFila():
    if len(filaPrioritaria) >= 2:
        for _ in range(2):
            if filaPrioritaria:
                filaPrioritaria.pop(0)
        if filaNormal:
            filaNormal.pop(0)
        print("Duas pessoas removidas da Lista Prioritária e uma pessoa \
            removida da Lista Normal.")
    else:
        if filaPrioritaria:
            filaPrioritaria.pop(0)
        if filaNormal:
            filaNormal.pop(0)

    while filaPrioritaria or filaNormal:
        if filaPrioritaria:
            filaPrioritaria.pop(0)
        if filaNormal:
            filaNormal.pop(0)


def adicionarEmFilaPrioritaria():
    name = input("Qual seu nome? ")
    filaPrioritaria.append(name)
    print("Adicionado em Fila Prioritária")


def adicionarEmFilaNormal():
    name = input("Qual seu nome? ")
    filaNormal.append(name)
    print("Adicionado em Fila Normal")


def iniciar():
    opcao = int(input("O que você quer fazer: Adicionar (1) ou Remover (2)? "))
    if opcao == 2:
        andarFila()
    else:
        idade = int(input("Qual sua idade? "))
        if idade >= 60:
            adicionarEmFilaPrioritaria()
        else:
            adicionarEmFilaNormal()


# Versão em Construtores/Class


class Fila:
    def __init__(self) -> None:
        self.filaNormal: List[str] = []
        self.filaPrioritaria: List[str] = []

    def andarFila(self) -> None:
        if len(self.filaPrioritaria) >= 2:
            for _ in range(2):
                if self.filaPrioritaria:
                    self.filaPrioritaria.pop(0)
            if self.filaNormal:
                self.filaNormal.pop(0)
            print(
                "Duas pessoas removidas da Lista Prioritária e uma pessoa \
                    removida da Lista Normal.")
        else:
            if self.filaPrioritaria:
                self.filaPrioritaria.pop(0)
            if self.filaNormal:
                self.filaNormal.pop(0)

        while self.filaPrioritaria or self.filaNormal:
            if self.filaPrioritaria:
                self.filaPrioritaria.pop(0)
            if self.filaNormal:
                self.filaNormal.pop(0)

    def adicionarEmFilaPrioritaria(self) -> None:
        name = input("Qual seu nome? ")
        self.filaPrioritaria.append(name)
        print("Adicionado em Fila Prioritária")

    def adicionarEmFilaNormal(self) -> None:
        name = input("Qual seu nome? ")
        self.filaNormal.append(name)
        print("Adicionado em Fila Normal")

    def iniciar(self) -> None:
        opcao = int(
            input("O que você quer fazer: Adicionar (1) ou Remover (2)? "))
        if opcao == 2:
            self.andarFila()
        else:
            idade = int(input("Qual sua idade? "))
            if idade >= 60:
                self.adicionarEmFilaPrioritaria()
            else:
                self.adicionarEmFilaNormal()


fila = Fila()
fila.iniciar()
