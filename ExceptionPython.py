
ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:
     # raise Exception("Products Card count not matching")
    pass

# assert - expect a condition

assert(ItemsInCart == 0)

# try, catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Some how I reached this block beacuse there is failure in try block")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up records")






