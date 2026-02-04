class Registers:
    def __init__(self):
        self.rs = {
            "r1":0,
            "r2":0,
            "r3":0,
            "r4":0,
            "r5":0,
            "r6":0,
            "r7":0,
            "r8":0,
        }
    def register(self , address,value):
        self.rs[address] = value
    def clearall(self):
        self.rs = {
            "r1":0,
            "r2":0,
            "r3":0,
            "r4":0,
            "r5":0,
            "r6":0,
            "r7":0,
            "r8":0,
        }
    def __call__(self, address, *args, **kwds):
        return self.rs[address]

class ALU:
    def __init__(self):
        self.state = "Nan"
    def Add(self,A,B):
        self.state = "Add"
        return A + B
    def minus(self,A,B):
        self.state = "Minus"
        return A - B
    def multiply(self,A,B):
        self.state = "Multiply"
        return A * B
    def division(self,A,B):
        self.state = "Devision"
        return A//B

class ProgramCounter:
    def __init__(self):self.Count = 0
    def step(self):self.Count += 1
    def get(self):return self.Count
    def clear(self): self.Count = 0
    def setC(self,n):self.Count = n

class ControlUnit:
    def __init__(self,r:Registers,a:ALU,c:ProgramCounter):
        self.Register = r
        self.ALU = a
        self.Counter = c
    def perform(self,instruction):
        if instruction[0] == "add":
            a = self.Register.rs[instruction[2]]
            b = self.Register.rs[instruction[3]]
            result = self.ALU.Add(a,b)
            self.Register.register(instruction[1],result)
            self.Counter.step()
        if instruction[0] == "minus":
            a = self.Register.rs[instruction[2]]
            b = self.Register.rs[instruction[3]]
            result = self.ALU.minus(a,b)
            self.Register.register(instruction[1],result)
            self.Counter.step()
        if instruction[0] == "multiply":
            a = self.Register.rs[instruction[2]]
            b = self.Register.rs[instruction[3]]
            result = self.ALU.multiply(a,b)
            self.Register.register(instruction[1],result)
            self.Counter.step()
        if instruction[0] == "divide":
            a = self.Register.rs[instruction[2]]
            b = self.Register.rs[instruction[3]]
            result = self.ALU.division(a,b)
            self.Register.register(instruction[1],result)
            self.Counter.step()
        if instruction[0] == "load":
            self.Register.register(instruction[1],instruction[2])
            self.Counter.step()
        if instruction[0] == "jump":
            self.Counter.setC(instruction[1])