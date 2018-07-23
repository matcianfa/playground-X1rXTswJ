texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at accumsan nisl, ac aliquet tellus. Sed maximus leo lacus, nec pulvinar purus maximus vel. Morbi sagittis suscipit risus, sed luctus metus bibendum vitae. Sed ac odio dignissim, efficitur ipsum eu, imperdiet ante. Sed eu lobortis nulla, placerat fermentum purus. Cras sollicitudin metus et imperdiet condimentum. Nulla a sapien sollicitudin nunc tincidunt interdum. Praesent elementum dolor id lacus lacinia, eu viverra arcu molestie. In nec neque ac ligula posuere gravida. Nulla maximus augue in consequat viverra. Integer euismod nibh a elit ullamcorper venenatis. In egestas, urna quis congue aliquam, risus lacus mollis nibh, sed venenatis dui lorem sed eros. Aliquam erat volutpat. Sed sagittis quam sed vestibulum ultricies. Cras sit amet efficitur nunc. Pellentesque mattis fermentum dui, finibus sagittis lacus sollicitudin quis. Praesent luctus pharetra nunc, vitae commodo ante laoreet sed. Sed eu lectus lectus. Nam luctus nisi quis porta fringilla. Quisque a tempus lectus. Cras at mauris tincidunt, volutpat eros vel, venenatis urna. Integer et tellus ut dui vulputate interdum ut id nunc."

compteur=0
for car in texte:
    if car in "aeiouyAEIOUY" : 
        compteur += 1
        
print(compteur)




# --------------------------------------------------------------------
# Solution en une ligne

print(sum([texte.lower().count(v) for v in "aeiouy"]))
