
import os
import zipfile

#------------------------------------------------------------
#   Create a zip file from the list of all the files from the 
#   specified directory
#------------------------------------------------------------
def create_zip_file(file_list:list)->str:   
    zip_file = f"{os.getcwd()}/output/test.zip"    
    with zipfile.ZipFile(zip_file, "w") as zf:
        for file in file_list:                
            zf.write(file, os.path.basename(file))
    return zip_file


#-------------------------------------------------#
#  Unzip the file                                 #
#-------------------------------------------------#
def unzip_file(zip_file:str)->str:
    """
    Unzip the file and save the extracted files in the output folder
    """
    output_folder = f"{os.getcwd()}/output/test1"
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_folder)  
    return output_folder


files = []
file1 = f"{os.getcwd()}/input/819853.jpg"
file2 = f"{os.getcwd()}/input/temp/226296.jpg"
files.extend([file1, file2])

zip_file = create_zip_file(files)
zip_folder = unzip_file(zip_file)
print(zip_folder)
