
import PIL.Image
import PIL.ImageTk
import PIL.ImageDraw

def ProfileImage(root,path, size=100, apply_circle=True):
    image = PIL.Image.open(path)
    if apply_circle:
        bigsize = (image.size[0] * 3, image.size[1] * 3)
        mask = PIL.Image.new('L', bigsize, 0)
        draw = PIL.ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(image.size, PIL.Image.ANTIALIAS)
        image.putalpha(mask)
    image = image.resize((size, size), PIL.Image.ANTIALIAS)
    image_photo = PIL.ImageTk.PhotoImage(master=root,image=image)
    return image_photo
