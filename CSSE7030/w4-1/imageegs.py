from imagegui import *
#
# See the comments in imagegui.py for downloading the PIL library
#
# im.size is width and height as pair
# im.getdata() gets data as an object like a list of colour triples (RGB)
# im.putdata(data) loads lists of triples into image
#
# alternative - im.load() - pixels as "2D array"


im = Image.open("sarah.jpg")
#display_image(im)


def img2bw(img, rv, gv, bv):
    """Convert img to a black and white image using the given contribution of
    red, green and blue

    img2bw(img, int, int, int) -> None
    """
    total = rv+gv+bv
    rf = rv/total
    gf = gv/total
    bf = bv/total
    data = img.getdata()
    result = []
    for r,g,b in data:
        grey = int(r*rf + g*gf + b*bf)
        #result.append((grey,grey, grey))
        #result.append((grey,0,0)) #- can only see red
        #result.append((grey,0,grey)) #- can only see purple
        # (red,yellow,blue)
    img.putdata(result)

img2bw(im,1,1,1)   
display_image(im)

