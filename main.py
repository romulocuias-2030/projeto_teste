#teste de envio de atualização
import customtkinter as ctk
from tkinter import messagebox


def mostrar_login_autorizado():
	messagebox.showinfo("Login", "Login Autorizado")


janela = ctk.CTk()
janela.title("Sistema Teste")
janela.geometry("400x200")
button = ctk.CTkButton(janela, text="Clique aqui", command=mostrar_login_autorizado)
button.pack(pady=20)
mensagem = ctk.CTkLabel(janela, text="Ben vindo ao sitema Teste")
mensagem.pack(expand=True)

janela.mainloop()
