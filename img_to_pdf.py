from PIL import Image
from imutils import paths
 
im_list = [Image.open(x).convert('RGB') for x in paths.list_images("pdfp")]
pdf1_filename = "myfile.pdf"
im_list[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list[1:])
