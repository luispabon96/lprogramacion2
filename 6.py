print "Cantidad de euros"
euros = float(raw_input())
print "Intereses"
intereses = float(raw_input())
print "Anios"
anios = raw_input()
vueltas = 0
capital = 0
while vueltas < int(anios):
    vueltas = vueltas +1
    intereses_anual = euros * intereses / 100
    euros += intereses_anual
    print "Ganancias por anios " + str(intereses_anual) + " Capital = " + str(euros)
    pass
