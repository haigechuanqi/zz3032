def getBondDuration(y,face,couponRate,m,ppy=1):
    cf = face*couponRate
    pvcfsum = 0
    pv_t = 0
    for i in range(1,m):
            pv = cf/(1+y)**(i)
            pvcfsum = pvcfsum+pv
            bp = pvcfsum + (face+cf)/(1+y)**m
            pv_t =  pv_t+pv*i
    pv_t1 = pv_t + m* (face+cf)/(1+y)**m
    duration = pv_t1/bp
    return(duration)
    
    