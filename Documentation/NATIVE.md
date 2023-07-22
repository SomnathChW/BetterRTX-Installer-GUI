## Module: NATIVE
## File Name: `native.py`
This module contains the native graphical user interface page for the installer.

## Class: NativePage
This class represents the Native page in the application. It inherits from `customtkinter.CTkFrame` and provides functionality for selecting and installing presets.

### Methods
- `__init__(self, parent)`: Initializes the NativePage object.
- `combobox_callback(self, selected_name)`: Handles the event when a preset is selected from the combobox.
- `download_file(self, url, filename)`: Downloads a file from the specified URL and saves it with the given filename.
- `populate(self)`: Populates the combobox with preset names and initializes the default preset.
- `install(self)`: Initiates the installation process by starting a separate thread for downloading and installing the selected preset.
- `uninstall(self)`: Initiates the restoration process by starting a separate thread for downloading and installing the vanilla preset.
- `download_install(self)`: Downloads the necessary files and executes the installation or restoration process.

### Attributes
- `preset_selector`: A combobox widget for selecting presets.
- `buttons_frame`: A frame that contains the Install and Restore buttons.
- `uninstall_button`: A button widget for restoring the vanilla preset.
- `install_button`: A button widget for installing the selected preset.
- `seperator_label`: A label widget used as a visual separator.
- `note_label`: A label widget that displays a note about rebooting.
- `preset_list`: A list of presets obtained from the server.
- `stub_url`: The URL for downloading the stub file.
- `tonemapping_url`: The URL for downloading the tonemapping file.

### Example Usage
```python
native_page = NativePage(parent)
native_page.pack()
```


---
**Author:** SomnathChW  
**Last Modified:** July 22, 2023  

[![Discord](https://img.shields.io/badge/Join%20me%20on-Discord-7289DA?style=flat-square&logo=discord)](https://discord.com/users/753294480609902712)    
[![GitHub](https://img.shields.io/badge/Check%20out%20my-GitHub-181717?style=flat-square&logo=github)](https://github.com/SomnathChW)