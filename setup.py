"""
O setup.py serve para executar os programas em outros computadores.
-Na pasta do arquivo a ser executado, colocar o arquivo.py e setup.py, sifht+botão direito do mouse, entrar no cmd,
e escrever 'python setup.py build'.

"""
import sys
from cx_Freeze import setup, Executable
import pygame


base = None
if sys.platform == "win64":
    base = "Win64GUI"

executables = [
        Executable("snake.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame"],
        include_files = [],
        excludes = []
)




setup(
    name = "Snake",
    version = "1.0",
    description = "Jogo da cobrinha",
    options = dict(build_exe = buildOptions),
    executables = executables, requires=['pygame']
 )
