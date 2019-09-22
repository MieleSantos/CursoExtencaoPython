from tkinter import*

def exemplo_Rotulo(container):
    def clica_botaoA(event):
        botaoA['background'] ="green"
        info['fg']="white"
        info['bg']="green"
        info['width']=100
        info['height']=20     
        info['text']= "Mudando rotulo e o texto"
        
           
    info=Label(container,text="Tkinter-interface de Python")
    info['fg']="yellow"
    info['bg']="blue"
    info['height']=10
    info.pack()
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
    janela.mainloop()
    
main()
