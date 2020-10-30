import os
import base64
import struct
import codecs
import shutil
#import indian_celeb1
ids=[]
names=[]
fid = open("C:\\MS_Celeb_Indian\\relabel_list_128Vec_T058.txt", "r",encoding="ISO-8859-1")
sourcepath = "C:\MS_Celeb_Indian\\aligned_face_images1\\"
destpath = "C:\\MS_Celeb_Indian\\aligned_face_images2\\"
cleanpath=open("C:\\MS_Celeb_Indian\\clean_list_128Vec_WT051_P010.txt","r")
if not os.path.exists(destpath):
  os.mkdir(destpath)
bbox_file = open(destpath + '\\bboxes.txt', 'w')
c=0
ind=open("E:\\MS-Celeb-1M\\data\\aligned_face_images\\india_celeb1.txt","r")
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
  clean_line=cleanpath.readline()
  # i+=1
  # if(i<20):
	# break
  if line:
    data_info = line.split(' ')
    # clean_info=clean_line.split(' ')
    # print(clean_info)
# 
#     # 0: Freebase MID (unique key for each entity)
#     # 1: ImageSearchRank
#     # 4: FaceID
#     # 5: bbox
#     # 6: img_data

    if data_info[0] in ids:
      # print(data_info[1]==clean_info[1])
#       # x=ids.index(data_info[0])
      l+=1
      # print("\rExtracting Image : " + str(l) ,end="")
      filename =  data_info[1] 
      filename = filename.replace("-F","_F")
      filename = filename.replace("/","\\")
      filename = filename.replace("\n","")
      
      # print(filename)
#       # bbox = struct.unpack('ffff', data_info[5].decode("base64"))
#       # bbox_file.write(filename + " "+ (" ".join(str(bbox_value) for bbox_value  in bbox)) + "\n")

      x=sourcepath+filename	  
      # print(os.path.exists(x),x)
      if os.path.exists(x):
        print(destpath + data_info[0])
		
        if not os.path.exists(destpath+data_info[0]):
          os.mkdir(destpath+data_info[0])

        # fname=filename.split("\\")
        # fname[1]="r_"+fname[1]
        # filename="\\".join(map(str,fname))
        
        shutil.copy(sourcepath + filename,destpath +data_info[0] +"\\" + "relabeled_" + filename.split("\\")[1])
        print("\rcopying file : " + filename,end="")
	  
      
  else:
    break

bbox_file.close()
fid.close()

#bbox_file.close()
#fid.close()