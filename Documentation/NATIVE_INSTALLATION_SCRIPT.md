## BetterRTX Installation with MyKernel32 (Powershell Script)
### File Name : `native_installation.ps1`

This PowerShell script installs the RTXStub and RTXPostFX.Tonemapping.material.bin files for Minecraft using Native MyKernel32.

### Error Codes

Here are the error codes and their meanings:

- `NTMNF001`: Minecraft not found. Please make sure Minecraft is installed and the paths are correct.
- `NTSFNF001`: Source files not found. Please make sure the source files are properly downloaded in the script's directory.
- `NTSDNSP001`: Source and destination are not in the same partition.
- `NTACL001`: Failed to get the ACLs.
- `NTMSF001`: Failed to create the move schedule.
- `NTMSF002`: An error occurred during script execution.

### Execution Flow

1. **Check Minecraft Installation**
   - **Description:** Check if Minecraft is installed by obtaining the installation location using `Get-AppxPackage`.
   - **Error Code:** `NTMNF001`

2. **Check Source Files Existence**
   - **Description:** Check if the source files (`RTXStub.material.bin` and `RTXPostFX.Tonemapping.material.bin`) exist in the script's directory.
   - **Error Code:** `NTSFNF001`
   - **Note:** Make sure the source files are properly downloaded and placed in the same directory as the script.

3. **Check Destination Files Existence**
   - **Description:** Check if the destination files (`RTXStub.material.bin` and `RTXPostFX.Tonemapping.material.bin`) exist in the Minecraft installation location.
   - **Error Code:** `NTMFNF001`

4. **Check Source and Destination Partitions**
   - **Description:** Check if the source and destination files are located in the same partition (drive letter).
   - **Error Code:** `NTSDNSP001`

5. **Get ACLs (Access Control Lists) from Source Files**
   - **Description:** Retrieve the ACLs from the destination files.
   - **Error Code:** `NTACL001`

6. **Copy ACLs to Destination Files**
   - **Description:** Copy each access rule from the source ACLs to the destination ACLs.
   - **Error Code:** None

7. **Create Move Schedule**
   - **Description:** Create move schedules for the source files to be moved to the destination files using the `MoveFileEx` function.
   - **Error Code:** `NTMSF001`

8. **Completion Status**
   - **Description:** Based on the success of the installation process, the script displays either a success message indicating a successful installation or an error message indicating a failed installation.
   - **Error Code:** `NTMSF002`

**Note:** 
1. The source files (`RTXStub.material.bin` and `RTXPostFX.Tonemapping.material.bin`) need to be downloaded and placed in the same directory as the script for successful execution.
2. The Script requres that this installer, source files and destination files are in the **SAME PARTITION** (drive letter).

## Usage

To use the script, provide the required parameter values when calling the script from the command line or integrate it into your existing workflow as needed.

```powershell
.\native_installation.ps1
```

---
**Author:** SomnathChW  
**Last Modified:** July 22, 2023  

[![Discord](https://img.shields.io/badge/Join%20me%20on-Discord-7289DA?style=flat-square&logo=discord)](https://discord.com/users/753294480609902712)    
[![GitHub](https://img.shields.io/badge/Check%20out%20my-GitHub-181717?style=flat-square&logo=github)](https://github.com/SomnathChW)