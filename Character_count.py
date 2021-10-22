#Có thể dùng cách này để count the occurrences of character in string variable. The scale can raise up the milion characters.
import pprint #dùng pprint module có thể sử dụng các function of module này để giúp print ra đẹp và rõ ràng hơn.
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
# pprint.pprint(count)
print(pprint.pformat(count))
m = 2+2