import dearpygui.dearpygui as dpg
import json

def salvar(sender, app_data):
    dict = {"campanha_nome": dpg.get_value("campanha_nome"),
    "campanha": dpg.get_value("campanha"),
    "personagem1": dpg.get_value("personagem1"),
    "personagem2": dpg.get_value("personagem2"),
    "personagem3": dpg.get_value("personagem3"),
    "personagem4": dpg.get_value("personagem4"),
    "personagem5": dpg.get_value("personagem5"),
    "personagem6": dpg.get_value("personagem6"),
    "personagem7": dpg.get_value("personagem7"),
    "pdv1": dpg.get_value("pdv1"),
    "pdv2": dpg.get_value("pdv2"),
    "pdv3": dpg.get_value("pdv3"),
    "pdv4": dpg.get_value("pdv4"),
    "pdv5": dpg.get_value("pdv5"),
    "pdv6": dpg.get_value("pdv6"),
    "pdv7": dpg.get_value("pdv7"),
    "armor1": dpg.get_value("armor1"),
    "armor2": dpg.get_value("armor2"),
    "armor3": dpg.get_value("armor3"),
    "armor4": dpg.get_value("armor4"),
    "armor5": dpg.get_value("armor5"),
    "armor6": dpg.get_value("armor6"),
    "armor7": dpg.get_value("armor7"),
    "pde1": dpg.get_value("pde1"),
    "pde2": dpg.get_value("pde2"),
    "pde3": dpg.get_value("pde3"),
    "pde4": dpg.get_value("pde4"),
    "pde5": dpg.get_value("pde5"),
    "pde6": dpg.get_value("pde6"),
    "pde7": dpg.get_value("pde7"),
    "tracoPos1": dpg.get_value("tracoPos1"),
    "tracoPos2": dpg.get_value("tracoPos2"),
    "tracoPos3": dpg.get_value("tracoPos3"),
    "tracoPos4": dpg.get_value("tracoPos4"),
    "tracoPos5": dpg.get_value("tracoPos5"),
    "tracoPos6": dpg.get_value("tracoPos6"),
    "tracoPos7": dpg.get_value("tracoPos7"),
    "tracoNeg1": dpg.get_value("tracoNeg1"),
    "tracoNeg2": dpg.get_value("tracoNeg2"),
    "tracoNeg3": dpg.get_value("tracoNeg3"),
    "tracoNeg4": dpg.get_value("tracoNeg4"),
    "tracoNeg5": dpg.get_value("tracoNeg5"),
    "tracoNeg6": dpg.get_value("tracoNeg6"),
    "tracoNeg7": dpg.get_value("tracoNeg7"),
    "estado1": dpg.get_value("estado1"),
    "estado2": dpg.get_value("estado2"),
    "estado3": dpg.get_value("estado3"),
    "estado4": dpg.get_value("estado4"),
    "estado5": dpg.get_value("estado5"),
    "estado6": dpg.get_value("estado6"),
    "estado7": dpg.get_value("estado7"),
    "pts_xp1": dpg.get_value("pts_xp1"),
    "pts_xp2": dpg.get_value("pts_xp2"),
    "pts_xp3": dpg.get_value("pts_xp3"),
    "pts_xp4": dpg.get_value("pts_xp4"),
    "pts_xp5": dpg.get_value("pts_xp5"),
    "pts_xp6": dpg.get_value("pts_xp6"),
    "pts_xp7": dpg.get_value("pts_xp7"),
    "notas_mestre": dpg.get_value("notas_mestre"),
    "major_nome1": dpg.get_value("major_nome1"),
    "major_nome2": dpg.get_value("major_nome2"),
    "major_nome3": dpg.get_value("major_nome3"),
    "major_nome4": dpg.get_value("major_nome4"),
    "major_nome5": dpg.get_value("major_nome5"),
    "major_nome6": dpg.get_value("major_nome6"),
    "major_nome7": dpg.get_value("major_nome7"),
    "major_nome8": dpg.get_value("major_nome8"),
    "major_nome9": dpg.get_value("major_nome9"),
    "major_nome10": dpg.get_value("major_nome10"),
    "major_nome11": dpg.get_value("major_nome11"),
    "major_nome12": dpg.get_value("major_nome12"),
    "major_nome13": dpg.get_value("major_nome13"),
    "major_nome14": dpg.get_value("major_nome14"),
    "major_nome15": dpg.get_value("major_nome15"),
    "major_nome16": dpg.get_value("major_nome16"),
    "major_nome17": dpg.get_value("major_nome17"),
    "major_nome18": dpg.get_value("major_nome18"),
    "major_nome19": dpg.get_value("major_nome19"),
    "major_nome20": dpg.get_value("major_nome20"),
    "major_dif1": dpg.get_value("major_dif1"),
    "major_dif2": dpg.get_value("major_dif2"),
    "major_dif3": dpg.get_value("major_dif3"),
    "major_dif4": dpg.get_value("major_dif4"),
    "major_dif5": dpg.get_value("major_dif5"),
    "major_dif6": dpg.get_value("major_dif6"),
    "major_dif7": dpg.get_value("major_dif7"),
    "major_dif8": dpg.get_value("major_dif8"),
    "major_dif9": dpg.get_value("major_dif9"),
    "major_dif10": dpg.get_value("major_dif10"),
    "major_dif11": dpg.get_value("major_dif11"),
    "major_dif12": dpg.get_value("major_dif12"),
    "major_dif13": dpg.get_value("major_dif13"),
    "major_dif14": dpg.get_value("major_dif14"),
    "major_dif15": dpg.get_value("major_dif15"),
    "major_dif16": dpg.get_value("major_dif16"),
    "major_dif17": dpg.get_value("major_dif17"),
    "major_dif18": dpg.get_value("major_dif18"),
    "major_dif19": dpg.get_value("major_dif19"),
    "major_dif20": dpg.get_value("major_dif20"),
    "major_vida1": dpg.get_value("major_vida1"),
    "major_vida2": dpg.get_value("major_vida2"),
    "major_vida3": dpg.get_value("major_vida3"),
    "major_vida4": dpg.get_value("major_vida4"),
    "major_vida5": dpg.get_value("major_vida5"),
    "major_vida6": dpg.get_value("major_vida6"),
    "major_vida7": dpg.get_value("major_vida7"),
    "major_vida8": dpg.get_value("major_vida8"),
    "major_vida9": dpg.get_value("major_vida9"),
    "major_vida10": dpg.get_value("major_vida10"),
    "major_vida11": dpg.get_value("major_vida11"),
    "major_vida12": dpg.get_value("major_vida12"),
    "major_vida13": dpg.get_value("major_vida13"),
    "major_vida14": dpg.get_value("major_vida14"),
    "major_vida15": dpg.get_value("major_vida15"),
    "major_vida16": dpg.get_value("major_vida16"),
    "major_vida17": dpg.get_value("major_vida17"),
    "major_vida18": dpg.get_value("major_vida18"),
    "major_vida19": dpg.get_value("major_vida19"),
    "major_vida20": dpg.get_value("major_vida20"),
    "major_energia1": dpg.get_value("major_energia1"),
    "major_energia2": dpg.get_value("major_energia2"),
    "major_energia3": dpg.get_value("major_energia3"),
    "major_energia4": dpg.get_value("major_energia4"),
    "major_energia5": dpg.get_value("major_energia5"),
    "major_energia6": dpg.get_value("major_energia6"),
    "major_energia7": dpg.get_value("major_energia7"),
    "major_energia8": dpg.get_value("major_energia8"),
    "major_energia9": dpg.get_value("major_energia9"),
    "major_energia10": dpg.get_value("major_energia10"),
    "major_energia11": dpg.get_value("major_energia11"),
    "major_energia12": dpg.get_value("major_energia12"),
    "major_energia13": dpg.get_value("major_energia13"),
    "major_energia14": dpg.get_value("major_energia14"),
    "major_energia15": dpg.get_value("major_energia15"),
    "major_energia16": dpg.get_value("major_energia16"),
    "major_energia17": dpg.get_value("major_energia17"),
    "major_energia18": dpg.get_value("major_energia18"),
    "major_energia19": dpg.get_value("major_energia19"),
    "major_energia20": dpg.get_value("major_energia20"),
    "major_xp1": dpg.get_value("major_xp1"),
    "major_xp2": dpg.get_value("major_xp2"),
    "major_xp3": dpg.get_value("major_xp3"),
    "major_xp4": dpg.get_value("major_xp4"),
    "major_xp5": dpg.get_value("major_xp5"),
    "major_xp6": dpg.get_value("major_xp6"),
    "major_xp7": dpg.get_value("major_xp7"),
    "major_xp8": dpg.get_value("major_xp8"),
    "major_xp9": dpg.get_value("major_xp9"),
    "major_xp10": dpg.get_value("major_xp10"),
    "major_xp11": dpg.get_value("major_xp11"),
    "major_xp12": dpg.get_value("major_xp12"),
    "major_xp13": dpg.get_value("major_xp13"),
    "major_xp14": dpg.get_value("major_xp14"),
    "major_xp15": dpg.get_value("major_xp15"),
    "major_xp16": dpg.get_value("major_xp16"),
    "major_xp17": dpg.get_value("major_xp17"),
    "major_xp18": dpg.get_value("major_xp18"),
    "major_xp19": dpg.get_value("major_xp19"),
    "major_xp20": dpg.get_value("major_xp20"),
    "temp_nome1": dpg.get_value("temp_nome1"),
    "temp_nome2": dpg.get_value("temp_nome2"),
    "temp_nome3": dpg.get_value("temp_nome3"),
    "temp_nome4": dpg.get_value("temp_nome4"),
    "temp_nome5": dpg.get_value("temp_nome5"),
    "temp_nome6": dpg.get_value("temp_nome6"),
    "temp_nome7": dpg.get_value("temp_nome7"),
    "temp_nome8": dpg.get_value("temp_nome8"),
    "temp_nome9": dpg.get_value("temp_nome9"),
    "temp_nome10": dpg.get_value("temp_nome10"),
    "temp_nome11": dpg.get_value("temp_nome11"),
    "temp_nome12": dpg.get_value("temp_nome12"),
    "temp_nome13": dpg.get_value("temp_nome13"),
    "temp_nome14": dpg.get_value("temp_nome14"),
    "temp_nome15": dpg.get_value("temp_nome15"),
    "temp_dif1": dpg.get_value("temp_dif1"),
    "temp_dif2": dpg.get_value("temp_dif2"),
    "temp_dif3": dpg.get_value("temp_dif3"),
    "temp_dif4": dpg.get_value("temp_dif4"),
    "temp_dif5": dpg.get_value("temp_dif5"),
    "temp_dif6": dpg.get_value("temp_dif6"),
    "temp_dif7": dpg.get_value("temp_dif7"),
    "temp_dif8": dpg.get_value("temp_dif8"),
    "temp_dif9": dpg.get_value("temp_dif9"),
    "temp_dif10": dpg.get_value("temp_dif10"),
    "temp_dif11": dpg.get_value("temp_dif11"),
    "temp_dif12": dpg.get_value("temp_dif12"),
    "temp_dif13": dpg.get_value("temp_dif13"),
    "temp_dif14": dpg.get_value("temp_dif14"),
    "temp_dif15": dpg.get_value("temp_dif15"),
    "temp_vida1": dpg.get_value("temp_vida1"),
    "temp_vida2": dpg.get_value("temp_vida2"),
    "temp_vida3": dpg.get_value("temp_vida3"),
    "temp_vida4": dpg.get_value("temp_vida4"),
    "temp_vida5": dpg.get_value("temp_vida5"),
    "temp_vida6": dpg.get_value("temp_vida6"),
    "temp_vida7": dpg.get_value("temp_vida7"),
    "temp_vida8": dpg.get_value("temp_vida8"),
    "temp_vida9": dpg.get_value("temp_vida9"),
    "temp_vida10": dpg.get_value("temp_vida10"),
    "temp_vida11": dpg.get_value("temp_vida11"),
    "temp_vida12": dpg.get_value("temp_vida12"),
    "temp_vida13": dpg.get_value("temp_vida13"),
    "temp_vida14": dpg.get_value("temp_vida14"),
    "temp_vida15": dpg.get_value("temp_vida15"),
    "temp_energia1": dpg.get_value("temp_energia1"),
    "temp_energia2": dpg.get_value("temp_energia2"),
    "temp_energia3": dpg.get_value("temp_energia3"),
    "temp_energia4": dpg.get_value("temp_energia4"),
    "temp_energia5": dpg.get_value("temp_energia5"),
    "temp_energia6": dpg.get_value("temp_energia6"),
    "temp_energia7": dpg.get_value("temp_energia7"),
    "temp_energia8": dpg.get_value("temp_energia8"),
    "temp_energia9": dpg.get_value("temp_energia9"),
    "temp_energia10": dpg.get_value("temp_energia10"),
    "temp_energia11": dpg.get_value("temp_energia11"),
    "temp_energia12": dpg.get_value("temp_energia12"),
    "temp_energia13": dpg.get_value("temp_energia13"),
    "temp_energia14": dpg.get_value("temp_energia14"),
    "temp_energia15": dpg.get_value("temp_energia15"),
    "temp_xp1": dpg.get_value("temp_xp1"),
    "temp_xp2": dpg.get_value("temp_xp2"),
    "temp_xp3": dpg.get_value("temp_xp3"),
    "temp_xp4": dpg.get_value("temp_xp4"),
    "temp_xp5": dpg.get_value("temp_xp5"),
    "temp_xp6": dpg.get_value("temp_xp6"),
    "temp_xp7": dpg.get_value("temp_xp7"),
    "temp_xp8": dpg.get_value("temp_xp8"),
    "temp_xp9": dpg.get_value("temp_xp9"),
    "temp_xp10": dpg.get_value("temp_xp10"),
    "temp_xp11": dpg.get_value("temp_xp11"),
    "temp_xp12": dpg.get_value("temp_xp12"),
    "temp_xp13": dpg.get_value("temp_xp13"),
    "temp_xp14": dpg.get_value("temp_xp14"),
    "temp_xp15": dpg.get_value("temp_xp15")
    }
    with open("master.json", "w") as file:
        json.dump(dict, file, indent=4)
    with dpg.window(label="Salvando", tag="salvando", width=150, height=20, pos=(500, 300), popup=True, modal=True, no_title_bar=True):
        dpg.add_text("Arquivo salvo!")
        dpg.add_button(label="Fechar", callback=lambda: dpg.delete_item("salvando"))
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (89, 89, 89), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("salvando", item_theme)

def carregar(sender, app_data):
    with open("master.json", "r") as file:
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

def master_window():
    with dpg.window(label="Mestre",width=600, no_close=True, pos=(0, 0)):
        with dpg.tab_bar(label="MenuMaster"):
            with dpg.tab(label="Geral"):
                with dpg.group():
                    dpg.add_text("Nome da Campanha")
                    dpg.add_input_text(width=450, tag="campanha_nome")
                    dpg.add_text("Campanha")
                    dpg.add_input_text(width=450, multiline=True, tag="campanha")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group():
                    dpg.add_text("Tabela de Dificuldades")
                    with dpg.table(label="Difficulties", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Teste", width=125, width_fixed=True)
                        dpg.add_table_column(label="Descrição")
                        
                        with dpg.table_row():
                            dpg.add_text("Força")
                            dpg.add_text("Combate corpo-a-corpo, peso, escalar, nadar")
                        
                        with dpg.table_row():
                            dpg.add_text("Resis. Física")
                            dpg.add_text("Resistir a danos físicos, se defender")
                        
                        with dpg.table_row():
                            dpg.add_text("Resis. Mental")
                            dpg.add_text("Resistir qualquer ação que afete a mente")
                        
                        with dpg.table_row():
                            dpg.add_text("Sobrevivência")
                            dpg.add_text("Resistir elementos naturais, venenos ou químicas")
                        
                        with dpg.table_row():
                            dpg.add_text("Agilidade")
                            dpg.add_text("Iniciativa de combate, armas de curta, média e longa distância e arremessar objetos")
                        
                        with dpg.table_row():
                            dpg.add_text("Destreza")
                            dpg.add_text("Performaces corporais, esportes e conduzir veículos")
                        
                        with dpg.table_row():
                            dpg.add_text("Competência")
                            dpg.add_text("Realizar um trabalho específico (decifrar um código, destrancar uma porta)")
                        
                        with dpg.table_row():
                            dpg.add_text("Criatividade")
                            dpg.add_text("Imaginar, deduzir, investigar, rastrear, analisar, improvisar objetos ou situações")
                        
                        with dpg.table_row():
                            dpg.add_text("Manipulação")
                            dpg.add_text("Blefar, trapacear, influenciar, simular, atuar e liderar")
                        
                        with dpg.table_row():
                            dpg.add_text("Sorte")
                            dpg.add_text("Qualquer ação que não dependa da sua performance")
                    
                    dpg.add_spacer()
                    dpg.add_text("Exemplos de ações genéricas")
                    with dpg.table(label="Example", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Ação")
                        dpg.add_table_column(label="Dificuldade")
                        dpg.add_table_column(label="Teste")

                        with dpg.table_row():
                            dpg.add_text("Saltar 1,5 metros")
                            dpg.add_text("20")
                            dpg.add_text("Força")

                        with dpg.table_row():
                            dpg.add_text("Esquivar de um golpe")
                            dpg.add_text("21")
                            dpg.add_text("Agilidade")

                        with dpg.table_row():
                            dpg.add_text("Intimidar")
                            dpg.add_text("22")
                            dpg.add_text("Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Identificar blefe")
                            dpg.add_text("26")
                            dpg.add_text("Resis. Mental")

                        with dpg.table_row():
                            dpg.add_text("Ganhar no cara e coroa")
                            dpg.add_text("31")
                            dpg.add_text("Sorte")

                        with dpg.table_row():
                            dpg.add_text("Salto carpado")
                            dpg.add_text("38")
                            dpg.add_text("Destreza")

                        with dpg.table_row():
                            dpg.add_text("Pintar um retrato")
                            dpg.add_text("41")
                            dpg.add_text("Criatividade")

                        with dpg.table_row():
                            dpg.add_text("Resistir um golpe")
                            dpg.add_text("42")
                            dpg.add_text("Resis. Física")

                        with dpg.table_row():
                            dpg.add_text("Resistir hipotermia")
                            dpg.add_text("42")
                            dpg.add_text("Sobrevivência")

                        with dpg.table_row():
                            dpg.add_text("Falsificar documento")
                            dpg.add_text("52")
                            dpg.add_text("Competência")

                    dpg.add_spacer()
                    dpg.add_text("Estados")
                    with dpg.table(label="States", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Estado")
                        dpg.add_table_column(label="Testes afetados (-)")

                        with dpg.table_row():
                            dpg.add_text("Medo")
                            dpg.add_text("Resis. Mental, Competência")

                        with dpg.table_row():
                            dpg.add_text("Desespero")
                            dpg.add_text("Resis. Mental, Competência, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Estresse")
                            dpg.add_text("Resis. Mental, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Descontrole")
                            dpg.add_text("Resis. Mental, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Inconsciente")
                            dpg.add_text("Resis. Física, Competência")

                        with dpg.table_row():
                            dpg.add_text("Tontura")
                            dpg.add_text("Força, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Embriaguez")
                            dpg.add_text("Resis. Mental, Competência, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Náusea")
                            dpg.add_text("Força, Criatividade, Competência")

                        with dpg.table_row():
                            dpg.add_text("Hemorragia")
                            dpg.add_text("Força, Resis. Física, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Fratura")
                            dpg.add_text("Força, Resis. Física, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Envenenamento")
                            dpg.add_text("Força, Sobrevivência")

                        with dpg.table_row():
                            dpg.add_text("Fome")
                            dpg.add_text("Força, Sobrevivência")

                        with dpg.table_row():
                            dpg.add_text("Frio/Calor")
                            dpg.add_text("Força, Agilidade")

                        with dpg.table_row():
                            dpg.add_text("Humilhação")
                            dpg.add_text("Resis. Mental, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Trauma Físico")
                            dpg.add_text("Força, Resis. Física")

                        with dpg.table_row():
                            dpg.add_text("Trauma Psicológico")
                            dpg.add_text("Resis. Mental, Competência, Criatividade")

                        with dpg.table_row():
                            dpg.add_text("Mente Controlada")
                            dpg.add_text("Resis. Mental, Competência, Criatividade")

                        with dpg.table_row():
                            dpg.add_text("Estado crítico de saúde")
                            dpg.add_text("Todos os testes")

                    dpg.add_spacer()
                    dpg.add_text("Armas")
                    with dpg.table(label="Weapons", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Armas")
                        dpg.add_table_column(label="Mod. de Dano")
                        dpg.add_table_column(label="Teste usado")
                        dpg.add_table_column(label="Peso")

                        with dpg.table_row():
                            dpg.add_text("Faca/Adaga")
                            dpg.add_text("+15")
                            dpg.add_text("Força")
                            dpg.add_text("0.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Faca/Adaga")
                            dpg.add_text("+15")
                            dpg.add_text("Força")
                            dpg.add_text("0.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Foice")
                            dpg.add_text("+20")
                            dpg.add_text("Força")
                            dpg.add_text("3Kg")

                        with dpg.table_row():
                            dpg.add_text("Espada")
                            dpg.add_text("+30")
                            dpg.add_text("Força")
                            dpg.add_text("2.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Espada longa (2-mãos)")
                            dpg.add_text("+40")
                            dpg.add_text("Força")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Katana (2-mãos)")
                            dpg.add_text("+42")
                            dpg.add_text("Força")
                            dpg.add_text("2.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Machadinho")
                            dpg.add_text("+18")
                            dpg.add_text("Força")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Machado de guerra")
                            dpg.add_text("+33")
                            dpg.add_text("Força")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Alabarda/Machado Grande (2-mãos)")
                            dpg.add_text("+35")
                            dpg.add_text("Força")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Marreta (2-mãos)")
                            dpg.add_text("+45")
                            dpg.add_text("Força")
                            dpg.add_text("10Kg")

                        with dpg.table_row():
                            dpg.add_text("Porrete")
                            dpg.add_text("+18")
                            dpg.add_text("Força")
                            dpg.add_text("3Kg")

                        with dpg.table_row():
                            dpg.add_text("Maça dentada")
                            dpg.add_text("+23")
                            dpg.add_text("Força")
                            dpg.add_text("7Kg")

                        with dpg.table_row():
                            dpg.add_text("Chicote")
                            dpg.add_text("+8")
                            dpg.add_text("Força")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Tridente (2-mãos")
                            dpg.add_text("+33")
                            dpg.add_text("Força")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Bastão (2-mãos)")
                            dpg.add_text("+9")
                            dpg.add_text("Força")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Arco curto")
                            dpg.add_text("+16")
                            dpg.add_text("Destreza")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Arco longo")
                            dpg.add_text("+20")
                            dpg.add_text("Destreza")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Shuriken")
                            dpg.add_text("+15")
                            dpg.add_text("Destreza")
                            dpg.add_text("0.1Kg")

                        with dpg.table_row():
                            dpg.add_text("Rifle de precisão")
                            dpg.add_text("+80")
                            dpg.add_text("Destreza")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Besta")
                            dpg.add_text("+18")
                            dpg.add_text("Agilidade")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Revólver")
                            dpg.add_text("+28")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1Kg")

                        with dpg.table_row():
                            dpg.add_text("Pistola semi-auto")
                            dpg.add_text("+30")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1Kg")

                        with dpg.table_row():
                            dpg.add_text("Espingarda")
                            dpg.add_text("+40")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Submetralhadora")
                            dpg.add_text("+33")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Rifle de assalto")
                            dpg.add_text("+45")
                            dpg.add_text("Agilidade")
                            dpg.add_text("2Kg")

                    dpg.add_spacer()
                    dpg.add_text("Equipamentos")
                    with dpg.table(label="Armor", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Equipamento")
                        dpg.add_table_column(label="Pontos de Armadura")
                        dpg.add_table_column(label="Peso")

                        with dpg.table_row():
                            dpg.add_text("Traje de peles")
                            dpg.add_text("4")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Traje de couro")
                            dpg.add_text("6")
                            dpg.add_text("2.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Cota de malha")
                            dpg.add_text("13")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Peitoral de ferro")
                            dpg.add_text("20")
                            dpg.add_text("10Kg")

                        with dpg.table_row():
                            dpg.add_text("Colete à prova de balas (leve)")
                            dpg.add_text("30")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Colete à prova de balas (médio)")
                            dpg.add_text("40")
                            dpg.add_text("6Kg")

                        with dpg.table_row():
                            dpg.add_text("Armadura samurai")
                            dpg.add_text("30")
                            dpg.add_text("15Kg")

                        with dpg.table_row():
                            dpg.add_text("Couraça de aço")
                            dpg.add_text("35")
                            dpg.add_text("20Kg")

                        with dpg.table_row():
                            dpg.add_text("Colete à prova de balas (pesado)")
                            dpg.add_text("50")
                            dpg.add_text("10Kg")

                        with dpg.table_row():
                            dpg.add_text("Arm. Cavaleiro")
                            dpg.add_text("60")
                            dpg.add_text("30Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo de madeira")
                            dpg.add_text("15")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Scutum (escudo romano)")
                            dpg.add_text("18")
                            dpg.add_text("6Kg")

                        with dpg.table_row():
                            dpg.add_text("Broquel (escudo pequeno)")
                            dpg.add_text("12")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo de ferro")
                            dpg.add_text("22")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo de aço")
                            dpg.add_text("28")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo eletrônico")
                            dpg.add_text("50")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Capacete de couro")
                            dpg.add_text("4")
                            dpg.add_text("1Kg")

                        with dpg.table_row():
                            dpg.add_text("Capacete de obras")
                            dpg.add_text("6")
                            dpg.add_text("0.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Capacete militar moderno")
                            dpg.add_text("12")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Elmo Viking")
                            dpg.add_text("5")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Elmo de cavaleiro")
                            dpg.add_text("10")
                            dpg.add_text("2Kg")

            with dpg.tab(label="Jogadores"):
                with dpg.group():
                    dpg.add_text("Jogadores da campanha")
                    with dpg.table(label="Players", width=1000, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Personagem")
                        dpg.add_table_column(label="PdV")
                        dpg.add_table_column(label="PdA")
                        dpg.add_table_column(label="PdE")
                        dpg.add_table_column(label="Traço +")
                        dpg.add_table_column(label="Traço -")
                        dpg.add_table_column(label="Estado")
                        dpg.add_table_column(label="Pts XP")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem1")
                            dpg.add_input_int(tag="pdv1")
                            dpg.add_input_int(tag="armor1")
                            dpg.add_input_int(tag="pde1")
                            dpg.add_input_text(tag="tracoPos1")
                            dpg.add_input_text(tag="tracoNeg1")
                            dpg.add_input_text(tag="estado1")
                            dpg.add_input_int(tag="pts_xp1")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem2")
                            dpg.add_input_int(tag="pdv2")
                            dpg.add_input_int(tag="armor2")
                            dpg.add_input_int(tag="pde2")
                            dpg.add_input_text(tag="tracoPos2")
                            dpg.add_input_text(tag="tracoNeg2")
                            dpg.add_input_text(tag="estado2")
                            dpg.add_input_int(tag="pts_xp2")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem3")
                            dpg.add_input_int(tag="pdv3")
                            dpg.add_input_int(tag="armor3")
                            dpg.add_input_int(tag="pde3")
                            dpg.add_input_text(tag="tracoPos3")
                            dpg.add_input_text(tag="tracoNeg3")
                            dpg.add_input_text(tag="estado3")
                            dpg.add_input_int(tag="pts_xp3")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem4")
                            dpg.add_input_int(tag="pdv4")
                            dpg.add_input_int(tag="armor4")
                            dpg.add_input_int(tag="pde4")
                            dpg.add_input_text(tag="tracoPos4")
                            dpg.add_input_text(tag="tracoNeg4")
                            dpg.add_input_text(tag="estado4")
                            dpg.add_input_int(tag="pts_xp4")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem5")
                            dpg.add_input_int(tag="pdv5")
                            dpg.add_input_int(tag="armor5")
                            dpg.add_input_int(tag="pde5")
                            dpg.add_input_text(tag="tracoPos5")
                            dpg.add_input_text(tag="tracoNeg5")
                            dpg.add_input_text(tag="estado5")
                            dpg.add_input_int(tag="pts_xp5")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem6")
                            dpg.add_input_int(tag="pdv6")
                            dpg.add_input_int(tag="armor6")
                            dpg.add_input_int(tag="pde6")
                            dpg.add_input_text(tag="tracoPos6")
                            dpg.add_input_text(tag="tracoNeg6")
                            dpg.add_input_text(tag="estado6")
                            dpg.add_input_int(tag="pts_xp6")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem7")
                            dpg.add_input_int(tag="pdv7")
                            dpg.add_input_int(tag="armor7")
                            dpg.add_input_int(tag="pde7")
                            dpg.add_input_text(tag="tracoPos7")
                            dpg.add_input_text(tag="tracoNeg7")
                            dpg.add_input_text(tag="estado7")
                            dpg.add_input_int(tag="pts_xp7")

                    dpg.add_spacer()
                    dpg.add_separator()
                    dpg.add_spacer()
                    dpg.add_text("Notas")
                    dpg.add_input_text(width=500, height=400, multiline=True, tag="notas_mestre")

            with dpg.tab(label="NPCs"):
                dpg.add_text("NPCs - Non-Player Characters")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group():
                    dpg.add_text("Recorrentes")
                    with dpg.table(label="major", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Nome")
                        dpg.add_table_column(label="Dificuldade")
                        dpg.add_table_column(label="Pontos de Vida")
                        dpg.add_table_column(label="Pontos de Energia")
                        dpg.add_table_column(label="Experiência")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome1")
                            dpg.add_input_int(tag="major_dif1")
                            dpg.add_input_text(tag="major_vida1")
                            dpg.add_input_text(tag="major_energia1")
                            dpg.add_input_text(tag="major_xp1")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome2")
                            dpg.add_input_int(tag="major_dif2")
                            dpg.add_input_text(tag="major_vida2")
                            dpg.add_input_text(tag="major_energia2")
                            dpg.add_input_text(tag="major_xp2")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome3")
                            dpg.add_input_int(tag="major_dif3")
                            dpg.add_input_text(tag="major_vida3")
                            dpg.add_input_text(tag="major_energia3")
                            dpg.add_input_text(tag="major_xp3")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome4")
                            dpg.add_input_int(tag="major_dif4")
                            dpg.add_input_text(tag="major_vida4")
                            dpg.add_input_text(tag="major_energia4")
                            dpg.add_input_text(tag="major_xp4")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome5")
                            dpg.add_input_int(tag="major_dif5")
                            dpg.add_input_text(tag="major_vida5")
                            dpg.add_input_text(tag="major_energia5")
                            dpg.add_input_text(tag="major_xp5")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome6")
                            dpg.add_input_int(tag="major_dif6")
                            dpg.add_input_text(tag="major_vida6")
                            dpg.add_input_text(tag="major_energia6")
                            dpg.add_input_text(tag="major_xp6")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome7")
                            dpg.add_input_int(tag="major_dif7")
                            dpg.add_input_text(tag="major_vida7")
                            dpg.add_input_text(tag="major_energia7")
                            dpg.add_input_text(tag="major_xp7")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome8")
                            dpg.add_input_int(tag="major_dif8")
                            dpg.add_input_text(tag="major_vida8")
                            dpg.add_input_text(tag="major_energia8")
                            dpg.add_input_text(tag="major_xp8")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome9")
                            dpg.add_input_int(tag="major_dif9")
                            dpg.add_input_text(tag="major_vida9")
                            dpg.add_input_text(tag="major_energia9")
                            dpg.add_input_text(tag="major_xp9")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome10")
                            dpg.add_input_int(tag="major_dif10")
                            dpg.add_input_text(tag="major_vida10")
                            dpg.add_input_text(tag="major_energia10")
                            dpg.add_input_text(tag="major_xp10")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome11")
                            dpg.add_input_int(tag="major_dif11")
                            dpg.add_input_text(tag="major_vida11")
                            dpg.add_input_text(tag="major_energia11")
                            dpg.add_input_text(tag="major_xp11")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome12")
                            dpg.add_input_int(tag="major_dif12")
                            dpg.add_input_text(tag="major_vida12")
                            dpg.add_input_text(tag="major_energia12")
                            dpg.add_input_text(tag="major_xp12")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome13")
                            dpg.add_input_int(tag="major_dif13")
                            dpg.add_input_text(tag="major_vida13")
                            dpg.add_input_text(tag="major_energia13")
                            dpg.add_input_text(tag="major_xp13")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome14")
                            dpg.add_input_int(tag="major_dif14")
                            dpg.add_input_text(tag="major_vida14")
                            dpg.add_input_text(tag="major_energia14")
                            dpg.add_input_text(tag="major_xp14")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome15")
                            dpg.add_input_int(tag="major_dif15")
                            dpg.add_input_text(tag="major_vida15")
                            dpg.add_input_text(tag="major_energia15")
                            dpg.add_input_text(tag="major_xp15")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome16")
                            dpg.add_input_int(tag="major_dif16")
                            dpg.add_input_text(tag="major_vida16")
                            dpg.add_input_text(tag="major_energia16")
                            dpg.add_input_text(tag="major_xp16")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome17")
                            dpg.add_input_int(tag="major_dif17")
                            dpg.add_input_text(tag="major_vida17")
                            dpg.add_input_text(tag="major_energia17")
                            dpg.add_input_text(tag="major_xp17")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome18")
                            dpg.add_input_int(tag="major_dif18")
                            dpg.add_input_text(tag="major_vida18")
                            dpg.add_input_text(tag="major_energia18")
                            dpg.add_input_text(tag="major_xp18")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome19")
                            dpg.add_input_int(tag="major_dif19")
                            dpg.add_input_text(tag="major_vida19")
                            dpg.add_input_text(tag="major_energia19")
                            dpg.add_input_text(tag="major_xp19")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome20")
                            dpg.add_input_int(tag="major_dif20")
                            dpg.add_input_text(tag="major_vida20")
                            dpg.add_input_text(tag="major_energia20")
                            dpg.add_input_text(tag="major_xp20")
                    
                    dpg.add_spacer()
                    dpg.add_text("Temporários")
                    with dpg.table(label="Temporary", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Nome")
                        dpg.add_table_column(label="Dificuldade")
                        dpg.add_table_column(label="Pontos de Vida")
                        dpg.add_table_column(label="Pontos de Energia")
                        dpg.add_table_column(label="Experiência")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome1")
                            dpg.add_input_int(tag="temp_dif1")
                            dpg.add_input_text(tag="temp_vida1")
                            dpg.add_input_text(tag="temp_energia1")
                            dpg.add_input_text(tag="temp_xp1")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome2")
                            dpg.add_input_int(tag="temp_dif2")
                            dpg.add_input_text(tag="temp_vida2")
                            dpg.add_input_text(tag="temp_energia2")
                            dpg.add_input_text(tag="temp_xp2")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome3")
                            dpg.add_input_int(tag="temp_dif3")
                            dpg.add_input_text(tag="temp_vida3")
                            dpg.add_input_text(tag="temp_energia3")
                            dpg.add_input_text(tag="temp_xp3")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome4")
                            dpg.add_input_int(tag="temp_dif4")
                            dpg.add_input_text(tag="temp_vida4")
                            dpg.add_input_text(tag="temp_energia4")
                            dpg.add_input_text(tag="temp_xp4")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome5")
                            dpg.add_input_int(tag="temp_dif5")
                            dpg.add_input_text(tag="temp_vida5")
                            dpg.add_input_text(tag="temp_energia5")
                            dpg.add_input_text(tag="temp_xp5")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome6")
                            dpg.add_input_int(tag="temp_dif6")
                            dpg.add_input_text(tag="temp_vida6")
                            dpg.add_input_text(tag="temp_energia6")
                            dpg.add_input_text(tag="temp_xp6")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome7")
                            dpg.add_input_int(tag="temp_dif7")
                            dpg.add_input_text(tag="temp_vida7")
                            dpg.add_input_text(tag="temp_energia7")
                            dpg.add_input_text(tag="temp_xp7")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome8")
                            dpg.add_input_int(tag="temp_dif8")
                            dpg.add_input_text(tag="temp_vida8")
                            dpg.add_input_text(tag="temp_energia8")
                            dpg.add_input_text(tag="temp_xp8")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome9")
                            dpg.add_input_int(tag="temp_dif9")
                            dpg.add_input_text(tag="temp_vida9")
                            dpg.add_input_text(tag="temp_energia9")
                            dpg.add_input_text(tag="temp_xp9")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome10")
                            dpg.add_input_int(tag="temp_dif10")
                            dpg.add_input_text(tag="temp_vida10")
                            dpg.add_input_text(tag="temp_energia10")
                            dpg.add_input_text(tag="temp_xp10")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome11")
                            dpg.add_input_int(tag="temp_dif11")
                            dpg.add_input_text(tag="temp_vida11")
                            dpg.add_input_text(tag="temp_energia11")
                            dpg.add_input_text(tag="temp_xp11")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome12")
                            dpg.add_input_int(tag="temp_dif12")
                            dpg.add_input_text(tag="temp_vida12")
                            dpg.add_input_text(tag="temp_energia12")
                            dpg.add_input_text(tag="temp_xp12")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome13")
                            dpg.add_input_int(tag="temp_dif13")
                            dpg.add_input_text(tag="temp_vida13")
                            dpg.add_input_text(tag="temp_energia13")
                            dpg.add_input_text(tag="temp_xp13")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome14")
                            dpg.add_input_int(tag="temp_dif14")
                            dpg.add_input_text(tag="temp_vida14")
                            dpg.add_input_text(tag="temp_energia14")
                            dpg.add_input_text(tag="temp_xp14")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome15")
                            dpg.add_input_int(tag="temp_dif15")
                            dpg.add_input_text(tag="temp_vida15")
                            dpg.add_input_text(tag="temp_energia15")
                            dpg.add_input_text(tag="temp_xp15")
            
            with dpg.tab(label="Salvar"):
                dpg.add_text("Importante! Salve todas as alterações no botão abaixo!")
                dpg.add_text("Importante! Carregue os dados já salvos ")
                dpg.add_button(label="Salvar", callback=salvar)
                dpg.add_button(label="Carregar", callback=carregar)