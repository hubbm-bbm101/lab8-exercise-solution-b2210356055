import sys
class IsimBulunamadiHatasi(Exception):pass

try:
    studentsFile = open("students.txt", "r")
    students = {line.replace("\n", "").split(":")[0]: tuple(line.replace("\n", "").split(":")[1].split(",")) for line in studentsFile.readlines()}
    studentsFile.close()
    names=sys.argv[2].split(",")
    for name in names:
        if not(name in students.keys()):
            raise IsimBulunamadiHatasi(f"{name} bulunamadı")
        print(f"{name} : {students[name][0]} , {students[name][1]}")
except IOError:
    print("ERROR: IOError !! students.txt dosyasını bulamıyorum!!!")
except IsimBulunamadiHatasi as hata:
    print(f"ERROR: IsimBulunamadiHatasi !! {hata}")