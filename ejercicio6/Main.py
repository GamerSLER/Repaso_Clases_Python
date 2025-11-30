from functools import reduce

from ejercicio6.User import User, Activity

users = []
try :
    usr1 = User("Pepe", "pepegmail.com", 19)
    usr2 = User("  A", "santimago@gmail.com", 22)
    usr3 = User("413", "num@gmail.com", 0)
    usr4 = User("Palda", "@.", 7)

    Felipe = User("Felipe", "felipeParra@gmail.com", 21)
    Rafael = User("Rafael", "ManinLoco@gmail.com", 22)
    Santi = User("Santiago", "Santimago@gmail.com", 22)
    Rafael.desactivate()
    users.append(Felipe)
    users.append(Rafael)
    users.append(Santi)
    print("")
    for usr in users:
        print(usr)
except ValueError as e:
    print(e)

print("")

actividades = []
try:
    act1 = Activity("asd", "compra", 19)
    act2 = Activity(usr2, "pelota", 31)
    act3 = Activity(usr3, "visita", -1)

    act4 = Activity(Felipe, "login", 21)
    act5 = Activity(Rafael, "comentario", 3)
    act6 = Activity(Santi, "visita", 10)
    print("")
    actividades.append(act4)
    actividades.append(act5)
    actividades.append(act6)
    for act in actividades:
        print(act)
except ValueError as e:
    print(e)


solo_activos = list(filter(lambda usr: usr.get_active(), users))
print("")
print("Activos: ")
for act in solo_activos:
    print(f"\t{act}")

solo_durations = list(map(lambda act: act.get_duration(), actividades))
for duration in solo_durations:
    print(f"duración: {duration}")

suma_durations = reduce(lambda cont, act:cont + act.get_duration(), actividades, 0)
print(f"total duraciónes: {suma_durations}")