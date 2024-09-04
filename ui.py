import tkinter as tk
from tkinter import messagebox
from crud_operations import create_record, read_record, update_record, delete_record, get_all_records


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD con CouchDB")

        # Labels y entradas
        self.id_label = tk.Label(root, text="ID:")
        self.id_label.grid(row=0, column=0, padx=10, pady=10)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(root, text="Nombre:")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botones CRUD
        self.create_button = tk.Button(
            root, text="Crear", command=self.create_record)
        self.create_button.grid(row=2, column=0, padx=10, pady=10)

        self.read_button = tk.Button(
            root, text="Leer", command=self.read_record)
        self.read_button.grid(row=2, column=1, padx=10, pady=10)

        self.update_button = tk.Button(
            root, text="Actualizar", command=self.update_record)
        self.update_button.grid(row=2, column=2, padx=10, pady=10)

        self.delete_button = tk.Button(
            root, text="Eliminar", command=self.delete_record)
        self.delete_button.grid(row=2, column=3, padx=10, pady=10)

        # Listbox para mostrar todos los registros
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        self.refresh_listbox()

    def create_record(self):
        record = {
            "_id": self.id_entry.get(),
            "name": self.name_entry.get()
        }
        create_record(record)
        self.refresh_listbox()
        messagebox.showinfo("Info", "Registro creado con éxito")

    def read_record(self):
        record_id = self.id_entry.get()
        record = read_record(record_id)
        if record:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, record.get("name", ""))
        else:
            messagebox.showerror("Error", "Registro no encontrado")

    def update_record(self):
        record_id = self.id_entry.get()
        new_data = {"name": self.name_entry.get()}
        update_record(record_id, new_data)
        self.refresh_listbox()
        messagebox.showinfo("Info", "Registro actualizado con éxito")

    def delete_record(self):
        record_id = self.id_entry.get()
        delete_record(record_id)
        self.refresh_listbox()
        messagebox.showinfo("Info", "Registro eliminado con éxito")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        records = get_all_records()
        for record in records:
            self.listbox.insert(
                tk.END, f"ID: {record['_id']}, Nombre: {record.get('name', '')}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
