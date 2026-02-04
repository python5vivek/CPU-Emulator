import customtkinter as ctk
import CPU
import ProgramCompiler

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class CPU_UI(ctk.CTk):

    def __init__(self, cpu, compiler):
        super().__init__()

        self.cpu = cpu
        self.compiler = compiler
        self.running = False

        self.title("8-bit CPU Emulator")
        self.geometry("520x500")
        self.resizable(False, False)

        # ===== REGISTERS =====
        reg_frame = ctk.CTkFrame(self)
        reg_frame.pack(padx=20, pady=15, fill="x")

        reg_title = ctk.CTkLabel(reg_frame, text="REGISTERS", font=("Consolas", 18, "bold"))
        reg_title.pack(pady=5)

        self.reg_labels = {}

        grid = ctk.CTkFrame(reg_frame)
        grid.pack(pady=5)

        for i, r in enumerate(self.cpu.Register.rs):
            label = ctk.CTkLabel(
                grid,
                text=f"{r}: 0",
                font=("Consolas", 16),
                width=120,
                anchor="w"
            )
            label.grid(row=i // 2, column=i % 2, padx=10, pady=5)
            self.reg_labels[r] = label

        # ===== CPU STATE =====
        state_frame = ctk.CTkFrame(self)
        state_frame.pack(padx=20, pady=10, fill="x")

        self.pc_label = ctk.CTkLabel(state_frame, text="PC: 0", font=("Consolas", 16))
        self.pc_label.pack(anchor="w", padx=10, pady=3)

        self.alu_label = ctk.CTkLabel(state_frame, text="ALU: None", font=("Consolas", 16))
        self.alu_label.pack(anchor="w", padx=10, pady=3)

        self.inst_label = ctk.CTkLabel(
            state_frame,
            text="INST: ---",
            font=("Consolas", 15),
            wraplength=460,
            justify="left"
        )
        self.inst_label.pack(anchor="w", padx=10, pady=6)

        # ===== CONTROLS =====
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=15)

        self.step_btn = ctk.CTkButton(btn_frame, text="STEP", width=100, command=self.step)
        self.step_btn.grid(row=0, column=0, padx=10)

        self.run_btn = ctk.CTkButton(btn_frame, text="RUN", width=100, command=self.run)
        self.run_btn.grid(row=0, column=1, padx=10)

        self.reset_btn = ctk.CTkButton(btn_frame, text="RESET", width=100, command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=10)

        self.update_ui()

    # ===== CPU EXECUTION =====
    def step(self):
        pc = self.cpu.Counter.get()
        if pc >= len(self.compiler.instructions):
            return

        instr = self.compiler.instructions[pc]
        self.cpu.perform(instr)
        self.update_ui()

    def run(self):
        if not self.running:
            self.running = True
            self.run_loop()

    def run_loop(self):
        if not self.running:
            return

        self.step()
        self.after(700, self.run_loop)

    def reset(self):
        self.running = False
        self.cpu.Register.clearall()
        self.cpu.Counter.clear()
        self.cpu.ALU.state = "None"
        self.update_ui()

    # ===== UI UPDATE =====
    def update_ui(self):
        for r, lbl in self.reg_labels.items():
            lbl.configure(text=f"{r}: {self.cpu.Register.rs[r]}")

        self.pc_label.configure(text=f"PC: {self.cpu.Counter.get()}")
        self.alu_label.configure(text=f"ALU: {self.cpu.ALU.state}")

        pc = self.cpu.Counter.get()
        if pc < len(self.compiler.instructions):
            instr = self.compiler.instructions[pc]
            self.inst_label.configure(text=f"INST: {' '.join(map(str, instr))}")
        else:
            self.inst_label.configure(text="INST: ---")


