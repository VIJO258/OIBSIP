import tkinter as tk
from tkinter import ttk


def calculate_bmi():
    error_label.config(text="")

    try:
        weight = float(weight_entry.get())
    except ValueError:
        error_label.config(text="Enter a valid number for weight, such as 68.")
        weight_entry.focus_set()
        return

    if weight < 0:
        error_label.config(text="Weight cannot be negative.")
        weight_entry.focus_set()
        return

    try:
        height = float(height_entry.get())
    except ValueError:
        error_label.config(text="Enter a valid number for height, such as 1.7.")
        height_entry.focus_set()
        return

    if height < 0:
        error_label.config(text="Height cannot be negative.")
        height_entry.focus_set()
        return
    if height == 0:
        error_label.config(text="Height cannot be zero.")
        height_entry.focus_set()
        return

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
        category_color = "#2878A5"
    elif bmi < 25:
        category = "Normal weight"
        category_color = "#17805D"
    elif bmi < 30:
        category = "Overweight"
        category_color = "#B66A12"
    else:
        category = "Obese"
        category_color = "#B42318"

    bmi_value_label.config(text=f"{bmi:.2f}")
    category_label.config(text=category, foreground=category_color)


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_value_label.config(text="--")
    category_label.config(text="Awaiting calculation", foreground="#53636B")
    error_label.config(text="")
    weight_entry.focus_set()


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x580")
root.resizable(False, False)
root.configure(background="#F2F6F5")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("App.TFrame", background="#F2F6F5")
style.configure("Card.TFrame", background="#FFFFFF")
style.configure(
    "Title.TLabel",
    background="#F2F6F5",
    foreground="#17333A",
    font=("Segoe UI", 23, "bold"),
)
style.configure(
    "Subtitle.TLabel",
    background="#F2F6F5",
    foreground="#53636B",
    font=("Segoe UI", 10),
)
style.configure(
    "Field.TLabel",
    background="#F2F6F5",
    foreground="#263D43",
    font=("Segoe UI", 10, "bold"),
)
style.configure("Input.TEntry", padding=9, font=("Segoe UI", 11))
style.configure(
    "Primary.TButton",
    background="#087F8C",
    foreground="#FFFFFF",
    padding=(12, 10),
    font=("Segoe UI", 10, "bold"),
)
style.map("Primary.TButton", background=[("active", "#066B76")])
style.configure(
    "Secondary.TButton",
    background="#E3ECEA",
    foreground="#17333A",
    padding=(12, 9),
    font=("Segoe UI", 10),
)
style.configure(
    "ResultTitle.TLabel",
    background="#FFFFFF",
    foreground="#53636B",
    font=("Segoe UI", 10),
)
style.configure(
    "ResultValue.TLabel",
    background="#FFFFFF",
    foreground="#17333A",
    font=("Segoe UI", 34, "bold"),
)
style.configure(
    "Category.TLabel",
    background="#FFFFFF",
    foreground="#53636B",
    font=("Segoe UI", 14, "bold"),
)

main_frame = ttk.Frame(root, style="App.TFrame", padding=32)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="BMI Calculator", style="Title.TLabel").pack(anchor="w")
ttk.Label(
    main_frame,
    text="Enter your measurements to calculate your BMI.",
    style="Subtitle.TLabel",
).pack(anchor="w", pady=(4, 24))

ttk.Label(main_frame, text="Weight (kg)", style="Field.TLabel").pack(anchor="w")
weight_entry = ttk.Entry(main_frame, style="Input.TEntry")
weight_entry.pack(fill="x", pady=(6, 16))

ttk.Label(main_frame, text="Height (m)", style="Field.TLabel").pack(anchor="w")
height_entry = ttk.Entry(main_frame, style="Input.TEntry")
height_entry.pack(fill="x", pady=(6, 18))

ttk.Button(
    main_frame,
    text="Calculate BMI",
    style="Primary.TButton",
    command=calculate_bmi,
).pack(fill="x")

error_label = tk.Label(
    main_frame,
    text="",
    background="#F2F6F5",
    foreground="#B42318",
    font=("Segoe UI", 9),
    anchor="w",
    wraplength=420,
)
error_label.pack(fill="x", pady=(8, 4))

result_frame = ttk.Frame(
    main_frame,
    style="Card.TFrame",
    padding=(20, 18),
    relief="solid",
    borderwidth=1,
)
result_frame.pack(fill="x", pady=(12, 18))
ttk.Label(result_frame, text="YOUR BMI", style="ResultTitle.TLabel").pack()
bmi_value_label = ttk.Label(result_frame, text="--", style="ResultValue.TLabel")
bmi_value_label.pack(pady=(4, 0))
category_label = ttk.Label(
    result_frame,
    text="Awaiting calculation",
    style="Category.TLabel",
)
category_label.pack(pady=(0, 4))

ttk.Button(
    main_frame,
    text="Clear",
    style="Secondary.TButton",
    command=clear_fields,
).pack(fill="x")

ttk.Label(
    main_frame,
    text="BMI is a general screening measure, not a medical diagnosis.",
    style="Subtitle.TLabel",
    wraplength=420,
).pack(anchor="w", pady=(18, 0))

weight_entry.focus_set()
root.mainloop()
