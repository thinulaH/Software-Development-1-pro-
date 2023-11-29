test_file = open('test.txt','w')
a = 'Hi'
b = 'my'
c = 'name is'
d = 'Thinula'
test_file.write(f"{a} {b} {c} {d}\n")
test_file.write("Finish")
test_file.close()


test_file = open('test.txt','r')
data = test_file.read()
test_file.close()
print(data)
