import tkinter as tk
from tkinter import ttk
import uuid
from Elemento import *
from fazEquipa import criaOvDic, fazEquipas,escreveSolucoesOrdenadas
from tkinter import messagebox
from tkinter import simpledialog
import threading
import os
import subprocess



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
elementos: dict[str, Elemento] = {}

supFrame.grid_rowconfigure(0, weight=1)
supFrame.grid_rowconfigure(1, weight=1)
supFrame.grid_columnconfigure(0, weight=1)

def geraEquipas():
    nEquipas = simpledialog.askinteger("Nº de Equipas", "Quantas equipas deseja fazer:")
    if nEquipas is None:
        messagebox.showerror('Inválido', 'men preenche lá isso')
        return

    # Cria uma janela de progresso
    progress_win = tk.Toplevel(mainWindow)
    progress_win.title("A gerar equipas...")
    progress_win.geometry("300x80")
    progress_win.resizable(False, False)
    progress_win.grab_set()
    tk.Label(progress_win, text="A gerar equipas, por favor aguarde...").pack(pady=5)
    progress = ttk.Progressbar(progress_win, mode='indeterminate')
    progress.pack(fill='x', padx=20, pady=10)
    progress.start(10)

    listElementos=list(elementos.values())
    def worker():
        try:
            solucoes = fazEquipas(listElementos, nEquipas, 1000000 * nEquipas)
        except Exception as e:
            solucoes = None
            error = str(e)
        else:
            error = None

        def on_finish():
            progress.stop()
            progress_win.destroy()
            if error:
                messagebox.showerror('Erro', f'Ocorreu um erro: {error}')
            elif not solucoes:
                messagebox.showerror('Elementos Insuficientes', 'Elementos incompatíveis com o nº de equipas indicado!')
            else:
                messagebox.showinfo('Feito','Equipas feitas, serão colocadas em ficheiro!')
                # abrir o ficheiro solucoes_equipas_ordenadas.txt
                escreveSolucoesOrdenadas(listElementos,solucoes,nEquipas)
                file_path = "solucoes_equipas_ordenadas.txt"
                # Tenta abrir o ficheiro com o programa padrão do SO
                try:
                    if os.name == 'nt':  # Windows
                        os.startfile(file_path)
                    elif os.name == 'posix':
                        subprocess.call(('xdg-open', file_path))
                    else:
                        messagebox.showinfo('Ficheiro criado', f'Ficheiro criado: {file_path}')
                except Exception as e:
                    messagebox.showinfo('Ficheiro criado', f'Ficheiro criado: {file_path}\nNão foi possível abrir automaticamente: {e}')

        mainWindow.after(0, on_finish)

    threading.Thread(target=worker, daemon=True).start()

geraButton = ttk.Button(
    supFrame,
    text="✨ Gerar Equipas ✨",
    style="Embelezado.TButton",
    cursor="hand1",
    command=geraEquipas
)
geraButton.grid(row=0, column=0, pady=(40,10), ipadx=10, ipady=6, sticky='n')


# ==========================
# 5. BOTÃO ADICIONAR
# ==========================


def abrir_janela_adicionar():
    janela = tk.Toplevel(mainWindow)
    janela.title("Adicionar Elemento")
    janela.geometry("500x700")
    janela.configure(bg="#e8b687")
    janela.grab_set()  # Foca nesta janela até fechar

    # Labels e entradas para cada atributo
    tk.Label(janela, text="Nome:").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="Secção:").pack()
    seccao_entry = tk.StringVar(value='II')
    comboSec= ttk.Combobox(janela,textvariable=seccao_entry)
    comboSec['values']=('II','III','IV')
    comboSec.pack()

    tk.Label(janela, text="Ano na Secção:").pack()
    spinAno= ttk.Spinbox(janela,from_=1, to=4)
    spinAno.pack()

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
    tk.Label(overall_frame, text="Técnica", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Amarrações:", row, 0, overall)
    add_labeled_entry(overall_frame, "Nós:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Froissartage:", row, 0, overall)
    add_labeled_entry(overall_frame, "Cartografia, Orientação:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Códigos:", row, 0, overall)
    add_labeled_entry(overall_frame, "Fogo:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Socorrismo:", row, 0, overall)
    row += 1

    # Interpessoais 17,5%
    tk.Label(overall_frame, text="Interpessoais", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Trabalho em Equipa:", row, 0, overall)
    add_labeled_entry(overall_frame, "Gestão de Conflitos:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Liderança:", row, 0, overall)
    add_labeled_entry(overall_frame, "Animação:", row, 1, overall)
    row += 1

    # Físicas 12,5%
    tk.Label(overall_frame, text="Físicas", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Destreza Física:", row, 0, overall)
    add_labeled_entry(overall_frame, "Destreza Manual:", row, 1, overall)
    row += 1

    # Atitude 20%
    tk.Label(overall_frame, text="Atitude", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Compromisso:", row, 0, overall)
    add_labeled_entry(overall_frame, "Motivação:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Resiliência:", row, 0, overall)
    add_labeled_entry(overall_frame, "Criatividade:", row, 1, overall)
    row += 1

    # Mental 15%
    tk.Label(overall_frame, text="Mental", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Inteligência:", row, 0, overall)
    add_labeled_entry(overall_frame, "Memória:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Atenção:", row, 0, overall)
    row += 1

    # Vida em Campo 7,5%
    tk.Label(overall_frame, text="Vida em Campo", font=('Verdana', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=(8,2), columnspan=4)
    row += 1
    add_labeled_entry(overall_frame, "Arrumação:", row, 0, overall)
    add_labeled_entry(overall_frame, "Montagens:", row, 1, overall)
    row += 1
    add_labeled_entry(overall_frame, "Cooperação:", row, 0, overall)

    def confirmar():
        nome = nome_entry.get()
        if not nome.strip():
            messagebox.showerror("Erro", "Nome inválido. Por favor, insira um nome.")
            return
        seccao = comboSec.get()
        ano = spinAno.get() or "1"
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

def printOverall(d):
    # Gera uma string com cada chave e valor em linhas separadas
    return "\n".join(f"{k}: {v}" for k, v in d.items())

def show_elemento(_):
    selecionado = infTab.selection()
    if not selecionado:
        return
    elem = elementos[selecionado[0]]
    msg = printOverall(elem.overDetalhado)
    messagebox.showinfo(elem.nome, msg)

#Comportamento
infTab.bind('<Delete>', delete_elemento)
infTab.bind('<<TreeviewSelect>>', show_elemento)
#Run
mainWindow.mainloop()