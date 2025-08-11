full_name= "Leo Messi"
index_1 = full_name.index(" ")
length= len(full_name)
first_name = full_name [0 :index_1]
last_name = full_name[index_1+1:length]
full_name = full_name.replace("Leo", "Leonid")
full_name = full_name.replace("ss","cc")
celeb= "Peer Tasi"
counter= celeb.count("e")

print(first_name)
print(last_name)
print(full_name)
price= "25"
price_as_int= int(price)
final_price= price_as_int+4
print(final_price)

shirt_price= 34
shirt_price_after_tax=34+7
shirt_price_as_str= str(shirt_price)
length_shirt= len(shirt_price_as_str)
print ("test end")