import os
import sys
import argparse

def getFileName(filepath):
    filenames = os.listdir(filepath)
    return filenames


#change single filename

def getreplacedfileName(filename):
    if (filename.find('.')-filename.find('_')) == 2:
        filename = filename[:filename.find('_')+1] + '0' +\
            filename[filename.find('.')-1:]

    return filename
   # afterunderline = filename.split('_')

   # afterdot = afterunderline[1].split('.')
   # if len(afterdot[0]) == 1:

   #     afterdot[0] = '0'+ afterdot[0]
   #     print afterdot[0]
   #     print afterdot

   # print  afterunderline[0] + "_" + afterdot[0] +'.'+ afterdot [1]
   # return afterunderline[0] + "_" + afterdot[0] + '.' + afterdot [1]

def getallsubdir(rootpath):
    subdirs = os.listdir(rootpath)
    for index, subdir in enumerate(subdirs):
        subdirs[index] = os.path.join(rootpath,subdir)
    #print subdirs
    return subdirs


def replacefilenames(filename,subdir):

    oldfilename = filename
    newfilename = getreplacedfileName(filename)
  #  print "xin ming zi :" + newfilename
  #  print os.path.join(subdir, newfilename)
  #  print "jiu ming zi :" + oldfilename
  #  print os.path.join(subdir, oldfilename)
    os.rename(os.path.join(subdir, oldfilename),os.path.join( subdir,newfilename))



if  __name__ == '__main__':
  #  rootpath = sys.path[0]
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Useage: --path your parent dir path")
    args =vars( parser.parse_args())
    rootpath = args['path']


    subdirs = getallsubdir(rootpath)
  #  print subdirs
    for subdir in subdirs :
   #     print subdir
        filenames = getFileName(subdir)
        for filename in filenames:
            replacefilenames(filename, subdir)





