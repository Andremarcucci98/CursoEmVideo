def vogal(parametro):
    if parametro in 'aeiouAEIOU':
        return True
    else:
        return False


print(vogal(str(input('Digite uma vogal: '))))