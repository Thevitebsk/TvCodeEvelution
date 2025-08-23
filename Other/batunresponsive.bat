rem gF6D.bat
rem an attempt on a language made in batch

@echo off
rem ---------------------------MAIN---------------------------
title bat unresponsive
echo BU responsive
echo Created by Thevitebsk/Gaham
pause
set /p n= Please enter your name:
cls
rem ---------------------COMMAND CHECKING---------------------
set /p i= %CD%\
:cl
set /p i= %CD%\
if %i% equ save goto save
if %i% equ save set list=!list!save
if %i% equ say goto print
if %i% equ say set list=!list!say
goto cl
:save
set f=%list% Made by %n%
echo %f% > BUprogram.txt
echo please remove the "save" text at the bottom before the "Made by text" of your "BUprogram.txt" file
goto end
:print
echo %i%
goto cl
:end
echo BU unresponsive
pause
