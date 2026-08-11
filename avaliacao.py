#avaliação1
def calcular_tempo_download():
    #float pede quantidade decimal e input pede para o usuario digitar o valor
    tamanho = float(input("Digite o tamanho do arquivo (MB): "))
    velocidade = float(input("Digite a velocidade (Mbps): "))
#calculo em segundos, dividindo o tamanho do arquivo pela velocidade convertida para MB/s
    print(f"O tempo de download do arquivo é: {tamanho / (velocidade / 8)} segundos")

#chama a funcao para calcular o tempo de download
calcular_tempo_download()