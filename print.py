import customtkinter
from datetime import datetime

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mostrar Hora Atual")
        self.geometry("400x200")

        # Cria um botão
        self.botao = customtkinter.CTkButton(self, text="Mostrar Hora", command=self.mostrar_hora)
        self.botao.pack(pady=20)

        # Cria um label para exibir a hora
        self.label_hora = customtkinter.CTkLabel(self, text="Hora Atual: ")
        self.label_hora.pack(pady=20)

    def mostrar_hora(self):
        hora_atual = datetime.now().strftime("%H:%M:%S")
        self.label_hora.configure(text=f"Hora Atual: {hora_atual}")

# Cria e executa a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
