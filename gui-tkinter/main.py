import os
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox

import humanize

root = tk.Tk()
root.geometry("800x600")
root.title("TreeSize")

frame1 = tk.Frame(root)
frame1.pack(side="top", fill="both", expand=True)

label1 = tk.Label(frame1, text="TreeSize")
label1.pack(side="top", padx=10, pady=10)
label2 = tk.Label(frame1, text="")
label2.pack(side="top", pady=10)

treeview = ttk.Treeview(frame1)
treeview.pack(side="left", fill="both", expand=True)
column_size = "Size"
column_modified = "Modified"
treeview.config(columns=(column_size, column_modified))

treeview.heading("#0", text="Name", anchor=tk.W)
treeview.heading(column_size, text=column_size, anchor=tk.W)
treeview.heading(column_modified, text=column_modified, anchor=tk.W)

treeview.column("#0", width=500, minwidth=400, stretch=tk.NO)
treeview.column(column_size, width=100, minwidth=100, stretch=tk.NO)
treeview.column(column_modified, width=150, minwidth=150, stretch=tk.NO)

scrollbar = tk.Scrollbar(frame1, orient="vertical", command=treeview.yview)
scrollbar.pack(side="right", fill="y")

treeview.configure(yscrollcommand=scrollbar.set)

for col in ("Size", "Modified"):
    treeview.heading(col,
                     text=col,
                     command=lambda c=col: treeview_sort_column(treeview,
                                                                c,
                                                                False))


def sort_natural_size(tv, item, col):
    value = tv.set(item, col)
    try:
        # If the value can be converted to an integer, return it as is
        sort_key = int(value)
    except ValueError:
        try:
            # If the value is a file size in string format, convert it to integer bytes
            suffixes = {"Bytes": 0, "KiB": 1, "MiB": 2, "GiB": 3, "TiB": 4}
            number, suffix = value.split(" ")
            sort_key = int(float(number) * (1024 ** suffixes[suffix]))
        except ValueError:
            # If the value can't be converted to an integer or file size, return it as is
            sort_key = value
    return sort_key


def treeview_sort_column(tv, col, reverse):
    if col == "Size":
        # l = [(float(tv.set(k, col)), k) for k in tv.get_children("root_item")]
        l = [(sort_natural_size(tv, k, col), k) for k in
             tv.get_children("root_item")]
    else:
        l = [(tv.set(k, col), k) for k in tv.get_children("root_item")]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, "root_item", index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


def calculate_folder_size(folder_path):
    total_size = 0
    folder_path = os.path.join(treeview.item("root_item")['text'], folder_path)
    for item in os.listdir(folder_path):
        path = os.path.join(folder_path, item)
        if os.path.isfile(path):
            total_size += os.path.getsize(path)
        elif os.path.isdir(path):
            total_size += calculate_folder_size(path)
    return total_size


def select_folder():
    folder_selected = filedialog.askdirectory()
    label2.config(text=folder_selected)
    if folder_selected:
        treeview.delete(*treeview.get_children())
        parent = "root_item"
        treeview.insert("",
                        index="end",
                        id=parent,
                        text=folder_selected,
                        open=True)
        for item in os.listdir(folder_selected):
            recursive_folder(parent, folder_selected, item)


def recursive_folder(
    parent,
    folder_selected,
    item):
    """

    :param parent:
    :param folder_selected:
    :param item:
    :return:
    """
    path = os.path.join(folder_selected, item)
    """
    treeview.insert()

    :param parent: 부모 아이템의 ID
    :param index:
        "" : 루트 아이템의 바로 아래에 추가합니다.
        "end" : 현재 선택된 아이템(선택된 아이템이 없을 경우 루트 아이템)의 바로 아래에 추가합니다.
        아이템의 ID : 지정된 아이템의 바로 아래에 추가합니다.
    :param text: 표시할 텍스트
    """
    if os.path.isfile(path):
        size = os.path.getsize(path)
        natural_size = humanize.naturalsize(size, binary=True)
        modified = os.path.getmtime(path)
        modified_str = datetime.fromtimestamp(modified).strftime(
            "%Y-%m-%d %H:%M:%S")

        treeview.insert(parent=parent,
                        index="end",
                        text=item,
                        values=(natural_size, modified_str))
    elif os.path.isdir(path):
        size = calculate_folder_size(path)
        natural_size = humanize.naturalsize(size, binary=True)
        new_parent = parent + item
        treeview.insert(parent=parent,
                        id=new_parent,
                        index="end",
                        text=item,
                        values=(natural_size, ""))
        for item in os.listdir(path):
            recursive_folder(new_parent, path, item)


def calculate():
    selected_item = treeview.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a folder.")
        return
    folder_selected = treeview.item(selected_item)["text"]
    total_size = calculate_folder_size(folder_selected)
    human_readable_size = humanize.naturalsize(total_size, binary=True)
    messagebox.showinfo("Total size",
                        f"The total size of {folder_selected} is {human_readable_size} bytes.")


button_frame = tk.Frame(root)
button_frame.pack(side="bottom", padx=10, pady=10)

select_folder_button = tk.Button(
    button_frame,
    text="Select Folder",
    command=select_folder)
select_folder_button.pack(side="left", padx=5)

calculate_button = tk.Button(
    button_frame,
    text="Calculate",
    command=calculate)
calculate_button.pack(side="left", padx=5)

root.mainloop()
