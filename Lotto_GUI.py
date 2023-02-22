import tkinter
import Lotto as lt
import customtkinter as ctk # <- import the CustomTkinter module

#--------------------------base-------------------------------------
root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x500")
root_tk.title("Freds awesome Lucky Number Generator")
root_tk.config(bg="#282c36")

ctk.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)


#--------------------------FUNCTIONS------------------------------

def eurofct():
    zz_text.configure(text="Zusatzzahlen")
    zz_output = lt.Zusatzzahlen.go()
    if type(zz_output) == str:
        zz_out.configure(text=zz_output)
    elif type(zz_output) == list:
        zz_out.configure(text=(", ".join(map(str, lt.Zusatzzahlen.go()))))
    hz_text.configure(text="Hauptzahlen")
    hh_output = lt.Hauptzahlen.go()
    if type(hh_output) == str:
        hz_out.configure(text=hh_output)
    elif type(hh_output) == list:
        hz_out.configure(text=(", ".join(map(str, lt.Hauptzahlen.go()))))

def hausfct():
    th_text.configure(text="Traumhaus Lotterie")
    th_output = lt.Traumhaus.go()
    if type(th_output) == str:
        th_out.configure(text=th_output)
    elif type(th_output) == list:
        th_out.configure(text=(", ".join(map(str, lt.Traumhaus.go()))))

def toggle_mode():
    global mode
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Light":
        ctk.set_appearance_mode("Dark")
        root_tk.config(bg="#282c36")
        toggle_mode.configure(text="Dark")
    else:
        ctk.set_appearance_mode("Light")
        root_tk.config(bg="#ffffff")
        toggle_mode.configure(text="Light")

#---------------------------check functions----------------------------

#--------------------------Color Variables-------------------------------------


primary_color_light = "#6CFFC3"
primary_color_dark = "#000000"
secondary_color_light = "#6CF1FF"
secondary_color_dark = "#000000"
text_color_light = "#ffffff"
text_color_dark = "#ffffff"
border_color_light = "#ccd1e0"
border_color_dark = "#000000"
background_color_light = "#ffffff"
background_color_dark = "#000000"
foreground_color_light = "#000000"
foreground_color_dark = "#000000"


#------------------------------------BUTTONS------------------------------------


def create_button(fct, txt, x_pos, y_pos, **attrs):
    color_pl = attrs.get("color_pl", primary_color_light)
    color_pd = attrs.get("color_pd", primary_color_dark)
    color_sl = attrs.get("color_sl", secondary_color_light)
    color_sd = attrs.get("color_sd", secondary_color_dark)
    width = attrs.get("width", 160)
    button = ctk.CTkButton(master=root_tk,
                                    command=fct,
                                    fg_color=(color_pl,color_pd),
                                    text_color=("black", "white"),
                                    text=txt,
                                    hover_color=(color_sl, color_sd),
                                    width=width,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10)
    button.place(relx=x_pos, rely=y_pos, anchor=tkinter.CENTER)
    return button


#------------------------------------FRAMES------------------------------------


def create_frame(x_pos, y_pos, **attrs):
    color_pl = attrs.get("color_pl", primary_color_light)
    color_pd = attrs.get("color_pd", primary_color_dark)
    width = attrs.get("width", 400)
    height = attrs.get("height", 20)
    corner_radius = attrs.get("corner_radius", 0)
    border_width = attrs.get("border_width", 0)


    frame = ctk.CTkFrame(master=root_tk,
                               fg_color=(color_pl, color_pd),
                               width=width,
                               height=height,
                               corner_radius=corner_radius,
                               border_width=border_width)
    frame.place(relx=x_pos, rely=y_pos, anchor=tkinter.CENTER)
    return frame




#------------------------------------Labels----------------------------------

def create_label(master, text, x_pos, y_pos, **attrs):
    label = ctk.CTkLabel(master=master,                                     # master = übergeordnetes Objekt
                      text=text,
                      font=("Helvetica", 16))
    label.place(relx=x_pos, rely=y_pos, anchor=tkinter.CENTER)
    return label






#______________________Hauptzahlen_______________________________

header              = create_frame(x_pos=0.5, y_pos=0.0, color_pl="#6CA8FF", height=120)  ##HEADER

rahmen_lotto        = create_frame(x_pos=0.5, y_pos=0.355, color_pl="white", height=70, width=250, corner_radius=10, border_width=2)  #Output Rahmen Lotto
rahmen_traumhaus    = create_frame(x_pos=0.5, y_pos=0.655, color_pl="white", height=70, width=250, corner_radius=10, border_width=2)  #Output Rahmen Haus


toggle_mode   = create_button(toggle_mode, "dark", 0.1, 0.18, width = 50)
#button_lotto        = create_button(eurofct, "Press here to win millions!", 0.5, 0.2)
button_traumhaus    = create_button(hausfct, "Press here to win a Dreamhouse!", 0.5, 0.5)

label_header        = create_label(header, "GC Number Generator", 0.5, 0.75)

hz_out = ctk.CTkLabel(master=root_tk,
                               text="xxxxx",
                               width=90,
                               height=25)
hz_out.place(relx=0.47, rely=0.39, anchor=tkinter.E)

#______________________Zusatzzahlen_______________________________

zz_text = ctk.CTkLabel(master=root_tk,
                               text="Zusatzzahlen:",
                               width=90,
                               height=25)
zz_text.place(relx=0.53, rely=0.32, anchor=tkinter.W)

zz_out = ctk.CTkLabel(master=root_tk,
                               text="xx",
                               width=90,
                               height=25)
zz_out.place(relx=0.53, rely=0.39, anchor=tkinter.W)

#______________________Traumhaus_______________________________


th_text = ctk.CTkLabel(master=root_tk,
                               text="Taumhaus Losnummer:",
                               width=120,
                               height=25)
th_text.place(relx=0.5, rely=0.62, anchor=tkinter.CENTER)

th_out = ctk.CTkLabel(master=root_tk,
                               text="XXXXXXXXXXXXX",
                               width=120,
                               height=25)
th_out.place(relx=0.5, rely=0.69, anchor=tkinter.CENTER)
#======================================================
root_tk.mainloop()

