import os
import os.path
import shutil
import glob

print("Your current working directory is :"+ os.getcwd() )

current=raw_input("Input FIle directory: ")
if not current:
    current= os.getcwd()
else:
    pass

def Filecreator(FileName):
    FileLocation= current+'/'+FileName
    if os.path.isdir(FileLocation) == False:
        os.mkdir(FileLocation)
    else:
        pass

Filecreator("Docs")
Filecreator("Audio&Video")
Filecreator("Programs")
Filecreator("Archived")
Filecreator("Misc")
Filecreator("Image")


images=['jpeg','JPG','jpg','png','gif','webp','tiff','tif','psd','raw','bmp','svg','ai','eps']
documents=['doc','docx','html','htm','odt','pdf','xls','xlsx','ods','ppt','pptx','txt','log']
audiovid=['webm','mpg','mp2','mpeg','mpe','mpv','ogg','mp4','m4p','m4v','avi','wmv','mov','qt','flv','swf','avchd']
programs=['ppk','lnk','bat','bin','cmd','com','cpl','exe','inf1','ins','msc','msi','msp','pif','scr','vb','vbe','vbs','sh','deb','jar','java']
archived=['rar','7z','zip','tar.gz']


def FileMover(extensions,dir):
    fileLocation = current
    source = fileLocation+"/"
    dest= fileLocation+"/{}".format(dir)
    for ext in extensions:
        for file in glob.glob( source + '*.' + ext ):
            shutil.move(file,dest)

FileMover(audiovid,"Audio&Video")
FileMover(images,"Image")
FileMover(documents,"Docs")
FileMover(programs,"Programs")
FileMover(archived,"Archived")
