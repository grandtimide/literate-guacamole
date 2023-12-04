from tkinter import Tk, filedialog
from PIL import Image, ImageEnhance

def ameliorer_qualite_image(chemin_image_entree, chemin_image_sortie, facteur_amelioration):
    image = Image.open(chemin_image_entree)
    enhance = ImageEnhance.Contrast(image)
    image_amelioree = enhance.enhance(facteur_amelioration)
    image_amelioree.save(chemin_image_sortie)
    print("Amélioration de la qualité terminée. Image enregistrée à", chemin_image_sortie)

def selectionner_image():
    chemin_image_entree = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif")])

    if chemin_image_entree:
        chemin_image_sortie = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Images PNG", "*.png")])

        if chemin_image_sortie:
            facteur_amelioration = 1.5  # Ajustez ce facteur selon vos besoins
            ameliorer_qualite_image(chemin_image_entree, chemin_image_sortie, facteur_amelioration)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  
    selectionner_image()
    root.destroy()
