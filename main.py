# main.py
# -*- coding: utf-8 -*-
import customtkinter as ctk
from ui import NovelGeneratorGUI


def configure_ui_theme():
    """配置全局主题，提升界面一致性。"""
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")


def main():
    configure_ui_theme()
    app = ctk.CTk()
    gui = NovelGeneratorGUI(app)
    app.mainloop()

if __name__ == "__main__":
    main()
