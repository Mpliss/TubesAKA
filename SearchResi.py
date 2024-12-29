import time
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sys

sizes_logged = []
iterative_times_logged = []
recursive_times_logged = []

def generate_resi_list(size):
    return [f"R{i:04d}" for i in range(1001, 1001 + size)]
 
def iterative_search(resi_list, target):
    index = 0
    while index < len(resi_list) :
        if resi_list[index] == target: 
            return index
        else :
            index += 1
    return -1

def recursive_search(resi_list, target, index=0):
    if resi_list[index] == target:
        return index
    elif index < len(resi_list):
        return recursive_search(resi_list, target, index + 1)
    else :
        return -1

def start_search():
    global sizes_logged, iterative_times_logged, recursive_times_logged
    try:
        size = int(entry_size.get())
        if size <= 0:
            raise ValueError("Ukuran data harus lebih dari 0.")
        
        resi_list = generate_resi_list(size)

        daftar_resi = "\n".join(resi_list[:20])
        messagebox.showinfo("Daftar Nomor Resi", f"Daftar nomor resi (contoh):\n\n{daftar_resi}\n\nTotal: {len(resi_list)} resi")
        sys.setrecursionlimit(10000)
        target_resi = entry_target.get()
        if not target_resi:
            raise ValueError("Nomor resi tidak boleh kosong.")
        if not target_resi.startswith('R'):
            target_resi = 'R' + target_resi

        start_time = time.time()
        iterative_result = iterative_search(resi_list, target_resi)
        iterative_time = time.time() - start_time

        start_time = time.time()
        recursive_result = recursive_search(resi_list, target_resi)
        recursive_time = time.time() - start_time

        sizes_logged.append(size)
        iterative_times_logged.append(iterative_time)
        recursive_times_logged.append(recursive_time)

        if iterative_result == -1:
            result_text = f"Nomor Resi yang Dicari: {target_resi}\n\nNomor resi tidak ditemukan dalam daftar."
        else:
            result_text = f"Nomor Resi yang Dicari: {target_resi}\n\n"
            result_text += f"Iteratif: Ditemukan di indeks {iterative_result} dalam {iterative_time:.6f} detik\n"
            result_text += f"Rekursif: Ditemukan di indeks {recursive_result} dalam {recursive_time:.6f} detik\n"

        messagebox.showinfo("Hasil Pencarian", result_text)

        plt.figure()
        methods = ["Iteratif", "Rekursif"]
        times = [iterative_time, recursive_time]
        plt.plot(methods, times, marker='o', linestyle='-', color='b', label="Waktu Eksekusi")
        plt.title("Perbandingan Waktu Eksekusi untuk Pencarian Saat Ini")
        plt.ylabel("Waktu (detik)")
        plt.xlabel("Metode Pencarian")
        for i, time_val in enumerate(times):
            plt.text(i, time_val, f"{time_val:.6f}", ha='center', va='bottom')
        plt.grid()
        plt.show()

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def show_all_graph():
    global sizes_logged, iterative_times_logged, recursive_times_logged
    if not sizes_logged:
        messagebox.showinfo("Data Kosong", "Belum ada data pencarian untuk ditampilkan.")
        return

    plt.figure()
    plt.plot(sizes_logged, iterative_times_logged, marker='o', linestyle='-', color='b', label="Iteratif")
    plt.plot(sizes_logged, recursive_times_logged, marker='o', linestyle='-', color='r', label="Rekursif")
    plt.title("Perbandingan Waktu Eksekusi untuk Semua Pencarian")
    plt.xlabel("Ukuran Data")
    plt.ylabel("Waktu (detik)")
    plt.legend()
    plt.grid()
    plt.show()

root = tk.Tk()
root.title("Perbandingan Waktu Pencarian Resi")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

label_size = tk.Label(frame, text="Ukuran Data:")
label_size.grid(row=0, column=0, sticky="e")
entry_size = tk.Entry(frame)
entry_size.grid(row=0, column=1)

label_target = tk.Label(frame, text="Target Resi:")
label_target.grid(row=1, column=0, sticky="e")
entry_target = tk.Entry(frame)
entry_target.grid(row=1, column=1)

button_search = tk.Button(frame, text="Cari", command=start_search)
button_search.grid(row=2, column=0, columnspan=2, pady=10)

button_all_graph = tk.Button(frame, text="Tampilkan Grafik Semua", command=show_all_graph)
button_all_graph.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()