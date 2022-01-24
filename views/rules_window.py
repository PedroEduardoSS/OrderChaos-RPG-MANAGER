import dearpygui.dearpygui as dpg

def rules_window():
    with dpg.window(label="Regras", width=700, pos=(0, 0)):
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
                dpg.add_text("Os Testes são ações realizadas pelo Mestre e os\njogadores que possuem alguma dificuldade.", color=(255, 0, 0))
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Tabela de Dificuldades")
                with dpg.table(label="Difficulties", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column(label="Teste", width=200, width_fixed=True)
                    dpg.add_table_column(label="Descrição")

                    with dpg.table_row():
                        dpg.add_text("Força (VIG + HAB)")
                        dpg.add_text("Combate corpo-a-corpo, peso, escalar, nadar")

                    with dpg.table_row():
                        dpg.add_text("Resis. Física (VIG + PER)")
                        dpg.add_text("Resistir a danos físicos, se defender")

                    with dpg.table_row():
                        dpg.add_text("Resis. Mental (VIG + INT)")
                        dpg.add_text("Resistir qualquer ação que afete a mente")

                    with dpg.table_row():
                        dpg.add_text("Sobrevivência (VIG + DOM)")
                        dpg.add_text("Resistir elementos naturais, venenos ou químicas")

                    with dpg.table_row():
                        dpg.add_text("Agilidade (HAB + PER)")
                        dpg.add_text("Iniciativa de combate, armas de curta, média e longa distância e arremessar objetos")

                    with dpg.table_row():
                        dpg.add_text("Destreza (HAB + DOM)")
                        dpg.add_text("Performaces corporais, esportes e conduzir veículos")

                    with dpg.table_row():
                        dpg.add_text("Competência (INT + HAB)")
                        dpg.add_text("Realizar um trabalho específico (decifrar um código, destrancar uma porta)")

                    with dpg.table_row():
                        dpg.add_text("Criatividade (INT + PER)")
                        dpg.add_text("Imaginar, deduzir, investigar, rastrear, analisar, improvisar objetos ou situações")

                    with dpg.table_row():
                        dpg.add_text("Manipulação (INT + DOM)")
                        dpg.add_text("Blefar, trapacear, influenciar, simular, atuar e liderar")

                    with dpg.table_row():
                        dpg.add_text("Sorte (DOM + PER)")
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

            with dpg.tab(label="Características"):
                pass
            with dpg.tab(label="Itens & Equipamentos"):
                pass
            with dpg.tab(label="Combate"):
                pass
            with dpg.tab(label="Magias & Habilidades Especiais"):
                pass