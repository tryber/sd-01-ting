from ting_file_management.file_process import FileProcess
from time import sleep


def f_main():
    path = "statics/arquivo_teste.txt"
    print("iniciando a execuçao")
    file_process = FileProcess()
    sleep(1)
    file_process.process(path)
    sleep(1)
    file_process.remove()
    sleep(1)
    file_process.process(path)
    sleep(1)
    file_process.file_metadata(0)
    sleep(1)
    print("terminando a execuçao")
    return None


f_main() 
