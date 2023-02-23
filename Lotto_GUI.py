import tkinter
import threading
import Lotto as lotto
import customtkinter as ctk # <- import the CustomTkinter module

bg_color_l = "#F0F9F8"
bg_color_d = "#3E4453"
#"#6CA8FF"
#--------------------------base-------------------------------------
root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x500")
root_tk.title("Freds awesome Lucky Number Generator")
root_tk.config(bg=bg_color_l)

ctk.set_appearance_mode("Light") # Other: "Light", "System" (only macOS)

#--------------------------Color Variables-------------------------------------
primary_color_light = "#A1DBF1"
primary_color_dark = "#316283"
secondary_color_light = "#A1F1DF"
secondary_color_dark = "#31837A"
acc_color_light = "#BBCCDD"
acc_color_dark = "#3A5775"
acc2_color_light = "#003739"
acc2_color_dark = "white"

#--------------------------FUNCTIONS------------------------------
def settings():
    pass

def eurofct():
    zz_output = lotto.Zusatzzahlen.go()
    if type(zz_output) == list:                                        # TRY brauchen wir um die Rückmeldung "Too Many Numbers" als string auszugeben

        label_zz_output.configure(text=(", ".join(map(str, lotto.Zusatzzahlen.go()))))
        button_lotto.configure(text="The Universe told me:")
    elif type(zz_output) == str:
        zz_output = str(zz_output)
        button_lotto.configure(text="Error:")
    else:
        button_lotto.configure(text="Error:")
        button_lotto.configure(text="Something went wrong")


    hz_output = lotto.Hauptzahlen.go()
    if type(hz_output) == list:
        label_hz_output.configure(text=(", ".join(map(str, lotto.Hauptzahlen.go()))))
    elif type(hz_output) == str:
        hz_output = str(hz_output)
        button_lotto.configure(text="Error:")
    else:
        button_lotto.configure(text="Error:")
        button_lotto.configure(text="Something went wrong")    

def lotto_loading():
    button_lotto.configure(text="Calculating...")
    threading.Thread(target=eurofct).start()
    
def hausfct():
    th_output = lotto.Traumhaus.go()
    label_th_output.configure(text=(", ".join(map(str, lotto.Traumhaus.go()))))
    button_traumhaus.configure(text="Highest propability:")

def haus_loading():
    button_traumhaus.configure(text="Calculating...")
    threading.Thread(target=hausfct).start()

def toggle_mode():
    global mode
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        root_tk.config(bg=bg_color_l)
    else:
        ctk.set_appearance_mode("Dark")
        root_tk.config(bg=bg_color_d)

#------------------------------------BUTTONS------------------------------------

def create_button(fct, txt, x_pos, y_pos, **attrs):
    color_pl = attrs.get("color_pl", primary_color_light)
    color_pd = attrs.get("color_pd", primary_color_dark)
    color_sl = attrs.get("color_sl", secondary_color_light)
    color_sd = attrs.get("color_sd", secondary_color_dark)
    width = attrs.get("width", 180)
    height = attrs.get("height", 32)
    color_txt_l = attrs.get("color_txt_l", "#14312F")
    color_txt_d = attrs.get("color_txt_d", "white")
    border = attrs.get("border", 1)
    corner = attrs.get("corner", 10)
    border_color = attrs.get("border_color", (acc_color_light ,acc_color_dark))
    txt_size = attrs.get("txt_size",12)
    master= attrs.get("master",root_tk)
    button = ctk.CTkButton(master=master,
                                    command=fct,
                                    fg_color=(color_pl,color_pd),
                                    text_color=(color_txt_l, color_txt_d),
                                    text=txt,
                                    hover_color=(color_sl, color_sd),
                                    width=width,
                                    height=height,
                                    border_width=border,
                                    border_color=border_color,
                                    corner_radius=corner,
                                    font=("Helvetica", txt_size))
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
                               border_color=("#BBCCDD", "#BBDDDD"),
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

#_________________________INPUTS___________________________
def create_entry(x_pos, y_pos, **attrs):
    master = attrs.get("master", root_tk)
    entry = ctk.CTkEntry(master=master,
                                width=100,
                                height=25,
                                corner_radius=5,
                                border_width=1)
    entry.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
    return entry

#______________________Building GUI_______________________________

header              = create_frame(x_pos=0.5, y_pos=0.0, color_pl=primary_color_light, height=60)  ##HEADER
label_header        = create_label("GC Number Generator", 0.5, 0.75, master=header, color_txt_l=acc2_color_light, color_txt_d=acc2_color_dark)

frame_lotto        = create_frame(x_pos=0.5, y_pos=0.355, color_pl=bg_color_l, color_pd=bg_color_d, height=70, width=250, corner_radius=10, border_width=1)  #Output Rahmen Lotto
frame_traumhaus    = create_frame(x_pos=0.5, y_pos=0.665, color_pl=bg_color_l, color_pd=bg_color_d, height=70, width=250, corner_radius=10, border_width=1)  #Output Rahmen Haus

#=============================DARK / LIGHT ========================

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
#=============================Settings ============================


def it_set():
    iterations = iter_entry.get()
    lotto.iter_allowed = int(iterations)
    print(iterations)
    return int(iterations)





def toggle_settings():
    if setting_label.winfo_viewable():
        setting_label.place_forget()
        settings_button.configure(text="Settings")
        iter_entry.place_forget()
        it_set_button.place_forget()
        setting_frame.place_forget()

    else:    
        setting_label.place(relx=0.1, rely=0.2)
        settings_button.configure(text="Hide Settings")
        iter_entry.place(relx=0.09, rely=0.5)
        it_set_button.place(relx=0.35, rely=0.52)
        setting_frame.place(relx=0.0, rely=0.78)

setting_frame = create_frame(x_pos=0.5, y_pos=0.895, color_pl=primary_color_light, height=110)
setting_frame.place_forget()

setting_label = create_label("Interations", 0.12, 0.5, master=setting_frame)
setting_label.place_forget()
iter_entry = create_entry(0.1,0.5, master=setting_frame)
iter_entry.place_forget()

it_set_button = create_button(it_set, "Set", 0.35, 0.52, width=20, height=20, corner=2, txt_size=10, master=setting_frame, color_pl="white")
it_set_button.place_forget()







#=============================BUTTONS =============================

settings_button = create_button(toggle_settings, "Settings",0.9, 0.11, width=40, height=20, corner=5, txt_size=10)
button_lotto        = create_button(lotto_loading, "Press here to win millions!", 0.5, 0.2)
button_traumhaus    = create_button(hausfct, "Press here to win a Dreamhouse!", 0.5, 0.51)



#_______________________Hauptzahlen________________________________

label_hauptz        = create_label("Hauptzahlen:", 0.47, 0.32, anchor=tkinter.E)
label_hz_output = create_label(" ", 0.47, 0.39, anchor=tkinter.E)

#______________________Zusatzzahlen_______________________________

label_zusatz        = create_label("Zusatzzahlen:", 0.53, 0.32, anchor=tkinter.W)
label_zz_output = create_label(" ", 0.53, 0.39, anchor=tkinter.W)

#______________________Traumhaus_______________________________
label_haus        = create_label("Los Nummer:", 0.5, 0.63)
label_th_output = create_label(" ", 0.5, 0.7)


#======================================================
root_tk.mainloop()

