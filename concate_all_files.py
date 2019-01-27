filenames = []
for i in range(511):
	filenames.append(str(i) + ".txt")	
print(filenames)

with open("home/mahsa/Desktop/final_data.txt", 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
