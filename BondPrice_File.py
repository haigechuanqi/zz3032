def getBondPrice(y,face,couponRate,m,ppy=1):
   cf = face*couponRate
   pvcfsum = 0
   if ppy==1:
       for i in range(1,m):
           pv = cf/(1+y)**(i)
           pvcfsum = pvcfsum+pv
           bp = pvcfsum + (face+cf)/(1+y)**m
   if ppy==2:
       cf = cf/2
       y = y/2
       m = m*2
       for i in range(1,m):
               pv = cf/(1+y)**(i)
               pvcfsum = pvcfsum+pv
               bp = pvcfsum + (face+cf)/(1+y)**m
   return(bp)
           
           
           
          