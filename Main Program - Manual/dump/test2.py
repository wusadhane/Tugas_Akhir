# library untuk GUI
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
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
    
    portofolio_data = []

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

        portofolio_data.append(
            (i+1, selected_assets, expectedReturn, volatility, sharpeRatio)
        )

    for data in portofolio_data:
        main_table.insert("", "end", text="",
            values=(data[0], ", ".join(data[1]), data[2], data[3], data[4]))

# fungsi untuk menampilkan detail portofolio
def details():
    # ambil data dari tabel
    selected_item = main_table.focus()
    if not selected_item:
        messagebox.showerror("Ups!", "Kamu belum pilih portofolionya.")
        return

    # Retrieve values of the selected row
    values = main_table.item(selected_item, "values")
    if not values:
        messagebox.showerror("Error", "Tidak ada data yang ditemukan untuk portofolio yang dipilih.")
        return

    # ambil nomor portofolio
    portofolio_nomor = values[0]

    # tampilkan detil portofolio
    detail_message = f"Portfolio: {values[0]}\nEmiten: {values[1]}\nExpected Return: {values[2]}\nRisk: {values[3]}\nSharpe Ratio: {values[4]}\n"

    # ambil informasi tambahan dari hasil optimasi
    selected_assets = values[1].split(", ")
    biaya = int(dana.get())

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

    detail_message += f"\nLot: {lot}\nAnggaran: {anggaran}\n\nProporsi Dana(%) :  {persensaham}\n\nSisa Uang: {sisaUang}\nHarga Terbaru: \n{harga_terbaru}"
    
    messagebox.showinfo("Portfolio Details", detail_message)

# Fungsi untuk perangkingan portofolio berdasarkan Expected Return
def rank():
    # Ambil target expected return dari input
    try:
        target_return = float(target_return_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Silakan masukkan nilai target expected return yang valid.")
        return
    
    # Ambil semua data dari tabel
    rows = main_table.get_children()
    if not rows:
        messagebox.showerror("Ups!", "Tidak ada data untuk dirangking.")
        return

    portfolio_data = []

    for row in rows:
        values = main_table.item(row, "values")
        portfolio_data.append(values)

    # Sort berdasarkan Expected Return (index ke-2 dari setiap item)
    portfolio_data.sort(key=lambda x: abs(target_return - float(x[2])))

    # Update tabel dengan data yang sudah dirangking
    for i, data in enumerate(portfolio_data):
        main_table.item(rows[i], values=(data[0], data[1], data[2], data[3], data[4], i + 1))

# -------------------------------/FUNCTION---------------------------

# ---------------------------------GUI------------------------------

# main window
main = tk.Tk()
main.title("Optimasi Saham Martkowiz - Auto")
main.geometry("1080x550")

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

# ---------------------------------Input 4------------------------------

# Input Target Expected Return
main_frame = LabelFrame(main, text="Target Expected Return", font=("roboto", 12))
main_frame.place(
    x=50,
    y=350,
)

target_return_entry = Entry(main_frame, width=25)
target_return_entry.grid(row=0, column=1, padx=10, pady=10)

# ---------------------------------BUTTON_PROSES------------------------------

# Tombol Proses
optimasi = Button(text="Process", command=View)
optimasi.place(
    x=50,
    y=450,
)

# ---------------------------------BUTTON_DETAIL------------------------------

detail_button = Button(text="Detail Portofolio", command=details)
detail_button.place(x=250, y=300)

# ---------------------------------BUTTON_RANK------------------------------

# Tombol untuk meranking portofolio
rank_button = Button(text="Rank Portfolios by Expected Return", command=rank)
rank_button.place(x=250, y=350)

# ---------------------------------/BUTTON_RANK------------------------------

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
    "Ranking"
)

# format kolom
main_table.column("#0", width=0, stretch=NO)
main_table.column("Portofolio", width=100, anchor=CENTER)
main_table.column("Emiten", width=250, anchor=CENTER)
main_table.column("Expected Return", width=120, anchor=CENTER)
main_table.column("Risk", width=100, anchor=CENTER)
main_table.column("Sharpe Ratio", width=100, anchor=CENTER)
main_table.column("Ranking", width=80, anchor=CENTER)

# judul kolom
main_table.heading("#0", text="", anchor=W)
main_table.heading("Portofolio", text="Portofolio", anchor=CENTER)
main_table.heading("Emiten", text="Emiten", anchor=CENTER)
main_table.heading("Expected Return", text="Expected Return", anchor=CENTER)
main_table.heading("Risk", text="Risk", anchor=CENTER)
main_table.heading("Sharpe Ratio", text="Sharpe Ratio", anchor=CENTER)
main_table.heading("Ranking", text="Ranking", anchor=CENTER)

# ---------------------------------/TABLE------------------------------


# end Main window
main.mainloop()

# ---------------------------------/GUI------------------------------
