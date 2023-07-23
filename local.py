import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import os
import requests
import threading
import subprocess

from settings import *

class LocalPage(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, fg_color=BACKGROUND_COLOR)

        self.iobit_path = tk.StringVar(value=IOBIT_UNLOCKER_PATH)
        self.stub_path = tk.StringVar(value="")
        self.tonemap_path = tk.StringVar(value="")
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
            self.iobit_message.set(IOBIT_FOUND_MESSAGE)
            self.iobit_status_label.configure(text_color=SUCCESS_TEXT_COLOR)
        else:
            self.iobit_message.set(IOBIT_NOT_FOUND_MESSAGE)
            self.iobit_status_label.configure(text_color=ERROR_TEXT_COLOR)

        self.stub_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)

        self.stub_location_input = ctk.CTkEntry(
            self.stub_frame,
            fg_color=ENTRYBOX_COLOR,
            border_width=0,
            state="disabled",
            textvariable=self.stub_path,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
            corner_radius=10,
            height=30,
            width=240,
        )
        self.stub_location_input.pack(side="left")

        self.browse_seperator_label =ctk.CTkLabel(
            self.stub_frame,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.browse_seperator_label.pack(side="left", padx=2, fill="x", expand=False)

        self.stub_location_button = ctk.CTkButton(
            self.stub_frame,
            fg_color=LIGHT_BUTTON_COLOR,
            text=BROWSE,
            font=FONT,
            text_color=TEXT_COLOR_LIGHT,
            command=self.stub_location_button_event,
            width=40,
            height=30,
            corner_radius=10,
            hover_color=HOVER_COLOR_LIGHT,
        )
        self.stub_location_button.pack(side="left", expand=True, fill="x")

        self.stub_frame.pack(expand=True, fill="x", side="top")

        self.tonemap_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)

        self.tonemap_location_input = ctk.CTkEntry(
            self.tonemap_frame,
            fg_color=ENTRYBOX_COLOR,
            border_width=0,
            state="disabled",
            textvariable=self.tonemap_path,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
            corner_radius=10,
            height=30,
            width=240,
        )
        self.tonemap_location_input.pack(side="left")

        self.browse_seperator_label =ctk.CTkLabel(
            self.tonemap_frame,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.browse_seperator_label.pack(side="left", padx=2, fill="x", expand=False)

        self.tonemap_location_button = ctk.CTkButton(
            self.tonemap_frame,
            fg_color=LIGHT_BUTTON_COLOR,
            text=BROWSE,
            font=FONT,
            text_color=TEXT_COLOR_LIGHT,
            command=self.tonemap_location_button_event,
            width=40,
            height=30,
            corner_radius=10,
            hover_color=HOVER_COLOR_LIGHT,
        )
        self.tonemap_location_button.pack(side="left", expand=True, fill="x")

        self.tonemap_frame.pack(expand=True, fill="x", side="top", pady=10)

        self.buttons_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
        self.buttons_frame.pack(expand=True, fill="x", side="top")

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
        )
        self.install_button.pack(side="right", fill="x", expand=True)

        self.iobit_location_input.bind("<Button-1>", self.iobit_location_button_event)

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

    def stub_location_button_event(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Binary Files", "*.bin")])
        self.stub_path.set(file_path)

    def tonemap_location_button_event(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Binary Files", "*.bin")])
        self.tonemap_path.set(file_path)

    def is_valid_file_path(self, file_path):
        return os.path.exists(file_path)

    def install(self):
        # disable button
        self.install_button.configure(state="disabled")

        current_directory = os.path.dirname(os.path.abspath(__file__))
        stub_path = self.stub_path.get()
        tone_mapping_path = self.tonemap_path.get()
        # Path to the PowerShell script
        script_path = os.path.join(current_directory, "iobit_installation.ps1")

        # Escape the iobit_path value for the command
        iobit_path_escaped = "'" + self.iobit_path.get() + "'"

        # check if stub or tone mapping path is not a valid file path
        if not self.is_valid_file_path(stub_path) or not self.is_valid_file_path(tone_mapping_path):
            # enable button
            self.install_button.configure(state="normal")
            self.stub_path.set(INVALID_FILE_PATH_MESSAGE)
            self.tonemap_path.set(INVALID_FILE_PATH_MESSAGE)
            return
        
        # change all forward slashes to backslashes
        stub_path = stub_path.replace("/", "\\")    
        tone_mapping_path = tone_mapping_path.replace("/", "\\")    

        # Escape the paths for PowerShell script arguments
        stub_path_escaped = "'" + stub_path + "'"
        tone_mapping_path_escaped = "'" + tone_mapping_path + "'"
            
        extra_arguments = fr"-iobitPath {iobit_path_escaped} -stubPath {stub_path_escaped} -toneMappingPath {tone_mapping_path_escaped}"

        p = subprocess.Popen(
            [
                "powershell.exe",
                "-ExecutionPolicy",
                "Bypass",
                "-noprofile",
                "-c",
                fr"""
                Start-Process -Verb RunAs -Wait powershell.exe -Args "
                -noprofile -ExecutionPolicy Bypass -c Set-Location \`"$PWD\`"; & '{script_path}' {extra_arguments}
                "
                """
            ]
        )
        p.communicate()

        # enable button
        self.install_button.configure(state="normal")



