input_file = open("project2_group_4_p1_mc.txt","r")
output_file = open("project2_group_4_p1_asm.txt","w")

output_file.write("Disassembling Machine Code from Program 1...\n \n")

for line in input_file:
    if (line[1:8] == "1111100"):
        output_file.write("XorR2R1              // R2 = R2 XOR R1 \n")

    elif (line[1:8] == "1111101"):
        output_file.write("AndR3                // R3 AND 1 \n")

    elif (line[1:8] == "1111001"):
        output_file.write("ShiftR               // R2 >> \n")

    elif (line[1:8] == "1111000"):
        output_file.write("ShiftL               // R2 << \n")

    elif (line[1:5] == "1110"):
        register = str(int(line[5:7],2))
        immediate = str(int(line[7],2))
        output_file.write("Init R" + register + ", " + immediate)
        output_file.write("         // R" + register + " = " + immediate + "\n")

    elif (line[1:4] == "110"):
        register1 = str(int(line[4:6],2))
        register2 = str(int(line[6:8],2))
        output_file.write("SltR1 R" + register1 + ", R" + register2)
        output_file.write("         // if R" + register1 + " < R" + register2 + ", R1 = 1 \n")

    elif (line[1:4] == "011"):
        register1 = str(int(line[4:6],2))
        register2 = str(int(line[6:8],2))
        output_file.write("Store R" + register1 + ", (R" + register2 + ")")
        output_file.write("         // M[R" + register2 + "] <- R" + register1 + "\n")

    elif (line[1:4] == "010"):
        register1 = str(int(line[4:6],2))
        register2 = str(int(line[6:8],2))
        output_file.write("Load R" + register1 + ", (R" + register2 + ")")
        output_file.write("         // R" + register1 + " <- M[R" + register2 + "] \n")

    elif (line[1:4] == "001"):
        register1 = str(int(line[4:6],2))
        register2 = str(int(line[6:8],2))
        output_file.write("Sub R" + register1 + ", R" + register2)
        output_file.write("         // R" + register1 + " = R" + register1 + " - R" + register2 + "\n")

    elif (line[1:4] == "000"):
        register1 = str(int(line[4:6], 2))
        register2 = str(int(line[6:8], 2))
        output_file.write("Add R" + register1 + ", R" + register2)
        output_file.write("         // R" + register1 + " = R" + register1 + " + R" + register2 + "\n")

    elif (line[1:6] == "10000"):
        register = str(int(line[6:8], 2))
        output_file.write("Jump R" + register)
        output_file.write("         // PC = PC - R" + register + "\n")

    elif (line[1:6] == "10101"):
        register = str(int(line[6:8], 2))
        output_file.write("bezR1, R" + register)
        output_file.write("         // if R1 ==0: PC = PC + R" + register + " | else: PC++ \n")
