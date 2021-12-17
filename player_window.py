import dearpygui.dearpygui as dpg
import json

def salvar(sender, app_data):
    dict = {"nome": dpg.get_value("nome"),
    "nome_jogador": dpg.get_value("nome_jogador"),
    "raca": dpg.get_value("raca"),
    "profissao": dpg.get_value("profissao"),
    "idade": dpg.get_value("idade"),
    "peso_carregado": dpg.get_value("peso_carregado"),
    "capacidade": dpg.get_value("capacidade"),
    "cap_combate": dpg.get_value("cap_combate"),
    "dinheiro": dpg.get_value("dinheiro"),
    "pts_xp": dpg.get_value("pts_xp"),
    "vigor": dpg.get_value("vigor"),
    "habilidade": dpg.get_value("habilidade"),
    "percepcao": dpg.get_value("percepcao"),
    "inteligencia": dpg.get_value("inteligencia"),
    "dominio": dpg.get_value("dominio"),
    "pdv_atual": dpg.get_value("pdv_atual"),
    "pdv_max": dpg.get_value("pdv_max"),
    "pda_atual": dpg.get_value("pda_atual"),
    "pda_max": dpg.get_value("pda_max"),
    "pde_atual": dpg.get_value("pde_atual"),
    "pde_max": dpg.get_value("pde_max"),
    "forca_valor": dpg.get_value("forca_valor"),
    "forca_traco": dpg.get_value("forca_traco"),
    "fisica_valor": dpg.get_value("fisica_valor"),
    "fisica_traco": dpg.get_value("fisica_traco"),
    "mental_valor": dpg.get_value("mental_valor"),
    "mental_traco": dpg.get_value("mental_traco"),
    "sobrevivencia_valor": dpg.get_value("sobrevivencia_valor"),
    "sobrevivencia_traco": dpg.get_value("sobrevivencia_traco"),
    "agilidade_valor": dpg.get_value("agilidade_valor"),
    "agilidade_traco": dpg.get_value("agilidade_traco"),
    "destreza_valor": dpg.get_value("destreza_valor"),
    "destreza_traco": dpg.get_value("destreza_traco"),
    "competencia_valor": dpg.get_value("competencia_valor"),
    "competencia_traco": dpg.get_value("competencia_traco"),
    "criatividade_valor": dpg.get_value("criatividade_valor"),
    "criatividade_traco": dpg.get_value("criatividade_traco"),
    "manipulacao_valor": dpg.get_value("manipulacao_valor"),
    "manipulacao_traco": dpg.get_value("manipulacao_traco"),
    "sorte_valor": dpg.get_value("sorte_valor"),
    "sorte_traco": dpg.get_value("sorte_traco"),
    "tracos_estados": dpg.get_value("tracos_estados"),
    "arma1": dpg.get_value("arma1"),
    "arma2": dpg.get_value("arma2"),
    "arma3": dpg.get_value("arma3"),
    "dano1": dpg.get_value("dano1"),
    "dano2": dpg.get_value("dano2"),
    "dano3": dpg.get_value("dano3"),
    "teste1": dpg.get_value("teste1"),
    "teste2": dpg.get_value("teste2"),
    "teste3": dpg.get_value("teste3"),
    "peso1": dpg.get_value("peso1"),
    "peso2": dpg.get_value("peso2"),
    "peso3": dpg.get_value("peso3"),
    "peso4": dpg.get_value("peso4"),
    "peso5": dpg.get_value("peso5"),
    "peso6": dpg.get_value("peso6"),
    "peso7": dpg.get_value("peso7"),
    "peso8": dpg.get_value("peso8"),
    "peso9": dpg.get_value("peso9"),
    "peso10": dpg.get_value("peso10"),
    "peso11": dpg.get_value("peso11"),
    "peso12": dpg.get_value("peso12"),
    "peso13": dpg.get_value("peso13"),
    "peso14": dpg.get_value("peso14"),
    "peso15": dpg.get_value("peso15"),
    "peso16": dpg.get_value("peso16"),
    "peso17": dpg.get_value("peso17"),
    "equip1": dpg.get_value("equip1"),
    "equip2": dpg.get_value("equip2"),
    "equip3": dpg.get_value("equip3"),
    "equip4": dpg.get_value("equip4"),
    "equip5": dpg.get_value("equip5"),
    "pda1": dpg.get_value("pda1"),
    "pda2": dpg.get_value("pda2"),
    "pda3": dpg.get_value("pda3"),
    "pda4": dpg.get_value("pda4"),
    "pda5": dpg.get_value("pda5"),
    "classe1": dpg.get_value("classe1"),
    "classe2": dpg.get_value("classe2"),
    "classe3": dpg.get_value("classe3"),
    "classe4": dpg.get_value("classe4"),
    "classe5": dpg.get_value("classe5"),
    "classe6": dpg.get_value("classe6"),
    "classe7": dpg.get_value("classe7"),
    "classe8": dpg.get_value("classe8"),
    "classe9": dpg.get_value("classe9"),
    "classe10": dpg.get_value("classe10"),
    "poder1": dpg.get_value("poder1"),
    "poder2": dpg.get_value("poder2"),
    "poder3": dpg.get_value("poder3"),
    "poder4": dpg.get_value("poder4"),
    "poder5": dpg.get_value("poder5"),
    "poder6": dpg.get_value("poder6"),
    "poder7": dpg.get_value("poder7"),
    "poder8": dpg.get_value("poder8"),
    "poder9": dpg.get_value("poder9"),
    "poder10": dpg.get_value("poder10"),
    "qtd1": dpg.get_value("qtd1"),
    "qtd2": dpg.get_value("qtd2"),
    "qtd3": dpg.get_value("qtd3"),
    "qtd4": dpg.get_value("qtd4"),
    "qtd5": dpg.get_value("qtd5"),
    "qtd6": dpg.get_value("qtd6"),
    "qtd7": dpg.get_value("qtd7"),
    "qtd8": dpg.get_value("qtd8"),
    "qtd9": dpg.get_value("qtd9"),
    "item1": dpg.get_value("item1"),
    "item2": dpg.get_value("item2"),
    "item3": dpg.get_value("item3"),
    "item4": dpg.get_value("item4"),
    "item5": dpg.get_value("item5"),
    "item6": dpg.get_value("item6"),
    "item7": dpg.get_value("item7"),
    "item8": dpg.get_value("item8"),
    "item9": dpg.get_value("item9"),
    "historia": dpg.get_value("historia"),
    "notas": dpg.get_value("notas"),
    "descricao_fisica": dpg.get_value("descricao_fisica")}
    with open("player.json", "w") as file:
        json.dump(dict, file, indent=4)
    with dpg.window(label="Salvando", tag="salvando", width=150, height=20, pos=(500, 300), popup=True, modal=True, no_title_bar=True):
        dpg.add_text("Arquivo salvo!")
        dpg.add_button(label="Fechar", callback=lambda: dpg.delete_item("salvando"))
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (89, 89, 89), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("salvando", item_theme)

def carregar(sender, app_data):
    with open("player.json", "r") as file:
        dict = json.load(file)
        for k, v in dict.items():
            dpg.configure_item(k, default_value=v)
    with dpg.window(label="Carregando", tag="carregando", width=150, height=20, pos=(500, 300), popup=True, modal=True, no_title_bar=True):
        dpg.add_text("Arquivo carregado!")
        dpg.add_button(label="Fechar", callback=lambda: dpg.delete_item("carregando"))
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (89, 89, 89), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("carregando", item_theme)

def player_window():
    with dpg.window(label="Jogador", width=600, no_close=True, pos=(600, 0)):
        with dpg.tab_bar(label="MenuPlayer"):
            with dpg.tab(label="Parte 1"):
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_input_text(label="Nome", width=125, tag="nome")
                        dpg.add_input_text(label="Nome do Jogador", width=125, tag="nome_jogador")
                        dpg.add_input_text(label="Raça", width=125, tag="raca")
                        dpg.add_input_text(label="Profissão", width=125, tag="profissao")
                        dpg.add_input_text(label="Idade", width=125, tag="idade")
                    with dpg.group():
                        dpg.add_input_int(label="Peso Carregado", width=125, tag="peso_carregado")
                        dpg.add_input_int(label="Capacidade", width=125, tag="capacidade")
                        dpg.add_input_int(label="Cap. em Combate", width=125, tag="cap_combate")
                        dpg.add_input_int(label="Dinheiro", width=125, tag="dinheiro")
                        dpg.add_input_int(label="Pts de XP", width=125, tag="pts_xp")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(label="Atributes"):
                        dpg.add_text("Atributos")
                        dpg.add_input_int(label="Vigor", width=75, tag="vigor")
                        dpg.add_input_int(label="Habilidade", width=75, tag="habilidade")
                        dpg.add_input_int(label="Percepção", width=75, tag="percepcao")
                        dpg.add_input_int(label="Inteligência", width=75, tag="inteligencia")
                        dpg.add_input_int(label="Domínio", width=75, tag="dominio")
                    with dpg.group():
                        dpg.add_text("Status")
                        with dpg.table(label="Pontos", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                            dpg.add_table_column(label="", width=25, width_fixed=True)
                            dpg.add_table_column(label="Atual")
                            dpg.add_table_column(label="Máximo")
                            with dpg.table_row():
                                dpg.add_text("PdV")
                                dpg.add_input_int(tag="pdv_atual")
                                dpg.add_input_int(tag="pdv_max")
                            with dpg.table_row():    
                                dpg.add_text("PdA")
                                dpg.add_input_int(tag="pda_atual")
                                dpg.add_input_int(tag="pda_max")
                            with dpg.table_row():
                                dpg.add_text("PdE")
                                dpg.add_input_int(tag="pde_atual")
                                dpg.add_input_int(tag="pde_max")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group(horizontal=True):
                    with dpg.table(label="Tests&Traits", width=375, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Teste")
                        dpg.add_table_column(label="Valor")
                        dpg.add_table_column(label="Traço (+ ou -)")
                        with dpg.table_row():
                            dpg.add_text("Força\n(Vig+Hab)")
                            dpg.add_input_text(tag="forca_valor")
                            dpg.add_input_int(tag="forca_traco")
                        with dpg.table_row():
                            dpg.add_text("Resistência Física\n(Vig+Per)")
                            dpg.add_input_text(tag="fisica_valor")
                            dpg.add_input_int(tag="fisica_traco")
                        with dpg.table_row():
                            dpg.add_text("Resistência Mental\n(Vig+Int)")
                            dpg.add_input_text(tag="mental_valor")
                            dpg.add_input_int(tag="mental_traco")
                        with dpg.table_row():
                            dpg.add_text("Sobrevivência\n(Vig+Dom)")
                            dpg.add_input_text(tag="sobrevivencia_valor")
                            dpg.add_input_int(tag="sobrevivencia_traco")
                        with dpg.table_row():
                            dpg.add_text("Agilidade\n(Hab+Per)")
                            dpg.add_input_text(tag="agilidade_valor")
                            dpg.add_input_int(tag="agilidade_traco")
                        with dpg.table_row():
                            dpg.add_text("Destreza\n(Hab+Dom)")
                            dpg.add_input_text(tag="destreza_valor")
                            dpg.add_input_int(tag="destreza_traco")
                        with dpg.table_row():
                            dpg.add_text("Competência\n(Int+Hab)")
                            dpg.add_input_text(tag="competencia_valor")
                            dpg.add_input_int(tag="competencia_traco")
                        with dpg.table_row():
                            dpg.add_text("Criatividade\n(Int+Per)")
                            dpg.add_input_text(tag="criatividade_valor")
                            dpg.add_input_int(tag="criatividade_traco")
                        with dpg.table_row():
                            dpg.add_text("Manipulação\n(Int+Dom)")
                            dpg.add_input_text(tag="manipulacao_valor")
                            dpg.add_input_int(tag="manipulacao_traco")
                        with dpg.table_row():
                            dpg.add_text("Sorte\n(Dom+Per)")
                            dpg.add_input_text(tag="sorte_valor")
                            dpg.add_input_int(tag="sorte_traco")
                    with dpg.group():
                        dpg.add_text("Traços e Estados")
                        dpg.add_input_text(height=300, multiline=True, tag="tracos_estados")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group():
                    with dpg.table(label="Weapons", width=600, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Arma")
                        dpg.add_table_column(label="Dano")
                        dpg.add_table_column(label="Teste")
                        dpg.add_table_column(label="Peso")
                        with dpg.table_row():
                            dpg.add_input_text(tag="arma1")
                            dpg.add_input_int(tag="dano1")
                            dpg.add_input_text(tag="teste1")
                            dpg.add_input_int(tag="peso1")
                        with dpg.table_row():
                            dpg.add_input_text(tag="arma2")
                            dpg.add_input_int(tag="dano2")
                            dpg.add_input_text(tag="teste2")
                            dpg.add_input_int(tag="peso2")
                        with dpg.table_row():
                            dpg.add_input_text(tag="arma3")
                            dpg.add_input_int(tag="dano3")
                            dpg.add_input_text(tag="teste3")
                            dpg.add_input_int(tag="peso3")
                    with dpg.table(label="Armor", width=600, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Equipamento")
                        dpg.add_table_column(label="PdA")
                        dpg.add_table_column(label="Peso")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip1")
                            dpg.add_input_int(tag="pda1")
                            dpg.add_input_int(tag="peso4")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip2")
                            dpg.add_input_int(tag="pda2")
                            dpg.add_input_int(tag="peso5")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip3")
                            dpg.add_input_int(tag="pda3")
                            dpg.add_input_int(tag="peso6")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip4")
                            dpg.add_input_int(tag="pda4")
                            dpg.add_input_int(tag="peso7")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip5")
                            dpg.add_input_int(tag="pda5")
                            dpg.add_input_int(tag="peso8")
                    with dpg.table(label="Power&Magic", width=600, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Classe")
                        dpg.add_table_column(label="Magia/Poder")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe1")
                            dpg.add_input_text(tag="poder1")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe2")
                            dpg.add_input_text(tag="poder2")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe3")
                            dpg.add_input_text(tag="poder3")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe4")
                            dpg.add_input_text(tag="poder4")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe5")
                            dpg.add_input_text(tag="poder5")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe6")
                            dpg.add_input_text(tag="poder6")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe7")
                            dpg.add_input_text(tag="poder7")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe8")
                            dpg.add_input_text(tag="poder8")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe9")
                            dpg.add_input_text(tag="poder9")
                        with dpg.table_row():
                            dpg.add_input_text(tag="classe10")
                            dpg.add_input_text(tag="poder10")
                    with dpg.table(label="Items", width=600, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Qtd.")
                        dpg.add_table_column(label="Item")
                        dpg.add_table_column(label="Peso")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd1")
                            dpg.add_input_text(tag="item1")
                            dpg.add_input_int(tag="peso9")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd2")
                            dpg.add_input_text(tag="item2")
                            dpg.add_input_int(tag="peso10")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd3")
                            dpg.add_input_text(tag="item3")
                            dpg.add_input_int(tag="peso11")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd4")
                            dpg.add_input_text(tag="item4")
                            dpg.add_input_int(tag="peso12")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd5")
                            dpg.add_input_text(tag="item5")
                            dpg.add_input_int(tag="peso13")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd6")
                            dpg.add_input_text(tag="item6")
                            dpg.add_input_int(tag="peso14")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd7")
                            dpg.add_input_text(tag="item7")
                            dpg.add_input_int(tag="peso15")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd8")
                            dpg.add_input_text(tag="item8")
                            dpg.add_input_int(tag="peso16")
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd9")
                            dpg.add_input_text(tag="item9")
                            dpg.add_input_int(tag="peso17")

            with dpg.tab(label="Parte 2"):
                with dpg.group():
                    dpg.add_text("História progressa")
                    dpg.add_input_text(width=500, height=400, multiline=True, tag="historia")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_text("Notas")
                        dpg.add_input_text(width=400, height=400, multiline=True, tag="notas")
                    with dpg.group():
                        dpg.add_text("Descrição Física")
                        dpg.add_input_text(width=200, height=400, multiline=True, tag="descricao_fisica")
            with dpg.tab(label="Salvar"):
                dpg.add_text("Importante! Salve todas as alterações no botão abaixo!")
                dpg.add_text("Importante! Carregue os dados já salvos ")
                dpg.add_button(label="Salvar", callback=salvar)
                dpg.add_button(label="Carregar", callback=carregar)