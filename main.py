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

    with dpg.window(label="Início", width=400, height=250, pos=(400,100), collapsed=False, no_close=True):
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
        mi1 = dpg.add_menu_item(label="Regras Gerais", callback=lambda: rules_window())
        mi2 = dpg.add_menu_item(label="Mestre/Jogador", callback=lambda: perfil())

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (204, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, (204, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (210, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Tab, (204, 0, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (230, 184, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (179, 143, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (230, 184, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (230, 184, 0), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

if __name__ == "__main__":
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()