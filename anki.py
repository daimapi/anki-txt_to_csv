import csv
import os

paths = []
for file in os.listdir("./txt"):
    if file.endswith(".txt"):
        paths.append(os.path.join("./txt", file))
print(paths)

for path in paths:
    with open(path, "r", encoding="UTF-8") as txtfile:
        with open(
            "./csv/" + txtfile.name.split(".txt")[0].split("./txt")[1] + ".csv",
            "w",
            newline="",
            encoding="UTF-8",
        ) as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for line in txtfile:
                wlist = []
                trans = ""
                c = 0
                prec = c
                for _ in line:
                    if _ == " ":
                        wlist.append(line[prec:c])
                        prec = c + 1
                    c += 1
                wlist.append(line[prec:c])

                print(f"$${wlist}$$")

                c = 0
                prec = c
                for _ in wlist[1]:
                    if _ == ";":
                        trans += wlist[1][prec:c]
                        trans += "<br>"
                        prec = c + 1
                    c += 1
                if trans == "":
                    trans += wlist[1][0 : c + 1]
                else:
                    trans += wlist[1][prec:c]

                trans = (
                    trans
                    + "<br>"
                    + '<div style="text-align: right">'
                    + wlist[2]
                    + "</div>"
                )

                # print(f"$${wlist[0]}$$")
                # print(f"$${wlist[2]}$$")
                # print(f"$${trans}$$")
                print(wlist[0] + "," + "," + trans)
                writer.writerow([wlist[0]] + [] + [trans])
