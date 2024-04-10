import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import youtube_dl
import os

# Função para baixar uma playlist do YouTube
def baixar_playlist(url, formato, destino):
    ydl_opts = {
        'format': 'bestaudio/best' if formato == "mp3" else f'bestvideo[height<={formato}]+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if formato == "mp3" else [],
        'outtmpl': os.path.join(destino, '%(playlist_index)s - %(title)s.%(ext)s'),
        'download_archive': os.path.join(destino, 'downloaded.txt'),
        'ignoreerrors': True,  # Ignora erros durante a extração de informações
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    messagebox.showinfo("Download Concluído", "Playlist baixada com sucesso!")


# Função para processar o URL inserido pelo usuário
def processar_url():
    url = entry_url.get()
    if "youtube.com/playlist" not in url:
        messagebox.showerror("Erro", "Por favor, insira um URL de playlist do YouTube válido.")
        return
    formato = var_formato.get()
    destino = entry_destino.get()
    baixar_playlist(url, formato, destino)

# Função para selecionar um diretório de destino
def selecionar_destino():
    destino = filedialog.askdirectory()
    if destino:
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, destino)

# Configuração da GUI
root = tk.Tk()
root.title("Baixador de Playlists do YouTube")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_url = tk.Label(frame, text="URL da Playlist:")
label_url.grid(row=0, column=0, sticky="w")

entry_url = tk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, padx=5, pady=5)

label_destino = tk.Label(frame, text="Diretório de Destino:")
label_destino.grid(row=1, column=0, sticky="w")

entry_destino = tk.Entry(frame, width=40)
entry_destino.grid(row=1, column=1, padx=5, pady=5)

button_destino = tk.Button(frame, text="Selecionar", command=selecionar_destino)
button_destino.grid(row=1, column=2, padx=5, pady=5)

label_formato = tk.Label(frame, text="Formato:")
label_formato.grid(row=2, column=0, sticky="w")

var_formato = tk.StringVar()
var_formato.set("mp3")
radio_mp3 = tk.Radiobutton(frame, text="MP3", variable=var_formato, value="mp3")
radio_mp3.grid(row=2, column=1, padx=5, pady=5, sticky="w")
radio_360p = tk.Radiobutton(frame, text="360p", variable=var_formato, value="360")
radio_360p.grid(row=2, column=1, padx=5, pady=5)
radio_720p = tk.Radiobutton(frame, text="720p", variable=var_formato, value="720")
radio_720p.grid(row=2, column=1, padx=5, pady=5, sticky="e")

button_baixar = tk.Button(root, text="Baixar Playlist", command=processar_url)
button_baixar.pack(pady=10)

root.mainloop()
