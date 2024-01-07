from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, Tk, W
from googletrans import Translator
from PIL import Image, ImageTk
from tkinter.font import Font

class TranslatorApp:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("750x210")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.setup_components()

    def setup_components(self):
        main_frame = Frame(self.parent, bd=10)
        main_frame.pack(fill="both", expand=True)

        # Set background image
        self.background_image = Image.open("pemandangan.jpg")
        self.background_image_original = ImageTk.PhotoImage(self.background_image)
        self.background_label = Label(main_frame, image=self.background_image_original)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set top label
        font_style = Font(family="Montserrat", size=15, weight="bold")
        top_label = Label(main_frame, text='SYAHRANI NIM 220511094', font=font_style, bg='#2E8B57', fg='white')
        top_label.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

        # Labels
        Label(main_frame, text='Masukkan teks:', bg='#2E8B57', fg='white').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(main_frame, text='Hasil Terjemahan:', bg='#2E8B57', fg='white').grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Textboxes
        self.txt_source = Entry(main_frame, width=100, fg='#2E8B57')
        self.txt_source.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        self.txt_result = Entry(main_frame, width=100, fg='#2E8B57')
        self.txt_result.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

        # OptionMenu for language selection
        self.selected_language = StringVar()
        self.selected_language.set("Pilih Bahasa")
        languages = ["English", "Italian", "Hungarian"]
        self.option_menu = OptionMenu(main_frame, self.selected_language, *languages)
        self.option_menu.config(bg='#2E8B57', fg='white')
        self.option_menu.grid(row=2, column=2, padx=5, pady=5)

        # Translate button
        self.btn_translate = Button(main_frame, text='Terjemahkan!', command=self.on_translate, bg='#2E8B57', fg='white')
        self.btn_translate.grid(row=3, column=2, padx=5, pady=5)

        # Monitor frame resize
        self.parent.bind("<Configure>", self.on_resize)

    def on_translate(self):
        dest_lang = self.get_language_code(self.selected_language.get())
        translator = Translator()

        # Translate
        result = translator.translate(self.txt_source.get(), dest=dest_lang)

        # Clear previous result
        self.txt_result.delete(0, 'end')

        # Display translation result
        self.txt_result.insert('end', result.text)

    def on_resize(self, event):
        new_width = event.width
        new_height = event.height

        # Resize and update background image with antialiasing
        resized_image = self.background_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(resized_image)
        self.background_label.configure(image=self.background_image)

    def get_language_code(self, language):
        # Check the selected language and return language code
        language_codes = {"English": 'en', "Italian": 'it', "Hungarian": 'hu'}
        return language_codes.get(language, None)

    def on_exit(self):
        # Exit the application
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    app = TranslatorApp(root, "Aplikasi Translator")
    root.mainloop()
