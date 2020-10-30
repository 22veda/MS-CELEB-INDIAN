import os
import base64
import struct
import codecs
#import indian_celeb1
ids=[]
names=[]
fid = open("PATH_TO_THE_TSV_FILE", "r",encoding="ISO-8859-1")#Path of the tsv file of MS-Celeb dataset
base_path = "Your_folder_path"#create a folder to store the extracted images
if not os.path.exists(base_path):
  os.mkdir(base_path)
bbox_file = open(base_path + '\\bboxes.txt', 'w')
c=0
ind=open("PATH_TO_INDIAN_LIST_TEXT_FILE","r")#give the path of the file containing indian list of MS-Celeb
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
cnt=0
while True:
  line = fid.readline()
  
  if line:
    data_info = line.split('\t')

#     # 0: Freebase MID (unique key for each entity)
#     # 1: ImageSearchRank
#     # 4: FaceID
#     # 5: bbox
#     # 6: img_data

    if data_info[0] in ids:
      # x=ids.index(data_info[0])
      l+=1
      print("\rExtracting Image : " + str(l) ,end="")
      filename =  data_info[0] + "\\" + data_info[1] + "_" + data_info[4] + ".jpg"
      

      img_data = base64.b64decode(data_info[6])
      output_file_path = base_path + "\\" + filename 
      if os.path.exists(output_file_path):
        print(output_file_path + " exists")

      output_path = os.path.dirname(output_file_path)
      if not os.path.exists(output_path):
        os.mkdir(output_path)

      img_file = open(output_file_path, 'wb')
      img_file.write(img_data)
      img_file.close()
  else:
    break

bbox_file.close()
fid.close()

