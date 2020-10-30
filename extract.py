import os
import base64
import struct
import codecs
import shutil
#import indian_celeb1
ids=[]
names=[]
fid = open("PATH_TO_CLEAN_LIST.TXT_FILE", "r",encoding="ISO-8859-1")#give the path of the clean_list.txt file here
sourcepath = "PATH_OF_MAIN_EXTRACTED_FILES"#give the path of the file where all the indian celeb extracted images are present
destpath = "PATH_OF_DESTINATION_FOLDER"#cleaned folder path, if it doesn't exist,it creates
if not os.path.exists(destpath):
  os.mkdir(destpath)
bbox_file = open(destpath + '\\bboxes.txt', 'w')
c=0
ind=open("PATH_TO_INDIAN_CELEB.TXT_FILE","r")
while True:
  try:
    ind_line=ind.readline()
    if not ind_line:
      break
    else:
      c+=1
      ind_info=ind_line.split("\t")
      ids.append(ind_info[1].lstrip())
      names.append(ind_info[2].lstrip())    
  except:
    pass
# print(ids)
i=0
t=ids[0]
l=0
while True:
  line = fid.readline()
  # i+=1
  # if(i<20):
	# break
  if line:
    data_info = line.split(' ')

#     # 0: Freebase MID (unique key for each entity)
#     # 1: ImageSearchRank
#     # 4: FaceID
#     # 5: bbox
#     # 6: img_data

    if data_info[0] in ids:
     
      l+=1
      # print("\rExtracting Image : " + str(l) ,end="")
      filename =  data_info[1] 
      filename = filename.replace("-F","_F")
      filename = filename.replace("/","\\")
      filename = filename.replace("\n","")	  
     

      x=sourcepath+filename	  
      print(os.path.exists(x),x)
      if os.path.exists(x):
        print(destpath + data_info[0])
		
        if not os.path.exists(destpath + data_info[0]):
          os.mkdir(destpath+ data_info[0])
        shutil.copy(sourcepath + filename,destpath + data_info[0] + "\\")
        print("\rcopying file : " + filename,end="")
	  
      
  else:
    break

bbox_file.close()
fid.close()
