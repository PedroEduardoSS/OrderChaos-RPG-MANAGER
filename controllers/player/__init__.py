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
    "descricao_fisica": dpg.get_value("descricao_fisica"),
    "imagem": dpg.get_value("imagem")}
    with open("models/player.json", "w") as file:
        json.dump(dict, file, indent=4)
    with dpg.window(label="Salvando", tag="salvando", width=150, height=20, pos=(500, 300), popup=True, modal=True, no_title_bar=True):
        dpg.add_text("Arquivo salvo!")
        dpg.add_button(label="Fechar", callback=lambda: dpg.delete_item("salvando"))
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (89, 89, 89), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("salvando", item_theme)

def carregar(sender, app_data):
    with dpg.window(label="Carregando", tag="carregando", width=150, height=20, pos=(500, 300), popup=True, modal=True, no_title_bar=True):
        dpg.add_text("Arquivo carregado!")
        dpg.add_button(label="Fechar", callback=lambda: dpg.delete_item("carregando"))
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (89, 89, 89), category=dpg.mvThemeCat_Core)

        dpg.bind_item_theme("carregando", item_theme)
    with open("models/player.json", "r") as file:
        dict = json.load(file)
        for k, v in dict.items():
            dpg.configure_item(k, default_value=v)
            if k == "imagem": carregar_imagem()

def carregar_imagem():
    img = dpg.get_value("imagem")
    width, height, channels, data = dpg.load_image(img)
    with dpg.texture_registry() as registry:
        img = dpg.add_static_texture(width, height, data, tag="texture_tag")
    dpg.add_image("texture_tag" , tag="adicionar", width=350, height=400, parent="parent")