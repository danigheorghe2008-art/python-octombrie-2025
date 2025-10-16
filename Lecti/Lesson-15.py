listaElemente = [(1, 2, 3), (4, 5, 6)]
listaNoua = list(("Nume-1", "Nume-2"))
# print("test")


def askPersonalInfo():
    while True:
        firstName = input("Input your first name:")
        lastName = input("Input your last name:")
        yearBirth = input("Input your year of birth:")
        gender = input("Input your gender (M, F):")
        if (
            firstName == ""
            or lastName == ""
            or yearBirth == ""
            or gender == ""
            or gender not in ("F", "M")
        ):
            print("Wrong data!")
        else:
            return firstName, lastName, yearBirth, gender


def functieInmultireCu2(numar):
    return numar * 2


numarNou = functieInmultireCu2(5)
# print(numarNou)


def functieFaraReturnInmultireCu2(numar):
    numar * 2


numar = functieFaraReturnInmultireCu2(7)
# print(numar)  # None


def functieFaraReturnInmultireCu2SiPrint(numar):
    numar * 2
    # print(numar * 2)


numarPrint = functieFaraReturnInmultireCu2SiPrint(8)
# print(numarPrint)  # None


def functieCuReturn(numar: int):
    return numar + numar
    numar * 3
    print("test1-2-3")


numarAdunat = functieCuReturn(9)
# print(numarAdunat)  # 18


def verificareNumarContract(numarContract: int):
    if numarContract.is_integer():
        print("Este numarul de contract bun!")
    else:
        ValueError("Nu este un numar de contract corect")


verificareaNumaruluiDeContract = verificareNumarContract(5)
print(verificareaNumaruluiDeContract)
