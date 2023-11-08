from Programm import *
from ProgrammiInfo import *

def main():
    AlgOlek = VõtaOlek()
    programm = Programm(AlgOlek)
    LõppOlek = programm.JaaaaLäks()
    SalvestaOlek(LõppOlek)

main()