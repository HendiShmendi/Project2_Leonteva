# Вариант 25. С начала суток прошло N секунд (N — целое).
# Найти количество полных часов, прошедших с начала суток.

import tkinter as tk
from tkinter import messagebox

BG       = '#0a1a3a'  
ORANGE   = '#FF8C00'  
GOLD     = '#FFD700'  
WHITE    = '#ffffff'
GRAY_FG  = '#aaaaaa'
GREEN    = '#2ECC40'
RED_C    = '#FF4136'

FONT_HEAD  = ('Arial', 18, 'bold')
FONT_LABEL = ('Arial', 11, 'bold')
FONT_ENTRY = ('Arial', 11)
FONT_RES   = ('Arial', 13, 'bold')
FONT_BTN   = ('Arial', 11, 'bold')



def calculate():
    raw = entry_n.get().strip()
    if raw == PLACEHOLDER or raw == '':
        result_var.set('')
        lbl_result.config(fg=GOLD)
        messagebox.showerror('Ошибка', 'Введите количество секунд!')
        return
    try:
        n = int(raw)
    except ValueError:
        result_var.set('')
        messagebox.showerror('Ошибка', 'Ошибка: введите целое число!')
        return
    if n < 0:
        result_var.set('')
        messagebox.showerror('Ошибка', 'Ошибка: число должно быть положительным!')
        return
    hours = n // 3600
    result_var.set(f'Полных часов: {hours}')
    lbl_result.config(fg=GREEN)


def clear_form():
    entry_n.delete(0, 'end')
    entry_n.insert(0, PLACEHOLDER)
    entry_n.config(fg=GRAY_FG)
    result_var.set('')


def on_closing():
    if messagebox.askokcancel('Выход', 'Вы уверены, что хотите выйти?'):
        root.destroy()


root = tk.Tk()
root.title('Вариант 25')
root.geometry('420x320+400+200')
root.configure(bg=BG)
root.resizable(False, False)

hdr = tk.Frame(root, bg=ORANGE, height=50)
hdr.pack(fill='x', side='top')
hdr.pack_propagate(False)
tk.Label(
    hdr,
    text='Вариант 25',
    font=FONT_HEAD,
    bg=ORANGE, fg=GOLD
).place(relx=0.5, rely=0.5, anchor='center')


main = tk.Frame(root, bg=BG)
main.pack(expand=True, fill='both', padx=40, pady=20)


tk.Label(
    main,
    text='С начала суток прошло N секунд.',
    font=('Arial', 9),
    bg=BG, fg=WHITE,
    anchor='center'
).grid(row=0, column=0, columnspan=2, pady=(0, 2))

tk.Label(
    main,
    text='Найти количество полных часов.',
    font=('Arial', 9),
    bg=BG, fg=WHITE,
    anchor='center'
).grid(row=1, column=0, columnspan=2, pady=(0, 14))


tk.Label(
    main,
    text='Введите N (секунды):',
    font=FONT_LABEL,
    bg=BG, fg=GOLD,
    anchor='e'
).grid(row=2, column=0, padx=(0, 12), pady=8, sticky='e')

PLACEHOLDER = 'Введите целое число...'
entry_n = tk.Entry(
    main,
    font=FONT_ENTRY,
    width=22,
    bg=WHITE, fg=GRAY_FG,
    bd=0, highlightthickness=0, relief='flat'
)
entry_n.grid(row=2, column=1, pady=8, ipady=6)
entry_n.insert(0, PLACEHOLDER)


def on_focus_in(e):
    if entry_n.get() == PLACEHOLDER:
        entry_n.delete(0, 'end')
        entry_n.config(fg='black')


def on_focus_out(e):
    if not entry_n.get():
        entry_n.insert(0, PLACEHOLDER)
        entry_n.config(fg=GRAY_FG)


entry_n.bind('<FocusIn>',  on_focus_in)
entry_n.bind('<FocusOut>', on_focus_out)
entry_n.bind('<Return>',   lambda e: calculate())

result_var = tk.StringVar()
lbl_result = tk.Label(
    main,
    textvariable=result_var,
    font=FONT_RES,
    bg=BG, fg=GOLD,
    anchor='center'
)
lbl_result.grid(row=3, column=0, columnspan=2, pady=(10, 0))

bot = tk.Frame(root, bg=ORANGE, height=52)
bot.pack(fill='x', side='bottom')
bot.pack_propagate(False)

btn_f = tk.Frame(bot, bg=ORANGE)
btn_f.place(relx=0.5, rely=0.5, anchor='center')

tk.Button(
    btn_f,
    text='Вычислить',
    font=FONT_BTN,
    bg=GREEN, fg='white',
    bd=0, padx=18, pady=3,
    activebackground='#27ae36',
    command=calculate
).pack(side='left', padx=8)

tk.Button(
    btn_f,
    text='Очистить',
    font=FONT_BTN,
    bg=RED_C, fg='white',
    bd=0, padx=18, pady=3,
    activebackground='#cc2200',
    command=clear_form
).pack(side='left', padx=8)

root.protocol('WM_DELETE_WINDOW', on_closing)
root.mainloop()