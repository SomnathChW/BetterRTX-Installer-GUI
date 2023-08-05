import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import os
import requests
import threading
import subprocess

from settings import *

class NativePage(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, fg_color=BACKGROUND_COLOR)

        self.space_label =ctk.CTkLabel(
            self,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.space_label.pack(side="top", pady=5, fill="x", expand=False)

        self.preset_selector = ctk.CTkComboBox(
            self,
            command=self.combobox_callback,
            height=40,
            corner_radius=10,
            border_width=0,
            button_color=LIGHT_BUTTON_COLOR,
            button_hover_color=HOVER_COLOR,
            fg_color=ENTRYBOX_COLOR,
            text_color=TEXT_COLOR_DARK,
            font=FONT,
            state="readonly",
            justify="center",
            dropdown_font=FONT,
            dropdown_fg_color=BUTTON_COLOR,
            dropdown_hover_color=HOVER_COLOR,
            dropdown_text_color=TEXT_COLOR_LIGHT,
        )
        self.preset_selector.pack(side="top", anchor="w", expand=False, fill="x")

        self.loading_label = ctk.CTkLabel(
            self,
            fg_color=BACKGROUND_COLOR,
            text=LOADING_MESSAGE,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.loading_label.pack(side="top", anchor="w")

        self.buttons_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
        self.buttons_frame.pack(fill="x", side="top")

        self.uninstall_button = ctk.CTkButton(
            self.buttons_frame,
            fg_color=BUTTON_COLOR,
            text="Restore Vanilla",
            font=FONT,
            text_color=TEXT_COLOR_LIGHT,
            command=self.uninstall,
            height=40,
            corner_radius=10,
            hover_color=HOVER_COLOR,
            state="disabled",
        )
        self.uninstall_button.pack(side="right", fill="x", expand=True)

        self.seperator_label =ctk.CTkLabel(
            self.buttons_frame,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.seperator_label.pack(side="right", padx=5, fill="x", expand=False)

        self.install_button = ctk.CTkButton(
            self.buttons_frame,
            fg_color=BUTTON_COLOR,
            text="Install",
            font=FONT,
            text_color=TEXT_COLOR_LIGHT,
            command=self.install,
            height=40,
            corner_radius=10,
            hover_color=HOVER_COLOR,
            state="disabled",
        )
        self.install_button.pack(side="right", fill="x", expand=True)

        self.note_label = ctk.CTkLabel(
            self,
            fg_color=BACKGROUND_COLOR,
            text=NOTE_REBOOT,
            font=FONT_BIG,
            text_color=INFORMATION_TEXT_COLOR,
        )
        self.note_label.pack(side="top", anchor="w", expand=False, fill="x", pady=10)

        threading.Thread(target=self.populate).start()

    def combobox_callback(self, selected_name):
        selected_item = next(
            (item for item in self.preset_list if item["name"] == selected_name), None
        )
        if selected_item:
            self.stub_url = selected_item["stub"]
            self.tonemapping_url = selected_item["tonemapping"]

    def download_file(self, url, filename):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

    def populate(self):
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            self.preset_list = response.json()
        names = [item["name"] for item in self.preset_list]
        self.preset_selector.configure(values=names)

        if names:
            self.preset_selector.set(names[0])
            self.stub_url = self.preset_list[0]["stub"]
            self.tonemapping_url = self.preset_list[0]["tonemapping"]
            self.install_button.configure(state="normal")
            self.uninstall_button.configure(state="normal")

        self.loading_label.configure(text_color = TEXT_COLOR_LIGHT)

    def install(self):
        self.loading_label.configure(text_color = TEXT_COLOR_DARK)
        threading.Thread(target=self.download_install).start()


    def uninstall(self):
        self.loading_label.configure(text_color = TEXT_COLOR_DARK)
        self.stub_url = VANILLA_STUB_URL
        self.tonemapping_url = VANILLA_TONEMAP_URL

        threading.Thread(target=self.download_install).start()

    def download_install(self):
        # disable buttons and combobox
        self.install_button.configure(state="disabled")
        self.uninstall_button.configure(state="disabled")
        self.preset_selector.configure(state="disabled")

        self.download_file(self.stub_url, STUB_NAME)
        self.download_file(self.tonemapping_url, TONEMAP_NAME)

        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Path to the PowerShell script
        script_path = os.path.join(current_directory, "native_installation.ps1")

        print(script_path)


        p = subprocess.Popen([
            "powershell.exe",
            "-ExecutionPolicy",
            "Bypass",
            "-noprofile",
            "-c",
            fr"""
            Start-Process -Verb RunAs -Wait powershell.exe -Args "
            -noprofile -ExecutionPolicy Bypass -c Set-Location \`"$PWD\`"; & '{script_path}'
            "
            """
        ])
        p.communicate()

        # enable buttons and combobox
        self.install_button.configure(state="normal")
        self.uninstall_button.configure(state="normal")
        self.preset_selector.configure(state="readonly")

        self.loading_label.configure(text_color = TEXT_COLOR_LIGHT)
