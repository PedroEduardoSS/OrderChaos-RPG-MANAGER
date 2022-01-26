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
                dpg.add_text("Os Atributos são os pilares fundamentais para a construção\ndo seu personagem.", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Personagens de Jogador recém-criados começam\ncom dez pontos em cada um dos Atributos. Você\npode escolher retirar de um e adicionar em outro\nconforme desejar.\n\nAcima de 15 pontos, cada subsequente custará\num ponto a mais do que o anterior. Portanto,\nadicionar um décimo-sexto ponto custará 2 pontos,\no décimo-sétimo custará 3 pontos, e assim\nsucessivamente.", bullet=True)
                dpg.add_spacer()
                dpg.add_text("Personagens recém-criados não devem ultrapassar\n20 pontos ou ter menos de 1 em qualquer Atributo\n10 pontos representa o valor médio de um humano\nnormal.", bullet=True)
                dpg.add_spacer()
                dpg.add_text("Os Atributos são:")
                dpg.add_text("Vigor (VIG)\nExemplos: Força Física, Resistência, Saúde", bullet=True)
                dpg.add_text("Habilidade (HAB)\nExemplos: Performance, ação premeditada", bullet=True)
                dpg.add_text("Percepção (PER)\nExemplos: Intuição, Improviso, Adaptação", bullet=True)
                dpg.add_text("Inteligência (INT)\nExemplos: Desenvolver e Resolver problemas", bullet=True)
                dpg.add_text("Domínio (DOM)\nExemplos: Como se utiliza recursos físicos,\nmentais e sociais", bullet=True)

            with dpg.tab(label="Testes"):
                dpg.add_text("Os Testes são ações realizadas pelo Mestre e os\njogadores que possuem alguma dificuldade.", bullet=True)
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
                dpg.add_text("Etapa fundamental para Mestres e jogadores.", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Lista de características:")
                dpg.add_text("Raças: Caberá ao Mestre criar as raças e seus diferenciais no Atributos", bullet=True)
                dpg.add_text("Alinhamento: Um guia para a interpretação", bullet=True)
                dpg.add_text("Profissão: Pode ter valor narrativo e mecânico", bullet=True)
                dpg.add_text("Idade: Olhe a tabela baseada em um humano moderno.\nO mestre decide o valor do teste afetado", bullet=True)
                with dpg.table(label="Idade", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column(label="Idade")
                    dpg.add_table_column(label="teste afetado")

                    with dpg.table_row():
                        dpg.add_text("Infante (1-16)")
                        dpg.add_text("(-) Força e Resis. Física, (+) Criatividade")

                    with dpg.table_row():
                        dpg.add_text("Adulto (17-49)")
                        dpg.add_text("Nenhum")

                    with dpg.table_row():
                        dpg.add_text("Meia-idade (50-64)")
                        dpg.add_text("(-) Força e Agilidade, (+) Competência")

                    with dpg.table_row():
                        dpg.add_text("Idoso (65-90)")
                        dpg.add_text("(-) Força, Agilidade e Sobrevivência")

                    with dpg.table_row():
                        dpg.add_text("Ancião (90+)")
                        dpg.add_text("(-) Todos, exceto Sorte")

                dpg.add_text("Condição Financeira: 1d20 + Domínio, valor real é definido pelo Mestre.", bullet=True)
                with dpg.table(label="Idade", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column(label="1d20 + DOM")
                    dpg.add_table_column(label="Condição Financeira")

                    with dpg.table_row():
                        dpg.add_text("2-7")
                        dpg.add_text("Miserável ou de renúncia Material")

                    with dpg.table_row():
                        dpg.add_text("8-14")
                        dpg.add_text("Pobre, residência e posses humildes")

                    with dpg.table_row():
                        dpg.add_text("15-24")
                        dpg.add_text("Classe média, vive bem não ostensivamente")

                    with dpg.table_row():
                        dpg.add_text("25-34")
                        dpg.add_text("Classe média alta, bem assegurado")

                    with dpg.table_row():
                        dpg.add_text("35+")
                        dpg.add_text("Rico, tem acesso ao melhor que o dinheiro oferece")

                dpg.add_text("Traços: O personagem precisa de 1 traço positivo e 1 negativo,\ncontanto que não sejam antagônicos.", bullet=True)
                with dpg.table(label="TraitsPositives", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column(label="1d20")
                    dpg.add_table_column(label="Traços Positivos")
                    dpg.add_table_column(label="Testes afetados (+)")

                    with dpg.table_row():
                        dpg.add_text("20")
                        dpg.add_text("Sentidos aguçados\nSaúde de ferro\nEmpatia pura\nSerenidade")
                        dpg.add_text("Competência, Agilidade\nDestreza, Sobrevivência\nCriatividade, Sorte\nRes. Mental, Criatividade")

                    with dpg.table_row():
                        dpg.add_text("17-19")
                        dpg.add_text("Regeneração rápida\nRes. à temperatura/química\nValentia desmedida à...\nImunidade à...")
                        dpg.add_text("Resistência Física\nSobrevivência\nResistência Mental\nSobrevivência")

                    with dpg.table_row():
                        dpg.add_text("13-16")
                        dpg.add_text("Perfeccionismo\nConcentração\nSensatez\nModeração")
                        dpg.add_text("Competência\nDestreza\nCriatividade\nResistência Menta")

                    with dpg.table_row():
                        dpg.add_text("9-12")
                        dpg.add_text("Diligência\nOtimismo\nCoragem\nHonradez")
                        dpg.add_text("Competência\nResistência Mental\nResistência Mental\nManipulação")

                    with dpg.table_row():
                        dpg.add_text("5-8")
                        dpg.add_text("Hipertrofia\nRobustez\nAtraente\nConhecido como justo")
                        dpg.add_text("Força\nResistência Física\nManipulação\nManipulação")

                    with dpg.table_row():
                        dpg.add_text("2-4")
                        dpg.add_text("Paciência\nBom humor\nCeticismo\nFlexibilidade")
                        dpg.add_text("Manipulação\nResistência Mental\nResistência Mental\nCriatividade")

                    with dpg.table_row():
                        dpg.add_text("1")
                        dpg.add_text("Extroversão\nPerspicácia\nSagacidade\nEloquência")
                        dpg.add_text("Manipulação\nCriatividade\nAgilidade\nManipulação")
                dpg.add_spacer()
                with dpg.table(label="TraitsNegatives", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column(label="1d20")
                    dpg.add_table_column(label="Traços Negativos")
                    dpg.add_table_column(label="Testes afetados (-)")

                    with dpg.table_row():
                        dpg.add_text("1")
                        dpg.add_text("Limitação física/sensorial\nDoença degenerativa\nPsicopatia\nAutodestruição")
                        dpg.add_text("Força, R.Fís./Compet., R.Men.\nForça, R.Fís., Sobrevivência\nSorte, Criatividade\nRes. Mental, Criatividade")

                    with dpg.table_row():
                        dpg.add_text("2-4")
                        dpg.add_text("Doença crônica/mental**\nVulnerável à temp./quím.\nFobia incontrolável à\nAlergia à")
                        dpg.add_text("Força, R.Fís./Compet., R.Men.\nSobrevivência\nResistência Mental\nSobrevivência")

                    with dpg.table_row():
                        dpg.add_text("5-8")
                        dpg.add_text("Negligência\nDistração\nInsensatez\nCompulsão")
                        dpg.add_text("Competência\nDestreza\nCriatividade\nResistência Mental")

                    with dpg.table_row():
                        dpg.add_text("9-12")
                        dpg.add_text("Preguiça\nPessimismo\nCovardia\nDesonra")
                        dpg.add_text("Competência\nResistência Mental\nResistência Mental\nManipulação")

                    with dpg.table_row():
                        dpg.add_text("13-16")
                        dpg.add_text("Desnutrição\nBaixa estatura\nRepulsividade\nConhecido como injusto")
                        dpg.add_text("Força\nResistência Física\nManipulação\nManipulação")

                    with dpg.table_row():
                        dpg.add_text("17-19")
                        dpg.add_text("Pavio curto\nDepressão\nFanatismo\nTeimosia")
                        dpg.add_text("Manipulação\nResistência Mental\nResistência Mental\nCriatividade")

                    with dpg.table_row():
                        dpg.add_text("20")
                        dpg.add_text("Timidez\nIngenuidade\nMonotonia\nDicção prejudicada")
                        dpg.add_text("Manipulação\nCriatividade\nAgilidade\nManipulação")

                dpg.add_text("Estados: características passageiras que podem progredir e evoluir.\nO quanto o Estado afetará o Teste dependerá do Mestre.", bullet=True)
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

                dpg.add_text("Físico e gênero: Na Ficha de Personagem, poderá ser acrescentada\na descrição física para enriquecer a campanha.", bullet=True)
                dpg.add_text("História pregressa: Na Ficha de Personagem, você deve escrever a\nhistória do seu personagem antes da campanha.", bullet=True)

            with dpg.tab(label="Itens & Equipamentos"):
                dpg.add_text("Os Itens e os Equipamentos podem ter múltiplas serventias dentro da campanha.", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Peso e Capacidade: Capacidade = Força (cada ponto = 1Kg)\nCapacidade em Combate = Vigor (cada ponto = 1Kg)\nEm ambas Capacidades, caso excedida, O Jogador sofrerá\n-1 em Testes de Vigor e Habilidade para cada quilo excedente.", bullet=True)
                dpg.add_text("Sistema Econômico: Todos os objetos possuem um preço, cabe\nao Mestre definir o sistema monetário da campanha.", bullet=True)
                dpg.add_text("Itens Mágicos: Definidos pelo Mestre, (valor, peso, dano e\noutras características), contanto que não quebre\na mecânica do jogo.", bullet=True)
                dpg.add_text("Armas", bullet=True)
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
                dpg.add_text("Equipamentos", bullet=True)
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

            with dpg.tab(label="Combate"):
                dpg.add_text("A mecânica mais complexa e importante do Sistema O&C.\nDependendo do contexto, a narrativa sempre tomará precedência\nsobre uma situação de combate.", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Pontos de Vida (PdV): Vida do jogador. Se for = 0, o personagem está morto.\nCálculo = 2 x Vigor + Domínio.", bullet=True)
                dpg.add_text("Pontos de Energia (PdE): Recurso especial e/ou mágico. Uma vez zerado,\no personagem entrará em Estado de\nCansaço, sofrendo penalidades em todos Testes que\nenvolvem combate ou danos aos PdV até que um ponto\nde PdE seja recuperado.\nCálculo = Inteligência + Percepção + Domínio.", bullet=True)
                dpg.add_text("Pontos de Armadura (PdA): Todos os Itens & Equipamentos equipados.\nQuando o alvo é atingido, metade do dano\nserá consumido pela PdA e a outra pela PdV.\nSe o dano for menor que a metade da PdA, o dano consumirá\ntoda a PdA.", bullet=True)

                dpg.add_text("Acerto Crítico: Ação ou Retaliação com resultado do 1d20 = 20,\nignora o PdA.", bullet=True)
                dpg.add_text("Falha Crítica: Ação ou Retaliação com resultado do 1d20 = 1,\nocorre a Falha Crítica O Mestre deverá descrever a ação \ndentro do pior contexto possível e aplicar o Cálculo de Dano\nda Ação do personagem contra ele mesmo, com a Absorção\nde Dano equivalente a uma falha em Esquivar.", bullet=True)

                dpg.add_text("Cálculo de Dano")
                with dpg.table(label="CalcDano", header_row=False, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column()
                    dpg.add_table_column()

                    with dpg.table_row():
                        dpg.add_text("Armas corpo-a-corpo/a distância")
                        dpg.add_text("Valor obtido na Ação + Modificador de Dano")

                    with dpg.table_row():
                        dpg.add_text("Sem armas")
                        dpg.add_text("Valor obtido na Ação")

                    with dpg.table_row():
                        dpg.add_text("Uso de Magia/Habilidade Especial")
                        dpg.add_text("Valor obtido na Ação + quantidade de PdE usado")

                dpg.add_text("Absorção de Dano")
                with dpg.table(label="AbsDano", header_row=False, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                    dpg.add_table_column()
                    dpg.add_table_column()

                    with dpg.table_row():
                        dpg.add_text("Fora de Combate")
                        dpg.add_text("1d20 + Resistência Física vs. dano estipulado pelo Mestre")

                    with dpg.table_row():
                        dpg.add_text("Reação de Defender OU situação sem chance de esquiva ou defesa")
                        dpg.add_text("1d20 + Resistência Física vs. Cálculo de Dano")

                    with dpg.table_row():
                        dpg.add_text("Reação de Esquivar (no caso de falha)")
                        dpg.add_text("Resistência Física vs. Cálculo de Dano")

                    with dpg.table_row():
                        dpg.add_text("Reação de não Esquivar/Defender (Retaliação garantida)")
                        dpg.add_text("Resistência Física vs. Cálculo de Dano")

                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Turnos de combate:")
                dpg.add_text("[1] Iniciativa: 1d20 + Agilidade e ordem decrescente", bullet=True)
                dpg.add_text("[2] Ação: O Jogador/NPC descreve a ação e realiza o\nrespectivo teste", bullet=True)
                dpg.add_text("[3] Reação: Quem recebe a Ação descreve sua Reação\n(Esquivar = 1d20 + Agilidade ou Defender = 1d20 + Res. Física", bullet=True)
                dpg.add_text("[4a] Efeito da Ação: Se o teste da Ação > Reação,\nentão aplica o Cálculo de Dano vs. Absorção de Dano", bullet=True)
                dpg.add_text("[4b] Retaliação: Quando o Jogador/NPC decidir receber\no golpe diretamente (Leia o livro para mais informações)", bullet=True)
                dpg.add_text("[5] Fim de Turno: Recomeço de outra rodada, exceto\nquando o personagem perde a chance de retaliação com o resultado <= 11", bullet=True)

            with dpg.tab(label="Magias & Habilidades Especiais"):
                dpg.add_text("As Magias & Habilidades Especiais diferenciam \npersonagens em relação ao seu grupo e os que habitam\no universo da campanha. Podem ser interpretadas ou\nreconhecidas de formas diferentes, podendo ser mais ou\nmenos acessíveis de acordo com o contexto ou realismo da\nhistória da campanha que será jogada.", bullet=True)
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                dpg.add_text("Qualquer Magia ou Habilidade Especial utilizará Pontos \nde Energia, onde a quantia gasta indicará a potência da\nmesma.", bullet=True)
                dpg.add_text("Magias & Habilidades Especiais utilizam o Teste de\nCompetência, portanto personagens que possuem altas\npontuações em Habilidade e Inteligência possuem natural\nvantagem no exercício delas. Cada vez que utilizadas, o\nusuário deverá rolar o dado duas vezes (2d20), onde apenas\no maior resultado deverá ser somado ao Teste performado.", bullet=True)
                dpg.add_text("Existem talentos e poderes que não necessariamente\nse encaixam no que conhecemos por “magia”. Nesta\ncategoria, podemos incluir qualquer tipo de Ação que pode\nser considerada especial dentro do contexto da aventura.", bullet=True)
                dpg.add_spacer()
                dpg.add_text("Tipos de Magia + Exemplos (Leia o Livro para maiores informações):")
                dpg.add_text("Encantamentos & Maldições\n(Objetos, Animais, Plantas, Sencientes)", bullet=True)
                dpg.add_text("Abjuração\n(Anulação, Cura, Barreira Espiritual, Absorção/Exaustão)", bullet=True)
                dpg.add_text("Alquimia\n(Elixir de Cura, Veneno, Antídoto, Pó da Invisibilidade)", bullet=True)
                dpg.add_text("Transmutação\n(Transformação bestial/corpórea, Transfiguração,\nIlusão material, Réplica)", bullet=True)
                dpg.add_text("Translocação\n(Teleporte, Troca de Corpo, Telecinese, Projeção Astral)", bullet=True)
                dpg.add_text("Conjuração\n(Fogo, Ar, Água, Terra, Eletricidade, Natureza, Metal,\nLuz, Trevas)", bullet=True)
                dpg.add_text("Mentalização\n(Telepatia, Clarividência, Controle Mental, Psicometria)", bullet=True)