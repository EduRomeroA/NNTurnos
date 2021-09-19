import Red

def obternerTurno():
    import psycopg2
    from datetime import datetime
#from config import config
    conexion = psycopg2.connect(host="185.253.154.87", database="DBMovil", user="DBTesis2021", password="DBTesis2021",port="5432")
# Creamos el cursor con el objeto conexion
    cur = conexion.cursor()

# Ejecutamos una consulta
    cur.execute( "SELECT idturno,idusuario,fecharegistro,fechaturno,idclinica,estado,idespecialidades,idhorario FROM turnos where estado='P'" )
    i=0
    prueba=[]
    p=[]
# Recorremos los resultados y los mostramos
    for idturno,idusuario,fecharegistro,fechaturno,idclinica,estado,idespecialidades,idhorario in cur.fetchall() :
        r = fecharegistro
        r = int(r.strftime('%Y%m%d'))
   
        if(fechaturno == None):
            prueba.append({"idturno":idturno,"idusuario":idusuario,"fechaturno":r,"estado":estado,"idhorario":idhorario})
            print(r,"RRR")
    
        p.append(r)

        i=i+1
        print ((idturno,idusuario,fecharegistro,fechaturno,idclinica,estado,idespecialidades,idhorario),'todo')
    
        idt=idturno
    
        prueba1=[[idusuario],[r]]
        resultado = Red.modelo.predict(prueba1[1])
        s=int(resultado[0])


        #print(resultado,"resultado")
        #print(s)
        ft=Red.int2date(s)
        print(ft)
        i=i+1
        sql="UPDATE turnos set fechaturno= %s where idturno=%s and estado='P'"
        datos=(ft,idt)
        print(datos)

        cur.execute(sql,datos)
        conexion.commit()
    

# Cerramos la conexión
    conexion.close()

    print(prueba,'prueba')
    print(p)
    a = datetime.now()
    print(a)
    return prueba

