length = input("enter the length of rectangles: ").split()
width = input("enter the width of rectangles: ").split()
length = [float(l) for l in length]
width = [float(w) for w in width]
print("Num\t\tLength\t\tWidth\tArea(approx.)\n")
for i in range(len(width)):   #to count how many width user entered to calc. area         #or len(length)
    area=width[i]*length[i]
    print("%3d\t\t%4.2f\t\t%2.1f\t\t%.0f\t\t\t\t"%(i+1,length[i],width[i],area))