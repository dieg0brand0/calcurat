print("¡Saludos Humano!, soy la calcuratona y te ayudaré a comparar precios entre productos para encontrar la opción más conveniente.")
print("\n\tPuedo ayudarte con productos individuales o con packs de productos, a continuación escoge tu opción: \n1) Individuales.\n2) Packs.\n")
opcion = int(input("Ingresa una opción (1 / 2): "))

if opcion == 1:
    print("\tA continuación te pediré algunos datos de los productos a comparar . . .\n\n")
    elem1 = input("Dime un nombre para el primer producto a comparar: ")
    a1 = int(input("\nDime cuántos Gramos (gr) o Mililitros/Centímetros cúbicos (ml/cc) tiene el primer producto: "))
    b1 = int(input("\nDime el valor del primer producto: "))
    c = 1000
    def ded(a, b, c):
        precio = c*b/a
        return precio
    p1 = int(ded(a1, b1, c))

    elem2 = input("\n\nAhora dime un nombre para el segundo producto a comparar: ")
    a2 = int(input("\nDime cuántos Gramos (gr) o Mililitros/Centímetros cúbicos (ml/cc) tiene el segundo producto: "))
    b2 = int(input("\nDime el valor del segundo producto: "))
    p2 = int(ded(a2, b2, c))
    if p1 > p2:
        print("\nSegun mis complejos cálculos matemáticos,", elem2, " es más barato, con un valor de: $", p2, " por Litro o Kilo (según corresponda), contra $", p1, " que vale el/la ", elem1, ".")
    elif p1 == p2:
        print("\nSegun mis complejos cálculos matemáticos, ambos productos cuestan lo mismo.")
    else:
        print("\nSegun mis complejos cálculos matemáticos,", elem1, " es más barato, con un valor de: $", p1, " por Litro o Kilo (según corresponda), contra $", p2, " que vale el/la ", elem2, ".")

    print("Espero haber sido de ayuda, ¡vuelve cuando quieras!.")
elif opcion == 2:
    print("\tA continuación te pediré algunos datos de los packs a comparar . . .\n\n")
    elem1 = input("Dime un nombre para el primer pack a comparar: ")
    a1 = int(input("\nDime cuántos Gramos (gr) o Mililitros/Centímetros cúbicos (ml/cc) tiene un elemento del primer pack: "))
    b1 = int(input("\nDime el valor del primer pack: "))
    c = 1000
    d1 = int(input("\nDime cuántos productos tiene el primer pack: "))
    def pack(a, b, c, d):
        precio = (c*b)/(a*d)
        return precio
    p1 = int(pack(a1, b1, c, d1))

    elem2 = input("\n\nAhora dime un nombre para el segundo pack a comparar: ")
    a2 = int(input("\nDime cuántos Gramos (gr) o Mililitros/Centímetros cúbicos (ml/cc) tiene un elemento del segundo pack: "))
    b2 = int(input("\nDime el valor del segundo pack: "))
    d2 = int(input("\nDime cuántos productos tiene el segundo pack: "))
    p2 = int(pack(a2, b2, c, d2))
    if p1 > p2:
        print("\nSegun mis complejos cálculos matemáticos,", elem2, " es más barato, con un valor de: $", p2, " por Litro o Kilo (según corresponda), contra $", p1, " que vale el/la ", elem1, ".")
    elif p1 == p2:
        print("\nSegun mis complejos cálculos matemáticos, ambos productos cuestan lo mismo.")
    else:
        print("\nSegun mis complejos cálculos matemáticos,", elem1, " es más barato, con un valor de: $", p1, " por Litro o Kilo (según corresponda), contra $", p2, " que vale el/la ", elem2, ".")

    print("Espero haber sido de ayuda, ¡vuelve cuando quieras!.")
else:
    print("Vuelve a intentarlo con una opción váida por favor, solo puede ser 1 o 2")
