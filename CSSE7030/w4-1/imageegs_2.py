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
        result.append((grey, grey, grey))
    img.putdata(result)
[(50,0),(100,100),(170,170),(256,256)]


def img2grey(img, rv, gv, bv, cutoff=None):
    """Convert img to a greyscale image using the given contribution of
    red, green and blue

    ...
    """
    # cutoff=None means that cutoff is an option, can have the value or None
    total = rv+gv+bv
    rf = rv/total
    gf = gv/total
    bf = bv/total
    data = img.getdata()
    result = []
    for r,g,b in data:
        grey = int(r*rf + g*gf + b*bf)
        if cutoff is not None:
            for c,g in cutoff:
                if grey < c:
                    grey = g
                    break
        result.append((grey, grey, grey))
    img.putdata(result)

#img2grey(im,1,1,1,cutoff=[(50,0),(100,100),(170,170),(256,256)])

#display_image(im)

