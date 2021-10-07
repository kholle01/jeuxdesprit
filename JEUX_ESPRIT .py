
## Ceci est la creation de l'application jeux d'esprit 

#from tkinter import Canvas,Button,Label,PhotoImage,E,W,Entry,Tk
import tkinter as tk
from random import randint
import pygame
#cette application qui est une application pour le jeux d'esprit
pygame.init()

class JEUX:
	def __init__(self):
		self.root = first
		self.game_logo()
		#fself.image_background()
		self.instructions()
		self.list_equipe = ['tc1','tc2','dic1','dic2','dic3','TC1','TC2','DIC1','DIC2','DIC3']
		#self.root2 = self.petit_fenetre



	def first_menu(self):
		self.root = first
		self.instructions()
		self.game_logo()
		self.petit_fenetre.destroy()
		
	def game_logo(self):
		logo = tk.PhotoImage(file = 'logo.png')
		label_logo = tk.Label(image = logo)
		label_logo.image = logo
		label_logo.grid(row = 0 , padx = 275 , pady = 50 , sticky = tk.W)
    

	def instructions(self):
		nom_joueurs = tk.Label(self.root , text = 'Saisissez le nom des Equipes ainsi que des Joueurs', font = ('Cambria',20),bg = 'green',fg ='white')
		nom_joueurs.grid(row = 1 , column = 0 , pady = 4 , sticky = tk.W , padx = 100 )
		equipeA = tk.Label(self.root , text = 'Equipe A:' , font = ('cambria' ,30 , 'bold'))
		equipeA.grid(row = 2, column = 0 , sticky = tk.W , pady = 40 , padx = 0)
		self.champA = tk.Entry(self.root , width = 8 , font = ('Calibri',15,'bold'))
		self.champA.grid(row = 2 ,padx = 190 , sticky = tk.W )
		joueurA = tk.Label(self.root , text = 'Joueurs:' , font = ('calibri' ,30 , 'bold'))
		joueurA.grid(row = 2, sticky = tk.W , pady = 40 , padx = 300)
		self.champ_joueurs_A = tk.Entry(self.root , width = 30 , font = ('Calibri',15,'bold'))
		self.champ_joueurs_A.grid(row = 2 ,padx = 450 , sticky = tk.W  )
		equipeB = tk.Label(self.root , text = 'Equipe B:' , font = ('cambria' ,30 , 'bold'))
		equipeB.grid(row = 3, column = 0 , sticky = tk.W , pady = 40 , padx = 0)
		self.champB = tk.Entry(self.root , width = 8 , font = (('Calibri',15,'bold')))
		self.champB.grid(row = 3 ,padx = 190 , sticky = tk.W )
		joueurB = tk.Label(self.root , text = 'Joueurs:' , font = ('calibri' ,30 , 'bold'))
		joueurB.grid(row = 3, sticky = tk.W , pady = 40 , padx = 300)
		self.champ_joueurs_B = tk.Entry(self.root , width = 30 , font = ('Calibri',15,'bold'))
		self.champ_joueurs_B.grid(row = 3 ,padx = 450 , sticky = tk.W)
		valider = tk.Button(self.root , text = 'Valider les Entrees' ,command = self.fenetre_before, font = ('calibri','18','italic'),bg = 'green' , fg = 'white')
		valider.grid( sticky = tk.W , padx = 200)
		self.message_alerte = tk.Label(self.root , text = '' , font = ('Cambria', 12 , 'bold'))
		self.message_alerte.grid(row = 4)

	def verifier_champs(self):
		ca = self.champA.get()
		cja = self.champ_joueurs_A.get()
		cb = self.champB.get()
		cjb = self.champ_joueurs_B.get()
		#print(ca , cb)
		verifier = len(ca) != 0 and  len(cb) != 0  and ca in self.list_equipe and cb in self.list_equipe
		return verifier

	def fenetre_before(self):
		#avant que cette fenetre ne se charge on doit verifier si les donne ont ete bien entre
		# donc verifions par la methode
		if self.verifier_champs():
			# on recuperer ce qui est entre dans les champs
			self.equipeA_name = self.champA.get()
			self.equipeB_name = self.champB.get()
			self.joueurA_names = self.champ_joueurs_A.get()
			self.joueurB_names = self.champ_joueurs_B.get()
			self.root.destroy()
			self.items_before_fen()
			
		else:
			self.message_alerte['text'] = 'Entrez toutes les donnees valide du match'

	def items_before_fen(self):
		#print(self.equipeA_name + '.png')
		self.petit_fenetre = tk.Tk()
		self.petit_fenetre.title(self.equipeA_name.upper() +  ' vs '  + self.equipeB_name.upper())
		self.petit_fenetre.geometry('1300x600')
		self.petit_fenetre.resizable(width = False , height = False)
		#ajoutons un bg image
		bg = tk.PhotoImage(file = 'bg' + str(randint(1,9)) +'.png')
		bg_label = tk.Label(image = bg )
		bg_label.place(x= 0 , y = 0 ,relwidth = 1 , relheight = 1)
		# ici on ajoute un gif
		"""
		can = Canvas(self.petit_fenetre, width=240, height=320)
		can.place(x = 520  , y = 0)
		photo = PhotoImage(file="eclair" + str(randint(1,6)) + ".gif")
		can.create_image(0,0,anchor='nw', image=photo, tag='photo')
 
		self.ind = -1
		def update(delay=200):
			#global ind
			self.ind += 1
			if self.ind == 8: self.ind = 0
			#print (ind)
			photo.configure(format="gif -index " + str(self.ind))
			self.petit_fenetre.after(delay, update)
		update()
		"""


		logo_equipe_A = tk.PhotoImage( file = self.equipeA_name.lower() + '.png')
		logo_A = tk.Label(image = logo_equipe_A)
		logo_A.image = logo_equipe_A
		logo_A.place(x = 100 , y = 100)
		#logo_vs = PhotoImage( file = 'versus.png')
		#logo_vs_i = Label(image = logo_vs)
		#logo_vs_i.image = logo_vs
		#logo_vs_i.place(x = 520 , y = 150)
		logo_equipe_B = tk.PhotoImage( file = self.equipeB_name.lower() + '.png')
		logo_B = tk.Label(image = logo_equipe_B)
		logo_B.image = logo_equipe_B
		logo_B.place(x = 875 , y = 95)
		bouton = tk.Button(text = 'Entrez dans le Match' , font = ('calibri','18','italic'),bg = '#cc3638' , fg = 'white' , command = self.fenetre_principal )
		bouton.place(x = 520 ,y = 500)
		self.sound()
		#la on demarre le son
		self.petit_fenetre.mainloop()
		#time.sleep(3)
		son.stop()

	
	def sound(self):
		global son 
		son = pygame.mixer.Sound("son" + str(randint(2,5)) + ".mp3")
		son.set_volume(0.7)
		son.play(5)
		#son.stop()


	def fenetre_principal(self):
		self.petit_fenetre.destroy()
		self.fenetre_principal = tk.Tk()
		self.screen_width = self.fenetre_principal.winfo_screenwidth()
		self.screen_height = self.fenetre_principal.winfo_screenheight()
		self.fenetre_principal.geometry(str(self.screen_width) + "x" + str(self.screen_height))
		#ajout des widgets
		#print(self.equipeA_name + '.png')
		self.fenetre_principal.resizable(width = False , height = False)
		self.fenetre_principal.title(self.equipeA_name.upper() +  ' vs '  + self.equipeB_name.upper())
		#ajoutons un bg image
		#bg = tk.PhotoImage(file = 'bg' + str(randint(1,9)) +'.png')
		#bg_label = tk.Label(image = bg )
		#bg_label.place(x= 0 , y = 0 ,relwidth = 1 , relheight = 1)
		logo_equipe_A = tk.PhotoImage( file = self.equipeA_name + '.png')
		logo_A = tk.Label(image = logo_equipe_A)
		logo_A.image = logo_equipe_A
		logo_A.grid(sticky = tk.W , padx = self.screen_width/10  , pady = self.screen_height/9 , row = 0 )

		logo = tk.PhotoImage(file = 'logo.png')
		logo_p = tk.Label(image = logo)
		logo_p.place(x = 4*self.screen_width/10)
		logo_equipe_B = tk.PhotoImage( file = self.equipeB_name + '.png')
		logo_B = tk.Label(image = logo_equipe_B)
		logo_B.image = logo_equipe_B
		logo_B.grid(sticky = tk.W , padx = 7*self.screen_width/10 , row = 0 )

		# ajoutons le label score text
		score_title = tk.Label(self.fenetre_principal , text = 'Score' , font = ('algerian' , 50 , 'bold' , 'underline'))
		score_title.place(x = 4*self.screen_width/10 + 20  , y = 4*self.screen_height/9 - 50)

		# score pour equipeA
		self.scoreA = tk.Label(self.fenetre_principal , text = 0 , font = ('Book antiqua' , 120 , 'bold' , 'underline'), bg = 'green', fg = 'white')
		self.scoreA.place(x = 3*self.screen_width/10 - 60 , y = 5*self.screen_height/9 + 50)
		# score pour equipeB text
		self.scoreB = tk.Label(self.fenetre_principal , text = 0 , font = ('Book antiqua' , 120 , 'bold' , 'underline') , bg = 'green', fg = 'white')
		self.scoreB.place(x = 6*self.screen_width/10 , y = 5*self.screen_height/9 + 50)

		# entrey non apparent
		
		# label frame pour equipe 1
		grandlabel = tk.LabelFrame(self.fenetre_principal,text = "JOUEURS", font = ('cambria' , 40 , 'bold'))
		grandlabel.grid(row = 2 , sticky = tk.W , padx = 8  , pady = 0 )
		tk.Label(grandlabel,text = 'MOUHAMED DIENG' , font = ('verdana',22,'italic' )).grid(row = 2)
		tk.Label(grandlabel,text = 'Joueurs 2' , font = ('verdana',22 ,'italic')).grid(row = 3)
		tk.Label(grandlabel,text = 'Joueurs 3' , font = ('verdana',22 ,'italic')).grid(row = 4)
		tk.Label(grandlabel,text = 'Joueurs 4' , font = ('verdana',22 ,'italic')).grid(row = 5)
		tk.Label(grandlabel,text = 'Joueurs 5' , font = ('verdana',22 ,'italic')).grid(row = 6)

		# label frame pour equipe 2
		grandlabel_2 = tk.LabelFrame(self.fenetre_principal,text = "JOUEURS", font = ('cambria' , 40 , 'bold'))
		grandlabel_2.grid(row = 2 , sticky = tk.W , padx = 8*self.screen_width/10 , pady = 0 )
		tk.Label(grandlabel_2,text = 'Joueurs 1' , font = ('verdana',22,'italic' )).grid(row = 2)
		tk.Label(grandlabel_2,text = 'Joueurs 2' , font = ('verdana',22 ,'italic')).grid(row = 3)
		tk.Label(grandlabel_2,text = 'Joueurs 3' , font = ('verdana',22 ,'italic')).grid(row = 4)
		tk.Label(grandlabel_2,text = 'Joueurs 4' , font = ('verdana',22 ,'italic')).grid(row = 5)
		tk.Label(grandlabel_2,text = 'Joueurs 5' , font = ('verdana',22 ,'italic')).grid(row = 6)
		
		# bouton pour incrementer le score
		ajouter_10_equipe_A = tk.Button(text= 'ajouter 10 a A' , command = self.ajouter_10_equipe_A)
		ajouter_10_equipe_A.place( x =self.screen_width/10 )

		ajouter_10_equipe_B = tk.Button(text= 'ajouter 10 a B' , command = self.ajouter_10_equipe_B)
		ajouter_10_equipe_B.place( x = 7*self.screen_width/10 )

		#attibuer_med = tk.Button(text= 'attibuer medaile' , command = self.equipe_devant)
		#attibuer_med.place( x = 7*self.screen_width/10  + 20)

		
		self.equipe_devant()
		self.fenetre_principal.mainloop()
	

	def ajouter_10_equipe_A(self):
		ancien_score = self.scoreA['text']
		nouveau_score = ancien_score + 10
		self.scoreA['text'] = nouveau_score
		self.equipe_devant()

	def ajouter_10_equipe_B(self):
		ancien_score = self.scoreB['text']
		nouveau_score = ancien_score + 10
		self.scoreB['text'] = nouveau_score
		self.equipe_devant()

	#chargon la medaille
	
	

	
	def equipe_devant(self):
		#on charge la medaille
		self.canvas = tk.Canvas(width = 200, height = 200)

		self.medaille = tk.PhotoImage(file = 'med.png' )
		#self.pos_medaille = tk.Label(image = self.medaille)
		# on donne la medaille a l'equipe qui mene au score
		if self.scoreA['text'] > self.scoreB['text']:
			#on attribue le medaille a A
			self.canvas.place(x = 3*self.screen_width/10 - 20  , y = 2*self.screen_height/9 )
			self.canvas.create_image(0,0,anchor='nw', image = self.medaille ,  tag='photo')
		elif self.scoreA['text'] < self.scoreB['text']:
			#on attribue la medaille a B
			#self.pos_medaille.place(x = 8*self.screen_width/10 , y = 2*self.screen_height/9)
			self.canvas.place(x = 9*self.screen_width/10 - 20  , y = 2*self.screen_height/9 )
			self.canvas.create_image(0,0,anchor='nw', image = self.medaille ,  tag='photo')

		




# j'utilise ceci pour creer des trait de liaison
"""
zone_dessin = tk.Canvas(fenetre_principal,width=50,height=50)
zone_dessin.grid(row = 1)
zone_dessin.create_line(26,28,40,30, fill="black",width=2)
"""
# ajoutons le label score


if __name__ == '__main__':
	first = tk.Tk()
	first.title("Jeux d'Esprit")
	first.geometry("800x600")
	first.resizable(width=False,height=False)
	application = JEUX()
	first.mainloop()
    #first.configure(background)
    #root.minsize(width=500,height=100)
