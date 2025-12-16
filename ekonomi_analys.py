import customtkinter as ctk
from tkinter import messagebox

# Inställningar för modern look
ctk.set_appearance_mode("light")      # Vitt tema
ctk.set_default_color_theme("blue")   # Blå accenter (du kan byta till "green" eller annat)

app = ctk.CTk()
app.title("EkonomiAnalys")
app.geometry("800x600")

# Globla variabler för inmatningsfälten (så vi kommer åt dem lättare)
fornamn_entry = None
efternamn_entry = None
losen_entry = None
log_textbox = None

def clear_window():
    for widget in app.winfo_children():
        widget.destroy()

def show_login():
    clear_window()
    
    # Rosa rubrik
    ctk.CTkLabel(app, text="EkonomiAnalys", font=("Arial", 30, "bold"), 
                 text_color="#FF69B4").pack(pady=60)
    
    # Inloggningsram
    frame = ctk.CTkFrame(app, corner_radius=20)
    frame.pack(pady=20, padx=100, fill="both", expand=True)
    
    global fornamn_entry, efternamn_entry, losen_entry
    
    ctk.CTkLabel(frame, text="Förnamn").pack(pady=10)
    fornamn_entry = ctk.CTkEntry(frame, placeholder_text="t.ex. Anna", width=300)
    fornamn_entry.pack(pady=5)
    
    ctk.CTkLabel(frame, text="Efternamn").pack(pady=10)
    efternamn_entry = ctk.CTkEntry(frame, placeholder_text="t.ex. Andersson", width=300)
    efternamn_entry.pack(pady=5)
    
    ctk.CTkLabel(frame, text="Lösenord").pack(pady=10)
    losen_entry = ctk.CTkEntry(frame, placeholder_text="Minst 6 tecken", show="*", width=300)
    losen_entry.pack(pady=5)
    
    def login_check():
        fornamn = fornamn_entry.get().strip()
        efternamn = efternamn_entry.get().strip()
        losen = losen_entry.get()
        
        if fornamn and efternamn and len(losen) >= 6:
            show_main(f"{fornamn} {efternamn}")
        else:
            messagebox.showerror("Fel", "Fyll i alla fält och använd minst 6 tecken i lösenordet")
    
    ctk.CTkButton(frame, text="Logga in", command=login_check, 
                  width=200, height=40, corner_radius=15).pack(pady=40)

def show_main(namn):
    clear_window()
    
    ctk.CTkLabel(app, text=f"Välkommen {namn}!", font=("Arial", 26, "bold"), 
                 text_color="#FF69B4").pack(pady=40)
    
    # Loggram
    global log_textbox
    log_frame = ctk.CTkFrame(app, corner_radius=15)
    log_frame.pack(padx=50, pady=20, fill="both", expand=True)
    
    log_textbox = ctk.CTkTextbox(log_frame, font=("Arial", 14))
    log_textbox.pack(padx=20, pady=20, fill="both", expand=True)
    
    def run_analys():
        log_textbox.insert("end", "[System] Initialiserar analys...\n")
        log_textbox.insert("end", "[System] Laddar dina transaktioner...\n")
        log_textbox.insert("end", "[System] Beräknar saldo och prognos...\n")
        log_textbox.insert("end", "[System] Totalt saldo: 8500.00 kr\n")
        log_textbox.insert("end", "[System] Prognos nästa månad: +1500 kr\n")
        log_textbox.insert("end", "[System] Analys klar!\n\n")
        log_textbox.see("end")
    
    # Knappar längst ner
    btn_frame = ctk.CTkFrame(app)
    btn_frame.pack(pady=20)
    
    ctk.CTkButton(btn_frame, text="KÖR EKONOMIANALYS", command=run_analys,
                  width=300, height=50, corner_radius=15).pack(pady=10)
    
    ctk.CTkButton(btn_frame, text="Logga ut", command=show_login,
                  corner_radius=15).pack(pady=10)
    
    log_textbox.insert("end", "[System] Du är inloggad och redo!\n")
    log_textbox.insert("end", "Tryck på knappen för att köra analysen.\n\n")

# Starta med inloggningssidan
show_login()

app.mainloop()