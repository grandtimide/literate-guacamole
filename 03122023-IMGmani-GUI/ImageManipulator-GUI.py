from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def flip_horizontal(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def flip_vertical(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)

def rotate_90(img):
    return img.transpose(Image.ROTATE_90)

def rotate_custom(img, degrees):
    return img.rotate(degrees)

def choose_image():
    file_path = filedialog.askopenfilename(title="Sélectionnez une image")
    return file_path

def main():
    root = tk.Tk()
    root.withdraw()
    input_path = choose_image()

    img = Image.open(input_path)

    print("Choisissez une option :")
    print("1. Flip horizontal")
    print("2. Flip vertical")
    print("3. Rotation de 90 degrés")
    print("4. Rotation personnalisée")

    choice = input("Entrez le numéro de l'option choisie (1, 2, 3 ou 4) : ")

    if choice == '1':
        img_transformed = flip_horizontal(img)
    elif choice == '2':
        img_transformed = flip_vertical(img)
    elif choice == '3':
        img_transformed = rotate_90(img)
    elif choice == '4':
        degrees = float(input("Entrez l'angle de rotation personnalisé : "))
        img_transformed = rotate_custom(img, degrees)
    else:
        print("Option invalide. Veuillez choisir entre 1, 2, 3 ou 4.")
        return

    img_transformed.show()

    save_option = input("Voulez-vous sauvegarder l'image transformée? (Oui/Non) : ").lower()
    if save_option == 'oui':
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        img_transformed.save(output_path)
        print("Image transformée sauvegardée avec succès.")

if __name__ == "__main__":
    main()
