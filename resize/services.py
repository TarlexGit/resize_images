from PIL import Image
from .models import Image_model 
 
 
def resize_both(img_file, width=None, height=None): 
    img_file = Image.open(img_file)
    path = img_file.filename 
     
    w, h = img_file.size   
    if width and height:
        max_size = (width, height) 
    elif height == None:
        max_size = (width, h)  
    elif width == None:
        max_size = (w, height) 
    else: 
        raise RuntimeError('Width or height required!') 

    name = path.split('/')  
    new_name = str(width) + '_' + str(height) + '_' + name[2] 
    output_image_path = str(name[0]+'/'+name[1]+'/'+new_name)
     
    try:
        with img_file as im:
            img_file.thumbnail(max_size)
            im.save(output_image_path, "JPEG") 
            
            Image_model.objects.create(image_file=output_image_path)
    except:
        print("cannot create thumbnail for", output_image_path)
    
    return 'done'


