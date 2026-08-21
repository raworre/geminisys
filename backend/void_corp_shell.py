import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess
import threading
import re
import queue
import os
import sys

# Regex to strip ANSI color codes from terminal output
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class VoidCorpShell:
    def __init__(self, root):
        self.root = root
        self.root.title("VOID_CORP // GEMINISYS_UPLINK")
        self.root.geometry("900x700")
        self.root.configure(bg="#050505")

        # VOID_CORP Styling
        self.font = ("Courier New", 12, "bold")
        self.bg_color = "#050505"
        self.fg_color = "#00FF41"
        self.highlight_color = "#008F11"
        
        # Header
        self.header = tk.Label(
            self.root, 
            text="[ VOID_CORP SECURE TERMINAL ] -- LINKED TO: ANTIGRAVITY ENGINE",
            bg=self.bg_color,
            fg=self.highlight_color,
            font=("Courier New", 10, "bold")
        )
        self.header.pack(pady=(10, 0))

        # Output Text Area
        self.output_area = ScrolledText(
            self.root, 
            bg=self.bg_color, 
            fg=self.fg_color, 
            font=self.font, 
            wrap=tk.WORD, 
            state=tk.DISABLED,
            insertbackground=self.fg_color,
            selectbackground=self.highlight_color,
            borderwidth=0,
            highlightthickness=0
        )
        self.output_area.pack(padx=20, pady=(10, 10), fill=tk.BOTH, expand=True)

        # Input Frame
        self.input_frame = tk.Frame(self.root, bg=self.bg_color)
        self.input_frame.pack(padx=20, pady=(0, 20), fill=tk.X)

        self.prompt_label = tk.Label(
            self.input_frame, 
            text="SYS_OP>", 
            bg=self.bg_color, 
            fg=self.fg_color, 
            font=self.font
        )
        self.prompt_label.pack(side=tk.LEFT)

        self.input_entry = tk.Entry(
            self.input_frame, 
            bg="#111111",
            fg=self.fg_color, 
            font=self.font, 
            insertbackground=self.fg_color,
            relief=tk.SOLID,
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.highlight_color,
            highlightcolor=self.fg_color
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))
        self.input_entry.bind("<Return>", self.send_command)
        
        self.send_button = tk.Button(
            self.input_frame,
            text="[ SEND ]",
            bg=self.bg_color,
            fg=self.fg_color,
            font=self.font,
            activebackground=self.highlight_color,
            activeforeground=self.bg_color,
            relief=tk.FLAT,
            command=lambda: self.send_command(None)
        )
        self.send_button.pack(side=tk.RIGHT)

        self.root.bind("<Button-1>", lambda event: self.input_entry.focus_set())
        self.input_entry.focus_force()

        # Message Queue for Thread-Safe GUI Updates
        self.msg_queue = queue.Queue()

        self.print_to_output("[SYSTEM] SECURE UPLINK ESTABLISHED. READY FOR TRANSMISSION.\n")

        # Start the queue checking loop
        self.root.after(50, self.process_queue)

    def process_queue(self):
        buffer = ""
        while not self.msg_queue.empty():
            buffer += self.msg_queue.get()
        
        if buffer:
            self.print_to_output(buffer, newline=False)
            
        self.root.after(50, self.process_queue)

    def print_to_output(self, text, newline=True):
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, text + ("\n" if newline else ""))
        self.output_area.see(tk.END)
        self.output_area.config(state=tk.DISABLED)

    def send_command(self, event):
        command = self.input_entry.get()
        if not command.strip():
            return
            
        self.input_entry.delete(0, tk.END)
        self.print_to_output(f"\nSYS_OP> {command}\n", newline=False)
        
        # Lock UI while waiting
        self.input_entry.config(state=tk.DISABLED)
        self.send_button.config(state=tk.DISABLED)
        
        # Fire and forget in a background thread
        threading.Thread(target=self.run_agy_command, args=(command,), daemon=True).start()

    def run_agy_command(self, command):
        env = os.environ.copy()
        env["TERM"] = "dumb"
        
        # We use agy --print "message" --continue to simulate a continuous chat
        process = subprocess.Popen(
            ["agy", "--print", command, "--continue"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            text=True,
            bufsize=1,
            env=env
        )
        
        for line in iter(process.stdout.readline, ''):
            clean_text = ANSI_ESCAPE.sub('', line)
            self.msg_queue.put(clean_text)
            
        process.wait()
        
        # Unlock UI
        self.root.after(0, lambda: self.input_entry.config(state=tk.NORMAL))
        self.root.after(0, lambda: self.send_button.config(state=tk.NORMAL))
        self.root.after(0, lambda: self.input_entry.focus_set())

if __name__ == "__main__":
    root = tk.Tk()
    app = VoidCorpShell(root)
    root.mainloop()
