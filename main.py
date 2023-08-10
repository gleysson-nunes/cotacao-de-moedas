from customtkinter import *
import requests
from tkinter import messagebox

root = CTk()
root.geometry('500x450')
root.resizable(False, False)
root.title('Cotação de Moedas')
root.iconbitmap('icone.ico')
root.configure(fg_color='#14662C')


def vercotacao():
    try:
        # Acessando a API
        cotacoes_online = requests.get('https://economia.awesomeapi.com.br'
                                       '/last/USD-BRL,EUR-BRL,BTC-BRL')

        # Convertendo a API em formato Python
        cotacoes_online = cotacoes_online.json()

        valor = float(entryvalor.get())
        opcao = menude.get()
        if opcao == 'DÓLAR':
            cotacao_dolar = float(cotacoes_online['USDBRL']['bid'])
            dolarresu = valor * cotacao_dolar
            labelresu.configure(root, text=f'{dolarresu:.2f}')
        elif opcao == 'EURO':
            cotacao_euro = float(cotacoes_online['EURBRL']['bid'])
            euroresu = valor * cotacao_euro
            labelresu.configure(root, text=f'{euroresu:.2f}')
        elif opcao == 'BITCOIN':
            cotacao_bitcoin = float(cotacoes_online['BTCBRL']['bid'])
            bitcoinresu = valor * cotacao_bitcoin
            labelresu.configure(root, text=f'{bitcoinresu:.2f}')
    except ValueError:
        messagebox.showwarning(title='Aviso', message='O campo "VALOR" deve '
                                                      'ser preenchido com um '
                                                      'número')


labelresu = CTkLabel(root, text='', width=300, font=('Arial', 18, 'bold'),
                     anchor='center')
labelresu.place(relx=0.2, rely=0.65)

frame = CTkFrame(root, width=450, height=100, fg_color='#1B8F3D',
                 bg_color='#1B8F3D')
frame.place(relx=0.05, rely=0.05)

labelfrase1 = CTkLabel(frame, text='COTAÇÃO DE MOEDAS',
                       font=('Arial', 35, 'bold'))
labelfrase1.place(relx=0.07, rely=0.31)

labelfrase2 = CTkLabel(root, text='VEJA A COTAÇÃO DO DÓLAR, EURO E BITCOIN '
                                  'FRENTE AO REAL',
                       font=('Arial', 14, 'bold'))
labelfrase2.place(relx=0.06, rely=0.3)

labelvalor = CTkLabel(root, text='VALOR', font=('Arial', 14, 'bold'))
labelvalor.place(relx=0.14, rely=0.4)

entryvalor = CTkEntry(root, width=100, height=35, font=('Arial', 14, 'bold'),
                      justify='center',
                      fg_color='#1B8F3D')
entryvalor.place(relx=0.09, rely=0.47)

labelde = CTkLabel(root, text='DE', font=('Arial', 14, 'bold'))
labelde.place(relx=0.47, rely=0.4)

menude = CTkOptionMenu(root, width=110, height=35,
                       values=['DÓLAR', 'EURO', 'BITCOIN'],
                       anchor='center', font=('Arial', 14, 'bold'),
                       fg_color='#1B8F3D',
                       button_color='#156E2F',
                       button_hover_color='#105223',
                       dropdown_font=('Arial', 15, 'bold'),
                       dropdown_fg_color='#1B8F3D')
menude.place(relx=0.38, rely=0.47)

labelpara = CTkLabel(root, text='PARA', font=('Arial', 14, 'bold'))
labelpara.place(relx=0.75, rely=0.4)

menupara = CTkOptionMenu(root, width=110, height=35,
                         values=['REAL'], anchor='center',
                         font=('Arial', 14, 'bold'),
                         fg_color='#1B8F3D',
                         button_color='#156E2F',
                         button_hover_color='#105223',
                         dropdown_font=('Arial', 15, 'bold'),
                         dropdown_fg_color='#1B8F3D')
menupara.place(relx=0.68, rely=0.47)

botao = CTkButton(root, text='VER COTAÇÃO', font=('Arial', 14, 'bold'),
                  anchor='center',
                  fg_color='#1B8F3D',
                  hover_color='#105223', command=vercotacao)
botao.place(relx=0.36, rely=0.8)

labelfrase3 = CTkLabel(root, text='* valores atualizados a cada 30 segundos',
                       font=('Arial', 11))
labelfrase3.place(relx=0.3, rely=0.91)

root.mainloop()
