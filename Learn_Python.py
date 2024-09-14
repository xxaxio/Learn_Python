import tkinter as tk
from tkinter import ttk, messagebox
import random
import os


def get_audio_path(file_name):
    user_profile = os.getlogin()
    return f"C:/Users/{user_profile}/Desktop/Learn_Python/Bruitage/{file_name}"

class ApprentissagePythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apprentissage Python Amélioré")
        self.root.attributes("-fullscreen", True)  
        self.root.config(bg="#f0f4f8")  

        
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 11), padding=6, relief="flat", background="#005f73", foreground="#000")
        style.map("TButton", background=[("active", "#94d2bd")], foreground=[("active", "#000")])

     
        self.title_label = ttk.Label(root, text="Apprentissage Python", font=("Helvetica", 24, "bold"), background="#f0f4f8", foreground="#0a9396")
        self.title_label.pack(pady=20)

    
        self.quit_fullscreen_button = ttk.Button(root, text="Quitter le plein écran", command=self.quit_fullscreen)
        self.quit_fullscreen_button.pack(pady=10, padx=10, anchor="ne")

     
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10, padx=20)

      
        self.var_button = ttk.Button(self.button_frame, text="1. Les variables", command=self.afficher_variables)
        self.var_button.pack(pady=5, padx=10, fill="x")
        self.func_button = ttk.Button(self.button_frame, text="2. Les fonctions", command=self.afficher_fonctions)
        self.func_button.pack(pady=5, padx=10, fill="x")
        self.list_button = ttk.Button(self.button_frame, text="3. Les listes", command=self.afficher_listes)
        self.list_button.pack(pady=5, padx=10, fill="x")
        self.dict_button = ttk.Button(self.button_frame, text="4. Les dictionnaires", command=self.afficher_dictionnaires)
        self.dict_button.pack(pady=5, padx=10, fill="x")

     
        self.jeux_frame = ttk.Frame(root)
        self.jeux_frame.pack(pady=10, padx=20)
        self.quiz_button = ttk.Button(self.jeux_frame, text="Quiz Interactif", command=self.lancer_quiz)
        self.quiz_button.pack(pady=5, padx=10, fill="x")

   
        self.mention_speciale()

    def quit_fullscreen(self):
        self.root.attributes("-fullscreen", False)

    def creer_fenetre_lecon(self, titre, contenu):
        fenetre = tk.Toplevel(self.root)
        fenetre.title(titre)
        fenetre.geometry("900x700")
        fenetre.config(bg="#ffffff")

       
        bouton_retour = ttk.Button(fenetre, text="Retour au menu principal", command=fenetre.destroy)
        bouton_retour.pack(pady=10, padx=10, anchor="w")

      
        label_titre = tk.Label(fenetre, text=titre, font=("Helvetica", 20, "bold"), background="#ffffff", foreground="#0a9396")
        label_titre.pack(pady=10)

        texte_lecon = tk.Text(fenetre, wrap="word", font=("Helvetica", 12), bg="#f0f4f8", fg="#333333", padx=10, pady=10)
        texte_lecon.pack(fill="both", expand=True, padx=20, pady=10)

    
        texte_lecon.tag_configure("bold", font=("Helvetica", 12, "bold"))
        texte_lecon.tag_configure("italic", font=("Helvetica", 12, "italic"))
        texte_lecon.tag_configure("underline", font=("Helvetica", 12, "underline"))
        texte_lecon.tag_configure("heading", font=("Helvetica", 14, "bold"), foreground="#007f7f")
        texte_lecon.tag_configure("code", font=("Courier", 12), background="#eeeeee")

        
        texte_lecon.insert("end", "🔍 ", "bold")
        texte_lecon.insert("end", titre + "\n\n", "bold")
        texte_lecon.insert("end", "🌟 Introduction\n", "heading")
        texte_lecon.insert("end", contenu + "\n", "normal")
        texte_lecon.insert("end", "💡 Les éléments importants sont mis en valeur pour vous aider à mieux comprendre.\n", "italic")
        texte_lecon.config(state="disabled") 

    def afficher_variables(self):
        contenu = ("Les variables sont des espaces de stockage pour des données. Elles peuvent contenir divers types de valeurs, comme des nombres, des chaînes de caractères, etc.\n\n"
                   "🔎 Exemple:\n"
                   "```python\n"
                   "nombre = 10 # Une variable contenant un nombre\n"
                   "texte = 'Bonjour' # Une variable contenant une chaîne de caractères\n"
                   "```\n\n"
                   "Les variables sont essentielles pour effectuer des calculs, stocker des données et manipuler des informations.\n"
                   "En Python, vous pouvez utiliser des variables pour:\n"
                   "- Stocker des données temporaires\n"
                   "- Passer des informations entre les fonctions\n"
                   "- Gérer les états de votre programme\n")
        self.creer_fenetre_lecon("Les variables", contenu)

    def afficher_fonctions(self):
        contenu = ("Les fonctions sont des blocs de code réutilisables. Elles permettent de regrouper des instructions et de les exécuter plusieurs fois avec différents arguments.\n\n"
                   "🔎 Exemple:\n"
                   "```python\n"
                   "def dire_bonjour():\n"
                   "    print('Bonjour')\n\n"
                   "dire_bonjour() # Appel de la fonction\n"
                   "```\n\n"
                   "Les fonctions facilitent l'organisation du code et évitent la répétition.\n"
                   "Vous pouvez également:\n"
                   "- Passer des paramètres aux fonctions pour qu'elles soient plus flexibles\n"
                   "- Utiliser des valeurs de retour pour obtenir des résultats\n")
        self.creer_fenetre_lecon("Les fonctions", contenu)

    def afficher_listes(self):
        contenu = ("Les listes sont des collections ordonnées de valeurs. Elles permettent de stocker plusieurs éléments dans une seule variable.\n\n"
                   "🔎 Exemple:\n"
                   "```python\n"
                   "ma_liste = [1, 2, 3, 4] # Une liste contenant des nombres\n"
                   "ma_liste.append(5) # Ajoute 5 à la liste\n"
                   "```\n\n"
                   "Les listes sont très utiles pour gérer des ensembles de données.\n"
                   "Les opérations courantes sur les listes incluent:\n"
                   "- Ajouter ou retirer des éléments\n"
                   "- Accéder aux éléments par leur index\n"
                   "- Itérer sur les éléments de la liste\n")
        self.creer_fenetre_lecon("Les listes", contenu)

    def afficher_dictionnaires(self):
        contenu = ("Les dictionnaires stockent des paires clé-valeur. Ils permettent de créer des associations entre des clés uniques et des valeurs associées.\n\n"
                   "🔎 Exemple:\n"
                   "```python\n"
                   "mon_dict = {'nom': 'Alice', 'âge': 25} # Un dictionnaire contenant des paires clé-valeur\n"
                   "mon_dict['âge'] = 26 # Modifie la valeur associée à la clé 'âge'\n"
                   "```\n\n"
                   "Les dictionnaires sont utiles pour organiser et accéder rapidement à des données associées.\n"
                   "Vous pouvez:\n"
                   "- Ajouter, modifier ou supprimer des paires clé-valeur\n"
                   "- Accéder aux valeurs par leur clé\n")
        self.creer_fenetre_lecon("Les dictionnaires", contenu)

    def lancer_quiz(self):
        questions = [
            {"question": "Quelle est la syntaxe correcte pour définir une fonction ?", "reponses": ["def nom[]:", "def nom():", "function nom[]:", "function nom():"], "reponse_correcte": "def nom():"},
            {"question": "Comment ajouter un élément à une liste ?", "reponses": ["liste.append(element)", "liste.add(element)", "liste.insert(element)", "liste.append_element(element)"], "reponse_correcte": "liste.append(element)"},
            {"question": "Comment définir une variable en Python ?", "reponses": ["variable = valeur", "valeur = variable", "var valeur", "variable : valeur"], "reponse_correcte": "variable = valeur"}
        ]
        random.shuffle(questions)  

        score = 0

        def verifier_reponse(reponse, reponse_correcte, quiz_window):
            nonlocal score
            if reponse == reponse_correcte:
                messagebox.showinfo("Réponse", "Bonne réponse !")
                score += 1
            else:
                messagebox.showerror("Réponse", "Mauvaise réponse.")
            
            quiz_window.after(2000, lambda: quiz_window.destroy())

        for q in questions:
            quiz_window = tk.Toplevel(self.root)
            quiz_window.title("Quiz")
            quiz_window.geometry("400x300")
            quiz_window.attributes("-topmost", True)  
            tk.Label(quiz_window, text=q["question"], font=("Helvetica", 14)).pack(pady=10)
            for reponse in q["reponses"]:
                bouton_reponse = ttk.Button(quiz_window, text=reponse, command=lambda r=reponse: verifier_reponse(r, q["reponse_correcte"], quiz_window))
                bouton_reponse.pack(pady=5)
            bouton_quitter = ttk.Button(quiz_window, text="Quitter le quiz", command=quiz_window.destroy)
            bouton_quitter.pack(pady=10)
            quiz_window.wait_window(quiz_window)
        messagebox.showinfo("Quiz terminé", f"Votre score est {score}/{len(questions)}")

    def mention_speciale(self):
        mention = tk.Label(self.root, text="Développé par Axio", font=("Helvetica", 12, "italic"), background="#f0f4f8", foreground="#007f7f")
        mention.pack(side="bottom", pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ApprentissagePythonApp(root)
    root.mainloop()
