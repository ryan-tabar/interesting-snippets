@REM simple build batch file for C code

set COMPILER=gcc
set OBJ_DIR=obj
set SRC_DIR=src
set INC_DIR=inc

if not exist %OBJ_DIR%\ mkdir %OBJ_DIR%\
if not exist %INC_DIR%\ mkdir %INC_DIR%\
if not exist %SRC_DIR%\ mkdir %SRC_DIR%\

for %%f in (%SRC_DIR%\*.c) do %COMPILER% -Wall -c %%f -o %OBJ_DIR%\%%~nf.o
%COMPILER% %OBJ_DIR%\*.o -o main