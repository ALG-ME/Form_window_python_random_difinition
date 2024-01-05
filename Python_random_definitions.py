import tkinter as tk
import random

# Определения Python
definitions = {
    "While": "Цикл 'while' используется для выполнения блока кода, пока условие истинно.",
    "For": "Цикл 'for' используется для итерации по элементам последовательности (например, списку или строке).",
    "If": "Условие 'if' позволяет выполнить определенный блок кода, если условие истинно.",
    "Function": "Функция - это блок кода, который можно вызывать с определенными аргументами.",
    "List": "Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных."
}


# Функция для отображения случайного определения
def show_random_definition():
    random_key = random.choice(list(definitions.keys()))
    definition_text.config(text=f"{random_key} - {definitions[random_key]}")


# Создание главного окна
root = tk.Tk()
root.title("Определения Python")

# Стилизация
root.geometry("400x400+100+300")
root.configure(bg="#f0f0f0")

# Создание заголовка
title_label = tk.Label(root, text="Случайные определения Python", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# Создание текстового поля для определений
definition_text = tk.Label(root, text="", wraplength=350, font=("Arial", 22), bg="#f0f0f0")
definition_text.pack(pady=20)

# Создание кнопки "Показать определение"
show_definition_button = tk.Button(root, text="Показать определение", command=show_random_definition, bg="#00897B", fg="white", font=("Arial", 12))
show_definition_button.pack()

# Запуск главного цикла приложения
root.mainloop()
