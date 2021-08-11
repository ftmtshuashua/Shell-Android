@echo off 
keytool -list -v -keystore  %~1
pause