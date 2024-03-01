import time
import os
from pathlib import Path


while True:
    print("hello!")
    # get the current working directory
    current_working_directory = Path.cwd()
    # print output to the console
    print(current_working_directory)
    #salvar('teste.txt')
    time.sleep(5)