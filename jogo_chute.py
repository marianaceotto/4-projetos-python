# JOGO CHUTE UM NÚMERO - algorítimo que gera um valor aleatório, tentativa e erro até o número selecionado aparecer.

import random 
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        layout = [
            [sg.Text('Seu Chute',size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        self.janela = sg.Window('Chute o numero!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
                            break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()
            

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_min,self.valor_max)

chute = ChuteONumero()
chute.Iniciar()