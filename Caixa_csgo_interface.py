import PySimpleGUI as sg
import random

def janela_deposito():
    layout = [
        [sg.Text("Digite o valor que vai ser depositado R$: 10.000 é o limite: ")],
        [sg.InputText(key="valor_de_deposito")],
        [sg.Button("Depositar")],
    ]
    return sg.Window('Faça seu deposito', layout=layout, finalize=True)

def janela_abrir_caixa():
    layout = [
        [sg.Text("Quantas caixas vc quer abrir?")],
        [sg.InputText(key="abrir_caixa")],
        [sg.Button("Abrir")],
    ]
    return sg.Window('Abrir caixa', layout=layout, finalize=True)

def janela_mostrar_resultado():
    layout = [
        [sg.Text('esse é o final')],
        [sg.Button("Terminar")],
    ]
    return sg.Window('Resultado', layout=layout, finalize=True)


def estrutura_aposta(values):
    # criando lista q vai guardar os valores de 1 a 100000
    escolhas = []
    # Colocando valores de 1 a 100000 dentro da lista 
    for lista_total in range(100001):
        escolhas.append(lista_total)
    # Dicionário para contar o número de vezes que cada escolha é feita
    contagem = {escolha: 0 for escolha in escolhas}

    # Fazer a escolha aleatória n vezes e contar as ocorrências
    for i in range(int(values['abrir_caixa'])):
        escolha = random.choice(escolhas)
        contagem[escolha] += 1

    # Calcular a porcentagem de cada escolha
    porcentagens = {escolha: contagem[escolha] / int(values['abrir_caixa']) * 100 for escolha in escolhas}

    # quantas vezes o usuario vai abrir a caixa
    qtd_de_vezes_abrir_caixa = int(values['abrir_caixa'])

    # valor final da caixa 
    valor_da_caixa = 484.79 * qtd_de_vezes_abrir_caixa

    # contando quantas facas foram retiradas
    count = 0
    return count, valor_da_caixa, porcentagens


janela1, janela2, janela3 = janela_deposito(), None, None

while True:
    window, event, values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # primeira tela
    if window == janela1 and event == 'Depositar':
        saldo = float(values["valor_de_deposito"])
        #passando para a janela 2
        janela2 = janela_abrir_caixa()
        janela1.hide()
    # segunda tela
    if window == janela2 and event == 'Abrir':
        count, valor_da_caixa, porcentagens = estrutura_aposta(values)

        # verificando se o saldo do usuario é maior q o valor da caixa
        if saldo >= valor_da_caixa:

            # lista para guardar os valores das facas 
            ultima_tentativa = []
            for escolha, porcentagem in porcentagens.items():
                if porcentagem > 0:
                    #vendo qual numero foi sorteado e qual faca corresponde
                    if escolha <= 12245:
                        def faca1():
                            valor_da_faca1 = 388.96 
                            ultima_tentativa.append(valor_da_faca1)
                            count= count + 1
                            sg.Print(f'{count} || ★ Navaja Knife | Forest DDPAT (Field-Tested)  custa: {valor_da_faca1}')
                            
                    elif escolha >= 12246 and escolha <= 20693:
                        valor_da_faca2 = 400.14
                        ultima_tentativa.append(valor_da_faca2) 
                        count= count + 1
                        sg.Print(f'{count} || ★ Navaja Knife | Forest DDPAT (Battle-Scarred) custa: {valor_da_faca2}')
                            
                    elif escolha >= 20694 and escolha <= 30219:
                        valor_da_faca3 = 402.96
                        ultima_tentativa.append(valor_da_faca3)
                        count= count + 1
                        sg.Print(f'{count} || ★ Navaja Knife | Blue Steel (Battle-Scarred) custa: {valor_da_faca3}')
                            
                    elif escolha >= 30220 and escolha <= 53171:
                        valor_da_faca4 = 409.48
                        ultima_tentativa.append(valor_da_faca4)
                        count= count + 1
                        sg.Print(f'{count} || ★ Shadow Daggers | Rust Coat (Battle-Scarred) custa: {valor_da_faca4}')
                            
                    elif escolha >= 53172 and escolha <= 60624:
                        valor_da_faca5 = 412.81
                        ultima_tentativa.append(valor_da_faca5)
                        count= count + 1
                        sg.Print(f'{count} || ★ Navaja Knife | Blue Steel (Minimal Wear) custa: {valor_da_faca5}')
                            
                    elif escolha >= 60625 and escolha <= 63846:
                        valor_da_faca6 = 416.56
                        ultima_tentativa.append(valor_da_faca6)
                        count= count + 1
                        sg.Print(f'{count} || ★ Navaja Knife | Forest DDPAT (Minimal Wear) custa: {valor_da_faca6}')
                            
                    elif escolha >= 63847 and escolha <= 86801:
                        valor_da_faca7 = 426.20
                        ultima_tentativa.append(valor_da_faca7)
                        count= count + 1
                        sg.Print(f'{count} || ★ Navaja Knife | Rust Coat (Battle-Scarred) custa: {valor_da_faca7}')
                            
                    elif escolha >= 86802 and escolha <= 94785:
                        valor_da_faca8 = 432.82
                        ultima_tentativa.append(valor_da_faca8)
                        count= count + 1
                        sg.Print(f'{count} || ★ Navaja Knife | Blue Steel (Field-Tested) custa: {valor_da_faca8}')
                            
                    elif escolha >= 94786 and escolha <= 95337:
                        valor_da_faca9 = 549.94
                        ultima_tentativa.append(valor_da_faca9)
                        count= count + 1
                        sg.Print(f'{count} || ★ Shadow Daggers | Autotronic (Minimal Wear) custa: {valor_da_faca9}')
                            
                    elif escolha >= 95338 and escolha <= 95672:
                        valor_da_faca10 = 554.66
                        ultima_tentativa.append(valor_da_faca10)
                        count= count + 1
                        sg.Print(f'{count} || ★ Gut Knife | Bright Water (Minimal Wear) custa: {valor_da_faca10}')
                            
                    elif escolha >= 95673 and escolha <= 96237:
                        valor_da_faca11 = 555.12
                        ultima_tentativa.append(valor_da_faca11)
                        count= count + 1
                        sg.Print(f'{count} || ★ Gut Knife | Damascus Steel (Minimal Wear) custa: {valor_da_faca11}')
                            
                    elif escolha >= 96238 and escolha <= 96491:
                        valor_da_faca12 = 566.87
                        ultima_tentativa.append(valor_da_faca12)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Black Laminate (Battle-Scarred) custa: {valor_da_faca12}')
                            
                    elif escolha >= 96492 and escolha <= 96756:
                        valor_da_faca13 = 589.33
                        ultima_tentativa.append(valor_da_faca13)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Black Laminate (Field-Tested) custa: {valor_da_faca13}')
                            
                    elif escolha >= 96757 and escolha <= 97280:
                        valor_da_faca14 = 593.34
                        ultima_tentativa.append(valor_da_faca14)
                        count= count + 1
                        sg.Print(f'{count} || ★ Gut Knife | Damascus Steel (Factory New) custa: {valor_da_faca14}')
                            
                    elif escolha >= 97281 and escolha <= 97624:
                        valor_da_faca15 = 600.26
                        ultima_tentativa.append(valor_da_faca15)
                        count= count + 1
                        sg.Print(f'{count} || ★ Gut Knife | Bright Water (Factory New) custa: {valor_da_faca15}')
                            
                    elif escolha >= 97625 and escolha <= 97911:
                        valor_da_faca16 = 620.58
                        ultima_tentativa.append(valor_da_faca16)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Black Laminate (Minimal Wear) custa: {valor_da_faca16}')
                            
                    elif escolha >= 97912 and escolha <= 98083:
                        valor_da_faca17 = 753.03
                        ultima_tentativa.append(valor_da_faca17)
                        count= count + 1
                        sg.Print(f'{count} || ★ Shadow Daggers | Autotronic (Factory New) custa: {valor_da_faca17}')
                            
                    elif escolha >= 98084 and escolha <= 98226:
                        valor_da_faca18 = 795.82
                        ultima_tentativa.append(valor_da_faca18)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Black Laminate (Factory New) custa: {valor_da_faca18}')
                            
                    elif escolha >= 98227 and escolha <= 98392:
                        valor_da_faca19 = 813.21
                        ultima_tentativa.append(valor_da_faca19)
                        count= count + 1
                        sg.Print(f'{count} || ★ Gut Knife | Lore (Field-Tested) custa: {valor_da_faca19}')
                            
                    elif escolha >= 98393 and escolha <= 98518:
                        valor_da_faca20 = 971.11
                        ultima_tentativa.append(valor_da_faca20)
                        count= count + 1
                        sg.Print(f'{count} || ★ Bowie Knife | Autotronic (Minimal Wear) custa: {valor_da_faca20}')
                            
                    elif escolha >= 98519 and escolha <= 98645:
                        valor_da_faca21 = 1019.33
                        ultima_tentativa.append(valor_da_faca21)
                        count= count + 1
                        sg.Print(f'{count} || ★ Survival Knife | Case Hardened (Minimal Wear) custa: {valor_da_faca21}')
                            
                    elif escolha >= 98646 and escolha <= 98789:
                        valor_da_faca22 = 1113.98
                        ultima_tentativa.append(valor_da_faca22)
                        count= count + 1
                        sg.Print(f'{count} || ★ Flip Knife | Bright Water (Field-Tested) custa: {valor_da_faca22}')
                            
                    elif escolha >= 98790 and escolha <= 98921:
                        valor_da_faca23 = 1118.85
                        ultima_tentativa.append(valor_da_faca23)
                        count= count + 1
                        sg.Print(f'{count} || ★ Flip Knife | Freehand (Field-Tested) custa: {valor_da_faca23}')
                            
                    elif escolha >= 98922 and escolha <= 99164:
                        valor_da_faca24 = 1121.73
                        ultima_tentativa.append(valor_da_faca24)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Tiger Tooth (Factory New) custa: {valor_da_faca24}')
                            
                    elif escolha >= 99165 and escolha <= 99302:
                        valor_da_faca25 = 1353.40
                        ultima_tentativa.append(valor_da_faca25)
                        count= count + 1
                        sg.Print(f'{count} || ★ Bowie Knife | Gamma Doppler (Factory New) custa: {valor_da_faca25}')
                            
                    elif escolha >= 99303 and escolha <= 99358:
                        valor_da_faca26 = 1391.97
                        ultima_tentativa.append(valor_da_faca26)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Gamma Doppler (Factory New) custa: {valor_da_faca26}')
                            
                    elif escolha >= 99359 and escolha <= 99425:
                        valor_da_faca27 = 1396.75
                        ultima_tentativa.append(valor_da_faca27)
                        count= count + 1
                        sg.Print(f'{count} || ★ Huntsman Knife | Doppler (Factory New) custa: {valor_da_faca27}')
                            
                    elif escolha >= 99426 and escolha <= 99493:
                        valor_da_faca28 = 1454.51
                        ultima_tentativa.append(valor_da_faca28)
                        count= count + 1
                        sg.Print(f'{count} || ★ Falchion Knife | Lore (Factory New) custa: {valor_da_faca28}')
                            
                    elif escolha >= 99494 and escolha <= 99552:
                        valor_da_faca29 = 1559.37
                        ultima_tentativa.append(valor_da_faca29)
                        count= count + 1
                        sg.Print(f'{count} || ★ Flip Knife | Autotronic (Field-Tested) custa: {valor_da_faca29}')
                            
                    elif escolha >= 99553 and escolha <= 99586:
                        valor_da_faca30 = 1936.73
                        ultima_tentativa.append(valor_da_faca30)
                        count= count + 1
                        sg.Print(f'{count} || ★ Ursus Knife | Doppler (Factory New) custa: {valor_da_faca30}')
                            
                    elif escolha >= 99587 and escolha <= 99607:
                        valor_da_faca31 = 2352.57
                        ultima_tentativa.append(valor_da_faca31)
                        count= count + 1
                        sg.Print(f'{count} || ★ Flip Knife | Gamma Doppler (Factory New) custa: {valor_da_faca31}')
                            
                    elif escolha >= 99608 and escolha <= 99625:
                        valor_da_faca32 = 2412.69
                        ultima_tentativa.append(valor_da_faca32)
                        count= count + 1
                        sg.Print(f'{count} || ★ Survival Knife | Fade (Factory New) custa: {valor_da_faca32}')
                            
                    elif escolha >= 99626 and escolha <= 99638:
                        valor_da_faca33 = 3267.86
                        ultima_tentativa.append(valor_da_faca33)
                        count= count + 1
                        sg.Print(f'{count} || ★ Bayonet | Gamma Doppler (Factory New) custa: {valor_da_faca33}')
                            
                    elif escolha >= 99639 and escolha <= 99650:
                        valor_da_faca34 = 4073.12
                        ultima_tentativa.append(valor_da_faca34)
                        count= count + 1
                        sg.Print(f'{count} || ★ M9 Bayonet | Black Laminate (Minimal Wear) custa: {valor_da_faca34}')
                            
                    elif escolha >= 99651 and escolha <= 99697:
                        valor_da_faca35 = 4532.92
                        ultima_tentativa.append(valor_da_faca35)
                        count= count + 1
                        sg.Print(f'{count} || ★ Talon Knife | Marble Fade (Factory New) custa: {valor_da_faca35}')
                            
                    elif escolha >= 99698 and escolha <= 99739:
                        valor_da_faca36 = 4881.40
                        ultima_tentativa.append(valor_da_faca36)
                        count= count + 1
                        sg.Print(f'{count} || ★ Karambit | Damascus Steel (Factory New) custa: {valor_da_faca36}')
                            
                    elif escolha >= 99740 and escolha <= 99778:
                        valor_da_faca37 = 5174.43
                        ultima_tentativa.append(valor_da_faca37)
                        count= count + 1
                        sg.Print(f'{count} || ★ M9 Bayonet | Tiger Tooth (Factory New) custa: {valor_da_faca37}')
                            
                    elif escolha >= 99779 and escolha <= 99811:
                        valor_da_faca38 = 6075.20
                        ultima_tentativa.append(valor_da_faca38)
                        count= count + 1
                        sg.Print(f'{count} || ★ M9 Bayonet | Autotronic (Minimal Wear) custa: {valor_da_faca38}')
                            
                    elif escolha >= 99812 and escolha <= 99843:
                        valor_da_faca39 = 6304.41
                        ultima_tentativa.append(valor_da_faca39)
                        count= count + 1
                        sg.Print(f'{count} || ★ Karambit | Gamma Doppler (Factory New) custa: {valor_da_faca39}')
                            
                    elif escolha >= 99844 and escolha <= 99867:
                        valor_da_faca40 = 7444.50
                        ultima_tentativa.append(valor_da_faca40)
                        count= count + 1
                        sg.Print(f'{count} || ★ Karambit | Autotronic (Minimal Wear) custa: {valor_da_faca40}')
                            
                    elif escolha >= 99868 and escolha <= 99894:
                        valor_da_faca41 = 7815.50
                        ultima_tentativa.append(valor_da_faca41)
                        count= count + 1
                        sg.Print(f'{count} || ★ Butterfly Knife | Doppler (Factory New) custa: {valor_da_faca41}')
                            
                    elif escolha >= 99895 and escolha <= 99928:
                        valor_da_faca42 = 7853.82
                        ultima_tentativa.append(valor_da_faca42)
                        count= count + 1
                        sg.Print(f'{count} || ★ M9 Bayonet | Fade (Factory New) custa: {valor_da_faca42}')
                            
                    elif escolha >= 99929 and escolha <= 99949:
                        valor_da_faca43 = 8570.59
                        ultima_tentativa.append(valor_da_faca43)
                        count= count + 1
                        sg.Print(f'{count} || ★ Karambit | Lore (Minimal Wear) custa: {valor_da_faca43}')
                            
                    elif escolha >= 99950 and escolha <= 99968:
                        valor_da_faca44 = 8789.84
                        ultima_tentativa.append(valor_da_faca44)
                        count= count + 1
                        sg.Print(f'{count} || ★ Butterfly Knife | Gamma Doppler (Factory New) custa: {valor_da_faca44}')
                            
                    elif escolha >= 99969 and escolha <= 99985:
                        valor_da_faca45 = 10221.73
                        ultima_tentativa.append(valor_da_faca45)
                        count= count + 1
                        sg.Print(f'{count} || ★ Karambit | Fade (Factory New) custa: {valor_da_faca45}')
                            
                    elif escolha >= 99986 and escolha <= 100000:
                        valor_da_faca46 = 15644.14
                        ultima_tentativa.append(valor_da_faca46)
                        count= count + 1
                        sg.Print(f'{count} || ★ M9 Bayonet | Lore (Factory New) custa: {valor_da_faca46}')
            #vendo o valor final com as facas ganhas e o dinheiro gasto abrindo as caixas
            saldo_final =sum(ultima_tentativa)
            sg.Print(f'essa foi seu saldo: R${saldo_final}')

            janela3 = janela_mostrar_resultado()
            janela2.hide()
        else:
            sg.Print(f'O saldo não é suficiente para abrir a caixa\nEsse é seu saldo: R${saldo} e essa é o valor da caixa: R${valor_da_caixa}')

    if window == janela3 and event =='Terminar':
        break