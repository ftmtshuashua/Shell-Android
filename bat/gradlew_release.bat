@echo off
cd %~1
call gradlew app:assemble_FlavorsRelease_Release

