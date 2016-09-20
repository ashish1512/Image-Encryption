
from PIL import Image
im = Image.open('C:/Users/Ashish/Desktop/poo.png')
im.save('C:/Users/Ashish/Desktop/1.png')

pixels = im.load()
width, height=im.size

key=[0]*(width*height)
all_pixels=[]
c=0
for y in range(height):
    for x in range(width):
        cpixel=pixels[x,y]
        all_pixels.append(cpixel)
        key[c]=0
        c=c+1
#for a in range(width*2):
#        print all_pixels[a]




for y in range(height-1):
    for x in range(width-2):
        if all_pixels[x+(width*y)]==0 and all_pixels[(x+1)+(width*y)]==0 and all_pixels[x+2+(width*y)]==0:
            if(all_pixels[(width*(y+1))+x+1])==0:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=255
        elif all_pixels[x+(width*y)]==0 and all_pixels[x+1+(width*y)]==0 and all_pixels[x+2+(width*y)]==255:
            if(all_pixels[(width*(y+1))+x+1])==0:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=255
        elif all_pixels[x+(width*y)]==0 and all_pixels[x+1+(width*y)]==255 and all_pixels[x+2+(width*y)]==0:
            if(all_pixels[(width*(y+1))+x+1])==0:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=255
        elif all_pixels[x+(width*y)]==0 and all_pixels[x+1+(width*y)]==255 and all_pixels[x+2+(width*y)]==255:
            if(all_pixels[(width*(y+1))+x+1])==255:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=0
        elif all_pixels[x+(width*y)]==255 and all_pixels[x+1+(width*y)]==0 and all_pixels[x+2+(width*y)]==0:
            if(all_pixels[(width*(y+1))+x+1])==255:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=0
        elif all_pixels[x+(width*y)]==255 and all_pixels[x+1+(width*y)]==0 and all_pixels[x+2+(width*y)]==255:
            if(all_pixels[(width*(y+1))+x+1])==255:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=0
        elif all_pixels[x+(width*y)]==255 and all_pixels[x+1+(width*y)]==255 and all_pixels[x+2+(width*y)]==0:
            if(all_pixels[(width*(y+1))+x+1])==255:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=0
        elif all_pixels[x+(width*y)]==255 and all_pixels[x+1+(width*y)]==255 and all_pixels[x+2+(width*y)]==255:
            if(all_pixels[(width*(y+1))+x+1])==0:
                key[(width*(y+1))+x+1]=1
            all_pixels[(width*(y+1))+x+1]=255
cnt=0    
for y in range(height):
    for x in range(width):
        pixels[x,y]=all_pixels[cnt]
        cnt=cnt+1
im.save('C:/Users/Ashish/Desktop/encrypt.png')

pq = list()
pq=[0]*(width/2)
print pq
keyrc=list()
num=raw_input("How many elements should the Key have? (Key should contain only integers) ")
for i in range(0,int(num)):
    n=raw_input()
    keyrc.append(int(n))
print keyrc
lk=len(keyrc)

print "\nInitializing S"
s=list()
for i in range(width/2):
    s.append(int(i))
print s
print "Initialized"

print "Shuffled"

print "\nShuffling S Again"
i=0
j=0
a=0
k=list()
while a<(width/2):
    i=(i+1)%(width/2)
    j=(j+s[i])%(width/2)
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    k.append(s[(s[i]+s[j])%(width/2)])
    pq[k[a]]=pq[k[a]]+1
    a=a+1
print a
print "k"
print k



print "\nPQ"
print pq
s1=0
s2=0
for i in range(width/2):
    if pq[i]==0:
        s1=s1+1
    if pq[i]>1:
        s2=s2+1
print s1
print s2

i=0
while i<(width/2):
    j=0
    l=0
    if pq[i]==1 or pq[i]==0:
        i=i+1
        continue
    if pq[i]>1:
        z=i
        while pq[j]!=0:
            j=j+1
        while k[l]!=z:
            l=l+1
        k[l]=j
        pq[j]=pq[j]+1
        pq[i]=pq[i]-1
    j=0
    print i
    print pq[j]
    print pq[i]
    #print "i"
    #print i
print "pq"
print pq


print "k"
print k


for x in range(width/2):
    for y in range(height):
        t=all_pixels[x+(y*width)]
        all_pixels[x+(y*width)]=all_pixels[k[x]+(y*width)+(width/2)]
        all_pixels[k[x]+(y*width)+(width/2)]=t
cnt=0    
for y in range(height):
    for x in range(width):
        pixels[x,y]=all_pixels[cnt]
        cnt=cnt+1
im.save('C:/Users/Ashish/Desktop/encryptrc4.png')          


for x in range(width/2):
    for y in range(height):
        t=all_pixels[x+(y*width)]
        all_pixels[x+(y*width)]=all_pixels[k[x]+(y*width)+(width/2)]
        all_pixels[k[x]+(y*width)+(width/2)]=t
cnt=0    

cnt=0    
for y in range(height):
    for x in range(width):
        pixels[x,y]=all_pixels[cnt]
        cnt=cnt+1
im.save('C:/Users/Ashish/Desktop/decryptrc4.png') 
        
cnt=0
for y in range(height):
    for x in range(width):
        if key[(width*(y))+x]==1:
            if all_pixels[(width*(y))+x]==0:
                all_pixels[(width*(y))+x]=255
            else:
                all_pixels[(width*(y))+x]=0
        pixels[x,y]=all_pixels[cnt]
        cnt=cnt+1
im.save('C:/Users/Ashish/Desktop/imagedecrypt.png')        
#for a in range(width*2):
#    if a>width:
#        print all_pixels[a]
