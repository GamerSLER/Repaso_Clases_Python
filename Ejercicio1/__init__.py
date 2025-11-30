# edad = input("edad: ")
# try:
#     if isinstance(edad, float):
#         raise ValueError("Edad tiene decimal, debe ser entera")
#     try:
#         edad = int(edad)
#     except ValueError as e:
#         raise ValueError("Edad tiene que ser entera")
# except ValueError as e:
#     print(e)

try:
    if not isinstance(, int):
        raise ValueError("Edad debe ser entero.")
except ValueError as e:
    print(e)
