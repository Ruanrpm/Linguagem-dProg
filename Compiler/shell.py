import sys
import rpm

def executarArquivo(caminhoArquivo):
    if not caminhoArquivo.endswith('.rm'):
        print("A extensão do arquivo não é .rm")
        return
    
    try:
        with open(caminhoArquivo, 'r') as arquivo:
            texto = arquivo.read()
    except FileNotFoundError:
        print(f'Arquivo {caminhoArquivo} não encontrado')
    
    for numero, linha in enumerate(texto.split('\n'), start=1):
        if (linha.strip() == ''):
            continue

        resultado, erro = rpm.run(caminhoArquivo, linha)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Use: python shell.py <nomeArquivo.rm>")
    else:
        executarArquivo(sys.argv[1])