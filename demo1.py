values = [1, 2, "ruthel", 4, 5]
# List is data type that allows multiple values and can be different data types
print(values[0])  # 1

print(values[3])  # 4


print(values[-1])  # 5 last number

print(values[1:3])  # 2 ruthel

values.insert(3, "villaespin")  # [1, 2, 'ruthel', 'villaespin', 4, 5]
print(values)

values.append("End")  # [1, 2, 'ruthel', 'villaespin', 4, 5, 'End']
print(values)

values[2] = "RUTHEL"  # Updating
del values[0]  # [2, 'RUTHEL', 'villaespin', 4, 5, 'End']
print(values)

# Tuple - Same as LIST Data type but ummutable
val = (1, 2, "ruth", 4.5)

print(val[1])

# val[2] = "RUTH"


#  DICTIONARY
dic = {"a": 2, 4: "bcs", "c": "Hello World"}
print(dic[4])
print(dic["c"])


#
dict = {}

dict["firstname"] = "Ruth"

dict["lastname"] = "Villa"

dict["gender"] = "Female"

print(dict)
print(dict["lastname"])






