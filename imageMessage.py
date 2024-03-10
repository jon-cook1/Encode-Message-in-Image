from PIL import Image

def encode(img):
    image = Image.open(img)
    encoded = image.copy()
    x = encoded.size[0]
    y = encoded.size[1]

    message = inputMessage((x*y)//8-2)
    binaryStr = msgBinary(message)
    overlay(binaryStr,x,encoded)



def inputMessage(max):
    while True:
        message = input(f"Enter a message to be encoded (max characters: {max})\n> ")
        if len(message) > max:
            print("Message is too long for image\n")
        elif len(message) == 0:
            print("Message is too long for image\n")
        else:
            return message+"%%"

def msgBinary(message):
    binaryStr = ""
    for i in message:
        binaryStr+=toBinary(ord(i))
    return binaryStr


def toBinary(num):
    binStr = bin(num).replace("0b", "")
    leadingzero = ""
    if len(binStr)<8:
        for i in range(8-len(binStr)):
            leadingzero += "0"
    return leadingzero+binStr


def toDec(bin):
    return int(bin,2)



def overlay(binaryStr,width,encoded):
    for i in range(40):
        print(i,encoded.getpixel((i,0)))
    print("")
    pixels = encoded.load()
    x=0
    y=0

    for i in binaryStr:
        if x == width:
            x=0
            y+=1

        color_binary = toBinary(pixels[x,y][0])
        color_binary = color_binary[:-1]+i
        print(toDec(color_binary)) #wtf
        pixels[x,y] = (toDec(color_binary),pixels[x,y][1],pixels[x,y][2])
        x+=1

    encoded.save("images/encoded.jpg")
    for i in range(40):
        print(i,encoded.getpixel((i,0)))


def decode(imgname):
    image = Image.open(imgname)
    for i in range(40):
        print(i,image.getpixel((i,0)))
    binaryStr = getBinMsg(image)
    pixelmsg = ""
    binaryStr += "*"

    while len(binaryStr) > 1:
        current_char = binaryStr[:8]
        binaryStr = binaryStr[8:]
        pixelmsg += chr(toDec(current_char))

        if "%%" in pixelmsg:
            break
    pixelmsg = pixelmsg[:-2]
    print("Decoded Message:\n"+pixelmsg)


def getBinMsg(image):
    binaryStr = ""
    pixels = image.load()

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            color_binary = toBinary(pixels[x,y][0])
            binaryStr += color_binary[-1]
            #if "0010010100100101" in binaryStr: ##binary for % signs signalling end of message
                #return binaryStr

    return binaryStr


def main():
    image_name = "images/tree.jpg"
    #manually wirtten for now, could easily be taken as input
    choice = 3
    notfirst = False
    while choice not in ["1","2"]:
        if notfirst:
            print("Please enter 1 or 2\n")
        choice = input("Would you like to encode or decode [1,2]?\n> ")

    if choice == "1":
        encode(image_name)
    else:
        decode("images/encoded.jpg")

main()
