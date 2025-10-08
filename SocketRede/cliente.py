import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def receber_msg(sock,areaDeTexto):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            msg = data.decode("utf-8")
            areaDeTexto.insert(tk.END, f" Servidor: {msg}\n")
        except:
            break

def enviar_mensagem(sock,entry, areaDeTexto):
    msg = entry.get()
    if msg: 
        sock.sendall(msg.encode("utf-8"))
        areaDeTexto.insert(tk.END, f"Você: {msg}\n")
        entry.delete(0,tk.END)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.", 5000))


root = tk.Tk()
root.title("Cliente")
root.resizable(False,False)

areaDeTexto = ScrolledText(root, width=100, height=40)
areaDeTexto.pack()

entry = tk.Entry(root, width=80)
entry.pack(side=tk.LEFT, padx=5)

btn_enviar = tk.Button(root, text="Enviar", command=lambda: enviar_mensagem(sock, entry, areaDeTexto))
btn_enviar.pack(side=tk.LEFT)

threading.Thread(target=receber_msg,args=(sock, areaDeTexto ), daemon=True).start()

root.mainloop()
