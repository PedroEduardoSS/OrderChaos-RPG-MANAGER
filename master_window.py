import dearpygui.dearpygui as dpg

def master_window():
    with dpg.window(label="Master", no_close=True, pos=(0, 0)):
        with dpg.menu_bar(label="MenuMaster"):
            dpg.add_menu_item(label="a")
            dpg.add_menu_item(label="b")
        dpg.add_text("Hello, mestre")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)