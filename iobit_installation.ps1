param (
    [Parameter(Mandatory=$true)]
    [string]$iobitPath,
    [Parameter(Mandatory=$true)]
    [string]$stubPath,
    [Parameter(Mandatory=$true)]
    [string]$toneMappingPath
)

$success = $true

$installationLocation = Get-AppxPackage -Name "Microsoft.MinecraftUWP*" | Select-Object -ExpandProperty InstallLocation;

if ($installationLocation -eq $null) {
    Write-Host "Minecraft not found. Please make sure Minecraft is installed and the paths are correct." -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: IBMNF001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

$materialsLocation = Join-Path $installationLocation "data\renderer\materials";

$oldstubPath = Join-Path $materialsLocation "RTXStub.material.bin";
$oldtoneMappingPath = Join-Path $materialsLocation "RTXPostFX.Tonemapping.material.bin";

if (-not (Test-Path $stubPath) -or -not (Test-Path $toneMappingPath)) {
    Write-Host "Source files not found. Please make sure the source files are properly downloaded in the script's directory." -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: IBSFNF001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

if ([System.IO.File]::Exists($oldstubPath)) {
    Write-Host "Removing Old Stub"
    Write-Host "Click OK on the IObit prompt"
    Write-Host ""

    $result = Start-Process -FilePath $iobitPath -ArgumentList "/Delete `"$oldstubPath`"" -Wait -NoNewWindow -PassThru
    if ($result.ExitCode -ne 0) {
        $success = $false
        Write-Host "Failed To Delete Original Stub" -ForegroundColor Red
        Write-Host ""
        Write-Host "----------------------------"
        Write-Host "ERRORCODE: IBSTD001"
        Write-Host "----------------------------"
        Write-Host ""
        Write-Host "Exiting in 5 seconds..."
        Start-Sleep -Seconds 5
        exit 1
    }
}

if ([System.IO.File]::Exists($oldtoneMappingPath)) {
    Write-Host ""
    Write-Host "Removing Old Tonemapping"
    Write-Host "Click OK on the IObit prompt"
    Write-Host ""

    $result = Start-Process -FilePath $iobitPath -ArgumentList "/Delete `"$oldtoneMappingPath`"" -Wait -NoNewWindow -PassThru
    if ($result.ExitCode -ne 0) {
        $success = $false
        Write-Host "Failed To Delete Original ToneMapping" -ForegroundColor Red
        Write-Host ""
        Write-Host "----------------------------"
        Write-Host "ERRORCODE: IBTMD001"
        Write-Host "----------------------------"
        Write-Host ""
        Write-Host "Exiting in 5 seconds..."
        Start-Sleep -Seconds 5
        exit 1
    }
}

Write-Host ""
Write-Host "Inserting Stub"
Write-Host "Click OK on the IObit prompt"
Write-Host ""

$result = Start-Process -FilePath $iobitPath -ArgumentList "/Move `"$stubPath`" `"$materialsLocation`"" -Wait -NoNewWindow -PassThru
if ($result.ExitCode -ne 0) {
    $success = $false
    Write-Host "Failed To Move Stub" -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: IBSTM001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

Write-Host ""
Write-Host "Inserting Tonemapping"
Write-Host "Click OK on the IObit prompt"
Write-Host ""

$result = Start-Process -FilePath $iobitPath -ArgumentList "/Move `"$toneMappingPath`" `"$materialsLocation`"" -Wait -NoNewWindow -PassThru
if ($result.ExitCode -ne 0) {
    $success = $false
    Write-Host "Failed To Move ToneMapping" -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: IBTMM001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}

# if sucess is true then we are done
if ($success) {
    Write-Host ""
    Write-Host "Installed Sucessfully" -ForegroundColor Green
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "You Can Now Launch Minecraft"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 0
} else {
    Write-Host "Installation failed" -ForegroundColor Red
    Write-Host ""
    Write-Host "----------------------------"
    Write-Host "ERRORCODE: IBF001"
    Write-Host "----------------------------"
    Write-Host ""
    Write-Host "Exiting in 5 seconds..."
    Start-Sleep -Seconds 5
    exit 1
}