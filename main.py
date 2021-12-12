import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='RPG - Manager', width=1000, height=700)

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

with dpg.window(label="Mestre", no_close=True):
    dpg.add_text("Hello, mestre")
    dpg.add_button(label="Save", callback=button_callback)
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

with dpg.window(label="Jogador", no_close=True):
    dpg.add_text("Hello, jogador")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()