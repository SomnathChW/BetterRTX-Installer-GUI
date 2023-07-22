## Module: IOBIT
## File Name: `iobit.py`
This module contains the native graphical user interface page for the installer.

## Class: IOBitPage
This class represents the IOBit page in the application. It inherits from `customtkinter.CTkFrame` and provides functionality for selecting and installing presets with IOBit Unlocker.

### Methods
- `__init__(self, parent)`: Initializes the IOBitPage object.
- `iobit_location_button_event(self, event=None)`: Handles the event when the IOBit location button is clicked.
- `is_valid_file_path(self, file_path)`: Checks if a file path is valid.
- `combobox_callback(self, selected_name)`: Handles the event when a preset is selected from the combobox.
- `download_file(self, url, filename)`: Downloads a file from the specified URL and saves it with the given filename.
- `populate(self)`: Populates the combobox with preset names and initializes the default preset.
- `install(self)`: Initiates the installation process by starting a separate thread for downloading and installing the selected preset.
- `uninstall(self)`: Initiates the restoration process by starting a separate thread for downloading and installing the vanilla preset.
- `download_install(self)`: Downloads the necessary files and executes the installation or restoration process.

### Attributes
- `iobit_path`: A `StringVar` that stores the path to the IOBit Unlocker executable.
- `iobit_message`: A `StringVar` that stores the message related to the status of IOBit Unlocker.
- `iobit_frame`: A frame that contains the IOBit location input and browse button.
- `iobit_location_input`: An entry box for displaying the IOBit location.
- `browse_seperator_label`: A label widget used as a visual separator.
- `iobit_location_button`: A button for browsing and selecting the IOBit location.
- `iobit_status_label`: A label widget that displays the status of IOBit Unlocker.
- `preset_selector`: A combobox widget for selecting presets.
- `buttons_frame`: A frame that contains the Install and Restore buttons.
- `uninstall_button`: A button widget for restoring the vanilla preset.
- `seperator_label`: A label widget used as a visual separator.
- `install_button`: A button widget for installing the selected preset.
- `preset_list`: A list of presets obtained from the server.
- `stub_url`: The URL for downloading the stub file.
- `tonemapping_url`: The URL for downloading the tonemapping file.

### Example Usage
```python
iobit_page = IOBitPage(parent)
iobit_page.pack()
```

---
**Author:** SomnathChW  
**Last Modified:** July 22, 2023  

[![Discord](https://img.shields.io/badge/Join%20me%20on-Discord-7289DA?style=flat-square&logo=discord)](https://discord.com/users/753294480609902712)    
[![GitHub](https://img.shields.io/badge/Check%20out%20my-GitHub-181717?style=flat-square&logo=github)](https://github.com/SomnathChW)