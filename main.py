from tkinter import END, Tk, ttk
import tkinter as tk

from trie import Trie

root = Tk()

# root.geometry("200x300")

trie = Trie()

lbl_insert = ttk.Label(root, text = 'insert').grid(row = 0, column = 0, sticky = 'nsew')
ins_word = str(tk.StringVar())
ent_insert = ttk.Entry(root, textvariable = ins_word)
ent_insert.grid(row = 1, column = 0, sticky = 'nsew')

def insert_word():
    word = ent_insert.get()
    trie.insert(word)
    print('"{}" inserted'.format(word))
    ent_insert.delete(0, END)
    
btn_insert = ttk.Button(root, text = 'insert', command=insert_word).grid(row = 3, column = 0, sticky = 'nsew')

# lbl_search = ttk.Label(root, text = 'search').grid(row = 4, column = 0, sticky = 'nsew')
# sea_word = str(tk.StringVar())
# ent_search = ttk.Entry(root, textvariable = sea_word)
# ent_search.grid(row = 5, column = 0, sticky = 'nsew')

# def search_word():
#     word = ent_search.get()
#     if trie.search(word):
#         print('"{}" found'.format(word))
#     else:
#         print('"{}" not found'.format(word))
#     ent_search.delete(0, END)
    
# btn_search = ttk.Button(root, text = 'search', command=search_word).grid(row = 6, column = 0, sticky = 'nsew')

# lbl_starts_with = ttk.Label(root, text='starts with').grid(row = 7, column = 0, sticky='nsew')
# prefix = tk.StringVar()
# prefix.trace('w', lambda name, index, mode, sv=prefix: starts_with())
# ent_pref = ttk.Entry(root, textvariable= prefix)
# ent_pref.grid(row = 8, column = 0, sticky = 'nsew')

# def starts_with():
#     pref = ent_pref.get()
#     if trie.startsWith(pref):
#         print('found string that starts with "{}"'.format(pref))
#     else:
#         print('did not find string that starts with "{}"'.format(pref))
#     # ent_pref.delete(0, END)
    
# btn_starts_with = ttk.Button(root, text = 'search', command=starts_with).grid(row = 9, column=0, sticky='nsew')

lbl_autocomplete = ttk.Label(root, text='autocomplete').grid(row = 10, column= 0, sticky='nsew')

auto_pref = tk.StringVar()
auto_pref.trace('w', lambda name, index, mode, sv=auto_pref: autocomplete())
ent_autopref = ttk.Entry(root, textvariable=auto_pref)
ent_autopref.grid(row = 11, column=0, sticky='nsew')

auto_comp = tk.StringVar()

lbl_auto_comp = ttk.Label(root, textvariable=auto_comp).grid(row = 12, column = 0, sticky='nsew')

def autocomplete():
    pref = ent_autopref.get()
    
    auto_comp.set(trie.autoComplete(pref))


root.mainloop()
