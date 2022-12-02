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
            single_elf.append(line)

    f.close()
    return elves_data

cleaned_data = file_reader()
