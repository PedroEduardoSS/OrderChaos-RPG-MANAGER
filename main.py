import dearpygui.dearpygui as dpg
from views.master_window import *
from views.player_window import *
from views.rules_window import *

dpg.create_context()
dpg.create_viewport(title='RPG - Manager', width=1200, height=720, small_icon="icon.ico", large_icon="icon.ico")
dpg.setup_dearpygui()

with dpg.window(tag="Primary Window"):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Regras Gerais", callback=lambda: rules_window())
        with dpg.menu(label="Mestre/Jogador"):
            dpg.add_menu_item(label="Covil do Mestre", callback=lambda: master_window())
            dpg.add_menu_item(label="Ficha do Jogador", callback=lambda: player_window())

if __name__ == "__main__":
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()