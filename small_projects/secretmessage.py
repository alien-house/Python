import os

def rename_files():
    #  1)  get filename from a folder
    #  in windows os.listdir(r"C:/") 
    file_list = os.listdir("/Users/shinji/Mydata/personalmarketing/english/canada/school/CICCC/subject/python/img")
    print(file_list)
    save_path = os.getcwd()
    print("Current working directory is" + save_path)
    os.chdir("/Users/shinji/Mydata/personalmarketing/english/canada/school/CICCC/subject/python/img")
             
    #  2)  for each file rename the file name
    #  filename.translate(finlename.maketrans ('','','01238935'))
    for file_name in file_list:
        os.rename(file_name, file_name.translate(file_name.maketrans('','','0123456789')))

    os.chdir(save_path)
    
rename_files()



