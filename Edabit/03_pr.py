def area_shape(base, height, shape):
    if(shape=="triangle"):
        return base*height*0.5
    else:
        return base*height

a = area_shape(2.9, 1.3, "parallelogram")
print(a)