
from PIL import Image
im = Image.open('E:\suits4.png').convert('L')
#im=im.convert('1')

im.save('E:\mobivision\image1.png')

pixels = im.load()
width, height=im.size

gp=[]
key=[0]*(width*height)
all_pixels=[]
c=0
for y in range(height):
    for x in range(width):
        cpixel=pixels[x,y]
        all_pixels.append(cpixel)
        gp.append(cpixel)
        key[c]=0
        if all_pixels[c]<127:
            all_pixels[c]=0
        else:
            all_pixels[c]=255
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
im.save('E:\mobivision\encrypt(Rule30).jpeg')

pq = list()
pq=[0]*(width/2)
print pq


print "\nEnter Key 1 (RC4)"
ss1=raw_input()
key1=list()
for i in range(0,len(ss1)):
    key1.append(ord(ss1[i]))
#print key1
lk1=len(key1)

print "\nEnter Key 2 (RC4)"
ss2=raw_input()
key2=list()
for i in range(0,len(ss2)):
    key2.append(ord(ss2[i]))
#print key2
lk2=len(key2)


#print "\nInitializing S"
s1=list()
s2=list()
for i in range(0,(width/2)):
    s1.append(int(i))
    s2.append(int(i))
#print s1
print
#print s2
#print "Initialized"

#print "\nShuffling S"
j1=0
j2=0
for i in range(0,(width/2)-1):
    j1=(j1+s1[i]+key1[i%lk1])%(width/2)
    s1[i],s1[j1]=s1[j1],s1[i]
    j2=(j2+s2[i]+key2[i%lk2])%(width/2)
    s2[i],s2[j2]=s2[j2],s2[i]
print "s1",s1
print
print "s2",s2
#print "Shuffled"

#print "\nPRGA"
#print "\nShuffling S Again"
i=0
j1=0
j2=0
a=0
k=list()
while a<(width/2):
    i=(i+1)%(width/2)
    j1=(j1+s1[i])%(width/2)
    s1[i],s1[j1]=s1[j1],s1[i]
    j2=(j2+s2[i])%(width/2)
    s2[i],s2[j2]=s2[j2],s2[i]
    stream1=s1[(s1[i]+s1[j1])%(width/2)]
    stream2=s2[(s2[i]+s2[j2])%(width/2)]

    s1[s2[j1]],s1[s2[j2]]=s1[s2[j2]],s1[s2[j1]]
    s2[s1[j1]],s2[s1[j2]]=s2[s1[j2]],s2[s1[j1]]

    
    k.append((stream1^stream2)%(width/2))
    pq[k[a]]=pq[k[a]]+1
    a=a+1
#print "Shuffled Again\n"

#print "Key RC4: ",k



print "\nPQ"
print pq
s1=0
s2=0
for i in range(width/2):
    if pq[i]==0:
        s1=s1+1
    if pq[i]>1:
        s2=s2+1
print "S1",s1
print "s2",s2

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
    #print i
    #print pq[j]
    #print pq[i]
    #print "i"
    #print i

print "pq",pq

print "width/2",width/2
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
im.save('E:\mobivision\encryptrc4.jpeg')          


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
im.save('E:\mobivision\decryptrc4 - Rule30.jpeg') 
        
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
im.save('E:\mobivision\imagedecrypt.jpeg')

cnt=0    
for y in range(height):
    for x in range(width):
        pixels[x,y]=gp[cnt]
        cnt=cnt+1
im.save('E:\mobivision\greydecrypt.jpeg')

#for a in range(width*2):
#    if a>width:
#        print all_pixels[a]
