def ExC(n):
    if n == 1:
        return 1
    else:
        return ExC(n - 1) + n**2

resultado = ExC(3)
print(resultado)  
