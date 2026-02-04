import tkinter as tk
import CPU
import ProgramCompiler
from UI import CPU_UI

compileC = ProgramCompiler.ProgramCompiler()
compileC.Compile()

Register = CPU.Registers()
PC = CPU.ProgramCounter()
ALU = CPU.ALU()
CU = CPU.ControlUnit(Register, ALU, PC)

ui = CPU_UI(CU, compileC)
ui.mainloop()
