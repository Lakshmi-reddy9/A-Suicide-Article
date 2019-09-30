input_mapper = open("../dataset/master.txt","r") # Opening data file in read-only mode 
output_mapper = open("output_mapper.txt","w") # Opening output_mapper file in write mode (It will create file if file doesnot exist)
# For loop for reading each line from the text file
for line in input_mapper:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    # Checking the size of array
    if (len(data) == 12):
        # Assigning data to different variables
        country, year, sex, age, suicides_number, population, suicides_per_pop, country_year, hdi_per_year, gdp_per_year, gdp_per_captal, generation = data
        # Writing sex and suicides_number to output file
        output_mapper.write(sex+","+suicides_number+"\n")
        # printing sex and suicides_number to console
        print(sex+","+suicides_number+"\n")
# Closing all files
input_mapper.close()
output_mapper.close()