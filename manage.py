# Importação de bibliotecas nativas
import shelve
import sys
import tkinter.messagebox

# Importação de bibliotecas externas
try:
    import schedule
except Exception as e:
    tkinter.messagebox.showerror('Error',f'{e}. Error code: 0001')

class Manager:
    def __init__(manager) -> None:
        if len(sys.argv) != 3:
            print("Operação inválida!")
            sys.exit(1)
        
        if sys.argv[1] == '-c' and sys.argv[2] == 'task':
            manager.__create_task()

        if sys.argv[1] == '-u' and sys.argv[2] == 'task':
            manager.__update_task()

        if sys.argv[1] == '-d' and sys.argv[2] == 'task':
            manager.__delete_task()

        if sys.argv[1] == '-c' and sys.argv[2] == 'schedule':
            manager.__create_schedule()

        if sys.argv[1] == '-u' and sys.argv[2] == 'schedule':
            manager.__update_schedule()

        if sys.argv[1] == '-d' and sys.argv[2] == 'schedule':
            manager.__delete_schedule()

    def __create_task(manager):
        name = input("Nome para a tarefa: ")
        print(name)

    def __update_task(manager):
        pass

    def __delete_task(manager):
        pass

    def __create_schedule(manager):
        pass

    def __update_schedule(manager):
        pass

    def __delete_schedule(manager):
        pass 

if __name__ == '__main__':
    app = Manager()