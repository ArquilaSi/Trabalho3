doadores = []
alimentos = []

while True:
    print('------Obra Social------')
    print('1- Cadastrar doador')
    print('2- Cadastrar alimento')
    print('3- Informações / Check-in')
    opcao = input('Escolha a opção desejada: ')

    if opcao == "1":
        doador = {
            'Nome': input('Nome do doador: '),
            'Data da entrega': input('Data da entrega: '),
            'Responsável': input('Quem é o responsável? '),
            'Receptor': input('Nome e endereço do receptor: '),
            'Checkin': 'Pendente'
        }

        doadores.append(doador)
        print('Doador cadastrado com sucesso!\n')

    elif opcao == "2":
        alimento = {
            'Tipo de alimento': input('Qual é o tipo de alimento? '),
            'Validade': input('Qual é a data de validade? ')
        }

        alimentos.append(alimento)
        print('Alimento cadastrado com sucesso!\n')

    elif opcao == "3":
        print('\n----- Dados dos Doadores -----')
        for i, doador in enumerate(doadores, start=1):
            print(f'\nDoador {i}')
            print('Nome:', doador['Nome'])
            print('Data da entrega:', doador['Data da entrega'])
            print('Responsável:', doador['Responsável'])
            print('Receptor:', doador['Receptor'])
            print('Checkin atual:', doador['Checkin'])

            checkin = input('A cesta foi entregue? (Sim/Não): ')
            if checkin.lower() == 'sim':
                doador['Checkin'] = 'Foi entregue'
            else:
                doador['Checkin'] = 'Não foi entregue'

        print('\n----- Alimentos Arrecadados -----')
        for i, alimento in enumerate(alimentos, start=1):
            print(f'\nAlimento {i}')
            print('Tipo de alimento:', alimento['Tipo de alimento'])
            print('Validade:', alimento['Validade'])

        print('\nSaindo...')
        break

    else:
        print('Opção inválida. Digite uma opção válida!\n')