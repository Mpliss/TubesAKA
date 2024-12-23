import random
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def iterative_search(resi_list, target):
    """
    Algoritma pencarian iteratif untuk menemukan nomor resi
    """
    for index, resi in enumerate(resi_list):
        if resi == target:
            return index
    return -1

def recursive_search(resi_list, target, index=0):
    """
    Algoritma pencarian rekursif untuk menemukan nomor resi
    """
    if index >= len(resi_list):
        return -1
    if resi_list[index] == target:
        return index
    return recursive_search(resi_list, target, index + 1)

def generate_resi_list(size):
    """
    Membuat daftar nomor resi berurut dengan ukuran tertentu
    """
    # Generate nomor resi berurut dari 1001 hingga 1000+size
    return [f"R{i:04d}" for i in range(1001, 1001 + size)]

def start_search():
    try:
        size = int(entry_size.get())
        if size <= 0:
            raise ValueError("Ukuran data harus lebih dari 0.")
        
        resi_list = generate_resi_list(size)
        
        # Get user input for target resi
        target_resi = entry_target.get()
        if not target_resi:
            raise ValueError("Nomor resi tidak boleh kosong.")
        if not target_resi.startswith('R'):
            target_resi = 'R' + target_resi
            
        # Display generated resi list
        resi_list_text = "Daftar Nomor Resi:\n" + ", ".join(resi_list)
        messagebox.showinfo("Daftar Nomor Resi", resi_list_text)

        # Iterative Search
        start_time = time.time()
        iterative_result = iterative_search(resi_list, target_resi)
        iterative_time = time.time() - start_time

        # Recursive Search
        start_time = time.time()
        recursive_result = recursive_search(resi_list, target_resi)
        recursive_time = time.time() - start_time

        # Prepare result message
        if iterative_result == -1:
            result_text = f"Nomor Resi yang Dicari: {target_resi}\n\nNomor resi tidak ditemukan dalam daftar."
        else:
            result_text = f"Nomor Resi yang Dicari: {target_resi}\n\n"
            result_text += f"Iteratif: Ditemukan di indeks {iterative_result} dalam {iterative_time:.6f} detik\n"
            result_text += f"Rekursif: Ditemukan di indeks {recursive_result} dalam {recursive_time:.6f} detik\n"

        messagebox.showinfo("Hasil Pencarian", result_text)

        # Plot comparison if resi was found
        if iterative_result != -1:
            methods = ["Iteratif", "Rekursif"]
            times = [iterative_time, recursive_time]

            plt.figure()
            plt.bar(methods, times, color=['blue', 'green'])
            plt.title("Perbandingan Waktu Eksekusi")
            plt.ylabel("Waktu (detik)")
            plt.xlabel("Metode Pencarian")
            for i, time_val in enumerate(times):
                plt.text(i, time_val, f"{time_val:.6f}", ha='center', va='bottom')
            plt.show()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Pencarian Nomor Resi")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Data size input
label_size = tk.Label(frame, text="Masukkan ukuran data (jumlah nomor resi):")
label_size.grid(row=0, column=0, sticky="w")

entry_size = tk.Entry(frame, width=20)
entry_size.grid(row=0, column=1, padx=5, pady=5)

# Target resi input
label_target = tk.Label(frame, text="Masukkan nomor resi yang dicari (contoh: R1234):")
label_target.grid(row=1, column=0, sticky="w")

entry_target = tk.Entry(frame, width=20)
entry_target.grid(row=1, column=1, padx=5, pady=5)

button_start = tk.Button(frame, text="Mulai Pencarian", command=start_search)
button_start.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()