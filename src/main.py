import dearpygui.dearpygui as dpg
import os



dpg.create_context()
dpg.create_viewport(title='Markery', small_icon=os.path.join('res', 'logo.ico'))

with dpg.window(tag='main_window'):
    pass

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('main_window', True)
dpg.start_dearpygui()
dpg.destroy_context()


