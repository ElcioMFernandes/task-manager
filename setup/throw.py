import tkinter.messagebox

__errors = {
    "0001": "Erro na importação de biblioteca; ",
    "0002": "Erro na carregar variáveis de ambiente; ",
    "0003": "Erro ao atribuir variáveis do .env; ",
}

__warnings = {
}

__informations = {
}

def error(code: str, additional_message: str = None):
    if code in __errors:
        title = "Erro"
        message = f"{__errors[code]}{additional_message}"
    else:
        title = "Erro Desconhecido"
        message = f"Erro desconhecido; {additional_message}"
    tkinter.messagebox.showerror(title, message)

def warning(code: str, additional_message: str = None):
    if code in __warnings:
        title = "Aviso"
        message = f"{__warnings[code]}{additional_message}"
        tkinter.messagebox.showwarning(title, message)
    else:
        title = "Aviso Desconhecido"
        message = f"Aviso desconhecido; {additional_message}"
        tkinter.messagebox.showwarning(title, message)

def information(code: str, additional_message: str = None):
    if code in __informations:
        title = "Informação"
        message = f"{__informations[code]}{additional_message}"
        tkinter.messagebox.showinfo(title, message)
    else:
        title = "Informação Desconhecida"
        message = f"Informação desconhecida; {additional_message}"
        tkinter.messagebox.showinfo(title, message)