## Module: LOCAL

## File Name: `local.py`

This module contains the local graphical user interface page for the installer.

## Class: LocalPage

This class represents the Local page in the application. It inherits from `customtkinter.CTkFrame` and provides functionality for selecting and installing local presets with IOBit Unlocker.

### Methods

-   `__init__(self, parent)`: Initializes the LocalPage object.
-   `iobit_location_button_event(self, event=None)`: Handles the event when the IOBit location button is clicked.
-   `stub_location_button_event(self, event=None)`: Handles the event when the stub location button is clicked.
-   `tonemap_location_button_event(self, event=None)`: Handles the event when the tonemapping location button is clicked.
-   `is_valid_file_path(self, file_path)`: Checks if a file path is valid.
-   `install(self)`: Initiates the installation process by starting a separate thread for downloading and installing the selected preset.
-   `install_in_thread(self)`: Downloads the necessary files and executes the installation process.

### Attributes

-   `iobit_path`: A `StringVar` that stores the path to the IOBit Unlocker executable.
-   `iobit_message`: A `StringVar` that stores the message related to the status of IOBit Unlocker.
-   `stub_path`: A `StringVar` that stores the path to the stub file.
-   `tonemap_path`: A `StringVar` that stores the path to the tonemapping file.
-   `iobit_frame`: A frame that contains the IOBit location input and browse button.
-   `iobit_location_input`: An entry box for displaying the IOBit location.
-   `browse_seperator_label`: A label widget used as a visual separator.
-   `iobit_location_button`: A button for browsing and selecting the IOBit location.
-   `iobit_status_label`: A label widget that displays the status of IOBit Unlocker.
-   `stub_location_input`: An entry box for displaying the stub location.
-   `stub_location_button`: A button for browsing and selecting the stub location.
-   `tonemap_location_input`: An entry box for displaying the tonemapping location.
-   `tonemap_location_button`: A button for browsing and selecting the tonemapping location.
-   `buttons_frame`: A frame that contains the Install and Restore buttons.

### Example Usage

```python
local_page = LocalPage(parent)
local_page.pack()
```

---

**Author:** SomnathChW  
**Last Modified:** August 05, 2023

[![Discord](https://img.shields.io/badge/Join%20me%20on-Discord-7289DA?style=flat-square&logo=discord)](https://discord.com/users/753294480609902712)  
[![GitHub](https://img.shields.io/badge/Check%20out%20my-GitHub-181717?style=flat-square&logo=github)](https://github.com/SomnathChW)
