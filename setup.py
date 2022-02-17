import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["dearpygui", "json"],
"excludes": ["tkinter", "html", "email"],
"include_files": ["models", "imgs", "icon.ico"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "OrderChaos(RPG - MANAGER)",
    version = "1.1",
    description = "Gererenciador de Role-Playing Game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", icon="icon.ico", base=base)]
)