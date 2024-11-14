import tkinter as tk
from tkinter import messagebox

class PopulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("População dos Continentes")
        self.root.geometry("700x600")

        # Inicializar variáveis e criar widgets
        self.initialize_variables()
        self.create_widgets()

    def initialize_variables(self):
        self.ano = []
        self.p_Ásia = []
        self.p_África = []
        self.p_América = []
        self.p_Europa = []
        self.p_Oceania = []
        self.t_Ásia = []
        self.t_África = []
        self.t_América = []
        self.t_Europa = []
        self.t_Oceania = []

    def create_widgets(self):
        # Frame superior para entrada de dados
        frame_inputs = tk.Frame(self.root, padx=10, pady=10)
        frame_inputs.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Frame inferior para exibição de resultados
        frame_results = tk.Frame(self.root, padx=10, pady=10)
        frame_results.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Configurar proporções do grid
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        frame_results.grid_rowconfigure(0, weight=1)
        frame_results.grid_columnconfigure(0, weight=1)

        # Labels e campos de entrada para os dados
        self.lbl_ano = tk.Label(frame_inputs, text="Ano:", font=("Arial", 12), fg="blue")
        self.lbl_ano.grid(row=0, column=0, sticky="w")
        self.entry_ano = tk.Entry(frame_inputs)
        self.entry_ano.grid(row=0, column=1, pady=5)

        self.labels_pop = ["Ásia", "África", "América", "Europa", "Oceania"]
        self.entries_pop = {}
        self.entries_growth = {}
        
        for i, label in enumerate(self.labels_pop):
            lbl_pop = tk.Label(frame_inputs, text=f"População da {label}:", font=("Arial", 10), fg="green")
            lbl_pop.grid(row=i+1, column=0, sticky="w", pady=2)
            entry_pop = tk.Entry(frame_inputs)
            entry_pop.grid(row=i+1, column=1, pady=2)
            self.entries_pop[label] = entry_pop

            lbl_growth = tk.Label(frame_inputs, text=f"Aumento % da {label}:", font=("Arial", 10), fg="purple")
            lbl_growth.grid(row=i+1, column=2, sticky="w", pady=2)
            entry_growth = tk.Entry(frame_inputs)
            entry_growth.grid(row=i+1, column=3, pady=2)
            self.entries_growth[label] = entry_growth

        # Botões
        self.btn_calculate = tk.Button(frame_inputs, text="Calcular", command=self.calculate_population, bg="lightblue")
        self.btn_calculate.grid(row=len(self.labels_pop) + 1, column=0, columnspan=2, pady=10)

        self.btn_exit = tk.Button(frame_inputs, text="Sair", command=self.root.quit, bg="red", fg="white")
        self.btn_exit.grid(row=len(self.labels_pop) + 1, column=2, columnspan=2, pady=10)

        # Text widget para exibir os resultados
        self.txt_result = tk.Text(frame_results, wrap="word", font=("Arial", 10))
        self.txt_result.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar para o Text widget
        scrollbar = tk.Scrollbar(frame_results, command=self.txt_result.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.txt_result.config(yscrollcommand=scrollbar.set)

    def calculate_population(self):
        try:
            ano = int(self.entry_ano.get())
            self.ano.append(ano)
            
            pop_values = {label: float(self.entries_pop[label].get()) for label in self.labels_pop}
            growth_values = {label: float(self.entries_growth[label].get()) for label in self.labels_pop}
            
            # Cálculos de população futura para cada continente
            t_Ásia = pop_values["Ásia"] * (1 + growth_values["Ásia"] / 100)
            t_África = pop_values["África"] * (1 + growth_values["África"] / 100)
            t_América = pop_values["América"] * (1 + growth_values["América"] / 100)
            t_Europa = pop_values["Europa"] * (1 + growth_values["Europa"] / 100)
            t_Oceania = pop_values["Oceania"] * (1 + growth_values["Oceania"] / 100)

            # Armazenar os resultados em listas
            self.t_Ásia.append(t_Ásia)
            self.t_África.append(t_África)
            self.t_América.append(t_América)
            self.t_Europa.append(t_Europa)
            self.t_Oceania.append(t_Oceania)
            
            self.p_Ásia.append(growth_values["Ásia"])
            self.p_África.append(growth_values["África"])
            self.p_América.append(growth_values["América"])
            self.p_Europa.append(growth_values["Europa"])
            self.p_Oceania.append(growth_values["Oceania"])

            # Exibir os resultados
            self.display_results(ano, t_Ásia, t_África, t_América, t_Europa, t_Oceania, growth_values)
        except ValueError:
            messagebox.showerror("Erro de entrada", "Por favor, insira valores numéricos válidos.")

    def display_results(self, ano, t_Ásia, t_África, t_América, t_Europa, t_Oceania, growth_values):
        self.txt_result.insert(tk.END, f"Ano: {ano}\n")
        self.txt_result.insert(tk.END, f"População da Ásia: {t_Ásia:.0f} - Aumento: {growth_values['Ásia']:.2f}%\n")
        self.txt_result.insert(tk.END, f"População da África: {t_África:.0f} - Aumento: {growth_values['África']:.2f}%\n")
        self.txt_result.insert(tk.END, f"População da América: {t_América:.0f} - Aumento: {growth_values['América']:.2f}%\n")
        self.txt_result.insert(tk.END, f"População da Europa: {t_Europa:.0f} - Aumento: {growth_values['Europa']:.2f}%\n")
        self.txt_result.insert(tk.END, f"População da Oceania: {t_Oceania:.0f} - Aumento: {growth_values['Oceania']:.2f}%\n")
        self.txt_result.insert(tk.END, "-"*50 + "\n")
        self.txt_result.see(tk.END)  # Auto scroll para o final do Text

if __name__ == "__main__":
    root = tk.Tk()
    app = PopulationApp(root)
    root.mainloop()
