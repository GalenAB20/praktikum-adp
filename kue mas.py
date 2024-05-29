import os
import time
from termcolor import colored,cprint

os.system('cls')
print()
time.sleep(0.5)
head = colored("C O N G R A T S", "grey", attrs=["bold"])
head1 = colored("F O R        Y O U R", "grey", attrs=["bold"])
head2 = colored("G  R  A  D  U  A  T  I  O  N", "grey", attrs=["bold"])
print("{:<29}" "{:<16}".format(" ",head))
time.sleep(0.5)
print("{:<27}" "{:<22}".format(" ",head1))
time.sleep(0.5)
print("{:<23}" "{:<25}".format(" ",head2))
time.sleep(0.5)
tangkai1 = colored("\       /","grey")
tangkai2 = colored("\     /","grey")
print("{:<32}" "{:<9}".format(" ",tangkai1))
time.sleep(0.5)
print("{:<33}" "{:<7}".format(" ",tangkai2))
time.sleep(0.5)

print("{:<25}".format(" "),end="")
cprint("{:<23}".format(" "), "red","on_red")
time.sleep(0.5)

print("{:<25}".format(" "),end="")
cprint("{:<23}".format(" "), "white","on_white")
time.sleep(0.5)

print("{:<25}".format(" "),end="")
cprint("{:<23}".format(" "), "red","on_red")
time.sleep(0.5)

print("{:<22}".format(" "),end="")
cprint("{:<29}".format(" "), "light_red","on_light_red")
time.sleep(0.5)

print("{:<22}".format(" "),end="")
cprint("{:<29}".format(" "), "dark_grey","on_dark_grey")
time.sleep(0.5)

print("{:<22}".format(" "),end="")
cprint("{:<29}".format(" "), "light_red","on_light_red")

def print_meja():
    meja = [
        "_________________________________",
        "|||||||||||||||||||||||||||||||||",
        "_________________________________",
        "              //||\\\            ",
        "             // || \\\           ",
        "            //  ||  \\\          ",
        "           //   ||   \\\         ",
        "          //    ||    \\\        ",
        "         //     ||     \\\       ",
        "        //      ||      \\\      ",
        "       //       ||       \\\     ",
    ]

    for line in meja:
        print("{:<20}".format(" "),end="")
        print(colored(line, "black",attrs=["bold"]))


print_meja()


print()
print()
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("Note :                                            "), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("Selamat wisuda mas fathur, maaf aleng belum bisa  "), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("menghadiri wisuda mas di sana. Jadinya aleng bikin"), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("program ini sekalian untuk tugas aleng hehe."), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("Semoga ilmu yang udah didapat selama mas kuliah"), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("berguna untuk agama, keluarga, dan masyarakat, "), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("semoga dimudahkan dalam mencari kerjanya, semoga"), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("semua berjalan dengan keinginan mas. Dan yang"), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("terakhir jangan lupa doain aleng yaa untuk"), "dark_grey","on_light_yellow",attrs=["underline"])
time.sleep(3)
print("{:<11}".format(" "),end="")
cprint("{:<50}".format("kedepannya. With love from your little brother :D"), "dark_grey","on_light_yellow",attrs=["underline"])
