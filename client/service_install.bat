@echo off
echo Installing Laptop Monitor as a Windows Service...
nssm install LaptopMonitor "C:\Python39\python.exe" "%~dp0src\main.py"
nssm set LaptopMonitor DisplayName "Laptop Monitor Agent"
nssm set LaptopMonitor Description "Monitors system info and executes remote commands."
nssm set LaptopMonitor Start SERVICE_AUTO_START
nssm set LaptopMonitor AppStdout "%~dp0logs\stdout.log"
nssm set LaptopMonitor AppStderr "%~dp0logs\stderr.log"
nssm start LaptopMonitor
echo Done! Check services.msc for "Laptop Monitor Agent".
pause
