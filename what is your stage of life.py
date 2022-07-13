while True:
    nome_pessoa=input('Nome da pessoa:')
    idade_pessoa = int(input('Digite a idade da pessoa: '))

    if idade_pessoa != 0:
        fase = 0
        if idade_pessoa < 9:
            fase= ' Criança'
        elif 9 <= idade_pessoa < 12:
            fase = ' Pré-adoslecência'
        elif 12 <= idade_pessoa < 18:
            fase = ' Adoslecência'
        elif 18 <= idade_pessoa < 30:
            fase = ' Jovem-adulto'
        elif 30 <= idade_pessoa < 50:
            fase = ' Adulta'
        elif idade_pessoa >= 50:
            fase= 'Idoso'

        print(f'O cidadão {nome_pessoa} tem {idade_pessoa:.1f} anos e se encontra na fase da vida:{fase}')
