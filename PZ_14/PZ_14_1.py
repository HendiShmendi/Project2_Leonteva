import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class FormaZayavki(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Форма заявки")
        self.resizable(False, False)
        self.configure(bg="#d4d0c8")

        # Цвета в стиле Windows 2000 / классический зелёный заголовок
        GREEN_HEADER = "#1e7a40"
        WHITE = "#ffffff"
        LIGHT_GRAY = "#f0efea"
        BORDER = "#808080"

        # ── Заголовок ──────────────────────────────────────────────────────────
        header = tk.Frame(self, bg=GREEN_HEADER)
        header.pack(fill="x")
        tk.Label(
            header,
            text="Форма заявки",
            bg=GREEN_HEADER,
            fg=WHITE,
            font=("MS Sans Serif", 11, "bold"),
            pady=5,
        ).pack()

        # ── Главная рамка ──────────────────────────────────────────────────────
        outer = tk.Frame(self, bg=LIGHT_GRAY, bd=1, relief="solid")
        outer.pack(padx=2, pady=2, fill="both", expand=True)

        # ── Информационный блок ────────────────────────────────────────────────
        info_frame = tk.Frame(outer, bg=LIGHT_GRAY, bd=1, relief="solid")
        info_frame.pack(fill="x", padx=4, pady=(4, 2))

        info_text = (
            "Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
            "Макс. размер каждого файла: 1024kb.\n"
            "Макс. общий размер файла: 2048kb."
        )
        tk.Label(
            info_frame,
            text=info_text,
            bg=LIGHT_GRAY,
            fg="#000000",
            font=("MS Sans Serif", 8),
            justify="left",
            anchor="w",
            padx=4,
            pady=4,
        ).pack(fill="x")

        # ── Вспомогательные методы ─────────────────────────────────────────────
        def make_row(parent, label_text, required=False):
            """Одна строка: метка | поле ввода (+ метка *)"""
            row = tk.Frame(parent, bg=LIGHT_GRAY, bd=1, relief="solid")
            row.pack(fill="x", padx=4, pady=1)

            lbl = tk.Label(
                row,
                text=label_text,
                width=18,
                anchor="w",
                bg=LIGHT_GRAY,
                fg="#000000",
                font=("MS Sans Serif", 8),
                padx=4,
            )
            lbl.pack(side="left", ipady=3)

            entry = tk.Entry(row, font=("MS Sans Serif", 8), bd=1, relief="sunken")
            entry.pack(side="left", fill="x", expand=True, ipady=2)

            if required:
                tk.Label(
                    row,
                    text="*",
                    fg="red",
                    bg=LIGHT_GRAY,
                    font=("MS Sans Serif", 9, "bold"),
                    padx=2,
                ).pack(side="left")
            return entry

        def make_file_row(parent, label_text):
            """Строка с кнопкой 'Обзор...' и полем пути"""
            row = tk.Frame(parent, bg=LIGHT_GRAY, bd=1, relief="solid")
            row.pack(fill="x", padx=4, pady=1)

            tk.Label(
                row,
                text=label_text,
                width=18,
                anchor="w",
                bg=LIGHT_GRAY,
                fg="#000000",
                font=("MS Sans Serif", 8),
                padx=4,
            ).pack(side="left", ipady=3)

            path_var = tk.StringVar()
            path_entry = tk.Entry(
                row,
                textvariable=path_var,
                font=("MS Sans Serif", 8),
                bd=1,
                relief="sunken",
                state="readonly",
            )
            path_entry.pack(side="left", fill="x", expand=True, ipady=2)

            def browse():
                filename = filedialog.askopenfilename(
                    filetypes=[
                        ("Допустимые файлы", "*.zip *.rar *.txt *.doc *.jpg *.png *.gif *.odt *.xml"),
                        ("Все файлы", "*.*"),
                    ]
                )
                if filename:
                    path_var.set(filename)

            btn = tk.Button(
                row,
                text="Обзор...",
                font=("MS Sans Serif", 8),
                bd=1,
                relief="raised",
                padx=6,
                command=browse,
            )
            btn.pack(side="left", padx=(4, 2), pady=2)
            return path_var

        # ── Поля формы ─────────────────────────────────────────────────────────
        self.name_entry = make_row(outer, "Ваше имя:", required=True)
        self.email_entry = make_row(outer, "Ваш Email:", required=True)
        self.subject_entry = make_row(outer, "Тема письма:", required=False)

        self.file1 = make_file_row(outer, "Прикрепить файл:")
        self.file2 = make_file_row(outer, "Прикрепить файл:")
        self.file3 = make_file_row(outer, "Прикрепить файл:")

        # ── Сообщение ──────────────────────────────────────────────────────────
        msg_row = tk.Frame(outer, bg=LIGHT_GRAY, bd=1, relief="solid")
        msg_row.pack(fill="both", expand=True, padx=4, pady=1)

        msg_label_frame = tk.Frame(msg_row, bg=LIGHT_GRAY)
        msg_label_frame.pack(side="left", anchor="nw")
        tk.Label(
            msg_label_frame,
            text="Ваше сообщение:",
            width=18,
            anchor="nw",
            bg=LIGHT_GRAY,
            fg="#000000",
            font=("MS Sans Serif", 8),
            padx=4,
            pady=4,
        ).pack(side="left")
        tk.Label(
            msg_label_frame,
            text="*",
            fg="red",
            bg=LIGHT_GRAY,
            font=("MS Sans Serif", 9, "bold"),
        ).pack(side="left")

        text_frame = tk.Frame(msg_row, bg=LIGHT_GRAY)
        text_frame.pack(side="left", fill="both", expand=True, padx=(0, 4), pady=4)

        self.message_text = tk.Text(
            text_frame,
            font=("MS Sans Serif", 8),
            bd=1,
            relief="sunken",
            height=7,
            wrap="word",
        )
        scrollbar = tk.Scrollbar(text_frame, command=self.message_text.yview)
        self.message_text.configure(yscrollcommand=scrollbar.set)
        self.message_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ── Кнопки ─────────────────────────────────────────────────────────────
        btn_frame = tk.Frame(outer, bg=LIGHT_GRAY)
        btn_frame.pack(pady=6)

        send_btn = tk.Button(
            btn_frame,
            text="Отправить Email",
            font=("MS Sans Serif", 8),
            bd=2,
            relief="raised",
            padx=10,
            pady=2,
            command=self.send_email,
        )
        send_btn.pack(side="left", padx=8)

        clear_btn = tk.Button(
            btn_frame,
            text="Отчистить",
            font=("MS Sans Serif", 8),
            bd=2,
            relief="raised",
            padx=10,
            pady=2,
            command=self.clear_form,
        )
        clear_btn.pack(side="left", padx=8)

        # Зелёная нижняя полоска
        tk.Frame(self, bg=GREEN_HEADER, height=6).pack(fill="x", side="bottom")

    # ── Логика ────────────────────────────────────────────────────────────────
    def send_email(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        message = self.message_text.get("1.0", "end").strip()

        if not name:
            messagebox.showwarning("Ошибка", "Поле «Ваше имя» обязательно для заполнения.")
            return
        if not email:
            messagebox.showwarning("Ошибка", "Поле «Ваш Email» обязательно для заполнения.")
            return
        if not message:
            messagebox.showwarning("Ошибка", "Поле «Ваше сообщение» обязательно для заполнения.")
            return

        messagebox.showinfo(
            "Успешно",
            f"Сообщение отправлено!\n\nИмя: {name}\nEmail: {email}",
        )

    def clear_form(self):
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.subject_entry.delete(0, "end")
        self.message_text.delete("1.0", "end")
        self.file1.set("")
        self.file2.set("")
        self.file3.set("")


if __name__ == "__main__":
    app = FormaZayavki()
    app.mainloop()