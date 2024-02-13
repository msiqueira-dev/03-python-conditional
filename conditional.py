# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python
#   Esse é um exemplo de um programa em Python que ensina condicionais
# EN: 
#   This is a comment and will be ignored by Python.
#   This is an example of a Python program that teachs conditionals

CONST_GRADE_APPROVED = 5

def find_average_grade(grade1, grade2, grade3):
    """ 
        PT-BR:
            Isso é um comentário padrão de funções e será ignorado pelo Python
            Essa função serve para calcular a média a partir de 3 notas fornecidas por parâmetro
        EN: 
            This is a function comment and will be ignored by Python.
            This function serves the porpuse of calculating the average from from 3 given grades
    """
    average = (grade1 + grade2 + grade3) / 3
    return average

def verify_approved(grade1, grade2, grade3):
    """ 
        PT-BR: 
            Isso é um comentário padrão de funções e será ignorado pelo Python
            Essa função recebe 3 notas, e chama a função find_average_grade que calcula a média de 3 notas, 
            e então com o resultado retornado e armazenado nao variavel average do calculo da média, ela verifica 
            se a media é maior ou igual a 5, caso seja, retorna a string (text) Approved (Aprovado), 
            caso não retorna a string (texto) Failed (reprovado).
        EN: 
            This is a function comment and will be ignored by Python.
            This function receives 3 grades, and them calls the function find_average_grade that finds the average of the 3 give grades,
            and them it will receive the returned result in the variable average, and after it will check if the average value 
            is equal or higher than 5, if it is, it will return the string (text) Approved, 
            if it is less than 5 it will return the string (text) Failed.
    """
    average = find_average_grade(grade1, grade2, grade3)
    if average >= CONST_GRADE_APPROVED:
        return "Approved"
    else:
        return "Failed"

print(verify_approved(6, 6, 6))
print(verify_approved(4, 4, 4))
print(verify_approved(5, 5, 5))
print(verify_approved(4, 4, 8))