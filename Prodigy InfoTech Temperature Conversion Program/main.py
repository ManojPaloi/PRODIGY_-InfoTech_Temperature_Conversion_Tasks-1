import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a numeric value for temperature.")
        return

    unit = unit_var.get()
    result_text = ""
    
    if unit == "Celsius":
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        result_text = f"{temp} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K"
    elif unit == "Fahrenheit":
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        result_text = f"{temp} °F = {celsius:.2f} °C = {kelvin:.2f} K"
    elif unit == "Kelvin":
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        result_text = f"{temp} K = {celsius:.2f} °C = {fahrenheit:.2f} °F"

    result.set(result_text)
    history_list.insert(tk.END, result_text)

def clear_fields():
    entry_temp.delete(0, tk.END)
    result.set("")

def save_history():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for item in history_list.get(0, tk.END):
                file.write(item + "\n")
        messagebox.showinfo("Saved", "History saved successfully.")

def reset_history():
    history_list.delete(0, tk.END)

def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{widget.winfo_rootx() + 20}+{widget.winfo_rooty() + 20}")
    label = ttk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1, padding=5)
    label.pack()
    tooltip.withdraw()

    def show_tooltip(event):
        tooltip.deiconify()
    
    def hide_tooltip(event):
        tooltip.withdraw()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

# Create main window
root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Style
style = ttk.Style()
style.configure("TFrame", background="sky blue")
style.configure("TLabel", background="#f0f8ff", font=("Helvetica", 12))
style.configure("TButton", background="#4caf50", foreground="black", font=("Helvetica", 10, "bold"))
style.map("TButton", background=[("active", "#45a049")])

# Main frame
main_frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Title label
title_label = ttk.Label(main_frame, text="Temperature Conversion Tool", font=("Helvetica", 18, "bold"), background="green", foreground="white")
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Input field for temperature
entry_temp = ttk.Entry(main_frame, width=10, font=("Helvetica", 12))
entry_temp.grid(row=1, column=1, padx=10, pady=10)

# Tooltip for entry
create_tooltip(entry_temp, "Enter the temperature value to be converted. Example: 25")

# Dropdown menu for selecting unit
unit_var = tk.StringVar()
unit_var.set("Celsius")
dropdown_unit = ttk.OptionMenu(main_frame, unit_var, "Celsius", "Celsius", "Fahrenheit", "Kelvin")
dropdown_unit.grid(row=1, column=2, padx=10, pady=10)

# Tooltip for dropdown
create_tooltip(dropdown_unit, "Select the unit of the temperature value: Celsius, Fahrenheit, or Kelvin.")

# Label for input
label_temp = ttk.Label(main_frame, text="Enter temperature:", background="#f0f8ff", font=("Helvetica", 12))
label_temp.grid(row=1, column=0, padx=10, pady=10)

# Convert button
button_convert = ttk.Button(main_frame, text="Convert", command=convert_temperature, style="TButton")
button_convert.grid(row=2, column=0, columnspan=3, pady=10)

# Tooltip for convert button
create_tooltip(button_convert, "Click to convert the temperature to the other units.")

# Clear button
button_clear = ttk.Button(main_frame, text="Clear", command=clear_fields, style="TButton")
button_clear.grid(row=3, column=0, columnspan=3, pady=10)

# Tooltip for clear button
create_tooltip(button_clear, "Click to clear the input and result fields.")

# Save history button
button_save = ttk.Button(main_frame, text="Save History", command=save_history, style="TButton")
button_save.grid(row=4, column=0, columnspan=3, pady=10)

# Tooltip for save button
create_tooltip(button_save, "Click to save the conversion history to a text file.")

# Reset history button
button_reset = ttk.Button(main_frame, text="Reset History", command=reset_history, style="TButton")
button_reset.grid(row=5, column=0, columnspan=3, pady=10)

# Tooltip for reset button
create_tooltip(button_reset, "Click to reset the conversion history.")

# Result display
result = tk.StringVar()
label_result = ttk.Label(main_frame, textvariable=result, font=("Helvetica", 12, "italic"), background="#f0f8ff")
label_result.grid(row=6, column=0, columnspan=3, pady=10)

# Conversion history
history_label = ttk.Label(main_frame, text="Conversion History:", font=("Helvetica", 12, "bold"), background="#f0f8ff")
history_label.grid(row=7, column=0, columnspan=3, pady=(20, 10))

history_list = tk.Listbox(main_frame, height=6, font=("Helvetica", 10), background="#ffffff")
history_list.grid(row=8, column=0, columnspan=3, pady=10)

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)
main_frame.rowconfigure(5, weight=1)
main_frame.rowconfigure(6, weight=1)
main_frame.rowconfigure(7, weight=1)
main_frame.rowconfigure(8, weight=1)

# Run the application
root.mainloop()


