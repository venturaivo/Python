def nome():

  while True:
    nome_completo = input("Escreva o seu nome ")
    nomes = nome_completo.split()

    if len(nomes) >= 2:
      if all(nome.isalpha() for nome in nomes):
        return nomes[0], nomes[-1]
      else:
        print("Nome inválido, insira nome valido")
    else:
      print("Nome inválido, insira o primeiro e ultimo nome")

def main():

  try:
    primeiro_nome, ultimo_nome = nome()
  except ValueError:
    print("Nome inválido, insira o primeiro e ultimo nome")
  else:
    print(f"Primeiro nome: {primeiro_nome} ({len(primeiro_nome)} caracteres)")
    print(f"Último nome: {ultimo_nome} ({len(ultimo_nome)} caracteres)")

if __name__ == "__main__":
  main()
