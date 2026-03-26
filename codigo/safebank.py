from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
    
    @property
    def nome (self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)
    
    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(" ")
        return nome_quebrado[-1]
    
    def indentifica_socio(self):
        lista_sobrenome = ["Silva", "Beloto", "Fafa", "Duda", "Honozin", "Leitão"]
        return self._salario >= 100000 and (self.sobrenome() in lista_sobrenome)

    def decrescimento_salario(self):
            if self.indentifica_socio():
                decrescimo = self.salario * 0.1
                self._salario = self._salario - decrescimo
     
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("Salario muito alto para ganhar bônus ")
        return valor

    def pobre_ou_nao(self):
        if self.salario <= 1000:
            return "pobre"
    
    def __str__(self) -> str:
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'