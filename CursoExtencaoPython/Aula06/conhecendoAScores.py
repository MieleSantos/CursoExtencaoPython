from tkinter import*

def contaCores(container):
    
    def clicaBotao(event):
        global conta_cor
        conta_cor=conta_cor-1
        info['background']=lista_cores[conta_cor]
        botaoA['text']=lista_cores[conta_cor]
        botaoA['background']=lista_cores[conta_cor]
        if conta_cor==0:
            conta_cor=len(lista_cores)

    global conta_cor

    lista_cores=['white','blue','black','green','red','yellow','brown','pink','purple',
                 'darkgreen','moccasin','deepskyblue','dodgerblue','ghostwhite','navajowhite','limegreen']
    conta_cor=len(lista_cores)
    botaoA=Button(container)
    botaoA['text']="Troca cor!"
    botaoA['fg']="yellow"
    botaoA['width']=50
    botaoA['background'] ="black"
    botaoA['font']= ('arial',16,'bold')
    botaoA.pack()
    botaoA.bind("<Button-1>",clicaBotao)
    
    info=Label(container,text="Tkinter-interface de Python")
    info['font']=('arial',16,'bold')
    info.pack()


def main():
    janela=Tk()
    contaCores(janela)
    janela.mainloop()

main()
    
    
    
