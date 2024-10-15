import os
dir_list = os.listdir()
folders = []
table = [[]]
cols = 5
img_names = []
for directory in dir_list:
    if os.path.isdir(directory):
        f = open(directory + "/README.md", "r", encoding="utf-8")
        v = f.read()
        f.close()
        i = v.find("https://books.mgbot.ru/images/")
        if i != -1:
            i += 30 - 1
            s = ""
            while ".PNG" not in s:
                i += 1
                s += v[i]
            img_names.append(s)
            folders.append(directory)
            if len(table[-1]) < cols:
                table[-1].append(directory)
            else:
                table.append([directory])
print(folders, len(folders))
print(table)

md = ""
for row in table:
    md += "|"
    for val in row:
        md += f' [{val}](https://github.com/MAKblC/Codes/tree/master/{val.replace(" ", "%20")}) |'
    md += "\n|"
    for _ in row:
        md += " --- |"
    md += "\n|"
    for val in row:
        md += f' [![Device image](https://books.mgbot.ru/images/{img_names[folders.index(val)]})](https://github.com/MAKblC/Codes/tree/master/{val.replace(" ", "%20")}) |'
    md += "\n\n"

with open("modules.md", "w") as file:
    file.write(md)
    file.close()