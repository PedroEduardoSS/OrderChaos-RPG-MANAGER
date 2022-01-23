import dearpygui.dearpygui as dpg

def rules_window():
    with dpg.window(label="Regras", width=700, no_close=True, pos=(0, 0)):
        with dpg.tab_bar(label="MenuRules"):
            with dpg.tab(label="Sistema"):
                dpg.add_text("Nessa janela você verá o resumo dos principais tópicos\ndo sistema para te auxiliar.", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Esse software utiliza o sistema de RPG Order & Chaos,\npois é um sistema flexível e você poderá adaptar todas\nas histórias que sua imaginação permitir!\nLeia o livro oficial para ter as informações completas.")

            with dpg.tab(label="Atributos"):
                dpg.add_text("Os Atributos são os pilares fundamentais para a construção\ndo seu personagem", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Personagens de Jogador recém-criados começam\ncom dez pontos em cada um dos Atributos. Você\npode escolher retirar de um e adicionar em outro\nconforme desejar.\n\nAcima de 15 pontos, cada subsequente custará\num ponto a mais do que o anterior. Portanto,\nadicionar um décimo-sexto ponto custará 2 pontos,\no décimo-sétimo custará 3 pontos, e assim\nsucessivamente.", color=(255, 0, 0))
                dpg.add_spacer()
                dpg.add_text("Personagens recém-criados não devem ultrapassar\n20 pontos ou ter menos de 1 em qualquer Atributo\n10 pontos representa o valor médio de um humano\nnormal.", color=(255, 0, 0))
                dpg.add_spacer()
                dpg.add_text("Os Atributos são:")
                dpg.add_text("Vigor (VIG)\nExemplos: Força Física, Resistência, Saúde", bullet=True)
                dpg.add_text("Habilidade (HAB)\nExemplos: Performance, ação premeditada", bullet=True)
                dpg.add_text("Percepção (PER)\nExemplos: Intuição, Improviso, Adaptação", bullet=True)
                dpg.add_text("Inteligência (INT)\nExemplos: Desenvolver e Resolver problemas", bullet=True)
                dpg.add_text("Domínio (DOM)\nExemplos: Como se utiliza recursos físicos,\nmentais e sociais", bullet=True)

            with dpg.tab(label="Testes"):
                pass
            with dpg.tab(label="Características"):
                pass
            with dpg.tab(label="Itens & Equipamentos"):
                pass
            with dpg.tab(label="Combate"):
                pass
            with dpg.tab(label="Magias & Habilidades Especiais"):
                pass