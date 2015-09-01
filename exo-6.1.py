#1 miles = 1609 mètres

print("entres un distance en miles par heure", end=" ")

distance = float(input())
mph = distance
mps = distance * 1609/3600
kmh = distance * 1.609

print( distance , "est egale a " , mps , "m/sec ou " , kmh , "km/h" )
