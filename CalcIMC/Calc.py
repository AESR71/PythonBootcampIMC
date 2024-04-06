def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def main():
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: "))
            estatura = float(input("Ingrese su estatura en metros: "))
            if peso <= 0 or estatura <= 0:
                raise ValueError("El peso y la estatura deben ser mayores que cero.")
            break
        except ValueError:
            print("Por favor, asegúrese de ingresar cifras válidas para el peso y la estatura.")

    imc = calcular_imc(peso, estatura)
    print("Su índice de masa corporal (IMC) es:", imc)

if __name__ == "__main__":
    main()