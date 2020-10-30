import os
import base64
import struct
import codecs
#import indian_celeb1
ids=[]
names=[]
fid = open("E:\\MS-Celeb-1M\\data\\croped_face_images\\FaceImageCroppedWithOutAlignment.tsv", "r",encoding="ISO-8859-1")
base_path = "C:\\MS_Celeb_Indian\\aligned_face_images_cropnotalign\\"
if not os.path.exists(base_path):
  os.mkdir(base_path)
bbox_file = open(base_path + '\\bboxes.txt', 'w')
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
cnt=0
while True:
  line = fid.readline()
  # i+=1
  # if(i<20):
	# break
  # if l==1000:
  #   break
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
      # bbox = struct.unpack('ffff', data_info[5].decode("base64"))
      # bbox_file.write(filename + " "+ (" ".join(str(bbox_value) for bbox_value  in bbox)) + "\n")

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

#bbox_file.close()
#fid.close()