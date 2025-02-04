import customtkinter as ctk  # Importa a biblioteca customtkinter e a define como ctk.
from tkinter import filedialog as tkFileDialog, Menu  # Importa o módulo filedialog do tkinter e o Menu.

class TextEditor:  # Define a classe TextEditor que contém toda a lógica do editor de texto.
    def __init__(self, root):  # Método inicializador da classe, recebe a janela principal como argumento.
        self.root = root  # Atribui a janela principal à variável de instância root.
        self.root.title("Text Editor")  # Define o título da janela principal como "Text Editor".
        self.root.geometry("800x600")  # Define o tamanho da janela principal (largura x altura) para 800x600 pixels.
        self.root.minsize(400, 300)  # Define o tamanho mínimo da janela para 400x300 pixels.
        
        ctk.set_appearance_mode("dark")  # Define o modo escuro como padrão.
        
        # Configura a grade para permitir redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)

        # Cria a barra de menu
        self.menu_bar = Menu(root)
        self.root.config(menu=self.menu_bar)

        # Adiciona um menu Arquivo com a opção Salvar
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save", command=self.saveas)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Adiciona um menu Fonte com as opções de fonte
        self.font_menu = Menu(self.menu_bar, tearoff=0)
        self.font_menu.add_command(label="Helvetica", command=lambda: self.change_font("Helvetica"))
        self.font_menu.add_command(label="Courier", command=lambda: self.change_font("Courier"))
        self.menu_bar.add_cascade(label="Font", menu=self.font_menu)

        # Adiciona um menu Aparência com a opção de alternar entre modo claro e escuro
        self.appearance_menu = Menu(self.menu_bar, tearoff=0)
        self.appearance_menu.add_command(label="Light Mode", command=lambda: self.change_appearance("light"))
        self.appearance_menu.add_command(label="Dark Mode", command=lambda: self.change_appearance("dark"))
        self.menu_bar.add_cascade(label="Appearance", menu=self.appearance_menu)

        self.text = ctk.CTkTextbox(root)  # Cria um widget de texto usando customtkinter.
        self.text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Organiza o widget de texto na janela principal com preenchimento e expansão.

    def saveas(self):  # Método que salva o conteúdo do widget de texto em um arquivo.
        t = self.text.get("1.0", "end-1c")  # Obtém todo o conteúdo do widget de texto.
        savelocation = tkFileDialog.asksaveasfilename()  # Abre uma janela para salvar o arquivo e retorna o caminho.
        with open(savelocation, "w+") as file1:  # Abre o arquivo no local especificado para escrita.
            file1.write(t)  # Escreve o conteúdo do widget de texto no arquivo.

    def change_font(self, choice):  # Método que muda a fonte do widget de texto com base na escolha do usuário.
        if choice == "Helvetica":  # Se a escolha for Helvetica.
            self.text.configure(font=("Helvetica", 12))  # Configura a fonte do widget de texto para Helvetica com tamanho 12.
        elif choice == "Courier":  # Se a escolha for Courier.
            self.text.configure(font=("Courier", 12))  # Configura a fonte do widget de texto para Courier com tamanho 12.

    def change_appearance(self, mode):  # Método que altera o modo de aparência entre claro e escuro.
        ctk.set_appearance_mode(mode)  # Define o modo de aparência para o valor passado (light ou dark).

if __name__ == "__main__":  # Bloco que garante que o código dentro dele só seja executado se o script for executado diretamente.
    root = ctk.CTk()  # Cria a janela principal usando customtkinter.
    app = TextEditor(root)  # Cria uma instância da classe TextEditor passando a janela principal como argumento.
    root.mainloop()  # Inicia o loop principal da aplicação
