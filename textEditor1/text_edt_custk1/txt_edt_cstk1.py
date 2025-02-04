import customtkinter as ctk  # Importa a biblioteca customtkinter e a define como ctk.
from tkinter import filedialog as tkFileDialog  # Importa o módulo filedialog do tkinter e o define como tkFileDialog.

root = ctk.CTk()  # Usando customtkinter para criar a janela principal.
root.title("Text Editor")  # Define o título da janela principal como "Text Editor".

text = ctk.CTkTextbox(root)  # Usando customtkinter para criar o widget de texto.
text.grid(padx=10, pady=10, sticky="nsew")  # Organiza o widget de texto na janela principal com preenchimento e expansão.

def saveas():  # Define a função saveas.
    global text  # Declara que a variável text é global.
    t = text.get("1.0", "end-1c")  # Obtém todo o conteúdo do widget de texto.
    savelocation = tkFileDialog.asksaveasfilename()  # Abre uma janela para salvar o arquivo e retorna o caminho.
    file1 = open(savelocation, "w+")  # Abre o arquivo no local especificado para escrita.
    file1.write(t)  # Escreve o conteúdo do widget de texto no arquivo.
    file1.close()  # Fecha o arquivo.

button = ctk.CTkButton(root, text="Save", command=saveas)  # Usando customtkinter para criar o botão que chama a função saveas.
button.grid(padx=10, pady=10)  # Organiza o botão na janela principal com preenchimento.

def FontHelvetica():  # Define a função FontHelvetica.
    global text  # Declara que a variável text é global.
    text.configure(font=("Helvetica", 12))  # Configura a fonte do widget de texto para Helvetica com tamanho 12.

def FontCourier():  # Define a função FontCourier.
    global text  # Declara que a variável text é global.
    text.configure(font=("Courier", 12))  # Configura a fonte do widget de texto para Courier com tamanho 12.

font = ctk.CTkOptionMenu(root, values=["Helvetica", "Courier"])  # Usando customtkinter para criar um menu de opções.
font.grid(padx=10, pady=10)  # Organiza o menu de opções na janela principal com preenchimento.

def change_font(choice):  # Define a função change_font que muda a fonte com base na escolha do usuário.
    if choice == "Helvetica":  # Se a escolha for Helvetica.
        FontHelvetica()  # Chama a função FontHelvetica.
    elif choice == "Courier":  # Se a escolha for Courier.
        FontCourier()  # Chama a função FontCourier.

font.set("Select Font")  # Define o texto inicial do menu de opções como "Select Font".
font.configure(command=change_font)  # Configura o comando para alterar a fonte com base na escolha do menu de opções.

root.mainloop()  # Inicia o loop principal da aplicação customtkinter.
