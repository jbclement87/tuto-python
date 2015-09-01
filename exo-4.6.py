nbsecondes = 56894658
année = nbsecondes // (365*24*3600)
nbsecondes = nbsecondes % (365*24*3600)
mois =  nbsecondes // (30*24*3600)
nbsecondes = nbsecondes % (30*24*3600)
jours = nbsecondes // (24*3600)
nbsecondes = nbsecondes % (24*3600)
heures = nbsecondes // 3600
nbsecondes = nbsecondes % 3600
min = nbsecondes // 60
nbsecondes = nbsecondes % 60
sec = nbsecondes
print (année ,"année ", mois , "mois ",  jours , "jours " , heures, "heures ",  min , "mins " , sec ,"secs ")



