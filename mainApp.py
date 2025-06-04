import tkinter as tk
from tkinter import ttk
import uuid
from Elemento import *
from fazEquipa import criaOvDic, fazEquipas,escreveSolucoesOrdenadas



# ==========================
# 1. BASE
# ==========================

mainWindow = tk.Tk()
mainWindow.geometry('400x600')
mainWindow.title('Gerador de Equipas para o Vertical')
mainWindow.configure(bg="#e8b687")  # <-- muda a cor de fundo da janela principal



# ==========================
# 2. FRAME SUPERIOR
# ==========================

supFrame = ttk.Frame(mainWindow, width=400, height=300, borderwidth=10, relief=tk.GROOVE)
supFrame.pack_propagate(False)
supFrame.pack(fill='x', padx=10, pady=10)
supFrame.configure(style="SupFrame.TFrame")  # <-- aplica estilo ao frame

# Estilo personalizado para o botão e para o frame
style = ttk.Style()
style.theme_use("clam")  # para garantir que as cores funcionam bem




# ==========================
# 3. ESTILO BOTÕES
# ==========================

style.configure(
    "Embelezado.TButton",
    font=("Verdana", 12, "bold"),
    foreground="#3F1500",
    background="#d55a3f",
    borderwidth=2,
    focusthickness=3,
    focuscolor="#005999"
)
style.map(
    "Embelezado.TButton",
    background=[("active", "#98e915"), ("pressed", "#37287a")]
)

style.configure(
    "SupFrame.TFrame",
    background="#f7f0ea"  # cor de fundo do frame superior
)



# ==========================
# 4. BOTÃO GERAR
# ==========================

supFrame.grid_rowconfigure(0, weight=1)
supFrame.grid_rowconfigure(1, weight=1)
supFrame.grid_columnconfigure(0, weight=1)

geraButton = ttk.Button(
    supFrame,
    text="✨ Gerar Equipas ✨",
    style="Embelezado.TButton",
    cursor="hand1"
)
geraButton.grid(row=0, column=0, pady=(40,10), ipadx=10, ipady=6, sticky='n')




# ==========================
# 5. BOTÃO ADICIONAR
# ==========================

elementos: dict[str, Elemento] = {}

def abrir_janela_adicionar():
    janela = tk.Toplevel(mainWindow)
    janela.title("Adicionar Elemento")
    janela.geometry("900x750")
    janela.grab_set()  # Foca nesta janela até fechar

    # Labels e entradas para cada atributo
    tk.Label(janela, text="Nome:").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="Secção:").pack()
    seccao_entry = tk.Entry(janela)
    seccao_entry.pack()

    tk.Label(janela, text="Ano na Secção:").pack()
    ano_entry = tk.Entry(janela)
    ano_entry.pack()

    # Entradas para cada atributo
    overall = []

    # Função auxiliar para criar um campo com label e entry lado a lado
    def add_labeled_entry(parent, label_text, row, col, entry_list, label_width=25, entry_width=5):
        label = tk.Label(parent, text=label_text, anchor='w', width=label_width)
        label.grid(row=row, column=col*2, sticky='w', padx=(5,2), pady=2)
        entry = tk.Entry(parent, width=entry_width)
        entry.grid(row=row, column=col*2+1, sticky='w', padx=(0,10), pady=2)
        entry_list.append(entry)
        return entry

    # Usar um frame para os campos do overall
    overall_frame = tk.Frame(janela)
    overall_frame.pack(pady=10)

    overall = []
    row = 0

    # Técnica 27,5%
    tk.Label(overall_frame, text="Técnica 27,5%", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Amarrações 32,5%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Nós 15%:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Froissartage 7,5%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Cartografia, Orientação 10%:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Códigos 20%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Fogo 7,5%:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Socorrismo 7,5%:", row, 0, overall)
    row += 1

    # Interpessoais 17,5%
    tk.Label(overall_frame, text="Interpessoais 17,5%", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Trabalho em Equipa 55%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Gestão de Conflitos 15%:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Liderança 10%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Animação 20%:", row, 1, overall)
    row += 1

    # Físicas 12,5%
    tk.Label(overall_frame, text="Físicas 12,5%", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Destreza Física 60%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Destreza Manual 40%:", row, 1, overall)
    row += 1

    # Atitude 20%
    tk.Label(overall_frame, text="Atitude 20%", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Compromisso 30%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Motivação 30%:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Resiliência 15%:", row, 0, overall)
    add_labeled_entry(overall_frame, "Criatividade 15%:", row, 1, overall)
    row += 1

    # Mental 15%
    tk.Label(overall_frame, text="Mental 15%", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Inteligência:", row, 0, overall)
    add_labeled_entry(overall_frame, "Memória:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Atenção:", row, 0, overall)
    row += 1

    # Vida em Campo 7,5%
    tk.Label(overall_frame, text="Vida em Campo 7,5%", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Arrumação:", row, 0, overall)
    add_labeled_entry(overall_frame, "Montagens:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Cooperação:", row, 0, overall)

    def confirmar():
        nome = nome_entry.get()
        seccao = seccao_entry.get()
        ano = ano_entry.get() or "0"
        # Extrai os valores das entrys do overall
        overall_values = [float(e.get() or 0) for e in overall]
        id_elem = str(uuid.uuid4())
        overall_dic = criaOvDic(overall_values)
        elemento = Elemento(nome, seccao, int(ano), overall_dic)
        elementos[id_elem] = elemento
        infTab.insert('', 'end', iid=id_elem, values=(nome, seccao, ano, elemento.overall))
        janela.destroy()

    tk.Button(janela, text="Adicionar", command=confirmar).pack(pady=10)


addElemButton = ttk.Button(
    supFrame,
    text="👤 Adicionar Elemento 👤",
    style="Embelezado.TButton",
    cursor="hand1",
    command=abrir_janela_adicionar
)
addElemButton.grid(row=1, column=0, pady=(10,40), ipadx=10, ipady=6, sticky='n')





# ==========================
# 6. FRAME INFERIOR
# ==========================

infFrame = ttk.Frame(mainWindow, width=400, height=300, borderwidth=10, relief=tk.GROOVE, style="InfFrame.TFrame")
infFrame.pack(fill='both', expand=True, padx=10, pady=10)

style.configure(
    "InfFrame.TFrame",
    background="#d55a3f"  # cor de fundo do frame inferior
)


# ==========================
# 7. TABELA INFERIOR
# ==========================

x_scroll = ttk.Scrollbar(infFrame, orient='horizontal')
x_scroll.pack(side='bottom', fill='x')

infTab = ttk.Treeview(
    infFrame,
    columns=('nome', 'seccao', 'ano', 'overall'),
    show='headings',
    xscrollcommand=x_scroll.set
)
infTab.heading('nome', text='Nome')
infTab.heading('seccao', text='Secção')
infTab.heading('ano', text='Ano na Secção')
infTab.heading('overall', text='Overall')

infTab.column('nome', width=50)
infTab.column('seccao', width=50)
infTab.column('ano', width=50)
infTab.column('overall', width=50)

infTab.pack(fill='both', expand=True)
x_scroll.config(command=infTab.xview)

def delete_elemento(_):
    selecionados = infTab.selection()
    for iid in selecionados:
        if iid in elementos:
            del elementos[iid]
        infTab.delete(iid)
    print(elementos)

#Comportamento
infTab.bind('<Delete>', delete_elemento)

#Run
mainWindow.mainloop()