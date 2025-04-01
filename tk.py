import tkinter as tk
from tkinter import messagebox, ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro do Cliente")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for pagina in (Homepagina, Segundapagina):
            pagina_name = pagina.__name__
            frame = pagina(parent=container, controller=self)
            self.frames[pagina_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.show_frame("Homepagina")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_frame(self, pagina_name):
        frame = self.frames[pagina_name]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Você quer sair da aplicação?"):
            self.destroy()

class Homepagina(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(1, weight=1)  

        label = tk.Label(self, text="Cadastro Do Cliente", width=90, height=10, fg="white", bg='#2F4F4F')
        label.grid(row=0, columnspan=3, pady=10, padx=10, sticky="ew")

        tk.Label(self, text="Nome: ").grid(row=1, column=0, sticky="e")
        self.nome_entry = tk.Entry(self)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self, text="Validar Nome", command=lambda: [self.validate_nome(), self.check_all_validations()]).grid(row=1, column=2, padx=5, pady=5)

        tk.Label(self, text="Endereço: ").grid(row=2, column=0, sticky="e")
        self.endereco_entry = tk.Entry(self)
        self.endereco_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self, text="Validar Endereço", command=lambda: [self.validate_endereco(), self.check_all_validations()]).grid(row=2, column=2, padx=5, pady=5)

        tk.Label(self, text="Telefone: ").grid(row=3, column=0, sticky="e")
        self.telefone_entry = tk.Entry(self)
        self.telefone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self, text="Validar Telefone", command=lambda: [self.validate_telefone(), self.check_all_validations()]).grid(row=3, column=2, padx=5, pady=5)

        tk.Label(self, text="Email: ").grid(row=4, column=0, sticky="e")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self, text="Validar Email", command=lambda: [self.validate_email(), self.check_all_validations()]).grid(row=4, column=2, padx=5, pady=5)
        self.email_entry.bind('<Return>', lambda event: [self.validate_email(), self.check_all_validations()])

        tk.Label(self, text="CPF: ").grid(row=5, column=0, sticky="e")
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        tk.Button(self, text="Validar CPF", command=lambda: [self.validate_cpf(), self.check_all_validations()]).grid(row=5, column=2, padx=5, pady=5)
        self.cpf_entry.bind('<Return>', lambda event: [self.validate_cpf(), self.check_all_validations()])

        self.next_button = tk.Button(self, text="Ir para a Segunda Página", command=lambda: self.controller.show_frame("Segundapagina"))
        self.next_button.grid(row=6, columnspan=3, pady=20, sticky="ew")
        self.next_button.config(state=tk.DISABLED)

    def validate_nome(self):
        nome = self.nome_entry.get()
        if nome == "":
            messagebox.showerror("Erro", "O nome não pode estar vazio.")
            return False
        return True

    def validate_endereco(self):
        endereco = self.endereco_entry.get()
        if endereco == "":
            messagebox.showerror("Erro", "O endereço não pode estar vazio.")
            return False
        return True

    def validate_telefone(self):
        telefone = self.telefone_entry.get()
        if telefone == "":
            messagebox.showerror("Erro", "O telefone não pode estar vazio.")
            return False
        return True

    def validate_email(self):
        email = self.email_entry.get()
        if "@" not in email:
            messagebox.showerror("Erro", "O email deve conter '@'.")
            return False
        return True

    def validate_cpf(self):
        cpf = self.cpf_entry.get()
        if len(cpf) != 11 or not cpf.isdigit():
            messagebox.showerror("Erro", "O CPF deve ter 11 dígitos numéricos.")
            return False
        messagebox.showinfo("Sucesso", "CPF válido.")
        return True

    def check_all_validations(self):
        if self.validate_nome() and self.validate_endereco() and self.validate_telefone() and self.validate_email() and self.validate_cpf():
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

    def process_entries(self):
        nome = self.nome_entry.get()
        endereco = self.endereco_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()
        print(f"Nome: {nome}\nEndereço: {endereco}\nTelefone: {telefone}\nEmail: {email}\nCPF: {cpf}")

class Segundapagina(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        label = tk.Label(self, text="Sistema de Busca de Materiais de Construção", fg='white', bg='#2F4F4F', width=135, height=5)
        label.grid(row=0, column=0, columnspan=5, sticky="NSEW")

        mensagem2 = tk.Label(self, text="Digite ou selecione o material desejado")
        mensagem2.grid(row=3, column=0)

        mensagem3 = tk.Label(self, text="Caso você queira pegar mais de 1 material ao mesmo tempo, digite um material em cada linha")
        mensagem3.grid(row=6, column=0, columnspan=2)

        self.caixa_texto = tk.Text(self, width=60, height=5)
        self.caixa_texto.grid(row=7, column=0)

        self.caixa_texto_2 = tk.Text(self, width=60, height=5)
        self.caixa_texto_2.grid(row=7, column=2)
        self.caixa_texto_2.config(state=tk.DISABLED)

        # Tabelas
        self.materiais_de_construcao = {
            'cimento': 25.00,
            'tijolos': 0.85,
            'areia': 15.00,
            'brita': 20.00,
            'tinta': 30.00,
            'madeira': 50.00,
            'vergalhões': 100.00,
            'argamassa': 10.00,
            'telhas': 40.00,
            'pregos': 5.00,
            'fios elétricos': 2.00,
            'canos de PVC': 3.00,
            'manta asfáltica': 60.00,
            'revestimento': 70.00,
            'louças sanitárias': 25.00,
            'portas': 150.00,
            'segundapaginas': 120.00
        }

        self.quantidade_materiais = {
            'cimento': '90 kg',
            'tijolos': '175 unidades',
            'areia': '15 kg',
            'brita': '20 kg',
            'tinta': '30 litros',
            'madeira': '50 metros',
            'vergalhões': '100 unidades',
            'argamassa': '109 kg',
            'telhas': '407 unidades',
            'pregos': '510 unidades',
            'fios elétricos': '200 metros',
            'canos de PVC': '300 metros',
            'manta asfáltica': '60 metros',
            'revestimento': '70 metros quadrados',
            'louças sanitárias': '25 unidades',
            'portas': '15 unidades',
            'segundapaginas': '19 unidades'
        }

        self.mensagem_cotacao = tk.Label(self, text="")
        self.mensagem_cotacao.grid(row=3, column=2)

        materiais = list(self.materiais_de_construcao.keys())
        self.material = ttk.Combobox(self, values=materiais)
        self.material.grid(row=3, column=2, columnspan=2, sticky='w')

    # Botão Buscar produto (solo)
        botao = tk.Button(self, text="Buscar produto", command=self.buscar_produto)
        botao.grid(row=3, column=1)

    # Botão buscar produtos (conjunto)
        botao_multiplascotacoes = tk.Button(self, text="Buscar produtos", command=self.buscar_preco)
        botao_multiplascotacoes.grid(row=7, column=1)

    # Botão para voltar para a página inicial
        botao_voltar = tk.Button(self, text="Voltar para a Página Inicial", command=lambda: self.controller.show_frame("Homepagina"))
        botao_voltar.grid(row=8, column=1, pady=20)

    def buscar_produto(self):
        material_preenchido = self.material.get().lower()
        preco_material = self.materiais_de_construcao.get(material_preenchido)
        quantidade_material = self.quantidade_materiais.get(material_preenchido)
        if preco_material and quantidade_material:
            self.mensagem_cotacao.config(text=f'Preço do material {material_preenchido} é de {preco_material} reais. Quantidade: {quantidade_material}')
        else:
            self.mensagem_cotacao.config(text="Material não encontrado")

    def buscar_preco(self):
        texto = self.caixa_texto.get("1.0", tk.END).lower()
        lista_materiais = texto.split('\n')
        mensagem_cotacoes = []
        for item in lista_materiais:
            preco_material = self.materiais_de_construcao.get(item)
            quantidade_material = self.quantidade_materiais.get(item)
            if preco_material and quantidade_material:
                mensagem_cotacoes.append(f'{item}: {preco_material} reais. Quantidade: {quantidade_material}')
        self.caixa_texto_2.config(state=tk.NORMAL)
        self.caixa_texto_2.delete("1.0", tk.END)
        self.caixa_texto_2.insert(tk.END, '\n'.join(mensagem_cotacoes))
        self.caixa_texto_2.config(state=tk.DISABLED)

    # Inicialização
if __name__ == "__main__":
    app = App()
    app.mainloop()
