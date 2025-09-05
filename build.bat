@echo off
echo ===================================
echo  Godot Game Build Script
echo ===================================

echo.
echo NOTE: This script requires the following prerequisites:
echo 1. The Godot executable must be in your system's PATH.
echo 2. You must have the correct Godot export templates installed for your Godot version.
echo    (You can manage export templates in the Godot editor under Editor > Manage Export Templates)
echo.

echo Creating build directories...
if not exist "builds" mkdir "builds"
if not exist "builds\android" mkdir "builds\android"
if not exist "builds\ios" mkdir "builds\ios"
echo ...done.

echo.
echo Exporting for Android...
godot --headless --export-release "Android" "builds/android/game.apk"
if %errorlevel% neq 0 (
    echo ERROR: Android export failed.
    goto :eof
)
echo ...done.

echo.
echo Exporting for iOS...
godot --headless --export-release "iOS" "builds/ios/game.zip"
if %errorlevel% neq 0 (
    echo ERROR: iOS export failed.
    goto :eof
)
echo ...done.

echo.
echo ===================================
echo  Build complete.
echo ===================================
echo.
echo You can find the builds in the 'builds' directory.
