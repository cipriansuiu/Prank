import os
def rename_files():
    list=os.listdir(r"C:\Users\Ciprian\Desktop\Learning Python\prank")
    os.chdir(r"C:\Users\Ciprian\Desktop\Learning Python\prank")
    for file_name in list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
rename_files()
