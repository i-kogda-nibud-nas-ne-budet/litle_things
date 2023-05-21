import re
import docx2txt
#data=open('testKKS.txt', 'r').read()
data=docx2txt.process('kks.docx')
KKS=re.findall('\w\w\w\d\d\w\w\d\d\d',data)
print(KKS)