# MS-CELEB-INDIAN
A repo which extracts and relabels all the Indian Celebs images from C-MS-Celeb\

Firstly, the python scripts that I've written extracts and relabels the images of only Indian Celebrities from MS-Celeb. C-MS-Celeb is a cleaned version of MS-Celeb that has provided two text files i.e clean_list.txt and relabel_list.txt(Yeah, thank you for making this job easier!). These contain the id and path of all the celebrities of MS-celeb.\

Install the MS-Celeb dataset before extracting and relabeling. It contains two tsv files(cropwithoutalignment.tsv and cropwithalignment.tsv).

**Indian_celeb.txt**: A text file containing all the ids, names and designation of Indian Celebs.\
**clean_list.7z**: Zip file that contains two text files(clean_list.txt and relabel_list.txt). This Zip file has been taken from https://github.com/EB-Dodo/C-MS-Celeb/blob/master/clean_list.7z\ \
**main_extract.py**: Extracts all the images of Indian celebrities from MS-Celeb dataset by matching the ids with the ids in *"Indian_celeb.txt"*. You can give your desired tsv filepath here.\
**extract.py**: Cleans all the extracted images(using main_extract.py) with the help of ids specified in clean_list.txt file.\
**relabel.py**: Relabels all the cleaned images and mismatched images.

