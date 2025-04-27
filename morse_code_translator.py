import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import winsound
import time

class GUI_MorseC(tk.Tk):
     def __init__(self):
        super().__init__()
        self.title("Morse Code Translator")       
        self.morse_code = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.', 'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
        'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---', 'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--', 'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-', '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', '@': '.--.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', " ": "/", ":":"---···", "\n": "\n"
        }
        self.translation=[]
        self.ui_setup()
        self.mainloop()

     def ui_setup(self):
           buttons_frame=tk.Frame(self)
           buttons_frame.pack(padx=6, pady=6)     
           encrypt_button=tk.Button(buttons_frame, text="Encrypt", font=("Times New Roman", 12, "bold"), command=self.encrypt_text)
           encrypt_button.pack(padx=5, pady=5, side=tk.LEFT)           
           clear_button=tk.Button(buttons_frame, text="Clear", font=("Times New Roman", 12, "bold"), command=lambda : self.text_field.delete(1.0, tk.END))
           clear_button.pack(padx=5, pady=5, side=tk.RIGHT)
           decrypt_button=tk.Button(buttons_frame, text="Decrypt", font=("Times New Roman", 12, "bold"), command=self.decrypt_text)
           decrypt_button.pack(padx=5, pady=5, side=tk.LEFT)
           self.sound_button=tk.Button(buttons_frame, text="Sound", font=("Times New Roman", 12, "bold"), command=self.play_sound, state="disabled")
           self.sound_button.pack(padx=5, pady=5, side=tk.RIGHT)
           prompt_label=tk.Label(self, text="Encrypt/Decrypt Text...", font=("Times New Roman", 14, "bold"))
           prompt_label.pack(padx=5, pady=5)
           self.text_field=scrolledtext.ScrolledText(self, font=("Times New Roman", 10, "bold"), width=60, height=12)
           self.text_field.pack(padx=20, pady=14)
          

     def encrypt_text(self):
        encrypted_txt=self.text_field.get(1.0,tk.END)
        if encrypted_txt[-1]=='\n':
            encrypted_txt=encrypted_txt[:-1]
        unsupported_chars=[] 
        for char in encrypted_txt:
             if char.upper() in self.morse_code.keys():
                  self.translation.append(self.morse_code[char.upper()])
             else:
                  unsupported_chars.append(char)     
        if unsupported_chars:
             messagebox.showwarning("Warning", f"Following character(s) are not supported: {", ".join(repr(c) for c in unsupported_chars)}")
        else:
            self.text_field.delete(1.0, tk.END) 
            self.text_field.insert(1.0, " ".join(self.translation))
            self.sound_button.config(state="normal")
        self.translation.clear()    

     def decrypt_text(self):
        self.sound_button.config(state="disabled")
        unsupported_code=[]
        decrypted_txt=self.text_field.get(1.0,tk.END).split(" ")
        if "\n" in decrypted_txt[-1]:
            decrypted_txt[-1]=decrypted_txt[-1][:-1]
        detranslation=[]
        reverse_morse={v:k for k,v in self.morse_code.items()}
        for element in decrypted_txt:
          if element in reverse_morse.keys():
               detranslation.append(reverse_morse[element])
          else:
               unsupported_code.append(element)   
        if unsupported_code:
             messagebox.showwarning("Warning", f"Following morse code couldn't be decrypted: {", ".join(repr(c) for c in unsupported_code)}")
        else:
            self.text_field.delete(1.0, tk.END) 
            self.text_field.insert(1.0, "".join(detranslation))    

     def play_sound(self):
         freq=600
         dur=60
         for code in self.translation:
               for unit in code:
                    factor=False
                    if unit==".":
                         factor=1
                    elif unit=="-":
                         factor=3
                    elif unit=="/" or unit=="\n":
                         time.sleep(dur*7/1000)     
                    if factor:     
                         winsound.Beep(frequency=freq, duration=dur*factor)                        
                    if unit==code[-1]:
                         time.sleep(dur*3/1000)
                    else:
                         time.sleep(dur/1000)     

start=GUI_MorseC()