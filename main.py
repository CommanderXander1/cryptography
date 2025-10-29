# TO DO: finish delete functionality and add creation of json file if an existing one is not found, as well as file selector option
import random
import json
import os
import tkinter as tk


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
loaded = None


class Generator:
    def __init__(self, name, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        self.q = q
        self.r = r
        self.s = s
        self.t = t
        self.u = u
        self.v = v
        self.w = w
        self.x = x
        self.y = y
        self.z = z


def encode(sentence, code):
    encoded = ""
    if isinstance(code, dict):
        for letter in sentence:
            if letter.lower() in letters:
                encoded += code[letter.lower()]
            else:
                encoded += letter
            encoded += '-'
    else:
        for letter in sentence:
            if letter.lower() in letters:
                encoded += code.__dict__[letter.lower()]
            else:
                encoded += letter
            encoded += '-'
    print(encoded)
    return encoded


def decode(sentence, code):
    decoded = ""
    words = sentence.split("-")
    if isinstance(code, dict):
        for letter in words:
            if letter in letters or letter in numbers:
                for key, value in code.items():
                    if value == letter:
                        decoded += key
            else:
                decoded += letter
    else:
        for letter in words:
            if letter in letters or letter in numbers:
                for key, value in code.__dict__.items():
                    if value == letter:
                        decoded += key
            else:
                decoded += letter
    print(decoded)
    return decoded


def generate(name="code", type="number", ran=True, rev=0, offset=0):
    global loaded
    ll = []
    second = []
    if type == "letter":
        if ran:
            for letter in letters:
                num = random.randint(0, 25)
                while num in second:
                    num = random.randint(0, 25)
                second.append(num)
                ll.append(letters[num])
        # type is letter but not random
        else:
            current = 0
            if rev > 1:
                while current < 27:
                    second = numbers[current:current + (rev)]
                    for num in second[::-1]:
                        ll.append(letters[int(num)-1])
                    current += rev
            else:
                for letter in letters:
                    ll.append(letter)
    elif type == "number":
        if ran:
            for number in range(26):
                num = random.randint(0, 25)
                while str(num) in ll:
                    num = random.randint(0, 25)
                ll.append(str(num))
        # type is number but not random
        else:
            current = 0
            if rev > 1:
                while current < 27:
                    second = numbers[current:current + (rev)]
                    for num in second[::-1]:
                        ll.append(num)
                    current += rev
            else:
                for num in numbers:
                    ll.append(num)
            
    loaded = Generator(name, ll[ofs(0, offset)], ll[ofs(1, offset)], ll[ofs(2, offset)], ll[ofs(3, offset)],
                               ll[ofs(4, offset)], ll[ofs(5, offset)], ll[ofs(6, offset)], ll[ofs(7, offset)],
                               ll[ofs(8, offset)], ll[ofs(9, offset)], ll[ofs(10, offset)], ll[ofs(11, offset)],
                               ll[ofs(12, offset)], ll[ofs(13, offset)], ll[ofs(14, offset)], ll[ofs(15, offset)],
                               ll[ofs(16, offset)], ll[ofs(17, offset)], ll[ofs(18, offset)], ll[ofs(19, offset)],
                               ll[ofs(20, offset)], ll[ofs(21, offset)], ll[ofs(22, offset)], ll[ofs(23, offset)],
                               ll[ofs(24, offset)], ll[ofs(25, offset)])
    print(loaded.__dict__)
    return loaded


def load(name):
    global loaded
    with open('codes.json', 'r+') as f:
        codes = json.load(f)
    for item in codes["code_list"]:
        if item["name"] == name:
            loaded = item
            print(item)
            return item


def export(item):
    with open('codes.json', 'r+') as file:
        file_data = json.load(file)
        named = False
        for subset in file_data["code_list"]:
            if subset["name"] == item.name:
                named = True
                print("There is already a code with this name")
                break
        if not named:
            file_data["code_list"].append(item.__dict__)
            file.seek(0)
            json.dump(file_data, file, indent=4)


def ofs(num, offset):
    return (num + offset) % 26


def check_for_file():
    structure = json.dumps({"code_list": []}, indent=4)
    file = os.path.join(os.getcwd(), 'codes.json')
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write(structure)


def delete_code(code):
    pass


class gui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Xander's encoder")

        self.input_frame_label = tk.Label(self.root, text="Input", font=('Georgia', 20))
        self.input_frame_label.pack()

        self.main_input_frame = tk.Frame(self.root)
        self.main_input_frame.pack()

        # variable declarations
        self.user_input = tk.StringVar(self.root, name="user_input")
        self.selected_code = tk.StringVar(self.root, name="selected_code")
        self.generator_name = tk.StringVar(self.root, name="generator_name")
        self.generator_export = tk.BooleanVar(self.root, name="generator_export")
        self.generator_type = tk.StringVar(self.root, name="generator_type")
        self.generator_random = tk.BooleanVar(self.root, name="generator_random")
        self.generator_reverse = tk.IntVar(self.root, name="generator_reverse")
        self.generator_offset = tk.IntVar(self.root, name="generator_offset")
        self.fonts = ('Georgia', 15)

        self.input_frame_text_input = tk.Entry(self.main_input_frame, textvariable=self.user_input, font=self.fonts, width=30)
        self.input_frame_text_input.grid(row=0, column=0, padx=5)

        self.input_encode_button = tk.Button(self.main_input_frame, text="Encode", font=self.fonts, command=lambda: self.set_result(encode(sentence=self.user_input.get(), code=load(self.selected_code.get()))))
        self.input_encode_button.grid(row=0, column=1, pady=5, padx=5)

        self.input_decode_button = tk.Button(self.main_input_frame, text="Decode", font=self.fonts, command=lambda: self.set_result(decode(sentence=self.user_input.get(), code=load(self.selected_code.get()))))
        self.input_decode_button.grid(row=0, column=2, pady=5, padx=5)

        self.input_result_grid = tk.Frame(self.root)
        self.input_result_grid.pack()

        self.input_result_label = tk.Label(self.input_result_grid, text="Result:", font=self.fonts)
        self.input_result_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_result = tk.Text(self.input_result_grid, height=5, width=30,)
        self.input_result.grid(row=0, column=1, padx=5, pady=5)

        self.select_code_grid = tk.Frame(self.root)
        self.select_code_grid.pack()

        self.code_input_label = tk.Label(self.select_code_grid, text="Select a code:", font=self.fonts)
        self.code_input_label.grid(row=0, column=0, pady=5, padx=5)

        self.code_input = tk.Entry(self.select_code_grid, textvariable=self.selected_code, font=self.fonts)
        self.code_input.grid(row=0, column=1, padx=5, pady=5)

        self.code_input_delete_button = tk.Button(self.select_code_grid, text="Delete code", font=self.fonts)
        self.code_input_delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.selected_code_display = tk.Frame(self.root)
        self.selected_code_display.pack()

        self.codes_list_grid = tk.Frame(self.root)
        self.codes_list_grid.pack()

        self.codes_list_label = tk.Label(self.codes_list_grid, text="Codes list:", font=self.fonts)
        self.codes_list_label.grid(row=0, column=0, padx=5, pady=5)

        self.codes_list = tk.Text(self.codes_list_grid, height=1, width=20, font=self.fonts)
        self.get_codes('codes.json')
        self.codes_list.grid(row=0, column=1, padx=5, pady=5)

        self.codes_list_refresh = tk.Button(self.codes_list_grid, text="Refresh", font=self.fonts, command=lambda: self.get_codes('codes.json'))
        self.codes_list_refresh.grid(row=0, column=2, padx=5, pady=5)

        self.generator_label = tk.Label(self.root, text="Generator", font=('Georgia', 20))
        self.generator_label.pack()

        self.generator_grid = tk.Frame(self.root, borderwidth=2)
        self.generator_grid.pack()

        self.generator_name_label = tk.Label(self.generator_grid, text="Name", font=self.fonts)
        self.generator_name_label.grid(row=0, column=0)

        self.generator_name_input = tk.Entry(self.generator_grid, font=self.fonts, textvariable=self.generator_name)
        self.generator_name_input.grid(row=0, column=1)

        self.generator_type_label = tk.Label(self.generator_grid, text="Type (number/letter)", font=self.fonts)
        self.generator_type_label.grid(row=1, column=0)

        self.generator_type_input = tk.Entry(self.generator_grid, font=self.fonts, textvariable=self.generator_type)
        self.generator_type_input.grid(row=1, column=1)

        self.generator_reverse_label = tk.Label(self.generator_grid, text="Reverse", font=self.fonts)
        self.generator_reverse_label.grid(row=2, column=0)

        self.generator_reverse_input = tk.Scale(self.generator_grid, variable=self.generator_reverse, orient='horizontal', from_=0, to=25)
        self.generator_reverse_input.grid(row=2, column=1)

        self.generator_offset_label = tk.Label(self.generator_grid, text="Offset", font=self.fonts)
        self.generator_offset_label.grid(row=3, column=0)

        self.generator_offset = tk.Scale(self.generator_grid, variable=self.generator_offset, orient='horizontal', from_=0, to=25)
        self.generator_offset.grid(row=3, column=1)

        self.generator_export_input = tk.Checkbutton(self.generator_grid, text="Export", variable=self.generator_export, onvalue=True, offvalue=False, font=self.fonts)
        self.generator_export_input.grid(row=4, column=0)

        self.generator_random_input = tk.Checkbutton(self.generator_grid, text="Random", variable=self.generator_random, onvalue=True, offvalue=False, font=self.fonts)
        self.generator_random_input.grid(row=4, column=1)

        self.generator_generate = tk.Button(self.generator_grid, text="Generate", font=self.fonts, command=self.input_generator)
        self.generator_generate.grid(row=5, column=0)

        self.root.mainloop()


    def get_codes(self, file):
        codes = []
        self.codes_list.delete("1.0", "end")
        with open(file, 'r+') as f:
            scope = json.load(f)
            for item in scope["code_list"]:
                codes.append(item["name"])
        self.codes_list.insert(tk.END, codes)
        return codes


    def set_result(self, text):
        self.input_result.delete("1.0", "end")
        self.input_result.insert(tk.END, text)


    def input_generator(self):
        loaded = generate(name=self.generator_name.get(), type=self.generator_type.get(), ran=self.generator_random.get(), rev=self.generator_reverse.get(), offset=self.generator_offset.get())
        if self.generator_export.get():
            export(loaded)
        self.set_result(loaded.__dict__)


if __name__ == '__main__':
    check_for_file()
    ui = gui()
