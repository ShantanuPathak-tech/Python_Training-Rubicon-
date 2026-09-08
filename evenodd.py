number = int(input());

if number % 2 == 0:
    print("The number is even");
else:
    print("The number is odd")
    

if number > 0:
    print("The number is positive");
else:
    print("The number is negative");
    
for i in range(100):
    if i % 2 == 0:
        print(i);
        
        
str1 = "Hello";
str2 = "Python";
print(str1 + str2);
print(str2[0:3]);
print(str2.find("tho"));
print(str2.capitalize());
print(str2.title());
#print(str2.Lowercase());

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}  x  {j}  = {i*j}");

