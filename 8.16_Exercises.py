

fhand = open("mbox-short.txt")
for line in fhand:
    if not line.startswith("From:"): continue
    else: line_splitted = 
