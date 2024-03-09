import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os

def create_subject_folders():
    subject_folders = ["math", "francais", "histoire", "svt", "physique_chimie", "espagnol", "anglais", "technologie"]
    base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cours")
    for subject in subject_folders:
        folder_path = os.path.join(base_folder, subject)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def open_subject_page(subject):
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cours", subject)
    if os.path.exists(folder_path):
        files_list = os.listdir(folder_path)
        if files_list:
            display_files_page(files_list, folder_path)
        else:
            messagebox.showinfo("Aucun fichier", f"Aucun fichier trouvé dans le dossier {subject}.")
    else:
        messagebox.showerror("Dossier introuvable", f"Dossier {subject} introuvable.")

def display_files_page(files_list, folder_path):
    files_window = tk.Toplevel(root)
    files_window.title("Liste des fichiers")
    files_window.geometry("800x600")
    files_window.configure(bg="lightgrey")

    canvas = tk.Canvas(files_window, bg="lightgrey", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    frame = tk.Frame(canvas, bg="lightgrey")
    canvas.create_window((10, 10), window=frame, anchor="nw")

    for i, file_name in enumerate(files_list):
        file_frame = tk.Frame(frame, bg="white", highlightbackground="grey", highlightthickness=1)
        file_frame.grid(row=i, column=0, padx=10, pady=10, sticky="ew")

        file_label = tk.Label(file_frame, text=file_name, bg="white", padx=10, pady=5)
        file_label.grid(row=0, column=0, sticky="ew")

        open_button = ttk.Button(file_frame, text="Ouvrir", command=lambda file=file_name: open_file(file, folder_path))
        open_button.grid(row=0, column=1, padx=10, pady=5)

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    files_window.attributes('-topmost', True)

def open_file(selected_file, folder_path):
    file_path = os.path.join(folder_path, selected_file)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
        display_file_content(selected_file, file_content)
    except UnicodeDecodeError:
        try:
            os.startfile(file_path)
        except:
            messagebox.showerror("Erreur", "Impossible d'ouvrir le fichier")

def display_file_content(file_name, file_content):
    content_window = tk.Toplevel(root)
    content_window.title(file_name)

    text_widget = tk.Text(content_window, wrap="word")
    text_widget.insert(tk.END, file_content)
    text_widget.pack(fill="both", expand=True, padx=10, pady=10)

def open_image():
    file_path = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        try:
            img = tk.PhotoImage(file=file_path)
            img_label.config(image=img)
            img_label.image = img
        except tk.TclError:
            messagebox.showerror("Erreur", "Impossible d'ouvrir l'image")

create_subject_folders()

root = tk.Tk()
root.title("Logiciel d'Étude")

btns_subjects = {
    "Mathématique": "math",
    "Français": "francais",
    "Histoire": "histoire",
    "SVT": "svt",
    "Physique Chimie": "physique_chimie",
    "Espagnol": "espagnol",
    "Anglais": "anglais",
    "Technologie": "technologie"
}

for subject, folder in btns_subjects.items():
    btn = ttk.Button(root, text=subject, command=lambda folder=folder: open_subject_page(folder))
    btn.pack(pady=5)

open_image_button = ttk.Button(root, text="Ouvrir une image", command=open_image)
open_image_button.pack(pady=5)

img_label = tk.Label(root)
img_label.pack(padx=10, pady=10)

root.mainloop()
