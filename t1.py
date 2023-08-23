def ciclos_por_instrucao(destino_arquivo):
    ciclos_instrucao = {}  # Dicionário para armazenar o número de ciclos por instrução
    
    with open(destino_arquivo, 'r') as i:
        for linha in i:
            instrucao = linha.strip()  # Remove espaços em branco
            
            opcode = instrucao[-7:]  # Extrai os últimos 7 bits como opcode
            
            # Dicionário com o número de ciclos para cada opcode
            ciclos_opcode = {
                "1100011": 3,  # Tipo B
                "1101111": 3,  # Tipo J (jal)
                "1100111": 3,  # Tipo J (jalr)
                "0100011": 4,  # Tipo S (sw)
                "0000011": 5,  # Tipo L (lw)
                "0110011": 4,  # Tipo R
                "0110111": 1,  # LUI
                "0010111": 1,  # AUIPC
                "1110011": 2,  # Ecall
                "0010011": 3   # Tipo I
            }

            if opcode in ciclos_opcode:
                ciclos_instrucao[instrucao] = ciclos_opcode[opcode]
    
    return ciclos_instrucao

def calcular_cpi(ciclos_instrucao):
    ciclos_total = sum(ciclos_instrucao.values())  # Calcula o número total de ciclos
    total_instrucao = len(ciclos_instrucao)  # Obtém o número total de instruções
    cpi = ciclos_total / total_instrucao   # Calcula o CPI médio (evita divisão por zero)
    return ciclos_total, cpi

def main():
    destino_arquivo = r'D:\VSCode\Python\ex2.txt'  # Caminho para o arquivo contendo as instruções
    ciclos_instrucao = ciclos_por_instrucao(destino_arquivo)  # Obtém o dicionário de ciclos por instrução
    
    lista_instrucao = sorted(ciclos_instrucao.items(), key=lambda x: x[1], reverse=True)  # Ordena as instruções por número de ciclos
    
    print("\nInstruções classificadas por número de ciclos:")
    for instrucao, ciclos in lista_instrucao:
        print(f"Instrução: {instrucao}, Ciclos: {ciclos}")
    
    ciclos_total, cpi = calcular_cpi(ciclos_instrucao)  # Calcula o número total de ciclos e o CPI médio
    
    print("Número total de ciclos gastos:", ciclos_total)
    print("CPI médio:", cpi)

if __name__ == "__main__":
    main()
