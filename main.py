def file_reader():
    f = open("input.txt", "r")
    elves_data = []

    raw_dat = f.readlines()

    single_elf = []

    for line in raw_dat:
        if line == "\n":
            elves_data.append(single_elf)
            single_elf = [] 
        else:
            line = line.strip()
            single_elf.append(int(line))

    f.close()
    return elves_data

def get_highest_elf(data_list):
    highest = 0 
    
    for item in data_list:
        total = sum(item)
        if total > highest:
            highest = total 
    
    return highest
     
cleaned_data = file_reader()
highest_value = get_highest_elf(cleaned_data)

print(f"The highest calorie count is: {highest_value}")