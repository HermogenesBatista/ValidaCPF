class ValidCPF:

    def __init__(self, cpf):
        self.cpf = cpf

    def reorgCPF(self):
        self.cpf = self.cpf.split("-")
        self.cpf[0] = self.cpf[0].replace(".","")

        return self

    def validCPF(self):
        invalidos = ['000.000.000-00','111.111.111-11','222.222.222-22','333.333.333-33','444.444.444-44',
                     '555.555.555-55','666.666.666-66','777.777.777-77','888.888.888-88','999.999.999-99']

        if(self.cpf in invalidos):
            return False
        self.reorgCPF()
        
        peso = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0

        for i, item in enumerate(self.cpf[0]):
            #print(item)
            soma += int(item)*peso[i]


        #print(soma)
        dig1 = soma % 11

        if(dig1<2):
            digit1 = '0'
        else:
            digit1 = str(11-dig1)

        #print('primeiro digito',digit1, self.cpf[1])

        if(digit1 != self.cpf[1][0]):
            return False

        peso.insert(0,11)

        soma = 0

        for i, item in enumerate(peso):
            

            if(i<len(self.cpf[0])):
                soma += item * int(self.cpf[0][i])
                #print(item, int(self.cpf[0][i]))
            else:
                soma += item * int(digit1)
                #print(item, digit1)

        dig2 = soma % 11

        #print('Digito 2: resto e nums',dig2, self.cpf[1])

        if(dig2<2):
            digit2 = "0"
        else:
            digit2 = str(11-dig2)

        #print(digit1+digit2, self.cpf[1])

        if(digit1+digit2 != self.cpf[1]):
            return False

        return True

if __name__ == "__main__":
    n = ValidCPF('999.999.999-99')
    if(n.validCPF()):
        print("Válido!")
    else:
        print("Inválido!")
