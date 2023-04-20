from tkinter import *
fenetre0= Tk()
fenetre0.title("Que pasa ?")
fenetre0.geometry("500x300")
fenetre0.configure(bg='darkgreen')
intro=Label(fenetre0, font=("Comic Sans MS", 14), text="C'est donc ici que vous vous retrouvez ... \n Vous êtes donc tombé bien bas !", bg='darkgreen')
intro.pack()
# Coordonnées initiales du joueur
x = 150
y = 150


def jouer():
    
    fenetre1=Tk()
    fenetre1.configure(bg='darkgreen')
    fenetre1.title('Début du jeu ici :)')
    fenetre1.geometry('800x600')
    how=Label(fenetre1, text="Tu dois retrouver chemin rapidement,\n sinon les Enfers te garderont !", font=("Comic Sans MS", 20), bg='darkgreen')
    how.pack()
    fenetre0.focus_set()
    canvas = Canvas(fenetre1, width=300, height=300, bg='red', selectborderwidth=5,highlightbackground='black')
    canvas.pack()
    
    # Définir les coordonnées initiales du joueur
    x = 150
    y = 150

    # Dessin du joueur
    player = canvas.create_oval(x-10, y-10, x+10, y+10, fill='blue', outline='black')

    # Fonction de déplacement du joueur
    def move_player(dx, dy):
        nonlocal x, y
        new_x = x + dx
        new_y = y + dy
        # Vérifier si les nouvelles coordonnées sont en dehors du canevas
        if new_x < 10 or new_x > 290 or new_y < 10 or new_y > 290:
            return  # Ne pas déplacer le joueur
        x = new_x
        y = new_y
        canvas.coords(player, x-10, y-10, x+10, y+10)
        murs = [canvas.create_rectangle(120,110,125,300, fill='black'),
                canvas.create_rectangle(160,200,165,260, fill='black'),
                canvas.create_rectangle(160,200,200,195, fill='black'),
                canvas.create_rectangle(160,260,260,265, fill='black'),
                canvas.create_rectangle(260,265,265,40, fill='black'),
                canvas.create_rectangle(265,40,150,45, fill='black'),
                canvas.create_rectangle(110,45,40,40, fill='black'),
                canvas.create_rectangle(40,45,45,260, fill='black'),
                canvas.create_rectangle(45,260,0,265, fill='black'),
                canvas.create_rectangle(85,110,80,300,fill='black'),
                canvas.create_rectangle(120,110,125,80,fill='black'),
                canvas.create_rectangle(125,85,150,80,fill='black'),
                canvas.create_rectangle(150,85,155,45,fill='black')]
             # Vérifier si les nouvelles coordonnées sont en dehors du canevas
        if new_x < 10 or new_x > 290 or new_y < 10 or new_y > 290:
            return  # Ne pas déplacer le joueur
        # Vérifier si les nouvelles coordonnées sont à l'intérieur d'un mur
        for mur in [murs]:
            if canvas.coords(mur)[0] <= new_x <= canvas.coords(mur)[2] and canvas.coords(mur)[1] <= new_y <= canvas.coords(mur)[3]:
                return  # Ne pas déplacer le joueur
      
    # Fonctions de gestion des touches du clavier
    def left(event):
        move_player(-10, 0)

    def right(event):
        move_player(10, 0)

    def up(event):
        move_player(0, -10)

    def down(event):
        move_player(0, 10)
    
    # Lier les touches du clavier aux fonctions de déplacement
    fenetre1.bind('<Left>', left)
    fenetre1.bind('<Right>', right)
    fenetre1.bind('<Up>', up)
    fenetre1.bind('<Down>', down)
    fenetre1.mainloop()

jouer=Button(fenetre0,font=("Comic Sans MS", 14), text='Allez, viens par ici !', bg='darkgreen', fg="yellow", command=jouer)
jouer.pack()
fenetre0.mainloop()
