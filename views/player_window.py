import dearpygui.dearpygui as dpg
from controllers.player import *

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