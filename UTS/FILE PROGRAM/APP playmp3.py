import os
import threading
from tkinter import Tk, Button, Label, PhotoImage, OptionMenu, StringVar, Frame, font
import pygame

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemutar Musik")

        # Mengatur ukuran frame
        self.root.geometry("300x150")

        # Frame utama
        self.main_frame = Frame(root)
        self.main_frame.pack()

        # Menggunakan font STCaiyun bold dengan warna deep pink
        label_font = font.Font(family='Montserrat', size=13, weight='bold')
        label_color = '#030C54'  # deep pink color

        self.label = Label(self.main_frame, text="SYAHRANI NIM 220511094", font=label_font, fg=label_color)
        self.label.pack(pady=5, padx=5)

        # Menambahkan option menu untuk pilihan lagu
        self.selected_song = StringVar()
        self.selected_song.set("Pilih Lagu")
        song_list = ["Mahadewa - Immortal Love Song.mp3", "Maher Zain - Allahi Allah Kiya Karo.mp3", "Mitski - My Love All Mine.mp3"]
        self.song_menu = OptionMenu(self.main_frame, self.selected_song, *song_list)
        self.song_menu.pack(pady=5)

        self.button_play = Button(self.main_frame, text="Putar Musik", command=self.play_music, fg='#030C54')
        self.button_play.pack(pady=5, padx=5)

        # Menambahkan gambar untuk tombol jeda dan lanjut
        self.photo_pause = PhotoImage(file="pause.png").subsample(16)
        self.photo_resume = PhotoImage(file="play.png").subsample(16)

        self.button_pause = Button(self.main_frame, image=self.photo_pause, command=self.pause_resume_music, state="disabled")
        self.button_pause.pack(pady=5, padx=5)

        # Menambahkan callback untuk menutup mixer saat aplikasi ditutup
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        # Menambahkan atribut untuk melacak status musik
        self.music_paused = False

    def play_music(self):
        selected_song = self.selected_song.get()
        if selected_song != "Pilih Lagu":
            # Ganti 'tugas/dirayakan.mp3' dengan nama file MP3 yang ingin Anda putar
            file_path = os.path.join(os.getcwd(), selected_song)

            # Membuat thread terpisah untuk memutar musik
            self.music_thread = threading.Thread(target=self._play_music_thread, args=(file_path, ))
            self.music_thread.start()

            # Mengaktifkan tombol jeda
            self.button_pause.config(state="normal", image=self.photo_pause)

    def _play_music_thread(self, file_path):
        # Inisialisasi Pygame
        pygame.init()
        pygame.mixer.init()

        # Memutar file MP3
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Menunggu hingga lagu selesai atau dijeda
        while pygame.mixer.music.get_busy() or self.music_paused:
            pygame.time.Clock().tick(10)

        # Menampilkan durasi musik saat selesai
        duration = pygame.mixer.Sound(file_path).get_length()
        self.label.config(text=f"Durasi Musik: {duration:.2f} detik")

        # Mengaktifkan tombol putar kembali
        self.button_play.config(state="normal")
        # Menonaktifkan tombol jeda
        self.button_pause.config(state="disabled")

    def pause_resume_music(self):
        # Mengonfirmasi apakah musik sedang dijeda atau tidak
        if not self.music_paused:
            # Jika tidak dijeda, jeda musik
            pygame.mixer.music.pause()
            self.music_paused = True
            # Mengganti gambar tombol menjadi "Lanjut"
            self.button_pause.config(image=self.photo_resume)
        else:
            # Jika dijeda, lanjutkan musik
            pygame.mixer.music.unpause()
            self.music_paused = False
            # Mengganti gambar tombol menjadi "Jeda"
            self.button_pause.config(image=self.photo_pause)

    def close_app(self):
        # Membersihkan mixer sebelum menutup aplikasi
        pygame.mixer.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
