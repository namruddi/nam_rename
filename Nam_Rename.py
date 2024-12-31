import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

def browse_folder():
    folder_path.set(filedialog.askdirectory(title="Select Folder"))

def browse_file():
    folder_path.set(filedialog.askopenfilename(title="Select File"))

def rename_files():
    path = folder_path.get()
    if not os.path.exists(path):
        messagebox.showerror("Error", "The specified path does not exist")
        return

    # Collect data
    file_type = file_type_var.get()
    custom_name = custom_name_var.get()
    prefix = prefix_var.get()
    sensitivity = sensitivity_var.get()
    pieces = pieces_var.get()
    keep_original = keep_original_var.get()
    date = datetime.now().strftime("%d%m%y")

    try:
        files = []
        if os.path.isdir(path):
            files = os.listdir(path)
        else:
            files = [os.path.basename(path)]
            path = os.path.dirname(path)

        # Filter by type
        extensions = {
            "Photo": ["jpeg", "jpg", "png"],
            "Video": ["mp4", "mov", "avi"],
            "Archive": ["zip", "rar", "7z"],
            "GIF": ["gif"],
            "Folder": []
        }.get(file_type, [])

        if extensions:
            files = [f for f in files if f.split('.')[-1].lower() in extensions]

        # Rename files
        for index, file in enumerate(files, start=1):
            ext = file.split('.')[-1]
            if file_type == "Folder" and not os.path.isdir(os.path.join(path, file)):
                continue

            part_index = f"_p{index}"
            base_name = f"{custom_name}_{prefix}_{sensitivity}{part_index}_{pieces}p_{date}.{ext}".strip('_')
            if keep_original:
                base_name = f"{file.rsplit('.', 1)[0]}_{base_name}".strip('_')

            os.rename(os.path.join(path, file), os.path.join(path, base_name))

        messagebox.showinfo("Success", f"File renaming completed ({len(files)} files)")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create window
root = tk.Tk()
root.title("File Renamer")
root.geometry("900x600")
root.configure(bg="#314448")

folder_path = tk.StringVar()
custom_name_var = tk.StringVar(value="MyFile")
prefix_var = tk.StringVar(value="")
sensitivity_var = tk.StringVar(value="")
pieces_var = tk.StringVar(value="")
file_type_var = tk.StringVar(value="All")
keep_original_var = tk.BooleanVar()

# Title
title_label = tk.Label(root, text="File Renamer", bg="#314448", fg="#c7d3bf", font=("Consolas", 16))
title_label.pack(pady=10, anchor="w", padx=20)

# Path selection
frame_path = tk.Frame(root, bg="#314448")
frame_path.pack(pady=10, fill="x", padx=20)

tk.Entry(frame_path, textvariable=folder_path, width=40, relief="flat", highlightthickness=1, highlightbackground="#536d6c", highlightcolor="#536d6c").pack(side="left", padx=5, ipady=5)

tk.Button(frame_path, text="Browse", command=browse_folder, bg="#536d6c", fg="#c7d3bf", relief="flat", borderwidth=0, highlightthickness=0).pack(side="left", padx=5)

# File type selection
separator1 = tk.Frame(root, height=2, bg="#99AAB5")
separator1.pack(fill="x", padx=20, pady=5)

file_type_label = tk.Label(root, text="File Type", bg="#314448", fg="#c7d3bf", font=("Consolas", 16))
file_type_label.pack(pady=5, anchor="w", padx=20)

file_type_menu = ttk.Combobox(root, textvariable=file_type_var, values=["All", "Photo", "Video", "Archive", "GIF", "Folder"], state="readonly")
file_type_menu.pack(pady=5, padx=20, fill="x")

# Rename settings
separator2 = tk.Frame(root, height=2, bg="#99AAB5")
separator2.pack(fill="x", padx=20, pady=5)

frame_settings = tk.Frame(root, bg="#314448")
frame_settings.pack(pady=10, fill="x", padx=20)

# Custom name
custom_name_label = tk.Label(frame_settings, text="Custom Name:", bg="#314448", fg="#c7d3bf", font=("Consolas", 13))
custom_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
custom_name_entry = tk.Entry(frame_settings, textvariable=custom_name_var, width=25, relief="flat", highlightthickness=1, highlightbackground="#536d6c", highlightcolor="#536d6c")
custom_name_entry.grid(row=0, column=1, padx=5, pady=5)

custom_name_label = tk.Label(frame_settings, text="[CustomName_Prefix_Sensitivity_p1_Piece_Date]", bg="#314448", fg="#99AAB5", font=("Consolas", 10))
custom_name_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

# Prefix
prefix_label = tk.Label(frame_settings, text="Prefix:", bg="#314448", fg="#c7d3bf", font=("Consolas", 13))
prefix_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
prefix_menu = tk.Entry(frame_settings, textvariable=prefix_var, width=25, relief="flat", highlightthickness=1, highlightbackground="#536d6c", highlightcolor="#536d6c")
prefix_menu.grid(row=1, column=1, padx=5, pady=5)

prefix_hint_label = tk.Label(frame_settings, text="SS, mangaSS, photo, video, archive, mix", bg="#314448", fg="#99AAB5", font=("Consolas", 10))
prefix_hint_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# Sensitivity
sensitivity_label = tk.Label(frame_settings, text="Sensitivity:", bg="#314448", fg="#c7d3bf", font=("Consolas", 13))
sensitivity_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
sensitivity_menu = tk.Entry(frame_settings, textvariable=sensitivity_var, width=25, relief="flat", highlightthickness=1, highlightbackground="#536d6c", highlightcolor="#536d6c")
sensitivity_menu.grid(row=2, column=1, padx=5, pady=5)

# Sensitivity Hint
sensitivity_hint_label = tk.Label(frame_settings, text="NSC, SC, LSC, SC, VSC, mixSC", bg="#314448", fg="#99AAB5", font=("Consolas", 10))
sensitivity_hint_label.grid(row=2, column=2, padx=5, pady=5, sticky="w")


# Pieces
pieces_label = tk.Label(frame_settings, text="Pieces:", bg="#314448", fg="#c7d3bf", font=("Consolas", 13))
pieces_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
pieces_entry = tk.Entry(frame_settings, textvariable=pieces_var, width=25, relief="flat", highlightthickness=1, highlightbackground="#536d6c", highlightcolor="#536d6c")
pieces_entry.grid(row=3, column=1, padx=5, pady=5)

pieces_hint_label = tk.Label(frame_settings, text="1p, 50p, 100p", bg="#314448", fg="#99AAB5", font=("Consolas", 10))
pieces_hint_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

# Rename button
separator3 = tk.Frame(root, height=2, bg="#99AAB5")
separator3.pack(fill="x", padx=20, pady=5)

rename_button = tk.Button(root, text="Rename", command=rename_files, bg="#536d6c", fg="#c7d3bf", relief="flat", borderwidth=0, highlightthickness=0, font=("Consolas", 20))
rename_button.pack(pady=20, padx=20, fill="x")

root.mainloop()
