# JOGO DE DADOS - simular o uso de um dado, gerando um valor de 1 a 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = 'Você gostaria de jogar o dado?'
    
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # Janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('Agradecemos a participação')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('Ocoreu um erro')
 
    def GerarValorDoDado(self):
        print(random.randint(self.valor_min, self.valor_max))


simulador = SimuladorDeDado()
simulador.Iniciar()