import re

f = open("C:\\Users\\khan\\Downloads\\abc.txt", "r", encoding="utf8")
txt = f.read()

# txt = "https://youtu.be/7hCknPVDFZ4"
vids = re.findall("""((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)""", txt)
for vid in vids:
    print('"'+vid[3]+'"')

print(len(vids))
