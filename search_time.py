fr=open("fort.13",'r')
fw=open("output.txt",'w')
for line in fr:
   search='CHUNK_SIZE_P2T'
   if search in line:
       fw.write(next(fr))
   search='CHUNK_SIZE_M2M'
   if search in line:
       fw.write(next(fr))
   search='CHUNK_SIZE_M2L'
   if search in line:
       fw.write(next(fr))
   search='CHUNK_SIZE_P2M'
   if search in line:
       fw.write(next(fr))
   search='CHUNK_SIZE_P2T'
   if search in line:
       fw.write(next(fr))

fr.close()
fw.close()
