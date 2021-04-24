#open input file to read input
in1_file =open("sample_input.txt","r")
#open output file to write output
out1_file = open("sample_output.txt","w+")
goodies={}
out1_list=[]
#reading input file 
for f in in1_file:
    index_toRead_price=f.index(":")
    print(f[index_toRead_price+1:].strip())
    print(f[:index_toRead_price])
    goodies[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()
print(goodies) 
single_prices=list(goodies.values())


single_prices=[int(i)for i in single_prices]
#sorted list in decsending order to get prices to be distributed in order
single_prices.sort(reverse=True)
print(single_prices)
#taking inputs
num_of_employees=int(input("Enter number of employees: "))
length_considered=(len(single_prices)-num_of_employees)

print(length_considered)

#finding minimum difference between highest and lowest
for i in range(length_considered):
    max_price=single_prices[i]
    min_price=single_prices[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=single_prices[idx_choosen:num_of_employees+idx_choosen]
#differnce between high and low price
diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

count=0
for key,value in goodies.items():
    single_prices[count]
    print(value)
    if int(value)in choosen_prices and count<num_of_employees:
        str1=key+": "+value
        #preparing  list for output
        out1_list.append(str1)
        count+=1
        print(str1)
#writing to output file
out1_file.write("The goodies selected for distribution: ")

out1_file.write("\n")

for i in out_list:
    out1_file.write(i)
    out1_file.write("\n")
out1_file.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(diff))

in1_file.close()
out_file.close()
