q = open('Xenopus_laevis_genoom.fasta', 'r')
f = q.readlines () [1:]
#Open een fasta bestand en stop deze in een tijdelijke variable "f"

seq = " "
#Maak een lege variable aan die "seq" heet

for line in f:
    seq = seq + line
#Dit is een for loop die het bestand regel voor regel in de variable stopt

aantalg = int(seq.count("G"))
aantala = int(seq.count("A"))
aantalt = int(seq.count("T"))
aantalc = int(seq.count("C"))
#string.count(" ") telt automatisch alles wat je tussen de " " stopt

print("Aantal keer G",  aantalg)
print("Aantal keer A",  aantala)
print("Aantal keer T",  aantalt)
print("Aantal keer C",  aantalc)
#Print de hoeveelheid A, C, T, G die je getelt hebt

print("Aantal keer G en C", aantalg + aantalc)
#Print het aantal G en C

print("Aantal nucleotide in de sequentie", aantalg + aantalc + aantala +aantalt)
#Print het aantal nucleotiden in de sequentie

print("Percentage GC in de sequentie is:", ((aantalg + aantalc) / (aantalg + aantalc + aantala + aantalt) * 100, "%"))
#Print het GC% uit de sequentie
