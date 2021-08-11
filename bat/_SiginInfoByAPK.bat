@echo off 
keytool -list -printcert -jarfile %~1
pause