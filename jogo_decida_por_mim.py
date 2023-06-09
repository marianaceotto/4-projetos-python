# DECIDA POR MIM - faça uma pergunta para o programa e ele terá que te dar uma resposta

import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei',
            'Não faz isso!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        self.janela = sg.Window('Decida por Mim!',layout=layout)
        while True:
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
    
decida = DecidaPorMim()
decida.Iniciar()
    