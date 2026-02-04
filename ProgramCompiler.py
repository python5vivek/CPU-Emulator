class ProgramCompiler:
    def __init__(self):
        Programs = open("program.txt","r")
        Instructions = Programs.read()
        Programs.close()
        self.ListOfInstructions = Instructions.splitlines()
        self.instructions = []
    def Compile(self):
        for line in self.ListOfInstructions:
            words = line.split()
            
            if words[0] == "add" or words[0] == "minus" or words[0] == "multiply" or words[0] == "divide":
                self.instructions.append(words)
            if words[0] == "load":
                self.instructions.append([words[0],words[1],int(words[2])])
            if words[0] == "jump":
                self.instructions.append([words[0],int(words[1])])
