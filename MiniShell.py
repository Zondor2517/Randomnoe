from tkinter import Tk, Button, Label, Entry, messagebox
import os
import threading
class MiniShell:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini shell")
        self.root.configure(bg="#2c2c2c")
        self.root.geometry("300x150")
        
        # Метка с текущей директорией
        self.cwd_label = Label(root, text="", bg="#2c2c2c", fg="white")
        self.cwd_label.pack(pady=5)
        
        # Поле ввода команды
        self.entry = Entry(root, width=40)
        self.entry.pack(pady=10)
        
        # Кнопка выполнения
        self.button = Button(root, text="Выполнить", command=self.on_button_click)
        self.button.pack(pady=5)
        
        # Кнопка смены директории
        self.cd_button = Button(root, text="Сменить директорию", command=self.change_directory)
        self.cd_button.pack(pady=5)
        
        # Обновление метки с текущей директорией
        self.update_cwd_label()
    
    def update_cwd_label(self):
        """Обновляет метку с текущей директорией."""
        cwd = os.getcwd()
        self.cwd_label.config(text=f"Текущая директория: {cwd}")
    
    def on_button_click(self):
        """Выполняет команду из поля ввода."""
        user_input = self.entry.get().strip()
        if not user_input:
            messagebox.showwarning("Предупреждение", "Введите команду!")
            return

        def shell():
            try:
                # Безопаснее использовать subprocess вместо os.popen
                import subprocess
                result = subprocess.run(
                    user_input, 
                    shell=True, 
                    capture_output=True, 
                    text=True # Ограничение по времени
                )
                output = result.stdout if result.stdout else "Нет вывода"
                if result.returncode != 0:
                    output += f"\nОшибка (код {result.returncode})"
            except Exception as e:
                output = f"Ошибка: {str(e)}"
        
            messagebox.showinfo("Результат", output)
        threading.Thread(target=shell, daemon=True).start()
    def change_directory(self):
        """Меняет текущую директорию."""
        new_path = self.entry.get().strip()
        if not new_path:
            messagebox.showwarning("Предупреждение", "Введите путь!")
            return
        
        try:
            os.chdir(new_path)
            self.update_cwd_label()
            messagebox.showinfo("Успех", f"Директория изменена: {new_path}")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Директория не найдена!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сменить директорию: {str(e)}")

# Запуск приложения
root = Tk()
app = MiniShell(root)
root.mainloop()
