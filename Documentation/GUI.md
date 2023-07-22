## Module: GUI

## File Name: `gui.py`

This module contains the main graphical user interface for the installer.

## Class: App

This class represents the main application. It inherits from `customtkinter.CTk` and provides a graphical user interface for the installer.

### Methods

-   `__init__()`: Initializes the application.
-   `radiobutton_event()`: Handles the event when a radiobutton is selected.
-   `show_iobit_page()`: Displays the IOBit page.
-   `show_native_page()`: Displays the Native page.
-   `configure_title_bar_color(color)`: Configures the color of the title bar.

### Attributes

-   `splash_image`: An image displayed on the left half of the installer.
-   `splash_label`: A label widget that shows the splash image.
-   `main_frame`: The main frame of the application.
-   `selection_frame`: A frame that contains the radio button selection options.
-   `mode_selected`: An `IntVar` that stores the selected mode.
-   `radiobutton_1`: The first radio button for selecting the IOBit mode.
-   `radiobutton_2`: The second radio button for selecting the Native mode.
<!-- -   `divider_label`: A label widget used as a visual divider.  Not used anymore.  -->
-   `content_frame`: A frame that contains the content (IOBit and Native pages).
-   `iobit_page`: The IOBit page.
-   `native_page`: The Native page.
-   `links_frame`: A frame that contains the links and copyright information.
-   `discord_image`: An image for the Discord logo.
-   `github_image`: An image for the GitHub logo.
-   `padding_label`: A label widget used for spacing.
-   `github_label`: A label widget that displays the GitHub logo.
-   `seperator_label`: A label widget used as a visual separator.
-   `discord_label`: A label widget that displays the Discord logo.
-   `copyright_label`: A label widget that displays the copyright information.
-   `version_label`: A label widget that displays the version information.

### Example Usage

```python
app = App()
app.mainloop()
```

---

**Author:** SomnathChW  
**Last Modified:** July 22, 2023

[![Discord](https://img.shields.io/badge/Join%20me%20on-Discord-7289DA?style=flat-square&logo=discord)](https://discord.com/users/753294480609902712)  
[![GitHub](https://img.shields.io/badge/Check%20out%20my-GitHub-181717?style=flat-square&logo=github)](https://github.com/SomnathChW)
