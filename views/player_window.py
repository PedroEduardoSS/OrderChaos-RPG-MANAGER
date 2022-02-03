import dearpygui.dearpygui as dpg
from controllers.player import *

def calculo():
    vigor = dpg.get_value("vigor")
    habilidade = dpg.get_value("habilidade")
    percepcao = dpg.get_value("percepcao")
    inteligencia = dpg.get_value("inteligencia")
    dominio = dpg.get_value("dominio")
    forca = dpg.get_value("forca_traco")
    fisica = dpg.get_value("fisica_traco")
    mental = dpg.get_value("mental_traco")
    sobrevivencia = dpg.get_value("sobrevivencia_traco")
    agilidade = dpg.get_value("agilidade_traco")
    destreza = dpg.get_value("destreza_traco")
    competencia = dpg.get_value("competencia_traco")
    criatividade = dpg.get_value("criatividade_traco")
    manipulacao = dpg.get_value("manipulacao_traco")
    sorte = dpg.get_value("sorte_traco")
    peso_1 = dpg.get_value("peso1")
    peso_2 = dpg.get_value("peso2")
    peso_3 = dpg.get_value("peso3")
    peso_4 = dpg.get_value("peso4")
    peso_5 = dpg.get_value("peso5")
    peso_6 = dpg.get_value("peso6")
    peso_7 = dpg.get_value("peso7")
    peso_8 = dpg.get_value("peso8")
    peso_9 = dpg.get_value("peso9")
    peso_10 = dpg.get_value("peso10")
    peso_11 = dpg.get_value("peso11")
    peso_12 = dpg.get_value("peso12")
    peso_13 = dpg.get_value("peso13")
    peso_14 = dpg.get_value("peso14")
    peso_15 = dpg.get_value("peso15")
    peso_16 = dpg.get_value("peso16")
    peso_17 = dpg.get_value("peso17")
    qtd_1 = dpg.get_value("qtd1")
    qtd_2 = dpg.get_value("qtd2")
    qtd_3 = dpg.get_value("qtd3")
    qtd_4 = dpg.get_value("qtd4")
    qtd_5 = dpg.get_value("qtd5")
    qtd_6 = dpg.get_value("qtd6")
    qtd_7 = dpg.get_value("qtd7")
    qtd_8 = dpg.get_value("qtd8")
    qtd_9 = dpg.get_value("qtd9")
    pda_1 = dpg.get_value("pda1")
    pda_2 = dpg.get_value("pda2")
    pda_3 = dpg.get_value("pda3")
    pda_4 = dpg.get_value("pda4")
    pda_5 = dpg.get_value("pda5")
    peso_total = peso_1 + peso_2 + peso_3 + peso_4 + peso_5 + peso_6 + peso_7 + peso_8 + qtd_1*peso_9 + qtd_2*peso_10 + qtd_3*peso_11 + qtd_4*peso_12 + qtd_5*peso_13 + qtd_6*peso_14 + qtd_7*peso_15 + qtd_8*peso_16 + qtd_9*peso_17
    dpg.configure_item("peso_carregado", default_value=peso_total)
    dpg.configure_item("capacidade", default_value=vigor+habilidade+forca)
    dpg.configure_item("cap_combate", default_value=vigor)
    dpg.configure_item("pdv_max", default_value=2*vigor+dominio)
    dpg.configure_item("pda_max", default_value=pda_1+pda_2+pda_3+pda_4+pda_5)
    dpg.configure_item("pde_max", default_value=inteligencia+percepcao+dominio)
    dpg.configure_item("forca_valor", default_value=vigor+habilidade+forca)
    dpg.configure_item("fisica_valor", default_value=vigor+percepcao+fisica)
    dpg.configure_item("mental_valor", default_value=vigor+inteligencia+mental)
    dpg.configure_item("sobrevivencia_valor", default_value=vigor+dominio+sobrevivencia)
    dpg.configure_item("agilidade_valor", default_value=habilidade+percepcao+agilidade)
    dpg.configure_item("destreza_valor", default_value=habilidade+dominio+destreza)
    dpg.configure_item("competencia_valor", default_value=inteligencia+habilidade+competencia)
    dpg.configure_item("criatividade_valor", default_value=inteligencia+percepcao+criatividade)
    dpg.configure_item("manipulacao_valor", default_value=inteligencia+dominio+manipulacao)
    dpg.configure_item("sorte_valor", default_value=dominio+percepcao+sorte)

def player_window():
    with dpg.window(label="Jogador", width=1000, no_close=True, pos=(0, 20)):
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
                        dpg.add_input_int(label="Capacidade em Combate", width=125, tag="cap_combate")
                        dpg.add_input_int(label="Dinheiro", width=125, tag="dinheiro")
                        dpg.add_input_int(label="Pts de XP", width=125, tag="pts_xp")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group(horizontal=True, horizontal_spacing=15):
                    with dpg.group(label="Atributes"):
                        dpg.add_text("Atributos")
                        dpg.add_input_int(label="Vigor", width=75, tag="vigor", callback=calculo)
                        dpg.add_input_int(label="Habilidade", width=75, tag="habilidade", callback=calculo)
                        dpg.add_input_int(label="Percepção", width=75, tag="percepcao", callback=calculo)
                        dpg.add_input_int(label="Inteligência", width=75, tag="inteligencia", callback=calculo)
                        dpg.add_input_int(label="Domínio", width=75, tag="dominio", callback=calculo)
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
                    with dpg.table(label="Tests&Traits", width=400, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Teste")
                        dpg.add_table_column(label="Valor")
                        dpg.add_table_column(label="Traço (+ ou -)")
                        with dpg.table_row():
                            dpg.add_text("Força\n(Vig+Hab)")
                            dpg.add_input_int(tag="forca_valor")
                            dpg.add_input_int(tag="forca_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Resistência Física\n(Vig+Per)")
                            dpg.add_input_int(tag="fisica_valor")
                            dpg.add_input_int(tag="fisica_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Resistência Mental\n(Vig+Int)")
                            dpg.add_input_int(tag="mental_valor")
                            dpg.add_input_int(tag="mental_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Sobrevivência\n(Vig+Dom)")
                            dpg.add_input_int(tag="sobrevivencia_valor")
                            dpg.add_input_int(tag="sobrevivencia_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Agilidade\n(Hab+Per)")
                            dpg.add_input_int(tag="agilidade_valor")
                            dpg.add_input_int(tag="agilidade_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Destreza\n(Hab+Dom)")
                            dpg.add_input_int(tag="destreza_valor")
                            dpg.add_input_int(tag="destreza_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Competência\n(Int+Hab)")
                            dpg.add_input_int(tag="competencia_valor")
                            dpg.add_input_int(tag="competencia_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Criatividade\n(Int+Per)")
                            dpg.add_input_int(tag="criatividade_valor")
                            dpg.add_input_int(tag="criatividade_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Manipulação\n(Int+Dom)")
                            dpg.add_input_int(tag="manipulacao_valor")
                            dpg.add_input_int(tag="manipulacao_traco", callback=calculo)
                        with dpg.table_row():
                            dpg.add_text("Sorte\n(Dom+Per)")
                            dpg.add_input_int(tag="sorte_valor")
                            dpg.add_input_int(tag="sorte_traco", callback=calculo)
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
                            dpg.add_input_int(tag="pda1", callback=calculo)
                            dpg.add_input_int(tag="peso4")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip2")
                            dpg.add_input_int(tag="pda2", callback=calculo)
                            dpg.add_input_int(tag="peso5")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip3")
                            dpg.add_input_int(tag="pda3", callback=calculo)
                            dpg.add_input_int(tag="peso6")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip4")
                            dpg.add_input_int(tag="pda4", callback=calculo)
                            dpg.add_input_int(tag="peso7")
                        with dpg.table_row():
                            dpg.add_input_text(tag="equip5")
                            dpg.add_input_int(tag="pda5", callback=calculo)
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
                            dpg.add_input_int(tag="qtd1", callback=calculo)
                            dpg.add_input_text(tag="item1")
                            dpg.add_input_int(tag="peso9", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd2", callback=calculo)
                            dpg.add_input_text(tag="item2")
                            dpg.add_input_int(tag="peso10", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd3", callback=calculo)
                            dpg.add_input_text(tag="item3")
                            dpg.add_input_int(tag="peso11", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd4", callback=calculo)
                            dpg.add_input_text(tag="item4")
                            dpg.add_input_int(tag="peso12", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd5", callback=calculo)
                            dpg.add_input_text(tag="item5")
                            dpg.add_input_int(tag="peso13", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd6", callback=calculo)
                            dpg.add_input_text(tag="item6")
                            dpg.add_input_int(tag="peso14", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd7", callback=calculo)
                            dpg.add_input_text(tag="item7")
                            dpg.add_input_int(tag="peso15", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd8", callback=calculo)
                            dpg.add_input_text(tag="item8")
                            dpg.add_input_int(tag="peso16", callback=calculo)
                        with dpg.table_row():
                            dpg.add_input_int(tag="qtd9", callback=calculo)
                            dpg.add_input_text(tag="item9")
                            dpg.add_input_int(tag="peso17", callback=calculo)

            with dpg.tab(label="Parte 2"):
                with dpg.group(horizontal=True):
                    with dpg.group():
                        dpg.add_text("História pregressa")
                        dpg.add_input_text(width=500, height=500, multiline=True, tag="historia")
                    with dpg.group(tag="parent"):
                        dpg.add_text("Nome do arquivo da imagem")
                        dpg.add_input_text(tag="imagem", hint="Cuidado! Você pode adicionar APENAS UMA imagem!", width=350)
                        dpg.add_button(label="Adicionar", callback=carregar_imagem)

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