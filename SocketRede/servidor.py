import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

clientes = []

def handle_client(conexao, endereco, areaDeTexto):
    areaDeTexto.insert(tk.END, f"[+] Nova conexão de {endereco}\n")
    print(f"[DEBUG] Cliente {endereco} conectado")

    mensagem_boas_vindas = "Bem-vindo ao servidor! 🎉"
    conexao.sendall(mensagem_boas_vindas.encode("utf-8"))
    


    while True:
        try:
            data = conexao.recv(1024)
            if not data:
                break
            msg = data.decode("utf-8")
            print(f"[DEBUG] Recebido: {msg}")
            areaDeTexto.insert(tk.END, f"Cliente {endereco}: {msg}\n")
        except:
            break

    conexao.close()
    clientes.remove(conexao)
    areaDeTexto.insert(tk.END, f"[-] Cliente {endereco} desconectado\n")

def enviar_mensagem(entry, areaDeTexto):
    msg = entry.get()
    if msg:
        for c in clientes:
            c.sendall(msg.encode("utf-8"))
        areaDeTexto.insert(tk.END, f"Servidor: {msg}\n")
        entry.delete(0, tk.END)

def iniciar_servidor(areaDeTexto):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)
    areaDeTexto.insert(tk.END, "[*] Servidor iniciado na porta 5000\n")

    while True:
        conn, addr = server.accept()
        clientes.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr, areaDeTexto), daemon=True).start()

root = tk.Tk()
root.title("Servidor")
root.resizable(False, False)

areaDeTexto = ScrolledText(root, width=100, height=40)
areaDeTexto.pack()

entry = tk.Entry(root, width=80)
entry.pack(side=tk.LEFT, padx=5)

btn_enviar = tk.Button(root, text="Enviar", command=lambda: enviar_mensagem(entry, areaDeTexto))
btn_enviar.pack(side=tk.LEFT)

threading.Thread(target=iniciar_servidor, args=(areaDeTexto,), daemon=True).start()

root.mainloop()
