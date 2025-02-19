$installerUrl = "https://aka.ms/vs/17/release/vs_community.exe"
$installerPath = "$env:TEMP\vs_community.exe"

Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath

$installArgs = @(
    "--installPath", "C:\Program Files\Microsoft Visual Studio\2022\Community",
    "--add", "Microsoft.VisualStudio.Workload.NativeDesktop",
    "--add", "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
    "--add", "Microsoft.VisualStudio.Component.Windows10SDK",
    "--quiet",
    "--norestart",
    "--wait"
)

Start-Process -FilePath $installerPath -ArgumentList $installArgs -Wait

Write-Host "Visual Studio 2022 has been installed."