input("Введите сообщение: ")

exmassage = "google_san_francisco.txt\ngoogle_uar.txt\ngoogle_paris.txt\n"
exmassage += "Выберте офис Google из выше перечисленных: "
inmassage = input(exmassage)

direction = "/home/manas/Desktop/task/task4/"

if inmassage =="google_san_francisco.txt":
    direct = direction + inmassage
    with open(direct, "w") as claim:
        msgs_f = input("Чем мы можем помочь? ") 
        claim.write(msgs_f)

# остальные блоки кода создаются аналогичным образом через 
# elif - elif 