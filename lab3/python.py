fo = open ('/mit/ylwu/6.004/lab3/script.txt', "r+")
print "Name of the file:", fo.name

fo.seek(0,0)
for index in range(31):
    plus = index+1
    minus = 31-index
    fo.write("XAND%d A[%d:0] B%d#%d P%d_[31:%d] and2\n" %(index,minus,index,minus+1,index,index))
    fo.write("XFA%d P%d_[31:%d] s%d_[31:%d] 0 co%d_[30:%d] s%d_[31:%d] out%d co%d_[31:%d]\n" %(index, index ,index, index-1, index, index, index, index, plus, index, index, index))

fo.close()
