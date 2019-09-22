from tkinter import*

def exemplo_Rotulo(container):
    info=Label(container,text="Tkinter-interface de Python")
    info['fg']="yellow"
    info['bg']="blue"
    info['height']=10
    info.pack()

def exemplo_botaoA(container):
    def clica_botaoA(event):
        cor = botaoA['background']
        if cor =="red":botaoA['background']="yellow"
        elif cor == "yellow":botaoA['background']="blue"
        else: botaoA['background']="red"

    botaoA=Button(container)
    botaoA['text']="Clique em mim!"
    botaoA['width']=50
    botaoA['background'] ="yellow"
    botaoA['font']= ('arial',16,'bold')
    botaoA.pack()
    botaoA.bind("<Button-1>",clica_botaoA)
    
def main():
    janela=Tk()
    exemplo_Rotulo(janela)
    exemplo_botaoA(janela)
    janela.mainloop()
    
main()

