line = {
    #"0":"░░",
    "a":"═",
    "b":"║",
    "c1":"╔",
    "c2":"╚",
    "d1":"╗",
    "d2":"╝",
    "e1":"╦",
    "e2":"╩",
}

def replacer(s, newstring, index):
    return s[:index] + newstring + s[index + 1:]

def makewidth(width: int,hend:bool=False,reverse: bool = False):
    start =""
    end = ""
    if hend != True:
        if reverse == True:
            start = line["c2"]
            end = line["d2"]
        else:
            start = line["c1"]
            end = line["d1"]
    output = line["a"]*width
    return f"{start}{output}{end}"

def makeheight(height: int,hend:bool=False):
    start =""
    end = ""
    if hend == True:
        start = f'{line["e1"]}\n'
        end = line["e2"]
    output = f'{line["b"]}\n'*height
    return f"{start}{output}{end}"

def makespace(width: int):
    return " "*width

'''
def box_(width: int,height : int):
    w=makewidth(width)
    ww=makewidth(width,reverse=True)
    h="" #makeheight(height)
    for _ in range(height):
        h+= f'{line["b"]}{makespace(width)}{line["b"]}\n'
    return f"{w}\n{h}{ww}"
'''

def box1(items:list,width: int=0):
    maxwlength_a=0
    for item in items:
        a=len(item)+2
        if a > maxwlength_a:
            maxwlength_a = a
    h=""
    wlen = width or maxwlength_a
    w=makewidth(wlen)
    ww=makewidth(wlen,reverse=True)
    for item in items:
        h+= f'{line["b"]} {item}{makespace(wlen-len(item)-2)} {line["b"]}\n'
    return f"{w}\n{h}{ww}"

def box2(items:dict):
    maxwlength_a=0
    maxwlength_b=0
    maxwlength_=0
    itemss={}
    for item in items:
        itemss[item] = {"name":items[item],"widtha":len(item)+3,"widthb":len(items[item])+2}
        a=len(item)+3
        if a > maxwlength_a:
            maxwlength_a = a
        item=items[item]
        b=len(item)+2
        if b > maxwlength_b:
            maxwlength_b = b
    maxwlength_=maxwlength_a+maxwlength_b
    h=""
    for item in itemss:
        item_ = itemss[item]
        h+= f'{line["b"]} {item}{makespace(maxwlength_a-item_["widtha"])} {line["b"]} {item_["name"]}{makespace(maxwlength_b-item_["widthb"])} {line["b"]}\n'
    index=h.split('\n')[0].find(line["b"],2)
    w=replacer(makewidth(maxwlength_), line["e1"], index)
    ww=replacer(makewidth(maxwlength_,reverse=True), line["e2"], index)
    return f"{w}\n{h}{ww}"

if __name__ == "__main__":
    print(box1(["test1","test22","test333"]))
    print(box1(["test1","test22","test333"],20))
    print(box2({"test1":"> bruh 1","test22":"> bruh 222","test333":"> this bruh 333333"}))
