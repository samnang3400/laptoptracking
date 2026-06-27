@echo off
echo Stopping and removing Laptop Monitor service...
nssm stop LaptopMonitor
nssm remove LaptopMonitor confirm
pause
