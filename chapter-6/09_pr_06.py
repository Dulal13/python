sub1 = int(input("Enter the mark of sub1 : "))
sub2 = int(input("Enter the mark of sub2 : "))
sub3 = int(input("Enter the mark of sub3 : "))

if (sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
else:
    if((sub1+sub2+sub3)/3 < 40):
        print("You are fail")
    else:
        print("You are pass")