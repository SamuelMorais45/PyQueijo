import os
import pickle

# parte dos dictionary
produtos = {}
clientes = {}
try:
  arq_cliente = open("clientes.dat", "rb")
  clientes = pickle.load(arq_cliente)
except:
  arq_cliente = open("clientes.dat", "wb")
  arq_cliente.close()
  
resp = ''
# começo do programa
while resp != '0':
  os.system('clear')
  print("############################################")
  print("######       Projeto Fab_Queijo       ######")
  print("############################################")
  print("#####      1 - Módulo Clientes        #####")
  print("#####      2 - Módulo Produtos        #####")
  print("#####      3 - Módulo Vendas          #####")
  print("#####      4 - Módulo Informações     #####")
  print("#####      0 - Sair                   #####")
  resp = input("##### Escolha sua opção: ")
# mudulo de clientes
  if resp == '1':

    respCliente = ''
    while respCliente != '0' :
      os.system('clear')
      print()
      print("##############################################")
      print("#####     Você está no Módulo Clientes    ####")
      print("##############################################")
      print("#####      1 - Cadastrar Cliente         #####")
      print("#####      2 - Pesquisar Cliente         #####")
      print("#####      3 - Atualizar Cliente         #####")
      print("#####      4 - Apagar Cliente            #####")
      print("#####      0 - Voltar ao Menu Principal  #####")
      respCliente = input("##### Escolha sua opção: ")
      # cadastro de clientes
      if respCliente == '1':
        cadastro = ""
        while cadastro.lower() != 'n':
          os.system('clear')
          nome = input("Nome do Cliente: ")
          email = input("E-mail do Cliente: ")
          telefone = input("Telefone do Cliente: ")
          con_cliente = input("O cliente é pessoa fisica ou juridica(F/J)?:  ")
          if con_cliente.lower() == 'f' or con_cliente.lower() == "j": 
            if con_cliente.lower() == "j":
              cnpj = input("CNPJ do Cliente: ")
              clientes[cnpj] = [nome, email, telefone, con_cliente]
            else:
              cpf = input("CPF do Cliente: ")
              clientes[cpf] = [nome, email, telefone, con_cliente]
            print("Cadastro realizado com sucesso!!!")
            input("Pressione ENTER para continuar")
          else:
            print("Erro!!!")
          cadastro = input("Quer continuar? (S/N): ")
         

      # pesquisa de clientes
      
      elif respCliente == '2':
        cli_pesquisar = ''
        while cli_pesquisar.lower() != "n":
          os.system('clear')
          especifico = input("Quer ver um cliente específico (S/N)?: ")
          if especifico.lower() != "n":
              pesquisarCli = input("Digite o CPF/CNPJ do cliente: ")
              if pesquisarCli in clientes:
                print(clientes[pesquisarCli])
              else:
                print("Cliente não encontrado.")
              cli_pesquisar = input("Quer continuar? (S/N): ")
          else :
            if len(clientes) == 0:
              print("Não há clientes cadastrados.")
              cli_pesquisar = input("Quer continuar? (S/N): ")
            else:
              for cliente_id, cliente_info in clientes.items():
                print(cliente_info)
                cli_pesquisar = input("Quer continuar? (S/N): ")
      #atualização de clientes
      elif respCliente == '3':
        teste = ""
        update_resp = ""
        while update_resp != "0":
          os.system('clear')
          print("###################################################")
          print("#####     Você está no Módulo Clientes        ####")
          print("##################################################")
          print("#####      1 - Atualizar Nome                #####")
          print("#####      2 - Atualizar Email               #####")
          print("#####      3 - Atualizar Telefone            #####")
          print("#####      0 - Voltar Para o Modulo Cliente  #####")
          update_resp = input("##### Escolha sua opção: ")
  
          if update_resp == '1':
            while teste.lower() != "n":
              os.system('clear')
              update_nome = input("Digite o CPF/CNPJ do cliente: ")
              if update_nome in clientes:
                nome_update = input("Digite o novo nome: ")
                clientes[update_nome][0] = nome_update
                print("Nome atualizado com sucesso!!!")
                teste = input("Quer continuar? (S/N): ")
              else:
                print("Cliente nao encontrado ou CPF/CNPJ esta errado."	)
                teste = input("Quer continuar? (S/N): ")
          elif update_resp == '2':
            while teste.lower() != "n":
              os.system('clear')
              update_email = input("Digite o CPF/CNPJ do cliente: ")
              if update_email in clientes:
                email_atual = input("Digite o antigo email: ")
                teste = ""
                for email_atual in clientes[update_email]:
                  i = email_atual
                  email_update = input("Digite o novo email: ")
                  clientes[i]= [ email_update]
                  print("email atualizado com sucesso!!!")
                  teste = input("Quer continuar? (S/N): ")
                  if teste.lower() =="n":
                    break
              else:
                print("Cliente nao encontrado ou CPF/CNPJ esta errado."	)
                teste = input("Quer continuar? (S/N): ")
          elif respCliente == '3':
            teste = ""
            while teste.lower() != "n":
              os.system('clear')
              update_telefone = input("Digite o CPF/CNPJ do cliente: ")
              if update_telefone in clientes:
                telefone_atual = input("Digite o antigo telefone: ")
                teste = ""
                for telefone_atual in clientes[update_telefone]:
                  i = telefone_atual
                  telefone_update = input("Digite o novo telefone: ")
                  clientes[i]= [ telefone_update]
                  print("telefone atualizado com sucesso!!!")
                  teste = input("Quer continuar? (S/N): ")
                  if teste.lower() =="n":
                    break
              else:
                print("Cliente nao encontrado ou CPF/CNPJ esta errado."	)
                teste = input("Quer continuar? (S/N): ")
      #apagar cliente
      elif respCliente == '4':
        teste = ""
        while teste.lower() != "n":
          os.system('clear')
          apagar_cliente = input("Digite o CPF/CNPJ do cliente: ")
          if apagar_cliente in clientes:
            del clientes[apagar_cliente]
            print("Cliente apagado com sucesso!!!")
            teste = input("Quer continuar? (S/N): ")
          else:
            print("Cliente nao encontrado ou CPF/CNPJ esta errado."	)
            teste = input("Quer continuar? (S/N): ")
    
  elif resp == '2':
      os.system('clear')
      print()
      print("############################################")
      print("#####   Você está no Módulo Produtos    ####")
      print("############################################")
      print("#####      1 - Cadastrar Tipo de Queijo  #####")
      print("#####      2 - Receita do Queijo         #####")
      print("#####      3 - Estoque                   #####")
      print("#####      4 - Materia para Produção     #####")
      print("#####      0 - Voltar ao Menu Principal  #####")
      input("Tecle <ENTER> para continuar...")

      

      
  elif resp == '3':
      print()
      print("############################################")
      print("#####    Você está no Módulo Vendas    ####")
      print("############################################")
      print("#####     1 - Queijos Ofertados        #####")
      print("#####     2 - Quantidade de Quejios    #####")
      print("#####     3 - Informções dos Produtos  #####")
      print("#####     4 - Carrinho de Compras      #####")
      print("#####     0 - Voltar ao Menu Principal #####")
      input("Tecle <ENTER> para continuar...")
  elif resp == '4':
    print()
    print("############################################")
    print("#####  Você está no Módulo Informações  ####")
    print("############################################")
    print()
    print("##### Projeto de Gestão para uma Fábrica de Queijos   ####")
    print("##### Equipe de desenvolvimento:                      ####")
    print("##### Samuel Morais de Araujo                         ####")
    print("##### Contato:                                        ####")
    print("##### morais123samuel@gmail.com                       ####")
    print("##### Licença Pública Geral GNU                       ####")
    print("##### www.gnu.org/licenses/gpl.html                   ####")
    print()
    input("Tecle <ENTER> para continuar...")
print("")
print("Você encerrou o programa!")
print("Até logo!")

arq_cliente = open("clientes.dat", "wb")
pickle.dump(clientes, arq_cliente)
arq_cliente.close()

