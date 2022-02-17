import dearpygui.dearpygui as dpg
from views.master_window import *
from views.player_window import *
from views.rules_window import *

dpg.create_context()
dpg.create_viewport(title='RPG - Manager', width=1200, height=720, small_icon="icon.ico", large_icon="icon.ico")
dpg.setup_dearpygui()

def confirmar_1():
    master_window()

def confirmar_2():
    player_window()

def perfil():
    width1, height1, channels1, data1 = dpg.load_image("imgs/mestre.png")
    width2, height2, channels2, data2 = dpg.load_image("imgs/jogador.png")

    with dpg.texture_registry():
        dpg.add_static_texture(width1, height1, data1, tag="mestre_img")
        dpg.add_static_texture(width2, height2, data2, tag="jogador_img")

    with dpg.window(label="Início", width=400, height=250, pos=(400,100), collapsed=False):
        with dpg.group(width=190, horizontal=True):
            with dpg.group():
                dpg.add_image("mestre_img", width=150, height=150)
                dpg.add_text("Eu sou Mestre")
                dpg.add_button(tag="C_btn1", label="Confirmar", width=100, height=30, callback=confirmar_1)
            with dpg.group():
                dpg.add_image("jogador_img", width=150, height=150)
                dpg.add_text("Eu sou Jogador")
                dpg.add_button(tag="C_btn2", label="Confirmar", width=100, height=30, callback=confirmar_2)

with dpg.window(tag="Primary Window"):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Regras Gerais", callback=lambda: rules_window())
        dpg.add_menu_item(label="Mestre/Jogador", callback=lambda: perfil())

if __name__ == "__main__":
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()