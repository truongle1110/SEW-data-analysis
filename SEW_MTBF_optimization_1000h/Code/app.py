import tkinter as tk
from tkinter import messagebox
from main import genetic_algorithm, GENOME_LENGTH, POPULATION_SIZE, GENERATIONS, p_c_min, p_c_max, p_m_min, p_m_max

def run_algorithm():
    try:
        C_s = float(entry_Cs.get())
        C_d = float(entry_Cd.get())
        m = int(entry_m.get())
        
        best_individual, best_fitness = genetic_algorithm(GENOME_LENGTH, m, POPULATION_SIZE, GENERATIONS, p_c_min, p_c_max, p_m_min, p_m_max, C_s, C_d)
        
        result_label.config(text=f"Best Individual: {best_individual}\nBest Fitness: {best_fitness}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for C_s, C_d, and m.")

# Create main window
root = tk.Tk()
root.title("Genetic Algorithm GUI")
root.geometry("400x300")

# Labels and Entry Widgets
tk.Label(root, text="C_s (Setup Cost):").pack()
entry_Cs = tk.Entry(root)
entry_Cs.pack()

tk.Label(root, text="C_d (Downtime Cost Rate):").pack()
entry_Cd = tk.Entry(root)
entry_Cd.pack()

tk.Label(root, text="m (Number of Repairmen):").pack()
entry_m = tk.Entry(root)
entry_m.pack()

# Run Button
run_button = tk.Button(root, text="Run Genetic Algorithm", command=run_algorithm)
run_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
