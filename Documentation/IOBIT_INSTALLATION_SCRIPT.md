## BetterRTX Installation with IOBit Unlocker (Powershell Script)
### File Name : `iobit_installation.ps1`

This PowerShell script installs the RTXStub and RTXPostFX.Tonemapping.material.bin files for Minecraft using IOBit Unlocker. The script performs the following steps:

### Parameters

The script accepts the following parameters:

- `$iobitPath` (string, required): The path to the IOBit Unlocker executable.
- `$stubPath` (string, required): The path to the RTXStub material file.
- `$toneMappingPath` (string, required): The path to the RTXPostFX.Tonemapping.material.bin file.

### Error Codes

Here are the error codes and their meanings:

- `IBMNF001`: Minecraft not found. Please make sure Minecraft is installed and the paths are correct.
- `IBSFNF001`: Source files not found. Please make sure the source files are properly downloaded in the script's directory.
- `IBSTD001`: Failed to delete the original RTXStub.
- `IBTMD001`: Failed to delete the original RTXPostFX.Tonemapping.material.bin.
- `IBSTM001`: Failed to move the RTXStub.
- `IBTMM001`: Failed to move the RTXPostFX.Tonemapping.material.bin.
- `IBF001`: Installation failed.

### Execution Flow

1. Check Minecraft Installation:
   - **Description:** The script checks if Minecraft is installed by obtaining the installation location using the `Get-AppxPackage` cmdlet.
   - **Error Code:** `IBMNF001`

2. Set Materials Location:
   - **Description:** The script sets the materials location by joining the installation location with the "data\renderer\materials" path.
   - **Error Code:** None

3. Check Source Files Existence:
   - **Description:** The script checks if the source files (RTXStub and RTXPostFX.Tonemapping.material.bin) exist in the specified source paths.
   - **Error Code:** `IBSFNF001`

4. Remove Old Files (Optional):
   - **Description:** If the old RTXStub or RTXPostFX.Tonemapping.material.bin files exist in the materials location, the script uses IOBit Unlocker to remove them.
   - **Error Codes:** `IBSTD001`, `IBTMD001`

5. Move New Files:
   - **Description:** The script uses IOBit Unlocker to move the new RTXStub and RTXPostFX.Tonemapping.material.bin files to the materials location.
   - **Error Codes:** `IBSTM001`, `IBTMM001`

6. Completion Status:
   - **Description:** Based on the success of the installation process, the script displays either a success message indicating a successful installation or an error message indicating a failed installation.
   - **Error Code:** `IBF001`

> **Note:** This script assumes the availability and proper functioning of IOBit Unlocker. Make sure to have IOBit Unlocker installed and configured correctly before executing the script.

### Usage

To use the script, provide the required parameter values when calling the script from the command line or integrate it into your existing workflow as needed.

```powershell
.\iobit_installation.ps1 -iobitPath "C:\Program Files\IOBit Unlocker\IOBitUnlocker.exe" -stubPath "C:\path\to\new\RTXStub.material.bin" -toneMappingPath "C:\path\to\new\RTXPostFX.Tonemapping.material.bin"
```


---
**Author:** SomnathChW  
**Last Modified:** August 05, 2023

[![Discord](https://img.shields.io/badge/Join%20me%20on-Discord-7289DA?style=flat-square&logo=discord)](https://discord.com/users/753294480609902712)    
[![GitHub](https://img.shields.io/badge/Check%20out%20my-GitHub-181717?style=flat-square&logo=github)](https://github.com/SomnathChW)
