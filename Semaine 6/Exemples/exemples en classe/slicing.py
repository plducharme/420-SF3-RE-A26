citation = "L'erreur est humaine, mais ça prend un ordinateur pour réellement merder!"

liste_int = [x for x in range(25)]

# on utilise l'opérateur d'indexation pour faire du slicing (coupage)
# [debut:fin non-incluse: pas]
print(citation[0:10])
print(liste_int[5:20:3])

citation_inversee = citation[::-1]
print(citation_inversee)



