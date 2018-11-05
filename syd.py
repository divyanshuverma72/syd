import psutil
count = 100000000
num = 1
import cv2
camera = cv2.VideoCapture(0)
def myfun():
    
    for i in range(30):
     ret, im = camera.read()
    print("capturing image...")
    ret, image = camera.read()
    file = "G://image%d.png"%(num)
    cv2.imwrite(file, image)
print("No removable disk")
while 1==1:
    if count%100000000 == 0:
        
        dps = psutil.disk_partitions()
        fmt_str = "{:<8} {:<7} {:<7}"
        for i in range(len(dps)):
            dp = dps[i]
            amp=fmt_str.format(dp.device, dp.fstype, dp.opts)
            ask=amp.find("removable")
            if ask != -1:
                print("removable disk found")
                myfun()
                break
            num = num+1	
    count = count + 1
  
