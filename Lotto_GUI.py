import tkinter
import Lotto as lt
import customtkinter as ctk # <- import the CustomTkinter module

bg_color_l = "#E4F4F3"
bg_color_d = "#3E4453"
#"#6CA8FF"
#--------------------------base-------------------------------------
root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x500")
root_tk.title("Freds awesome Lucky Number Generator")
root_tk.config(bg=bg_color_l)

ctk.set_appearance_mode("Light") # Other: "Light", "System" (only macOS)


#--------------------------FUNCTIONS------------------------------

def eurofct():
    label_zusatz.configure(text="Zusatzzahlen")
    zz_output = lt.Zusatzzahlen.go()
    if type(zz_output) == str:
        label_zz_output.configure(text=zz_output)
    elif type(zz_output) == list:
        label_zz_output.configure(text=(", ".join(map(str, lt.Zusatzzahlen.go()))))
    label_hauptz.configure(text="Hauptzahlen")
    hh_output = lt.Hauptzahlen.go()
    if type(hh_output) == str:
        label_hz_output.configure(text=hh_output)
    elif type(hh_output) == list:
        label_hz_output.configure(text=(", ".join(map(str, lt.Hauptzahlen.go()))))

def hausfct():
    label_haus.configure(text="Traumhaus Lotterie")
    th_output = lt.Traumhaus.go()
    if type(th_output) == str:
        label_th_output.configure(text=th_output)
    elif type(th_output) == list:
        label_th_output.configure(text=(", ".join(map(str, lt.Traumhaus.go()))))

def toggle_mode():
    global mode
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        root_tk.config(bg=bg_color_l)
        toggle_mode.configure(text="Dark")
    else:
        ctk.set_appearance_mode("Dark")
        root_tk.config(bg=bg_color_d)
        toggle_mode.configure(text="Light")

#---------------------------check functions----------------------------

#--------------------------Color Variables-------------------------------------

primary_color_light = "#00B6BC"
primary_color_dark = "#324D5B"
secondary_color_light = "#71D5E4"
secondary_color_dark = "#517D94"
acc_color_light = "#A1DBF1"
acc_color_dark = "#3ad89d"
acc2_color_light = "#003739"
acc2_color_dark = "#B5FDFF"

""" primary_color_light = "#27C289"
primary_color_dark = "#324D5B"
secondary_color_light = "#43697C"
secondary_color_dark = "#517D94"
acc_color_light = "#517D94"
acc_color_dark = "#3ad89d" """



#------------------------------------BUTTONS------------------------------------


def create_button(fct, txt, x_pos, y_pos, **attrs):
    color_pl = attrs.get("color_pl", primary_color_light)
    color_pd = attrs.get("color_pd", primary_color_dark)
    color_sl = attrs.get("color_sl", secondary_color_light)
    color_sd = attrs.get("color_sd", secondary_color_dark)
    width = attrs.get("width", 160)
    height = attrs.get("height", 32)
    color_txt_l = attrs.get("color_txt_l", "white")
    color_txt_d = attrs.get("color_txt_d", "white")
    border = attrs.get("border", 0)
    corner = attrs.get("corner", 10)
    border_color = attrs.get("border_color", (acc_color_light ,acc_color_dark))
    button = ctk.CTkButton(master=root_tk,
                                    command=fct,
                                    fg_color=(color_pl,color_pd),
                                    text_color=(color_txt_l, color_txt_d),
                                    text=txt,
                                    hover_color=(color_sl, color_sd),
                                    width=width,
                                    height=height,
                                    border_width=border,
                                    border_color=border_color,
                                    corner_radius=corner)
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
    color_txt_l = attrs.get("color_txt_l", "white")
    color_txt_d = attrs.get("color_txt_d", "white")


    frame = ctk.CTkFrame(master=root_tk,
                               fg_color=(color_pl, color_pd),
                               width=width,
                               height=height,
                               corner_radius=corner_radius,
                               border_color=(acc_color_light, acc_color_dark),
                               border_width=border_width)
    frame.place(relx=x_pos, rely=y_pos, anchor=tkinter.CENTER)
    return frame




#------------------------------------Labels----------------------------------

def create_label(text, x_pos, y_pos, **attrs):
    master = attrs.get("master", root_tk)
    anchor = attrs.get("anchor", tkinter.CENTER)
    color_txt_l = attrs.get("color_txt_l", "black")
    color_txt_d = attrs.get("color_txt_d", "white")
    label = ctk.CTkLabel(master=master,                                     # master = übergeordnetes Objekt
                      text=text,
                      text_color=(color_txt_l, color_txt_d),
                      width=90,
                      height=25,
                      font=("Helvetica", 12))
    label.place(relx=x_pos, rely=y_pos, anchor=anchor)
    return label


#______________________Building GUI_______________________________

header              = create_frame(x_pos=0.5, y_pos=0.0, color_pl="#A1DBF1", height=60)  ##HEADER
label_header        = create_label("GC Number Generator", 0.5, 0.75, master=header, color_txt_l=acc2_color_light, color_txt_d=acc2_color_dark)

frame_lotto        = create_frame(x_pos=0.5, y_pos=0.355, color_pl=bg_color_l, color_pd=bg_color_d, height=70, width=250, corner_radius=10, border_width=1)  #Output Rahmen Lotto
frame_traumhaus    = create_frame(x_pos=0.5, y_pos=0.755, color_pl=bg_color_l, color_pd=bg_color_d, height=70, width=250, corner_radius=10, border_width=1)  #Output Rahmen Haus

toggle_mode_A   = create_button(toggle_mode,
                              " ",
                              0.05,
                              0.11,
                              width = 15,
                              height = 5,
                              color_pd=bg_color_l,
                              color_pl=bg_color_d,
                              border=1,
                              border_color=(bg_color_d,bg_color_l),
                              corner=0)
toggle_mode_B   = create_button(toggle_mode,
                              " ",
                              0.08,
                              0.11,
                              width = 15,
                              height = 5,
                              color_pd=bg_color_d,
                              color_pl=bg_color_l,
                              border=1,
                              border_color=(bg_color_d,bg_color_l),
                              corner=0)

button_lotto        = create_button(eurofct, "Press here to win millions!", 0.5, 0.2, border=1)
button_traumhaus    = create_button(hausfct, "Press here to win a Dreamhouse!", 0.5, 0.6)


#_______________________Hauptzahlen________________________________

label_hauptz        = create_label("Hauptzahlen:", 0.47, 0.32, anchor=tkinter.E)
label_hz_output = create_label("xxxxxxbxx", 0.47, 0.39, anchor=tkinter.E)

#______________________Zusatzzahlen_______________________________

label_zusatz        = create_label("Zusatzzahlen:", 0.53, 0.32, anchor=tkinter.W)
label_zz_output = create_label("xx", 0.53, 0.39, anchor=tkinter.W)

#______________________Traumhaus_______________________________
label_haus        = create_label("Zusatzzahlen:", 0.5, 0.72)
label_th_output = create_label("xx", 0.5, 0.79)


#======================================================
root_tk.mainloop()

