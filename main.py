import dearpygui.dearpygui as dpg
from views.master_window import *
from views.player_window import *

dpg.create_context()
dpg.create_viewport(title='RPG - Manager', width=1200, height=720, small_icon="icon.ico", large_icon="icon.ico")
dpg.setup_dearpygui()

master_window()
player_window()

if __name__ == "__main__":
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()