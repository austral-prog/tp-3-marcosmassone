def check_vowels():
    # Código a implementar utilizando input.
    # Para verificar este ejercicio ejecutar el comando
    # `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

    nombre = input("Inserte tu nombre: ")

    nombre_low = nombre.lower()

    print("Contiene a:" , "a" in nombre_low)

    print("Contiene e:" , "e" in nombre_low)

    print("Contiene i:" , "i" in nombre_low)

    print("Contiene o:" , "o" in nombre_low)

    print("Contiene u:" , "u" in nombre_low)

slice advanced !!!!!!!

def slice_advanced():
    # Código a implementar utilizando input.
    # Para verificar este ejercicio ejecutar el comando
    # `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
    txt = input ()
    print(txt[4: :2])
