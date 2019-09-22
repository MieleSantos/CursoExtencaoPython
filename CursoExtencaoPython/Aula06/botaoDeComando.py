from tkinter import*

def exemplo_botao(container):
    botaoA=Button(container)
    botaoA['text']="Clique em mim!"
    botaoA['width']=100
    botaoA['background'] ="yellow"
    botaoA['font']= ('arial',16,'bold')
    botaoA.pack()

def main():
    janela=Tk()
    exemplo_botao(janela)
    janela.mainloop()

main()
