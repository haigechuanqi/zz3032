def getBondPrice_Z(face, couponRate, times, yc):
    pvsum = 0
    cf = face*couponRate
    zipped = zip(yc, times)
    for (a,b) in zipped:
        mult = (1+a)**-b
        pv = mult*cf
        pvsum = pvsum +pv
    bp = pvsum + mult*face
    return(bp)

