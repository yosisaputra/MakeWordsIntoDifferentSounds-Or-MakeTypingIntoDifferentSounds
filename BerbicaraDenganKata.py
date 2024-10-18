import os
from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('600x400')
root.resizable(True, True)  # Allow resizing
root.config(bg='gray')  # Change background color to gray
root.title('BERBICARA DENGAN TEXT')

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=2)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

heading = Label(root, text='Mengubah Text Menjadi Berbagai Suara', font='Arial 20 bold', bg='light gray')
heading.grid(row=0, column=0, columnspan=3, pady=10)

text_label = Label(root, text='Masukkan Text :', font='Arial 15 bold', bg='light gray')
text_label.grid(row=1, column=0, sticky=W, padx=20, pady=(10, 5))

entry_field = Text(root, height=10, bg='white', fg='black', wrap=WORD)
entry_field.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=20, sticky=NSEW)

voice_options = {
    "English (US)": 'en',
    "English (UK)": 'en-uk',
    "Indonesian": 'id',
    "Russian": 'ru',
    "Chinese (Mandarin)": 'zh',
    "Malay": 'ms',
}

selected_voice = StringVar(value='en')

voice_label = Label(root, text='Pilih Bahasa :', font='Arial 15 bold', bg='light gray')
voice_label.grid(row=3, column=0, sticky=W, padx=20, pady=(5, 5))

voice_menu = OptionMenu(root, selected_voice, *voice_options.keys())
voice_menu.grid(row=3, column=1, pady=(5, 5), sticky=W)

def Text_to_speech():
    Message = entry_field.get("1.0", END).strip()
    if Message:
        language_code = voice_options[selected_voice.get()]
        speech = gTTS(text=Message, lang=language_code)
        speech.save('Data.mp3')
        playsound('Data.mp3')
        os.remove('Data.mp3')
def Exit():
    root.destroy()
def Reset():
    entry_field.delete("1.0", END)

button_frame = Frame(root, bg='light gray')
button_frame.grid(row=4, column=0, columnspan=3, pady=(10, 20))

Button(button_frame, text="MULAI", font='Arial 15 bold', command=Text_to_speech, width=8).pack(side=LEFT, padx=10)
Button(button_frame, text='KELUAR', font='Arial 15 bold', command=Exit, bg='OrangeRed1', width=8).pack(side=LEFT, padx=10)
Button(button_frame, text='RESET', font='Arial 15 bold', command=Reset, width=8).pack(side=LEFT, padx=10)

root.mainloop()