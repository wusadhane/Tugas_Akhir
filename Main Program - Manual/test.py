# library untuk GUI
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
import itertools
import random

# export fungsi
from saham import kalkulasi
from emiten import list

# deklarasi global variable buat saham
emitenYangDicari = []

# -------------------------------FUNCTION---------------------------

# Fungsi Isi table
def View():
    if (
        dana.get() == ""
        or saham.get() == ""
        or kombinasi.get() == ""
    ):
        return tk.messagebox.showerror("Perhatian", "Silahkan Isi Semuanya")
    
    kombinasi_portofolio = int(kombinasi.get())
    emitens = int(saham.get())
    biaya = int(dana.get())

    # hapus tabel jika ada data
    for row in main_table.get_children():
        main_table.delete(row)
    
    for i in range(kombinasi_portofolio):
        print(biaya)
        
        # Pilih secara acak aset-aset dari list
        selected_assets = random.sample(list, emitens)
        print(selected_assets)
        
        (
            anggaran,
            lot,
            sisaUang,
            persensaham,
            expectedReturn,
            volatility,
            sharpeRatio,
            harga_terbaru,
        ) = kalkulasi(selected_assets, biaya)
        
        
        print(lot)
        expectedReturn = round(expectedReturn, 2)
        volatility = round(volatility, 2)
        sharpeRatio = round(sharpeRatio, 2)

        # masukin hasil optimasi ke tabel
        main_table.insert("", "end", text="",
            values=(i+1, ", ".join(selected_assets), expectedReturn, volatility, sharpeRatio))


# fungsi untuk menampilkan detail portofolio

# Fungsi untuk menampilkan detail portofolio
def details():
    # Ambil data dari tabel
    selected_item = main_table.focus()
    if not selected_item:
        messagebox.showerror("Ups!", "Kamu belum pilih portofolionya.")
        return

    # Retrieve values of the selected row
    values = main_table.item(selected_item, "values")
    if not values:
        messagebox.showerror("Error", "No data found for selected portfolio.")
        return
    
    # Mendapatkan nomor portofolio, emitens, expected return, risk, dan Sharpe Ratio
    portofolio_nomor = values[0]
    emitens = values[1].split(", ")
    expected_return = values[2]
    risk = values[3]
    sharpe_ratio = values[4]

    # Tampilkan informasi detail menggunakan messagebox
    detail_message = f"Portofolio Nomor: {portofolio_nomor}\n"
    detail_message += f"Emiten: {', '.join(emitens)}\n"
    detail_message += f"Expected Return: {expected_return}\n"
    detail_message += f"Risk: {risk}\n"
    detail_message += f"Sharpe Ratio: {sharpe_ratio}\n\n"

    # Mendapatkan informasi tambahan untuk setiap emitens dalam portofolio
    detail_message += "Informasi Tambahan untuk Setiap Emiten:\n"
    for emiten in emitens:
        # Dapatkan informasi lot, anggaran, dan alokasi dana untuk setiap emiten
        lot, anggaran, alokasi_dana = get_emiten_details(emiten)
        detail_message += f"Emiten: {emiten}\n"
        detail_message += f"Lot: {lot}\n"
        detail_message += f"Anggaran: {anggaran}\n"
        detail_message += f"Alokasi Dana: {alokasi_dana * 100}%\n\n"  # Konversi alokasi_dana ke persen

    messagebox.showinfo("Detail Portofolio", detail_message)

# Fungsi untuk mendapatkan informasi lot, anggaran, dan alokasi dana untuk setiap emitens
def get_emiten_details(emiten):
    # Misalnya, Anda perlu mengganti bagian ini dengan fungsi atau logika yang sesuai
    # Ini hanya contoh pseudo kode
    lot = random.randint(10, 100)  # Contoh pengambilan lot secara acak
    anggaran = random.randint(1000, 10000)  # Contoh pengambilan anggaran secara acak
    alokasi_dana = random.uniform(0.1, 0.5)  # Contoh pengambilan alokasi dana secara acak (dalam bentuk persentase)
    return lot, anggaran, alokasi_dana




# -------------------------------/FUNCTION---------------------------

# ---------------------------------GUI------------------------------

# main window
main = tk.Tk()
main.title("Optimasi Saham Martkowiz - Auto")
main.geometry("1080x450")



# ---------------------------------Input 1------------------------------

# Input Dana
main_frame = LabelFrame(main, text="Dana Investasi", font=("roboto", 12))
main_frame.place(
    x=50,
    y=50,
)

dana = Entry(main_frame, width=25)
dana.grid(row=0, column=1, padx=10, pady=10)
# ---------------------------------Input 2------------------------------

# Input Saham
main_frame = LabelFrame(main, text="Jumlah Saham", font=("roboto", 12))
main_frame.place(
    x=50,
    y=150,
)

saham = Entry(main_frame, width=25)
saham.grid(row=0, column=1, padx=10, pady=10)

# ---------------------------------Input 3------------------------------

# Input kombinasi
main_frame = LabelFrame(main, text="Kombinasi Portofolio", font=("roboto", 12))
main_frame.place(
    x=50,
    y=250,
)

kombinasi = Entry(main_frame, width=25)
kombinasi.grid(row=0, column=1, padx=10, pady=10)

# ---------------------------------BUTTON_PROSES------------------------------

# Tombol Proses
optimasi = Button(text="Process", command=View)
optimasi.place(
    x=50,
    y=350,
)

# ---------------------------------BUTTON_HAPUS------------------------------

# tombol hapus
hapus = Button(text="Clear Table")
hapus.place(
    x=360,
    y=300,
)

# ---------------------------------BUTTON_DETAIL------------------------------

detail_button = Button(text="Detail Portofolio", command=details)
detail_button.place(x=250, y=300)

# ---------------------------------/BUTTON_DETAIL------------------------------

# ---------------------------------TABEL---------------------------------------
style = ttk.Style()
style.theme_use("default")
style.configure(
    "TreeView",
    backgroud="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3",
)
style.map("TreeView", background=[("selected", "#347083")])

# frame tabel
main_frame = Frame(
    main,
)
main_frame.place(x=250, y=50)

# scroll bar
main_scroll = Scrollbar(main_frame)
main_scroll.pack(side=RIGHT, fill=Y)

# setting scroll bar
main_scroll.config(command=main_frame)

# membuat tabel
main_table = ttk.Treeview(
    main_frame, yscrollcommand=main_scroll.set, selectmode="extended"
)
main_table.pack()

# membuat kolom
main_table["columns"] = (
    "Portofolio",
    "Emiten",
    "Expected Return",
    "Risk",
    "Sharpe Ratio",
)

# format kolom
main_table.column("#0", width=0, stretch=NO)
main_table.column("Portofolio", width=100, anchor=CENTER)
main_table.column("Emiten", width=250, anchor=CENTER)
main_table.column("Expected Return", width=120, anchor=CENTER)
main_table.column("Risk", width=100, anchor=CENTER)
main_table.column("Sharpe Ratio", width=80, anchor=CENTER)

# judul kolom
main_table.heading("#0", text="", anchor=W)
main_table.heading("Portofolio", text="Portofolio", anchor=CENTER)
main_table.heading("Emiten", text="Emiten", anchor=CENTER)
main_table.heading("Expected Return", text="Expected Return", anchor=CENTER)
main_table.heading("Risk", text="Risk", anchor=CENTER)
main_table.heading("Sharpe Ratio", text="Sharpe Ratio", anchor=CENTER)

# ---------------------------------/TABLE------------------------------


# end Main window
main.mainloop()

# ---------------------------------/GUI------------------------------