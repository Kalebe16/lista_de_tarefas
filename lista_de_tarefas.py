# desenvolvedor Kalebe Chimanski de Almeida

import PySimpleGUI as sg

fonte = "Verdana"
tema1 = ""
tema2 = ""
tema3 = ""
item_selecionado = "Padrão"


def criar_janela_inicial():
    tema1 = ""

    linha = [
        [sg.Checkbox(""), sg.Input("", expand_x=True)]

    ]

    layout1 = [
        [sg.Frame("Tarefas", layout=linha, key="container", expand_x=True, expand_y=True)],
        [sg.Button("Nova Tarefa"), sg.Button("Resetar"), sg.Button("Config"), sg.Button("Sobre")]
    ]

    return sg.Window("Lista de tarefas", layout=layout1, finalize=True, font=fonte, element_justification="center", margins=(0, 5))


def criar_janela_configuracoes():
    tema2 = ""

    layout2 = [
        [sg.Text("Essa é a lista de temas, escolha um que lhe agrade")],
        [sg.Listbox(values=sg.theme_list(),
                    size=(20, 12),
                    key='-LIST-',
                    enable_events=True), sg.Text("O tema atual é: " + item_selecionado)],
        [sg.Button("Confirmar"), sg.Button("Voltar")]
    ]

    return sg.Window('Configurações', layout=layout2, finalize=True, font=fonte, element_justification="center", margins=(0, 5))


def criar_janela_sobre():
    tema3 = ""

    layout3 = [
        [sg.Text("Desenvolvedor: Kalebe Chimanski de Almeida")],
        [sg.Button("Voltar")]

    ]

    return sg.Window("Sobre", layout=layout3, finalize=True, font=fonte, element_justification="center", no_titlebar=True)


# Criar a janela
janela1, janela2, janela3 = criar_janela_inicial(), None, None

# Criar as regras dessa janela
while True:
    window, event, values = sg.read_all_windows(timeout=1)

    if window == janela1 and event == sg.WIN_CLOSED:  # Quando a janela1 for fechada
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == "Nova Tarefa":
        janela1.extend_layout(janela1["container"],
                              [[sg.Checkbox(""), sg.Input("", expand_x=True)]])

    if window == janela1 and event == "Resetar":
        janela1.close()
        janela1 = criar_janela_inicial()

    if window == janela1 and event == "Config":
        janela2 = criar_janela_configuracoes()
        janela1.hide()  

    if window == janela1 and event == "Sobre":
        janela3 = criar_janela_sobre()

    if window == janela2 and event == "-LIST-":
        item_selecionado = str(values['-LIST-'])
        caracteres = "[]''"
        for x in range(len(caracteres)):
            item_selecionado = item_selecionado.replace(caracteres[x], "")
        print(item_selecionado)

    if window == janela2 and event == "Confirmar":
        janela1.close()
        janela2.close()
        tema1 = sg.theme(item_selecionado)
        tema2 = sg.theme(item_selecionado)
        tema3 = sg.theme(item_selecionado)
        janela1 = criar_janela_inicial()

    if window == janela2 and event == "Voltar":  
        janela1.un_hide()  
        janela2.hide()  

    if window == janela3 and event == "Voltar":
        janela3.close()
