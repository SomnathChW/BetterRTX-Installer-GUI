$installationLocation = Get-AppxPackage -Name "Microsoft.MinecraftUWP*" | Select-Object -ExpandProperty InstallLocation

if ($installationLocation -eq $null) {
    Write-Host "Minecraft not found. Please make sure Minecraft is installed and the paths are correct." -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: NTMNF001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

# # Wait 2 seconds for the user to read the message
Start-Sleep -Seconds 2  # Dont know why this is here, but it is crucial to the script working

$materialsLocation = Join-Path $installationLocation "data\renderer\materials"

$dststubPath = Join-Path $materialsLocation "RTXStub.material.bin"
$dsttoneMappingPath = Join-Path $materialsLocation "RTXPostFX.Tonemapping.material.bin"


$sourceStubPath = Join-Path $PSScriptRoot "RTXStub.material.bin"
$sourceToneMappingPath = Join-Path $PSScriptRoot "RTXPostFX.Tonemapping.material.bin"

# check if the source files exist
if (-not (Test-Path $sourceStubPath) -or -not (Test-Path $sourceToneMappingPath)) {
    Write-Host "Source files not found. Please make sure the source files are properly downloaded in the script's directory." -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: NTSFNF001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

# check if the destination files exist
if (-not (Test-Path $dststubPath) -or -not (Test-Path $dsttoneMappingPath)) {
    Write-Host "Destination files not found. Please make sure Minecraft is installed and the paths are correct." -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: NTMFNF001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

# check if they both are in the same partition by comparing the drive letter
if ($sourceStubPath[0] -ne $dststubPath[0]) {
    Write-Host "Source and destination are not in the same partition." -ForegroundColor Red
    Write-Host "Please move the source files to the same partition as the destination files." -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: NTSDNSP001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

try {
    # Get the ACL (Access Control List) from the source files
    $acl = Get-Acl -Path $dststubPath
    $acl2 = Get-Acl -Path $dsttoneMappingPath

    # Check if the ACL is empty
    if ($acl -eq $null -or $acl2 -eq $null) {
        Write-Host "Could Nor get the ACLs. Try Again with Administrative Rights" -ForegroundColor Red
        Write-Host ""
        Write-Host "----------------------------"
        Write-Host "ERRORCODE: NTACL001"
        Write-Host "----------------------------"
        Write-Host ""
        Write-Host "Exiting in 5 seconds..."
        Start-Sleep -Seconds 5
        exit 1
    }

    # Copy each access rule from the source ACLs to the destination ACLs
    $destinationAcl = New-Object System.Security.AccessControl.FileSecurity
    $acl.GetAccessRules($true, $true, [System.Security.Principal.SecurityIdentifier]) | ForEach-Object {
        $destinationAcl.AddAccessRule($_)
    }
    $acl2.GetAccessRules($true, $true, [System.Security.Principal.SecurityIdentifier]) | ForEach-Object {
        $destinationAcl.AddAccessRule($_)
    }

    # Set the ACL on the destination files
    Set-Acl -Path $sourceStubPath -AclObject $destinationAcl
    Set-Acl -Path $sourceToneMappingPath -AclObject $destinationAcl

Add-Type -TypeDefinition @"
    using System;
    using System.Diagnostics;
    using System.Runtime.InteropServices;
    public static class MyKernel32
    {
        [DllImport("kernel32.dll", CharSet=CharSet.Unicode)]
        public static extern bool MoveFileEx(
            String lpExistingFileName,
            String lpNewFileName,
            uint dwFlags);
    }
"@

    Write-Host "Creating Move Schedule for Stub"
    $stubScheduleCreated = [MyKernel32]::MoveFileEx($sourceStubPath, $dststubPath, 5)
    # Wait 2 seconds for the user to read the message
    Start-Sleep -Seconds 2

    Write-Host "Creating Move Schedule for Tone Mapping"
    $tonemappingScheduleCreated = [MyKernel32]::MoveFileEx($sourceToneMappingPath, $dsttoneMappingPath, 5)
    # Wait 2 seconds for the user to read the message
    Start-Sleep -Seconds 2

    if ($stubScheduleCreated -and $tonemappingScheduleCreated) {
        Write-Host ""
        Write-Host "------------------------------------------------"
        Write-Host "Successfully Created Move Schedule" -ForegroundColor Green
        Write-Host "------------------------------------------------"
        Write-Host ""
        Write-Host "You now need to restart your computer for the changes to take effect."
        Write-Host ""
        Write-Host "Exiting in 5 seconds..."
        # Wait 5 seconds for the user to read the message
        Start-Sleep -Seconds 5
    } else {
        Write-Host ""
        Write-Host "------------------------------------------------"
        Write-Host "Failed to Create Move Schedule"
        Write-Host "------------------------------------------------"
        Write-Host ""
        Write-Host "--------------------------------------------"
        Write-Host "ERRORCODE: NTMSF001"
        Write-Host "--------------------------------------------"
        Write-Host ""
        Write-Host "You need to Try Again"
        Write-Host "Exiting in 5 seconds..."
        # Wait 5 seconds for the user to read the message
        Start-Sleep -Seconds 5
    }
} catch {
    Write-Host "An error occurred: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: NTMSF002"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    # Wait 5 seconds for the user to read the message
    Start-Sleep -Seconds 5
}
