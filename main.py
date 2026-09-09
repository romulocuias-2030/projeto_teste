import customtkinter as ctk


janela = ctk.CTk()
janela.title("Sistema Teste")
janela.geometry("400x200")
button = ctk.CTkButton(janela, text="Clique aqui", command=LookupError)
button.pack(pady=20)
mensagem = ctk.CTkLabel(janela, text="Ben vindo ao sitema Teste")
mensagem.pack(expand=True)

janela.mainloop()

# teste