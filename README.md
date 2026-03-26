# 🏦 SafeBank - TDD & Qualidade de Código

Este projeto simula um sistema de gestão de funcionários de uma instituição financeira, com foco total em **Desenvolvimento Orientado a Testes (TDD)**. O objetivo principal é garantir que regras de negócio sensíveis, como cálculos de bônus e decréscimos salariais, sejam implementadas com 100% de segurança.

---

## 🗂️ Estrutura do Projeto

A organização do diretório segue as melhores práticas de desenvolvimento Python:

* **`codigo/`**: Contém a lógica principal (Classes e Métodos) do sistema.
* **`tests/`**: Suite de testes unitários utilizando a biblioteca `pytest`.
* **`.coveragerc`**: Arquivo de configuração para medição da cobertura de testes.
* **`requirements.txt`**: Lista de dependências do projeto (Pytest, Coverage, etc.).
* **`venv/`**: Ambiente virtual para isolamento das dependências.

---

## 🚀 Regras de Negócio Implementadas

O sistema gerencia objetos da classe `Funcionario` com as seguintes funcionalidades:

1.  **Cálculo de Idade**: Cálculo automático baseado na data de nascimento.
2.  **Identificação de Sócios**: Validação baseada em sobrenomes específicos e faixa salarial (acima de R$ 100.000,00).
3.  **Decréscimo Salarial**: Aplicação de redução estratégica para salários de sócios.
4.  **Cálculo de Bônus**: Regra de 10% do salário, com trava de segurança que impede bônus superiores a R$ 1.000,00 (disparando exceção).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pytest**: Framework de testes.
* **Coverage.py**: Ferramenta para medir a cobertura de código pelos testes.
* **TDD**: Metodologia de desenvolvimento.

---

## 🧪 Como rodar os testes

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute os testes:**
    ```bash
    pytest
    ```

3.  **Verifique a cobertura de código:**
    ```bash
    coverage run -m pytest
    coverage report
    ```

---

## 💻 Exemplo de Uso

```python
from codigo.modelo import Funcionario

# Criando um funcionário
func = Funcionario("Felipe Beloto", "10/10/1995", 150000)

# Verificando se é sócio
print(func.indentifica_socio()) # Retorna True

# Calculando bônus (Gera exceção caso valor > 1000)
try:
    bonus = func.calcular_bonus()
except Exception as e:
    print(e)
