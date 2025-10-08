# Programa para manipular IPv4 em notação CIDR
# Exemplo de entrada: 192.168.1.10/24

def ip_para_binario(ip):
   
    partes = ip.split(".")  # separa em 4 blocos
    partes_bin = [format(int(parte), "08b") for parte in partes]  # cada bloco vira 8 bits
    return ".".join(partes_bin)


def mascara_rede(prefixo):
  
    bits_mascara = "1" * prefixo + "0" * (32 - prefixo)  # cria string binária
    blocos = [bits_mascara[i:i+8] for i in range(0, 32, 8)]  # divide em blocos de 8
    blocos_dec = [str(int(b, 2)) for b in blocos]  # converte cada bloco para decimal
    return ".".join(blocos_dec), ".".join(blocos)  # retorna decimal e binário


def main():
    # Entrada do usuário
    entrada = input("Digite o endereço IPv4 com CIDR (ex: 192.168.1.10/24): ")
    ip, prefixo = entrada.split("/")  # separa IP e prefixo
    prefixo = int(prefixo)

    # Conversões
    ip_binario = ip_para_binario(ip)
    mascara_dec, mascara_bin = mascara_rede(prefixo)

    # Saída formatada
    print("\n=== RESULTADO ===")
    print(f"Endereço IP: {ip}")
    print(f"Endereço IP (binário): {ip_binario}")
    print(f"Prefixo CIDR: /{prefixo}")
    print(f"Máscara de Rede (decimal): {mascara_dec}")
    print(f"Máscara de Rede (binário): {mascara_bin}")


if __name__ == "__main__":
    main()
