#importa  a biblioteca tkinter para pode trabalha com
#interface grafica

from tkinter import*

def exemplo_Rotulo(container):
    info=Label(container,text="Tkinter-interface de Python")
    info['fg']="yellow"
    info['bg']="blue"
    inf['height']=10
    info.pack()#o pack torna o componente visivel


def main():
    janela=Tk()
    exemplo_Rotulo(janela)
    janela.mainloop()
    
