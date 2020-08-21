import os
import json

secret_directory='/home/sonu/Documents/Test/.secret'
working_directory='/home/sonu/Documents/Test'
key_name='jj'
try:
    os.mkdir(secret_directory)
except FileExistsError:
    pass

operation=input('\t1)Hide Files\n\t2)Get Back Files\n\t  Please choose an operation:  ')
while operation not in ('1','2'):
    print("Incorrect Operation!! Try Again!!")
    operation=input('\t1)Hide Files\n\t2)Get Back Files\n\t  Please choose an operation:  ')

if operation=='1':
    saved_paths=[]
    for dirpath,dirnames,filenames in os.walk(working_directory):
        for filename in filenames:
            if filename[ :len(key_name)]==key_name and str(os.path.splitext(filename)[1]) in ('.mp4','.png','.jpg','.jpeg'):
                if dirpath!=secret_directory:
                    original={
                        'file_name':filename,
                        'dir_path':dirpath
                    }
                    saved_paths.append(original)
                    os.system(f'mv "{os.path.join(dirpath,filename)}" "{secret_directory}"/')
                if len(saved_paths)>0:
                    with open(f"{secret_directory}/secret.json",'w') as file:
                        json.dump(saved_paths,file,indent=2)
    print('Files Hiding Successful!!')
elif operation=='2':
    with open(f"{secret_directory}/secret.json",'r') as file:
        python_data=json.load(file)
    for file_name in os.listdir(secret_directory):
        for file_dict in python_data:
            if file_name==file_dict['file_name']:
                os.system(f'mv \"{str(os.path.join(f"{secret_directory}/" + str(file_name)))}\" '
                          f'\"{str(os.path.join(file_dict["dir_path"]))}/\"')
    print("Got Back the Hidden File!!")
    