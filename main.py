import customtkinter
import PyPDF2  # Imports the library
import os  # provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory.


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x250")


def merge_pdf():  # function that we can connect to the buttons using the command keyword
    print("Test")
    merger = PyPDF2.PdfMerger()  # merger object that lets us merge the PDF files.

    new_file_name = entry1.get()
    for file in os.listdir(os.curdir):  # lists the current files in the directory
        if file.endswith(".pdf"):  # checks if the file is a pdf
            print(file)  # if the condition above is satisfied prints the name of the files in the current directory
            merger.append(file)
    merger.write(new_file_name + ".pdf")


frame = customtkinter.CTkFrame(master=root) # creating the frame and customizing it
frame.pack(pady=20, padx=60, fill="both", expand=True)


# below is defining objects that we will add to the frame and then the frame itself is added to the root
label = customtkinter.CTkLabel(master=frame, text="PDF Merger")
label.pack(pady=12, padx=10)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Merged File Name")
entry1.pack(pady=12, padx=10)


button = customtkinter.CTkButton(master=frame, text="Merge PDFs", command=merge_pdf)
button.pack(pady=12, padx=10)

root.mainloop()