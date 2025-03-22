def writesome(list_of_elements):
    with open("menin_faylym.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text += str(i) + ' '
        f.write(text)
        f.close()

writesome([14974, 56734989, "fsno", 634295,"dfdba",568])