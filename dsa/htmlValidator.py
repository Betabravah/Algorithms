from StackLab import stack

def htmlValidator(string):
    temp = ""
    tempStack = stack()
    i = 0
    empty_tags = ["img", "meta", "link", "hr", "br", "area", "base", "col", "embed", "input", "keygen", "param", "source", "track", "wbr"]
    while i < len(string):
        if string[i] == "<":
            if string[i+1] == "/":
                i += 2
                while i < len(string) and string[i] != ">":
                    temp += string[i]
                    i += 1
                if i < len(string) and string[i] == ">":
                    if tempStack.peek() == temp:
                        tempStack.pop()
                        temp = ""
                    else:
                        return False
                else:
                    return False
            else:
                i += 1
                while i < len(string) and string[i] != ">":
                    if string[i] == " ":
                        tempStack.push(temp)
                        temp = ""
                        break
                    else:
                        temp += string[i]
                    i += 1
                if i < len(string) and string[i] == ">":
                    if temp in empty_tags:
                        continue
                    else:
                        tempStack.push(temp)
                        temp = ""
        else:
            i += 1
    return tempStack.isEmpty()

with open("sample_html.py") as file:
        string = file.read()
        print(htmlValidator(string))
                
# print(htmlValidator("<html> ufhoseiu </html>"))
# print(htmlValidator("<html> <p> ufho </p> </html>"))
# print(htmlValidator("<html> ufhoseiu </html"))
# print(htmlValidator("<html> ufhoseiu <p> </html>"))
# print(htmlValidator("<a href> ufho </a>"))
# print(htmlValidator("<a href> ufho <a>"))
# print(htmlValidator("<img>"))


