import os
from PIL import Image
import sys

target_num = 2048

def process_image(p:os.DirEntry):
   if p.name.endswith('.png'):
       img = Image.open(p.path)
       w, h = img.size
       print(f"size: {img.size} max: {max(img.size)}")
       snap = 32

       nw = 0
       nh = 0

       # while nw < w:
       #     nw += 4

       scaleRatio_w=target_num/w

       goal_h=h*scaleRatio_w

       print(f"w={w} scale_w={scaleRatio_w}")
       print(f"closest num to meet ratio={goal_h}")


       while nh < goal_h:
           nh += 4

       # n = max(img.size)%snap
       # capToM4 = snap-n
       # goal = max(img.size)+capToM4
       # print(goal)

       rt = img.resize((target_num,nh),Image.ANTIALIAS)

       # rt = Image.new(img.mode, (nw,nh),0)
       # bg_w, bg_h = rt.size
       # offset = ((bg_w-w)//2,(bg_h-h)//2)
       # rt.paste(img,offset)

       ext = os.path.splitext(p.name)[0]+'_dxt5_'+str(target_num)+'.png'

       np = os.path.split(p)[0]+"/"+ext
       # print(np)
       rt.save(np,optimize=True,qualoty=100)


if __name__ == "__main__":
    input_path = sys.argv[1]
    target_num = int(sys.argv[2])
    print("Start resizing")
    for entry in os.scandir(input_path):
        if entry.is_dir():
            for e in os.scandir(entry):
                print(e.path)
                # img = Image.open(e.path)
                # b_size = os.path.getsize(e.path)
                # w, h = img.size
                # # rt = img.resize((int(w*0.5), int(h*0.5)), Image.ANTIALIAS)
                # # print(f"The image size dimensions are: {img.size}")
                # print("size before compress:" + str(b_size))
                # if e.name.endswith('.png'):
                #     rgb_img = img.convert('RGB')
                #     ext = os.path.splitext(e.name)[0] + '.jpg'
                #     p = entry.path + "/" + ext
                #     rgb_img.save(p, optimize=True, quality=40)
                #     a_size = os.path.getsize(p)
                #     os.remove(e.path)
                #     print("size after compress:" + str(a_size))
                # else:
                #     # os.remove(e.path)
                #     ext = os.path.splitext(e.name)[0] + '.jpg'
                #     p = entry.path + "/" + ext
                #     img.save(p, optimize=True, quality=40)
                #     a_size = os.path.getsize(e.path)
                #     print("size after compress:" + str(a_size))
        else:
            process_image(entry)

    print("Done compress")