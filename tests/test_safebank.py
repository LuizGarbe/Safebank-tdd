from codigo.safebank import Funcionario
import pytest
# from pytest import mark

class TestClass:
    def test_quando_calcular_idade_receber_13_03_2000_retorna_como_resposta_22(self):
        # Dado
        entrada = "13/03/2000"
        esperado = 24

        # Quando
        teste_nome_funcionario = Funcionario("Test", entrada, 1111)
        resultado = teste_nome_funcionario.idade()

        # Então
        assert resultado == esperado

    def test_quando_obter_sobrenome_recebe_cleber_silva_retorna_como_resposta_Silva(self):
        # Dado
        entrada = "Cleber Silva"
        esperado = "Silva"

        # Quando
        teste_sobrenome = Funcionario(entrada, "13/03/2000", 1111)
        resultado = teste_sobrenome.sobrenome()

        # Então
        assert resultado == esperado

    def test_decrescimo_salarial_recebe_100000_retorna_como_resposta_90000_dos_diretores_da_empresa(self):
        # Dado
        entrada_nome_diretor = "Cleber Silva"
        entrada_salario = 100000
        esperado = 90000

        # Quando
        teste_funcionario = Funcionario(entrada_nome_diretor, "13/03/2000", entrada_salario)
        teste_funcionario.decrescimento_salario()
        resultado = teste_funcionario.salario

        # Então
        assert resultado == esperado

    # @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_retorna_como_resposta_100(self):
        # Dado
        entrada = 1000
        esperado = 100

        # Quando
        teste_funcionario = Funcionario("Lucas", "13/03/2000", entrada)
        resultado = teste_funcionario.calcular_bonus()

        # Então
        assert resultado == esperado

    # @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_retorna_como_resposta_exception(self):
        # Dado
        with pytest.raises(Exception):
            entrada = 1000000

            # Quando
            funcionario = Funcionario("Lucas", "13/03/2000", entrada)
            funcionario.calcular_bonus()

    def test_quando_receber_salario_menor_que_1000_retorna_pobre(self):
        entrada = 1000
        esperado = "pobre"

        teste_funcionario = Funcionario("Lucas", "13/03", entrada)
        resultado = teste_funcionario.pobre_ou_nao()

        assert resultado == esperado