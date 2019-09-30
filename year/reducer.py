input_reducer = open("output_mapper.txt","r") # Opening data file(output_mapper) in read only mode
output_reducer = open("output_reducer.txt", "w")  # Opening output_reducer file in write mode (It will create file if file doesnot exist)
lines = input_reducer.readlines() # Reading each line from data and placing it in array
lines.sort() # sorting the array
dict = {} # creating an empty dictionary
# reading each line from array
for line in lines:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    year = data[0] # Assigning data to variable
    suicide_no = float(data[1]) # Assigning data to veriable
    # If-Else statement for adding number of suicides to particular year
    if year in dict.keys():
        dict[year] = dict[year] + suicide_no
    else:
        dict[year] = 1
# Loop for readng dictionary 
for key,value in dict.items():
    # writing year and total number of suicide in output file
    output_reducer.write("Year: "+key+","+"Total number of suicides: "+str(value) +"\n")
    # Writing year and total number of suicides to console
    print("Year: "+key+","+"Total number of suicides: "+str(value) +"\n")
# Closing all files
input_reducer.close()
output_reducer.close()