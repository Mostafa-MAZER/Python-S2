import sys
def infos_python():
    return sys.version, sys.platform
print(infos_python())

def arguments_programme():
    return sys.argv
print(arguments_programme())


def somme_arguments():
    s=0
    for arg in sys.argv[1:]:
        s+=int(arg)
    return s
print(somme_arguments())