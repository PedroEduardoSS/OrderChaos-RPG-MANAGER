import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='RPG - Manager', width=1000, height=700)

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

with dpg.window(label="Master", no_close=True, pos=(0, 0)) as master_window:
    with dpg.menu_bar(label="MenuMaster"):
        dpg.add_menu_item(label="a")
        dpg.add_menu_item(label="b")
    dpg.add_text("Hello, mestre")
    dpg.add_button(label="Save", callback=button_callback)
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

with dpg.window(label="Player", no_close=True, pos=(500, 0)) as player_window:
    with dpg.tab_bar(label="MenuPlayer"):
        with dpg.tab(label="Parte 1"):
            with dpg.group(label="features"):
                dpg.add_input_text(label="Nome")
                dpg.add_input_text(label="Raça")
                dpg.add_input_text(label="Profissão")
                dpg.add_input_text(label="idade")
            dpg.add_spacer()
            dpg.add_separator()
            dpg.add_spacer()
            with dpg.group(label="Atributes&Status", horizontal=True):
                with dpg.group(label="Atributes"):
                    dpg.add_input_int(label="Vigor", width=75)
                    dpg.add_input_int(label="Habilidade", width=75)
                    dpg.add_input_int(label="Percepção", width=75)
                    dpg.add_input_int(label="Inteligência", width=75)
                    dpg.add_input_int(label="Domínio", width=75)
                with dpg.group(label="Status"):
                    dpg.add_input_int(label="PdV", width=75)
                    dpg.add_input_int(label="PdA", width=75)
                    dpg.add_input_int(label="PdE", width=75)

        with dpg.tab(label="Parte 2"):
            dpg.add_text("Hello, parte 2")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()