import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import os
import requests
import threading
import subprocess

from settings import *

class IOBitPage(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, fg_color=BACKGROUND_COLOR)

        self.iobit_path = tk.StringVar(value=IOBIT_UNLOCKER_PATH)
        self.iobit_message = tk.StringVar(value=IOBIT_CHECKING_MESSAGE)

        self.iobit_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)

        self.iobit_location_input = ctk.CTkEntry(
            self.iobit_frame,
            fg_color=ENTRYBOX_COLOR,
            border_width=0,
            state="disabled",
            textvariable=self.iobit_path,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
            corner_radius=10,
            height=40,
            width=240,
        )
        self.iobit_location_input.pack(side="left")

        self.browse_seperator_label =ctk.CTkLabel(
            self.iobit_frame,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.browse_seperator_label.pack(side="left", padx=2, fill="x", expand=False)

        self.iobit_location_button = ctk.CTkButton(
            self.iobit_frame,
            fg_color=LIGHT_BUTTON_COLOR,
            text=BROWSE,
            font=FONT,
            text_color=TEXT_COLOR_LIGHT,
            command=self.iobit_location_button_event,
            width=40,
            height=40,
            corner_radius=10,
            hover_color=HOVER_COLOR_LIGHT,
        )
        self.iobit_location_button.pack(side="left", expand=True, fill="x")

        self.iobit_frame.pack(expand=True, fill="x", side="top")

        self.iobit_status_label = ctk.CTkLabel(
            self,
            fg_color=BACKGROUND_COLOR,
            textvariable=self.iobit_message,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.iobit_status_label.pack(side="top", anchor="w")

        iobit_status = self.is_valid_file_path(self.iobit_path.get())
        if iobit_status:
            print("IOBit Unlocker Found")
            self.iobit_message.set(IOBIT_FOUND_MESSAGE)
            self.iobit_status_label.configure(text_color=SUCCESS_TEXT_COLOR)
        else:
            print("IOBit Unlocker Not Found")
            self.iobit_message.set(IOBIT_NOT_FOUND_MESSAGE)
            self.iobit_status_label.configure(text_color=ERROR_TEXT_COLOR)

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
        self.preset_selector.pack(side="top", anchor="w", expand=True, fill="x")

        self.buttons_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
        self.buttons_frame.pack(expand=True, fill="x", side="top", pady=20)

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

        self.iobit_location_input.bind("<Button-1>", self.iobit_location_button_event)

        # Start fetching data in a separate thread
        threading.Thread(target=self.populate).start()

    def iobit_location_button_event(self, event=None):
        iobit_temp_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        if iobit_temp_path:
            if self.is_valid_file_path(iobit_temp_path):
                self.iobit_message.set(EXECUTABLE_FOUND_MESSAGE)
                self.iobit_status_label.configure(text_color=SUCCESS_TEXT_COLOR)

                self.iobit_path.set(iobit_temp_path)
            else:
                self.iobit_message.set(EXECUTABLE_NOT_FOUND_MESSAGE)
                self.iobit_status_label.configure(text_color=ERROR_TEXT_COLOR)

                self.iobit_path.set(iobit_temp_path)

    def is_valid_file_path(self, file_path):
        return os.path.exists(file_path)

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

    def install(self):
        threading.Thread(target=self.download_install).start()


    def uninstall(self):
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
        stub_path = os.path.join(current_directory, STUB_NAME)
        tone_mapping_path = os.path.join(current_directory, TONEMAP_NAME)
        # Path to the PowerShell script
        script_path = os.path.join(current_directory, "iobit_installation.ps1")

        # Escape the iobit_path value for the command
        iobit_path_escaped = "'" + self.iobit_path.get() + "'"

        # Escape the paths for PowerShell script arguments
        script_path_escaped = "'" + script_path + "'"
        stub_path_escaped = "'" + stub_path + "'"
        tone_mapping_path_escaped = "'" + tone_mapping_path + "'"

        extra_arguments = fr"-iobitPath {iobit_path_escaped} -stubPath {stub_path_escaped} -toneMappingPath {tone_mapping_path_escaped}"

        p = subprocess.Popen(
            [
                "powershell.exe",
                "-noprofile",
                "-c",
                fr"""
                Start-Process -Verb RunAs -Wait powershell.exe -Args "
                -noprofile -c Set-Location \`"$PWD\`"; & '{script_path}' {extra_arguments}
                "
                """
            ]
        )
        p.communicate()

        # enable buttons and combobox
        self.install_button.configure(state="normal")
        self.uninstall_button.configure(state="normal")
        self.preset_selector.configure(state="readonly")


