input = open("toy_dataset.csv", "r")
output = open("01.txt", "w")

for line in input:
    print(line)
    datalist = line.strip().split(",")
    
    
    Number, City, Gender, Age, Income, Illness = datalist

    

    output.write(Gender + "\t" + "1"+ "\n")

input.close()
output.close()