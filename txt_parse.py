csv_file = # csv input filename here

with open(csv_file, "r") as in_file:
    firstline = in_file.readline()
    for line in in_file:
        with open((line.split(",")[0] + ".txt"), "w") as out_file:
            line_list = (line.split(",", 1)[1:])
            line_str = ""
            for i in range(len(line_list)):
                line_str += line_list[i] + " "
            line_str = line_str.replace('"', '')
            out_file.write(line_str)
