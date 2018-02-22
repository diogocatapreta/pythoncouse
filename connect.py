import cx_Oracle


con = cx_Oracle.connect('xxml/mldesenvxxml@mldebspkg/MLDEBS')
print (con.version)
con.close()