import customtkinter as ctk
import tkinter
from settings import *
from PIL import Image, ImageTk
import webbrowser
import requests
import io
import threading

from iobit import IOBitPage
from native import NativePage
from local import LocalPage

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = BACKGROUND_COLOR)
        self.title(INSTALLER_NAME)
        self.iconbitmap('./assets/icon.ico')
        self.geometry("550x300")
        self.resizable(False, False)
        self.configure_title_bar_color(TITLE_BAR_COLOR)

        self.columnconfigure(0, weight=4, uniform="a")
        self.columnconfigure(1, weight=6, uniform="a")

        self.placeholder_image = Image.open("./assets/BetterRTX.png")
        
        self.splash_image = ctk.CTkImage(light_image=self.placeholder_image, size=(220, 300))
        self.splash_label = ctk.CTkLabel(self, image=self.splash_image, text="", fg_color=BACKGROUND_COLOR)
        self.splash_label.grid(row = 0, column = 0, sticky = "nsew")

        # Download the image from the internet in a separate thread
        threading.Thread(target=self.download_and_fade_in_image).start()

        self.splash_label.bind("<Button-1>", lambda e: self.web_callback(COPYRIGHT_URL))

        self.main_frame = ctk.CTkFrame(self, fg_color = BACKGROUND_COLOR)
        self.main_frame.grid(row = 0, column = 1, sticky = "nsew")

        self.selection_frame = ctk.CTkFrame(self.main_frame, fg_color = BACKGROUND_COLOR)
        self.selection_frame.pack(expand=True, fill="x", side = "top")

        self.selection_frame.columnconfigure(0, weight=1, uniform="a")
        self.selection_frame.columnconfigure(1, weight=1, uniform="a")
        self.selection_frame.rowconfigure(0, weight=8, uniform="a")
        self.selection_frame.rowconfigure(1, weight=1, uniform="a")
        self.selection_frame.rowconfigure(2, weight=8, uniform="a")

        self.mode_selected = tkinter.IntVar(value=1)
        self.radiobutton_1 = ctk.CTkRadioButton(
            self.selection_frame, 
            width=5,
            height=5,
            text=IOBIT_MODE_MESSAGE, 
            font=FONT, 
            text_color=TEXT_COLOR_DARK, 
            hover=False,
            fg_color=SELECTED_BUTTON_COLOR,
            border_width_checked=11,
            border_width_unchecked=11,
            command=self.radiobutton_event, 
            variable= self.mode_selected, 
            value=1)
        self.radiobutton_2 = ctk.CTkRadioButton(
            self.selection_frame, 
            width=5,
            height=5,
            text=NATIVE_MODE_MESSAGE,
            font=FONT, 
            text_color=TEXT_COLOR_DARK, 
            hover=False,
            fg_color=SELECTED_BUTTON_COLOR,
            border_width_checked=11,
            border_width_unchecked=11,
            command=self.radiobutton_event, 
            variable= self.mode_selected, 
            value=2)
        self.radiobutton_3 = ctk.CTkRadioButton(
            self.selection_frame,
            width=5,
            height=5,
            text=LOCAL_MODE_MESSAGE,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
            hover=False,
            fg_color=SELECTED_BUTTON_COLOR,
            border_width_checked=11,
            border_width_unchecked=11,
            command=self.radiobutton_event,
            variable=self.mode_selected,
            value=3)

        self.radiobutton_1.grid(row=0, column=0, sticky='nsew')
        self.radiobutton_2.grid(row=0, column=1, sticky='nsew')
        self.radiobutton_3.grid(row=2, column=0, sticky='nsew', columnspan=2)

        # self.divider_label =ctk.CTkLabel(
        #     self.main_frame,
        #     fg_color=BACKGROUND_COLOR,
        #     text='',
        #     font=FONT,
        #     text_color=TEXT_COLOR_DARK,
        # )
        # self.divider_label.pack(side="top", pady=2, fill="x", expand=False)

        
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color = BACKGROUND_COLOR)
        self.content_frame.pack(expand=True, fill="x", side = "top")

        self.iobit_page = IOBitPage(self.content_frame)
        self.iobit_page.grid(row=0, column=0, sticky='nsew')

        self.native_page = NativePage(self.content_frame)
        self.native_page.grid(row=0, column=0, sticky='nsew')

        self.local_page = LocalPage(self.content_frame)
        self.local_page.grid(row=0, column=0, sticky='nsew')

        self.show_iobit_page()

        self.links_frame = ctk.CTkFrame(self.main_frame, fg_color = BACKGROUND_COLOR)
        self.links_frame.pack(fill="both", side = "top", pady=10, expand=False)

        discord_image = Image.open("./assets/discord-mark-blue.png")
        discord_image = discord_image.resize((30, 22))

        github_image = Image.open("./assets/github-mark.png")
        github_image = github_image.resize((30,30))

        self.padding_label =ctk.CTkLabel(
            self.links_frame,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.padding_label.pack(side="right", padx=12, fill="x", expand=False)

        self.github_image = ImageTk.PhotoImage(github_image)
        self.github_label = ctk.CTkLabel(self.links_frame, image=self.github_image, text="")
        self.github_label.pack(side="right")

        self.github_label.bind("<Button-1>", lambda e: self.web_callback(GITHUB_URL))

        self.seperator_label =ctk.CTkLabel(
            self.links_frame,
            fg_color=BACKGROUND_COLOR,
            text='',
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.seperator_label.pack(side="right", padx=5, fill="x", expand=False)
        
        self.discord_image = ImageTk.PhotoImage(discord_image)
        self.discord_label = ctk.CTkLabel(self.links_frame, image=self.discord_image, text="")
        self.discord_label.pack(side="right")

        self.discord_label.bind("<Button-1>", lambda e: self.web_callback(DISCORD_URL))

        self.copyright_label = ctk.CTkLabel(
            self.links_frame,
            fg_color=BACKGROUND_COLOR,
            text=COPYRIGHT,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.copyright_label.pack(side="left", anchor="w")

        self.version_label = ctk.CTkLabel(
            self.links_frame,
            fg_color=BACKGROUND_COLOR,
            text=VERSION,
            font=FONT,
            text_color=TEXT_COLOR_DARK,
        )
        self.version_label.pack(side="left", anchor="c", expand=True, fill="x")

        self.mainloop()

    def radiobutton_event(self):
        selection = self.mode_selected.get()
        if selection == 1:
            self.show_iobit_page()
        elif selection == 2:
            self.show_native_page()
        else:
            self.show_local_page()    

    def show_iobit_page(self):
        self.iobit_page.lift()

    def show_native_page(self):
        self.native_page.lift()

    def show_local_page(self):
        self.local_page.lift()

    def configure_title_bar_color(self, color):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = color | 0x00FFFFFF
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass

    def web_callback(self, url):
        webbrowser.open_new(url)

    def download_and_fade_in_image(self):
        # Simulate downloading the image from the internet
        downloaded_image = self.download_image_from_endpoint()
        if downloaded_image:
            # Convert the downloaded image to a PhotoImage
            self.downloaded_image = ctk.CTkImage(light_image=downloaded_image, size=(220, 300))

            # Define the function for fading
            def fade_image(alpha=0):
                if alpha <= 255:
                    blended_image = Image.blend(self.placeholder_image, downloaded_image, alpha / 255.0)
                    self.blended_image = ctk.CTkImage(light_image=blended_image, size=(220, 300))
                    self.splash_label.configure(image=self.blended_image)
                    self.update_idletasks()
                    # Schedule the next fading step after a delay
                    self.after(1, fade_image, alpha + 10)

            # Start the fading process
            fade_image()

            # Set the final image to the downloaded image after fading is complete
            self.after(255, lambda: self.splash_label.configure(image=self.downloaded_image))

    def download_image_from_endpoint(self):
        try:
            response = requests.get(BANNER_IMAGE_URL)
            if response.status_code == 200:
                response_image = Image.open(io.BytesIO(response.content))
                overlay_image = Image.open("./assets/overlay.png")
                logo_image = Image.open("./assets/logo.png")
                response_image.paste(logo_image, (0, 0), logo_image)
                response_image.paste(overlay_image, (0, 0), overlay_image)

                # Replace the BetterRTX logo file with the one from the internet
                response_image.save("./assets/BetterRTX.png")

                return response_image
            else:
                return None
        except Exception as e:
            print(f"Error fetching the image: {e}")
            return None

if __name__ == "__main__":
    App()