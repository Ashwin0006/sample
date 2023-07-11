from tabulate import tabulate

infile = open(r"Front end\data\data.txt","r")
data= [["CUSTOMER ID","NAME","MOBILE NUMBER","MAIL ID"]]

for line in infile:
    if(line != "\n"):
        line = eval(line)
        data.append(line)

table = tabulate(data, headers="firstrow", tablefmt="grid")

outfile = open(r"Front end\data\table_data.txt","w")
outfile.write(table)
