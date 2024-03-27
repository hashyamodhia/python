# f = open ("funny.txt", "w")
# f.write("I love Python")
# f.close()

# f = open ("funny.txt", "a")
# f.write("\nI love C")
# f.close()

# f = open ("funny.txt", "r")
# for line in f:
#     print(line)
# f.close()

# f = open ("funny.txt", "r")

# for line in f:
#     tokens = line.split(' ')
#     print(tokens)
    
# f.close()

# f = open ("funny.txt", "r")
# f_out = open ("funny_wc.txt", "w")

# for line in f:
#     tokens = line.split(' ')
#     f_out.write("WordCount: " + str(len(tokens)) + ' ' + line)
    
# f.close()
# f_out.close()

with open("/home/hashyamodhia/Desktop/Data Engineering/Codebasics/python/fileio/funny.txt", "r") as f:
    print(f.read())

print(f.closed)