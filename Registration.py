import customtkinter as ctk 
from LoginSystem import LoginSystem
from PIL import Image

class Registration_Interface(LoginSystem):
    def __init__(self, parent):
        self.__parent = parent
        self.__root = ctk.CTkToplevel(self.__parent)
        self.__root.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.Main_Window()

    def __get_main_window_width(self):
        return self.__get_frame_width(0.8)
    
    def __get_main_window_height(self):
        return self.__get_frame_height(0.8)
    
    def __get_frame_height(self, percentage):
        return int(self.__root.winfo_screenheight() * percentage)
    
    def __get_frame_width(self, percentage):
        return int(self.__root.winfo_screenwidth() * percentage)
    
    def __get_frame_height(self, percentage):
        return int(self.__root.winfo_screenheight() * percentage)

    def __get_registrationframewindow_height(self, percentage):
        return int(self.__registrationframe.winfo_screenheight() * percentage)
    
    def __on_close(self):
        self.__parent.quit()
        self.__parent.destroy()
        self.__root.destroy()
            
    def Main_Window(self):
        self.__root.title("Expense Tracker/Registration")
        self.__root.after(50, lambda: self.__get_fullscreen())
        self.__root.configure(fg_color = "black")
        self.__root.minsize(self.__get_main_window_width(),self.__get_main_window_height())
        self._center_frame()
     
    def __get_fullscreen(self):
        return self.__root.state("zoomed")
    
    def _center_frame(self):
        self.__set_registration_frame()
        self._set_left_frame()
        self._set_right_frame()
        self.create_registration_form()
        self.__rightframe_contents()  

    def __get_registrationframe_width(self):
        return self.__get_frame_width(0.8)

    def __get_leftframe_width(self):
        return self.__get_frame_width(0.45)

    def __get_rightframe_width(self):
        return self.__get_frame_width(0.45)
    
    def __get_registrationframe_height(self):
        return self.__get_frame_height(1)

    def __get_leftframe_height(self):
        return self.__get_registrationframewindow_height(0.8)

    def __get_rightframe_height(self):
        return self.__get_registrationframewindow_height(0.8)
    

    def __set_registration_frame(self):
        self.__registrationframe = ctk.CTkFrame(self.__root, width=self.__get_registrationframe_width(), height=self.__get_registrationframe_height(), fg_color="#696969", corner_radius=0)
        self.__registrationframe.place(relx=0.5, rely=0.5, anchor="center")

    def __get_registration_frame(self):
        return self.__registrationframe

    def _set_left_frame(self):
        self.__leftFrame = ctk.CTkFrame(self.__get_registration_frame(), width=self.__get_leftframe_width(), height=self.__get_leftframe_height(), fg_color="#696969", corner_radius=0)
        self.__leftFrame.grid(row=0, column=0)

    def __get_left_frame(self):
        return self.__leftFrame

    def _set_right_frame(self):
        self.__rightFrame = ctk.CTkFrame(self.__get_registration_frame(), width=self.__get_rightframe_width(), height=self.__get_rightframe_height(), fg_color="white", corner_radius=0)
        self.__rightFrame.grid(row=0, column=1)

    def __get_right_frame(self):
        return self.__rightFrame

    def __get_font(self):
        return ("Poppins", 20)
    
    def __get_entry_width(self):
        return 250
    
    def create_registration_form(self):
        self.__set_first_name()
        self.__set_last_name()
        self.__set_age()
        self.__set_address()
        self.__set_username()
        self.__set_password()
        self.__get_hide_password()
        self.__get_signin()
        self.__set_signup()
        
    def __set_first_name(self):
        self.__first_name_var = ctk.StringVar()
        self.__first_name = ctk.CTkLabel(self.__get_left_frame(), text="First Name", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__first_name.place(relx= 0.2, y=30, anchor="n")
        self.__first_name_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", 
        height=50, text_color="white", border_color= "#2c2c2c", textvariable= self.__first_name_var)
        self.__first_name_entry.place(relx = 0.5, y= 20, anchor="n")  
           
    def __set_last_name(self):
        self.__last_name_var = ctk.StringVar()
        self.__last_name = ctk.CTkLabel(self.__get_left_frame(), text="Last Name", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__last_name.place(relx=0.2, y=90, anchor="n")
        self.__last_name_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(),
                                               corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c", textvariable= self.__last_name_var)
        self.__last_name_entry.place(relx = 0.5, y=80,anchor="n")  
    
    def __set_age(self):
        self.__age_var = ctk.StringVar()
        self.__age = ctk.CTkLabel(self.__get_left_frame(), text="Age", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__age.place(relx=0.2, y=150, anchor="n")
        self.__age_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), 
                                        corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c", textvariable=self.__age_var)
        self.__age_entry.place(relx = 0.5, y=140,anchor="n")  
    
    def __set_address(self):
        self.__address_var = ctk.StringVar()
        self.__address = ctk.CTkLabel(self.__get_left_frame(), text="Address", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__address.place(relx=0.2, y=210, anchor="n")
        self.__address_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(),
                                             corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c", textvariable=self.__address_var)
        self.__address_entry.place(relx = 0.5, y=200,anchor="n")  
    
    def __set_username(self):
        self.__reg_username_var = ctk.StringVar()
        self.__reg_username = ctk.CTkLabel(self.__get_left_frame(), text="Username", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__reg_username.place(relx=0.2, y=270, anchor="n")
        self.__reg_username_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(),
                                                  corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c", textvariable=self.__reg_username_var)
        self.__reg_username_entry.place(relx = 0.5, y=260,anchor="n")  
    
    def __set_password(self):
        self.__reg_password_var = ctk.StringVar()
        self.__reg_password = ctk.CTkLabel(self.__get_left_frame(), text="Password", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__reg_password.place(relx=0.2, y=330, anchor="n")
        self.__reg_password_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), 
                                                 corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", 
                                                 border_color= "#2c2c2c", show="*", textvariable=self.__reg_password_var)  
        self.__reg_password_entry .place(relx = 0.5, y=320,anchor="n")
    
    def __get_signin(self):
        self.__sign_up = ctk.CTkButton(self.__get_left_frame(), text="Sign-In", width= self.__get_entry_width(), height= 50, font=("Poppins", 20), fg_color= "#2c2c2c", text_color="#e1e1e1", corner_radius= 35)
        self.__sign_up.place(relx= 0.3, y = 400, anchor= "n")

    def __set_signup(self):
        self.__signup = ctk.CTkButton(self.__get_left_frame(), text="Sign-Up", fg_color="#2c2c2c", text_color="white", 
                      font=self.__get_font(), corner_radius=35, height=50, width=self.__get_entry_width(), command= lambda: self.__display())
        self.__signup.place(relx=0.7, y=400,anchor="n")

    def __display(self):
        print(self.__first_name_var.get())
        print(self.__last_name_var.get())
        print(self.__age_var.get())
        print(self.__address_var.get())
        print(self.__reg_username_var.get())
        print(self.__reg_password_var.get())

    def __rightframe_contents(self):
        self.__photo = ctk.CTkImage(light_image=self.get_image(),
                                   dark_image=self.get_image(),
                                   size=(200, 200))
        self.__photoplacement = ctk.CTkLabel(self.__get_right_frame(), image=self.__photo, text="", fg_color="white")
        self.__photoplacement.place(relx=0.5, rely=0.5, anchor="center")

    def get_image(self):
        return Image.open("default.png").convert("RGBA")

    def __get_image_show_password(self):
        return Image.open("updateeye.png").convert("RGBA")
    
    def __get_image_hide_password(self):
        return Image.open("eye.png").convert("RGBA")
    
    def __get_show_password(self):
        self.__photo = ctk.CTkImage(light_image=self.__get_image_show_password(),
                     dark_image=self.__get_image_show_password(),
                     size=(40, 25))
        self.__show_password = ctk.CTkButton(self.__get_left_frame(), image=self.__photo, text="", fg_color="#2c2c2c", width= 10, border_width= 2, border_color= "#2c2c2c", corner_radius=10)
        self.__show_password.place(relx= 0.5, y = 330, anchor= "n", x = 180)

    def __get_hide_password(self):
        self.__photo = ctk.CTkImage(light_image=self.__get_image_hide_password(),
                     dark_image=self.__get_image_hide_password(),
                     size=(40, 25))
        self.__show_password = ctk.CTkButton(self.__get_left_frame(), image=self.__photo, text="", fg_color="#2c2c2c", width= 10, border_width= 2, border_color= "#2c2c2c", corner_radius=10)
        self.__show_password.place(relx= 0.5, y = 330, anchor= "n", x = 180)
