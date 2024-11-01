import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart cctv")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.attributes('-fullscreen', True)



frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)

icon = Image.open('icons/spy.png')
icon = icon.resize((150,150), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.LANCZOS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((40,40), Image.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50,50), Image.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green', image=btn1_image,command=noise, compound='left')
btn1['font'] = btn_font
btn_font = font.Font(size=17)
btn1.grid(row=3, pady=(20,10))
btn1['bd'] = 5          # Border width
btn1['relief'] = 'raised'  # Border relief style (options: 'flat', 'raised', 'sunken', 'groove', 'ridge')

btn2 = tk.Button(frame1, text='Region Select', height=90, width=180, fg='orange', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,5))
btn2['bd'] = 5          # Border width
btn2['relief'] = 'raised' 

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)
btn4['bd'] = 5          # Border width
btn4['relief'] = 'raised' 


btn6 = tk.Button(frame1, text='Visitor', height=90, width=180, fg='green', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=4, pady=(20,10), column=2)
btn6['bd'] = 5          # Border width
btn6['relief'] = 'raised' 

btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=5, pady=(20,10))
btn5['bd'] = 5          # Border width
btn5['relief'] = 'raised' 

frame1.pack()
window.mainloop()


