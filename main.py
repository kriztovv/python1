# Úkol 1
name = input("Zadej své jméno: ")
print(f"Ahoj, {name}!")

# Úkol 2
a = float(input("Zadej první číslo: "))
b = float(input("Zadej druhé číslo: "))
print("Součet je:", a + b)

# Úkol 3
text = input("Zadej text: ")
print("Délka textu:", len(text))

# Úkol 4
word1 = input("Zadej první slovo: ")
word2 = input("Zadej druhé slovo: ")
longer = word1 if len(word1) > len(word2) else word2
print(f"Delší slovo je: {longer}")

# Úkol 5
num1 = float(input("Zadej první číslo: "))
num2 = float(input("Zadej druhé číslo: "))
if num1 > num2:
    print(f"Větší je: {num1}")
elif num1 < num2:
    print(f"Větší je: {num2}")
else:
    print("Čísla jsou stejná")

# Úkol 6
nums = [float(input("Zadej číslo: ")) for _ in range(3)]
nums.sort(reverse=True)
print("Čísla od největšího po nejmenší:", nums)

# Úkol 7
num = int(input("Zadej číslo: "))
print("Sudé" if num % 2 == 0 else "Liché")

# Úkol 8
text = input("Zadej text: ")
print("Velká písmena:", text.upper())
print("Malá písmena:", text.lower())

# Úkol 9
text = input("Zadej text: ")
if text:
    print(f"První znak: {text[0]}, Poslední znak: {text[-1]}")
else:
    print("Text je prázdný!")

# Úkol 10
text = input("Zadej text: ")
print("Obsahuje 'a'." if 'a' in text else "Neobsahuje 'a'.")

# Úkol 11
a = float(input("Zadej první číslo: "))
b = float(input("Zadej druhé číslo: "))
op = input("Zadej operaci (+, -, *, /): ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/' and b != 0:
    print(a / b)
else:
    print("Neplatná operace nebo dělení nulou")

# Úkol 12
month = int(input("Zadej číslo měsíce (1-12): "))
if month in [12, 1, 2]:
    print("Zima")
elif month in [3, 4, 5]:
    print("Jaro")
elif month in [6, 7, 8]:
    print("Léto")
elif month in [9, 10, 11]:
    print("Podzim")
else:
    print("Neplatné číslo měsíce")

# Úkol 13
word = input("Zadej slovo: ")
print("Je palindrom" if word == word[::-1] else "Není palindrom")

# Úkol 14
grade = int(input("Zadej známku (1-5): "))
grades = {1: "Výborný", 2: "Chvalitebný", 3: "Dobrý", 4: "Dostatečný", 5: "Nedostatečný"}
print(grades.get(grade, "Neplatná známka"))

# Úkol 15
text = input("Zadej text: ")
shifted = ''.join(chr(((ord(c) - 97 + 3) % 26) + 97) if 'a' <= c <= 'z' else 
                  chr(((ord(c) - 65 + 3) % 26) + 65) if 'A' <= c <= 'Z' else c for c in text)
print("Posunutý text:", shifted)

# Úkol 16
first_name = input("Zadej jméno: ")
last_name = input("Zadej příjmení: ")
nickname = (first_name[:3] + last_name[-3:]).lower()
print("Přezdívka:", nickname)
