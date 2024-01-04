from PyPDF2 import PdfMerger
birlestirme= PdfMerger()
ilk=open("ilki.pdf","rb")
ikincisi=open("ikincisi.pdf","rb")
#Eğer pdfleri tamamen birleştirmek istersen:
birlestirme.append(ilk)
birlestirme.append(ikincisi)
birlestirme.write("yeni.pdf")


#Eğer pdfi diğer pdfin belirli bir sayfasına eklemek istersen
birlestirme.append(ilk)
birlestirme.merge(0,ikincisi)
birlestirme.write("yeni2.pdf")