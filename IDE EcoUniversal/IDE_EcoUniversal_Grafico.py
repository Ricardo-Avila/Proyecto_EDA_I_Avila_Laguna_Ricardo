#--------------------------------Modulos----------------------------------------
from tkinter import *
from tkinter import messagebox
from datetime import *
import pickle
#--------------------------------Variables--------------------------------------
#Gracias a los dueños de las imagenes
#https://www.cronista.com/columnistas/La-compraventa-de-energia-renovable-como-una-ventana-de-oportunidades-20170613-0006.html
#https://www.freepik.es/vector-premium/automatizacion-empresa-eficaz-dibujos-animados-plana_4295232.htm
#https://www.osi.es/es/actualidad/blog/2014/09/19/te-contamos-por-que-es-importante-tener-diferentes-usuarios-en-tu-ordenador
#https://www.shutterstock.com/es/image-vector/cartoon-people-group-carrying-cash-dollars-1500288197
#https://www.dreamstime.com/illustration/money-withdrawal.html
#https://www.pinterest.com.mx/pin/393290979948930565/
#https://www.freepik.es/fotos-vectores-gratis/iconos-medio-ambiente
#--------------------------------Video--------------------------------------
#https://invoicehome.com/recibo
#https://iniciativafiscal.com/notificaciones-electronicas/
#https://abogados-de-madrid.net/que-es-la-fusion-de-empresas-que-tramites-conlleva/
#https://www.sonpersonitas.com/organizar-los-trabajos-de-los-ninos/
#https://www.freepik.es/fotos-vectores-gratis/iconos-medio-ambiente
#https://audiojungle.net/item/modern-upbeat-corporate-background/18060265?irgwc=1&clickid=SnF1gTWwixyORzCwUx0Mo3chUki1syzzUwm0100&iradid=275988&irpid=1262510&iradtype=ONLINE_TRACKING_LINK&irmptype=mediapartner&mp_value1=&utm_campaign=af_impact_radius_1262510&utm_medium=affiliate&utm_source=impact_radius
#https://www.ingenieria.unam.mx/
#https://web.facebook.com/UPE.UNAM/?_rdc=1&_rdr
#https://www.randstad.es/tendencias360/claves-de-una-empresa-unicornio/
#https://siglonuevo.mx/nota/1978.empresas-sustentables-en-mexico
#https://www.leonardo-gr.com/es/blog/el-impacto-medioambiental-del-papel
#https://www.dinero.com/empresas/articulo/rentabilidad-o-crecimiento-esa-es-la-cuestion-por-oliverio-gonzalez/231592

usuario = {}
empresa = {}
lista_ides = []
global genero
global nombre
global apellido1
global apellido2
global edad
global telefono
global estado
global municipio
IDE = ''
global contraseña
global nombre_empresa
global tipo_empresa
global empleados
global lider
global edad_empresa
global telefono_empresa
global estado_empresa
global municipio_empresa
global contraseña_empresa
global ingresar
#--------------------------------Cargar datos-----------------------------------
archivo_1 = open('memoria_usuarios.p','rb')
usuario = pickle.load(archivo_1)
archivo_1.close()
archivo_2 = open('ides_usuarios.p','rb')
lista_ides = pickle.load(archivo_2)
archivo_2.close()
archivo_3 = open('memoria_empresas.p','rb')
empresa = pickle.load(archivo_3)
archivo_3.close()

for i in range(0,len(lista_ides)):
    if lista_ides[i][0] == '1' or lista_ides[i][0] == '3':
        print('#{} USUARIO[{}]: {}'.format(i+1,lista_ides[i],usuario[lista_ides[i]]))
        print()
    else:
        print('#{} EMPRESA[{}]: {}'.format(i+1,lista_ides[i],empresa[lista_ides[i]]))
        print()
#---------------------------Funciones de Mensjaes-------------------------------
def guardarDatos():
    archivo_1 = open('memoria_usuarios.p','wb')
    pickle.dump(usuario,archivo_1)
    archivo_1.close()
    archivo_2 = open('ides_usuarios.p','wb')
    pickle.dump(lista_ides,archivo_2)
    archivo_2.close()
    archivo_3 = open('memoria_empresas.p','wb')
    pickle.dump(empresa,archivo_3)
    archivo_3.close()
    messagebox.showinfo('Guardar','Datos Guardados')

def infoAdicional():
    messagebox.showinfo('IDE EcoUniversal','Dueño del Programa: Pse.Ing. Avila Laguna Ricardo\nHecho por: Pse.Ing. Avila Laguna Ricardo\nDirigido por: Mtro.Ing.Marco Antonio Martinez Quintana\n\t*UNIDAD DE PLANEACION ENERGETICA*\n\t**FACULTAD DE INGENIERIA**\n***UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO***')

def avisoLicencia():
    messagebox.showwarning('Licencia','Producto bajo licencia GNU')
#--------------------------------Funciones--------------------------------------
def Numero_estado(estado):
    estados = ( ('aguascalientes',0),('baja california norte',1),('baja california sur',2),('campeche',3) ,
    ('coahuila',4),('colima',5),('chiapas',6),('chihuahua',7),('cdmx',8),('durango',9),('guanajuato',10),
    ('guerrero',11),('hidalgo',12),('jalisco',13),('mexico',14),('michoacan',15),('morelos',16),('nayarit',17),
    ('nuevo leon',18),('oaxaca',19),('puebla',20),('queretaro',21),('quintana roo',22),('san luis potosi',23),
    ('sinaloa',24),('sonora',25),('tabasco',26),('tamaulipas',27),('tlaxcala',28),('veracruz',29),('yucatan',30),('zacatecas',31) )
    for i in range(0,32):
        if estado == estados[i][0]:
            num = estados[i][1]
    return num

def Pagar_u(u_e,ide_p,cantidad,con):
    global IDE
    cant = float(cantidad)
    n=Descontar_u(cantidad)
    encontro=0
    if n == 1:
        for c in range(0,(len(lista_ides))):
            if ide_p == lista_ides[c]:
                if u_e == 'usuario' or u_e == 'USUARIO' or u_e == 'Usuario':
                    usuario[ide_p]['dinero'] += cant
                    mensaje = '-DATOS DE PAGO-  Usuario: {}      IDE: {}     Cantidad de deposito: $ {} [{}]'.format(usuario[IDE]['nombre'],IDE,cant,date.today())
                    usuario[ide_p]['mensajes'].append(mensaje)
                    messagebox.showinfo('Mensaje','Pago exitoso!')
                    encontro=1
                    #print('Pago de {} concretado a el usuario {} con el IDE {}'.format(cantidad,usuario[ide_p]['nombre'],ide_p))
                elif u_e == 'empresa' or u_e == 'EMPRESA' or u_e == 'Empresa':
                    empresa[ide_p]['dinero'] += cant
                    mensaje = '-DATOS DE PAGO-  Usuario: {}      IDE: {}     Cantidad de deposito: $ {} [{}]'.format(usuario[IDE]['nombre'],IDE,cant,date.today())
                    empresa[ide_p]['mensajes'].append(mensaje)
                    messagebox.showinfo('Mensaje','Pago exitoso!')
                    encontro=1
                    #print('Pago de {} concretado a la empresa {} con el IDE {}'.format(cantidad,empresa[ide_p]['nombre_empresa'],ide_p))
                break
    if encontro == 0:
        messagebox.showwarning('Proceso Inconcluso','Ide No Encntrado')
    return 0

def Pagar_e(u_e,ide_p,cantidad):
    global IDE
    cant = float(cantidad)
    n=Descontar_e(cantidad)
    encontro=0
    if n == 1:
        for c in range(0,(len(lista_ides))):
            if ide_p == lista_ides[c]:
                if u_e == 'usuario' or u_e == 'USUARIO' or u_e == 'Usuario':
                    usuario[ide_p]['dinero'] += cant
                    mensaje = '-DATOS DE PAGO-  Empresa: {}      IDE: {}     Cantidad de deposito: $ {} [{}]'.format(empresa[IDE]['nombre_empresa'],IDE,cant,date.today())
                    usuario[ide_p]['mensajes'].append(mensaje)
                    messagebox.showinfo('Mensaje','Pago exitoso!')
                    encontro=1
                    #print('Pago de {} concretado al usuario {} con el IDE {}'.format(cantidad,usuario[ide_p]['nombre'],ide_p))
                elif u_e == 'empresa' or u_e == 'EMPRESA' or u_e == 'Empresa':
                    empresa[ide_p]['dinero'] += cant
                    mensaje = '-DATOS DE PAGO-  Empresa: {}      IDE: {}     Cantidad de deposito: $ {} [{}]'.format(empresa[IDE]['nombre_empresa'],IDE,cant,date.today())
                    empresa[ide_p]['mensajes'].append(mensaje)
                    messagebox.showinfo('Mensaje','Pago exitoso!')
                    encontro=1
                    #print('Pago de {} concretado a la empresa {} con el IDE {}'.format(cantidad,empresa[ide_p]['nombre_empresa'],ide_p))
                break
    if encontro == 0:
        messagebox.showwarning('Proceso Inconcluso','Ide No Encntrado')
    return 0

def Descontar_u(cantidad):
    global IDE
    can = float(cantidad)
    if  usuario[IDE]['dinero'] >= can:
        usuario[IDE]['dinero'] -= can
        n=1
    else:
        messagebox.showwarning('Proceso Inconcluso','No tienes suficientes fondos')
        n=0
    return n

def Descontar_e(cantidad):
    global IDE
    can = float(cantidad)
    if  empresa[IDE]['dinero'] >= can:
        empresa[IDE]['dinero'] -= can
        n=1
    else:
        messagebox.showwarning('Proceso Inconcluso','No tienes suficientes fondos')
        n=0
    return n

def Cobrar_u(u_e,ide_p,cantidad):
    global IDE
    encontrar=0
    for c in range(0,(len(lista_ides))):
        if lista_ides[c] == ide_p:
            if u_e == 'usuario' or u_e == 'USUARIO' or u_e == 'Usuario':
                mensaje = '-DATOS DE COBRO-  Usuario: {}      IDE: {}     Cantidad de cobro: $ {} [{}]'.format(usuario[IDE]['nombre'],IDE,cantidad,date.today())
                usuario[ide_p]['mensajes'].append(mensaje)
                messagebox.showinfo('Mensaje','Mensaje de Cobro enviado!')
                encontrar=1
                #print('Mensaje de Cobro enviado')
            elif u_e == 'empresa' or u_e == 'EMPRESA' or u_e == 'Empresa':
                mensaje = '-DATOS DE COBRO-  Usuario: {}      IDE: {}     Cantidad de cobro: $ {} [{}]'.format(usuario[IDE]['nombre'],IDE,cantidad,date.today())
                empresa[ide_p]['mensajes'].append(mensaje)
                messagebox.showinfo('Mensaje','Mensaje de Cobro enviado!')
                encontrar=1
                #print('Mensaje de Cobro enviado')
            break
    if encontrar == 0:
        messagebox.showwarning('Proceso Inconcluso','Ide No Encntrado')
        #print('Ide Incorrecto')
    return 0

def Cobrar_e(u_e,ide_p,cantidad):
    global IDE
    encontro=0
    for c in range(0,(len(lista_ides))):
        if lista_ides[c] == ide_p:
            if u_e == 'usuario' or u_e == 'USUARIO' or u_e == 'Usuario':
                mensaje = '-DATOS DE COBRO-  Empresa: {}  ({})      IDE: {}     Cantidad de cobro: $ {} [{}]'.format(empresa[IDE]['nombre_empresa'],empresa[IDE]['tipo_empresa'],IDE,cantidad,date.today())
                usuario[ide_p]['mensajes'].append(mensaje)
                messagebox.showinfo('Mensaje','Mensaje de Cobro enviado!')
                encontro=1
                #print('Mensaje de Cobro enviado')
            elif u_e == 'empresa' or u_e == 'EMPRESA' or u_e == 'Empresa':
                mensaje = '-DATOS DE COBRO-  Empresa: {}  ({})      IDE: {}     Cantidad de cobro: $ {} [{}]'.format(empresa[IDE]['nombre_empresa'],empresa[IDE]['tipo_empresa'],IDE,cantidad,date.today())
                empresa[ide_p]['mensajes'].append(mensaje)
                messagebox.showinfo('Mensaje','Mensaje de Cobro enviado!')
                encontro=1
                #print('Mensaje de Cobro enviado')
            break
    if encontro == 0:
        messagebox.showwarning('Proceso Inconcluso','Ide No Encntrado')
            #print('Ide Incorrecto')
    return 0

def abrirVentana_raiz():
    def abrirVentana_ingresar_d():
        raiz.destroy()
        abrirVentana_ingresar()
    def abrirVentana_registrar_d():
        raiz.destroy()
        abrirVentana_registrar()
    raiz=Toplevel()
    raiz.iconbitmap('ide_a.ico')
    raiz.title('IDE EcoUniversal')
    raiz.geometry('710x390')
    barraMenu=Menu(raiz)
    #-----------------------BARRA---------------------------------
    raiz.config(background='dark turquoise',menu=barraMenu)
    def salirAplicacion():
        valor=messagebox.askokcancel('Cerrar','Deseas cerrar la Aplicacion')
        if valor == True:
            raiz.destroy()

    def cerrarDocumento():
        valor=messagebox.askretrycancel('Reintentar','No es posible cerrar. Documento bloqueado')
        if valor == False:
            raiz.destroy()

    archivoArchivo=Menu(barraMenu,tearoff=0)
    archivoArchivo.add_command(label='Nuevo')
    archivoArchivo.add_command(label='Guardar Datos',command=guardarDatos)
    archivoArchivo.add_separator()
    archivoArchivo.add_command(label='Cerrar',command=cerrarDocumento)
    archivoArchivo.add_command(label='Salir',command=salirAplicacion)

    archivoEdicion=Menu(barraMenu,tearoff=0)
    archivoEdicion.add_command(label='Cortar')
    archivoEdicion.add_command(label='Copiar')
    archivoEdicion.add_command(label='Pegar')

    archivoHerramientas=Menu(barraMenu,tearoff=0)
    archivoHerramientas.add_command(label='Extraer')
    archivoHerramientas.add_command(label='Importar')
    archivoHerramientas.add_command(label='Panel')

    archivoAyuda=Menu(barraMenu,tearoff=0)
    archivoAyuda.add_command(label='Licencia',command=avisoLicencia)
    archivoAyuda.add_command(label='Ayuda')
    archivoArchivo.add_separator()
    archivoAyuda.add_command(label='Acerca de IDE EcoUniversal',command=infoAdicional)

    barraMenu.add_cascade(label='Archivo',menu=archivoArchivo)
    barraMenu.add_cascade(label='Edicion',menu=archivoEdicion)
    barraMenu.add_cascade(label='Herramientas',menu=archivoHerramientas)
    barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)
    #-----------------------Grafico---------------------------------
    bienvenida1=Label(raiz,text='  BIENVENIDO ',bg='green',font=('Comic Sans MS',30)).place(x=10,y=40)
    bienvenida2=Label(raiz,text='A ',bg='green',font=('Comic Sans MS',30)).place(x=70,y=100)
    bienvenida3=Label(raiz,text='IDE EcoUniversal',bg='green',font=('Comic Sans MS',30)).place(x=10,y=160)
    imagen_raiz1=PhotoImage(file='raiz1.gif')
    imagen_raiz1_l=Label(raiz,image=imagen_raiz).place(x=340,y=40)
    botonRegistrarse=Button(raiz,text='Registrarse',relief='solid',font=(80),command=abrirVentana_registrar_d).place(x=150,y=310)
    botonIngresar=Button(raiz,text='Ingresar',relief='solid',font=(80),command=abrirVentana_ingresar_d).place(x=500,y=310)

#-----------------------Funciones Graficadoras----------------------------------
#---------------------------------INGRESAR--------------------------------------

def abrirVentana_ingresar():
    emr = IntVar()
    def regresar():
        ingresar.destroy()
        abrirVentana_raiz()
    def Verificar_u(ide_p,contra):
        global IDE
        for a in range(0,(len(lista_ides))):
            if  ide_p == lista_ides[a]:
                if contra == usuario[lista_ides[a]]['contraseña']:
                    IDE = str(ide_p)
                    ingresar.destroy()
                    abrirVentana_menu_Usuario()
                    return 1
                else:
                    messagebox.showwarning('Cuidado','Contraseña incorrecta')
                    return 0
        if ide_p != lista_ides[a]:
            messagebox.showwarning('Cuidado','IDE incorrecta')
        return 0
    def Verificar_e(ide_p,contra):
        global IDE
        print(len(lista_ides))
        for a in range(0,(len(lista_ides))):
            if  ide_p == lista_ides[a]:
                if contra == empresa[lista_ides[a]]['contraseña_empresa']:
                    IDE = str(ide_p)
                    ingresar.destroy()
                    abrirVentana_menu_Empresa()
                    return 1
                else:
                    messagebox.showwarning('Cuidado','Contraseña incorrecta')
        if ide_p != lista_ides[a]:
            messagebox.showwarning('Cuidado','IDE incorrecta')
        return 0

    def cuestionario():
        if emr.get() == 1:
            ide_l=Label(ingresar,text='Ingresa tu IDE:',bg='light goldenrod',font=(50),relief='solid')
            ide_l.grid(row=2,column=0,padx=5,pady=5,ipadx=5,ipady=5)
            cuadro_ide=Entry(ingresar,bg='RoyalBlue1',font=(50),relief='solid')
            cuadro_ide.grid(row=2,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            contras=Label(ingresar,text='Ingresa tu Contraseña:',bg='light goldenrod',font=(50),relief='solid')
            contras.grid(row=3,column=0,padx=5,pady=5,ipadx=5,ipady=5)
            cuadro_contras=Entry(ingresar,bg='RoyalBlue1',show='*',font=(50),relief='solid')
            cuadro_contras.grid(row=3,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            verificar=Button(ingresar,text='Entrar',relief='solid',command=lambda:Verificar_u(cuadro_ide.get(),cuadro_contras.get()))
            verificar.grid(row=4,column=1,padx=5,pady=5,ipadx=5,ipady=5)
        elif emr.get() == 2:
            ide_l=Label(ingresar,text='Ingresa tu IDE:',bg='light goldenrod',font=(50),relief='solid')
            ide_l.grid(row=2,column=0,padx=5,pady=5,ipadx=5,ipady=5)
            cuadro_ide=Entry(ingresar,bg='RoyalBlue1',font=(50),relief='solid')
            cuadro_ide.grid(row=2,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            contras=Label(ingresar,text='Ingresa tu Contraseña:',bg='light goldenrod',font=(50),relief='solid')
            contras.grid(row=3,column=0,padx=5,pady=5,ipadx=5,ipady=5)
            cuadro_contras=Entry(ingresar,bg='RoyalBlue1',show='*',font=(50),relief='solid')
            cuadro_contras.grid(row=3,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            verificar=Button(ingresar,text='Entrar',relief='solid',command=lambda:Verificar_e(cuadro_ide.get(),cuadro_contras.get()))
            verificar.grid(row=4,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    raiz.withdraw()
    ingresar=Toplevel()
    ingresar.iconbitmap('ide_a.ico')
    ingresar.geometry('470x250')
    barraMenu=Menu(ingresar)
    ingresar.config(background='gold',menu=barraMenu)
    #-----------------------BARRA---------------------------------
    def salirAplicacion():
        valor=messagebox.askokcancel('Cerrar','Deseas cerrar la Aplicacion')
        if valor == True:
            ingresar.destroy()

    def cerrarDocumento():
        valor=messagebox.askretrycancel('Reintentar','No es posible cerrar. Documento bloqueado')
        if valor == False:
            ingresar.destroy()

    archivoArchivo=Menu(barraMenu,tearoff=0)
    archivoArchivo.add_command(label='Nuevo')
    archivoArchivo.add_command(label='Guardar Datos',command=guardarDatos)
    archivoArchivo.add_separator()
    archivoArchivo.add_command(label='Cerrar',command=cerrarDocumento)
    archivoArchivo.add_command(label='Salir',command=salirAplicacion)

    archivoAyuda=Menu(barraMenu,tearoff=0)
    archivoAyuda.add_command(label='Licencia',command=avisoLicencia)
    archivoAyuda.add_command(label='Ayuda')
    archivoArchivo.add_separator()
    archivoAyuda.add_command(label='Acerca de IDE EcoUniversal',command=infoAdicional)

    barraMenu.add_cascade(label='Archivo',menu=archivoArchivo)
    barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)
    #-----------------------CODIGO---------------------------------
    bienvenida1=Label(ingresar,text='INGRESAR',bg='pink',font=(70),relief='solid')
    bienvenida1.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
    UoE=Label(ingresar,text='Usuario o Empresa',bg='pink',font=(50),relief='solid')
    UoE.grid(row=0,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(ingresar,text='Usuario',variable=emr,value=1,command=cuestionario,font=(50),bg='gold')
    opcion_u.grid(row=1,column=0,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_e=Radiobutton(ingresar,text='Empresa',variable=emr,value=2,command=cuestionario,font=(50),bg='gold')
    opcion_e.grid(row=1,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(ingresar,text='ATRAS',relief='solid',command=regresar)
    botonDestruir.grid(row=4,column=2,padx=5,pady=5,ipadx=5,ipady=5)
#--------------------------------REGISTRAR--------------------------------------

def abrirVentana_registrar():
    emp = IntVar()
    def regresar():
        registrar.destroy()
        abrirVentana_raiz()
    def crearIDE_u(contrase,genero,nombre,apellido1,apellido2,edad,telefono,estado,municipio):
        global IDE
        today = date.today()
        year = today.year
        mon = today.month
        day = today.day
        if  genero == 'M' or genero == 'Masculino' or genero == 'masculino' or genero == 'MASCULINO':
            g1 = 10
        elif genero == 'F' or genero == 'Femenino' or genero == 'femenino' or genero == 'FEMENINO':
            g1 = 30
        e = Numero_estado(estado)
        ide = str(g1) + str(year) + str(edad) + str(mon) + str(e) + str(day)
        IDE = str(ide)
        print(IDE)
        #Genero(Masculino,Femenino,Servicios,Productos) + año + edad + mes + estado + dia
        lista_ides.append(IDE)

        usuario[IDE] ={'contraseña':contrase,'genero':genero,'nombre':nombre,
        'apellido1':apellido1,'apellido2':apellido2,'edad':edad,'telefono':telefono,
        'estado':estado,'municipio':municipio,'entradas':0,'dinero':100000.0,'mensajes':[]}
        registrar.destroy()
        abrirVentana_menu_Usuario()
        return 0

    def crearIDE_e(contrase,nombre,tipo,empleados,lider,edad,telefono,estado,municipio):
        global IDE
        today = date.today()
        year = today.year
        mon = today.month
        day = today.day
        e = Numero_estado(estado)
        ide = str(year) + str(edad) + str(mon) + str(e) + str(day)
        IDE = str(ide)
        print(IDE)
        #Genero(Masculino,Femenino,Servicios,Productos) + año + edad + mes + estado + dia
        lista_ides.append(IDE)

        empresa[ide] ={'contraseña_empresa':contrase,'nombre_empresa':nombre,
        'tipo_empresa':tipo,'empleados':empleados,'lider':lider,
        'edad_empresa':edad,'telefono_empresa':telefono,'estado_empresa':estado,
        'municipio_empresa':municipio,'entradas':0,'dinero':100000.0,'mensajes':[]}
        registrar.destroy()
        abrirVentana_menu_Empresa()
        return 0

    def registro():
        if emp.get() == 1:
            #genero = input('GENERO (M/F):')
            genero_l=Label(registrar,text='GENERO:',relief='solid',font=(50),bg='light goldenrod')
            genero_l.grid(row=4,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            genero_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            genero_e.grid(row=4,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #nombre = input('NOMBRE:')
            nombre_l=Label(registrar,text='NOMBRE:',bg='light goldenrod',relief='solid',font=(50))
            nombre_l.grid(row=5,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            nombre_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            nombre_e.grid(row=5,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #apellido1 = input('APELLIDO PATERNO:')
            apellido1_l=Label(registrar,text='APELLIDO PATERNO:',bg='light goldenrod',relief='solid',font=(50))
            apellido1_l.grid(row=6,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            apellido1_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            apellido1_e.grid(row=6,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #apellido2 = input('APELLIDO MATERNO:')
            apellido2_l=Label(registrar,text='APELLIDO MATERNO:',bg='light goldenrod',relief='solid',font=(50))
            apellido2_l.grid(row=7,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            apellido2_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            apellido2_e.grid(row=7,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #edad = input('EDAD:')
            edad_l=Label(registrar,text='EDAD:',bg='light goldenrod',relief='solid',font=(50))
            edad_l.grid(row=8,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            edad_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            edad_e.grid(row=8,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #telefono = input('TELEFONO:')
            telefono_l=Label(registrar,text='TELEFONO:',bg='light goldenrod',relief='solid',font=(50))
            telefono_l.grid(row=9,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            telefono_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            telefono_e.grid(row=9,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #estado = input('ESTADO (minusculas):')
            estado_l=Label(registrar,text='ESTADO (minusculas):',bg='light goldenrod',relief='solid',font=(50))
            estado_l.grid(row=10,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            estado_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            estado_e.grid(row=10,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #municipio = input('MUNICIPIO o DELEGACION:')
            municipio_l=Label(registrar,text='MUNICIPIO o DELEGACION:',bg='light goldenrod',relief='solid',font=(50))
            municipio_l.grid(row=11,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            municipio_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            municipio_e.grid(row=11,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #contraseña = input('Contraseña:')
            contrase_l=Label(registrar,text='Contraseña:',bg='light goldenrod',relief='solid',font=(50))
            contrase_l.grid(row=12,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            contrase_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            contrase_e.grid(row=12,column=2,padx=5,pady=5,ipadx=5,ipady=5)

            ide_l=Button(registrar,text='Crear IDE',relief='solid',command=lambda:crearIDE_u(contrase_e.get(),genero_e.get(),nombre_e.get(),apellido1_e.get(),apellido2_e.get(),edad_e.get(),telefono_e.get(),estado_e.get(),municipio_e.get()))
            ide_l.grid(row=15,column=1,padx=5,pady=5,ipadx=5,ipady=5)
        elif emp.get() == 2:
            #nombre_empresa = input('NOMBRE DE LA EMPRESA:')
            nombre_l=Label(registrar,text='NOMBRE DE LA EMPRESA:',bg='light goldenrod',relief='solid',font=(50))
            nombre_l.grid(row=4,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            nombre_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            nombre_e.grid(row=4,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #tipo_empresa = input('TIPO DE EMPRESA [Servicios(S) / Productos(P)]:')
            tipo_l=Label(registrar,text='GIRO EMPRESARIAL:',bg='light goldenrod',relief='solid',font=(50))
            tipo_l.grid(row=5,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            tipo_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            tipo_e.grid(row=5,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #empleados = input('NUMERO DE EMPLEADOS:')
            empleados_l=Label(registrar,text='NUMERO DE EMPLEADOS:',bg='light goldenrod',relief='solid',font=(50))
            empleados_l.grid(row=6,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            empleados_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            empleados_e.grid(row=6,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #lider = input('NOMBRE DEL DUEÑO:')
            lider_l=Label(registrar,text='NOMBRE DEL DUEÑO:',bg='light goldenrod',relief='solid',font=(50))
            lider_l.grid(row=7,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            lider_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            lider_e.grid(row=7,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #edad_empresa = input('TIEMPO EN EL MERCADO:')
            edad_l=Label(registrar,text='TIEMPO EN EL MERCADO:',bg='light goldenrod',relief='solid',font=(50))
            edad_l.grid(row=8,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            edad_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            edad_e.grid(row=8,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #telefono_empresa = input('TELEFONO:')
            telefono_l=Label(registrar,text='TELEFONO:',bg='light goldenrod',relief='solid',font=(50))
            telefono_l.grid(row=9,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            telefono_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            telefono_e.grid(row=9,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #estado_empresa = input('UBICACION: ESTADO (minusculas):')
            estado_l=Label(registrar,text='UBICACION: ESTADO (minusculas):',bg='light goldenrod',relief='solid',font=(50))
            estado_l.grid(row=10,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            estado_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            estado_e.grid(row=10,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #municipio_empresa = input('MUNICIPIO o DELEGACION:')
            municipio_l=Label(registrar,text='MUNICIPIO o DELEGACION:',bg='light goldenrod',relief='solid',font=(50))
            municipio_l.grid(row=11,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            municipio_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            municipio_e.grid(row=11,column=2,padx=5,pady=5,ipadx=5,ipady=5)
            #contraseña_empresa = input('Contraseña:')
            contrase_l=Label(registrar,text='Contraseña:',bg='light goldenrod',relief='solid',font=(50))
            contrase_l.grid(row=12,column=1,padx=5,pady=5,ipadx=5,ipady=5)
            contrase_e=Entry(registrar,bg='RoyalBlue1',relief='solid',font=(50))
            contrase_e.grid(row=12,column=2,padx=5,pady=5,ipadx=5,ipady=5)

            ide_l=Button(registrar,text='Crear IDE',relief='solid',command=lambda:crearIDE_e(contrase_e.get(),nombre_e.get(),tipo_e.get(),empleados_e.get(),lider_e.get(),edad_e.get(),telefono_e.get(),estado_e.get(),municipio_e.get()))
            ide_l.grid(row=15,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    raiz.withdraw()
    registrar=Toplevel()
    registrar.iconbitmap('ide_a.ico')
    registrar.geometry('610x560') #X x Y
    barraMenu=Menu(registrar)
    registrar.config(background='salmon1',menu=barraMenu)
    #-----------------------BARRA---------------------------------
    def salirAplicacion():
        valor=messagebox.askokcancel('Cerrar','Deseas cerrar la Aplicacion')
        if valor == True:
            registrar.destroy()

    def cerrarDocumento():
        valor=messagebox.askretrycancel('Reintentar','No es posible cerrar. Documento bloqueado')
        if valor == False:
            registrar.destroy()

    archivoArchivo=Menu(barraMenu,tearoff=0)
    archivoArchivo.add_command(label='Nuevo')
    archivoArchivo.add_command(label='Guardar Datos',command=guardarDatos)
    archivoArchivo.add_separator()
    archivoArchivo.add_command(label='Cerrar',command=cerrarDocumento)
    archivoArchivo.add_command(label='Salir',command=salirAplicacion)

    archivoAyuda=Menu(barraMenu,tearoff=0)
    archivoAyuda.add_command(label='Licencia',command=avisoLicencia)
    archivoAyuda.add_command(label='Ayuda')
    archivoArchivo.add_separator()
    archivoAyuda.add_command(label='Acerca de IDE EcoUniversal',command=infoAdicional)

    barraMenu.add_cascade(label='Archivo',menu=archivoArchivo)
    barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)
    #-----------------------CODIGO---------------------------------
    bienvenida_1=Label(registrar,text='REGISTRAR',bg='orange',relief='solid',font=(50))
    bienvenida_1.grid(row=0,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    UoE=Label(registrar,text='Usuario o Empresa',bg='orange',relief='solid',font=(50))
    UoE.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(registrar,text='Usuario',variable=emp,value=1,command=registro,font=(50),bg='salmon1')
    opcion_u.grid(row=1,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_e=Radiobutton(registrar,text='Empresa',variable=emp,value=2,command=registro,font=(50),bg='salmon1')
    opcion_e.grid(row=1,column=2,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(registrar,text='Atras',relief='solid',command=regresar)
    botonDestruir.grid(row=15,column=2,padx=5,pady=5,ipadx=5,ipady=5)
#---------------------------MENU USUARIO----------------------------------------

def abrirVentana_menu_Usuario():
    global IDE
    usuario[IDE]['entradas'] += 1

    def regresar():
        guardarDatos()
        messagebox.showinfo('SALIR','GRACIAS POR ENTRAR!')
        usua.destroy()
        abrirVentana_raiz()

    def abrirVentana_menu_Usuario_pagos_d():
        usua.destroy()
        abrirVentana_menu_Usuario_pagos()
    def abrirVentana_menu_Usuario_cobros_d():
        usua.destroy()
        abrirVentana_menu_Usuario_cobros()

    usua=Toplevel()
    usua.iconbitmap('ide_a.ico')
    usua.geometry('450x530')
    barraMenu=Menu(usua)
    usua.config(background='green1',menu=barraMenu)
    #-----------------------BARRA---------------------------------
    def salirAplicacion():
        valor=messagebox.askokcancel('Cerrar','Deseas cerrar la Aplicacion')
        if valor == True:
            usua.destroy()

    def cerrarDocumento():
        valor=messagebox.askretrycancel('Reintentar','No es posible cerrar. Documento bloqueado')
        if valor == False:
            usua.destroy()

    archivoArchivo=Menu(barraMenu,tearoff=0)
    archivoArchivo.add_command(label='Nuevo')
    archivoArchivo.add_command(label='Guardar Datos',command=guardarDatos)
    archivoArchivo.add_separator()
    archivoArchivo.add_command(label='Cerrar',command=cerrarDocumento)
    archivoArchivo.add_command(label='Salir',command=salirAplicacion)

    archivoAyuda=Menu(barraMenu,tearoff=0)
    archivoAyuda.add_command(label='Licencia',command=avisoLicencia)
    archivoAyuda.add_command(label='Ayuda')
    archivoArchivo.add_separator()
    archivoAyuda.add_command(label='Acerca de IDE EcoUniversal',command=infoAdicional)

    barraMenu.add_cascade(label='Archivo',menu=archivoArchivo)
    barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)
    #-----------------------CODIGO---------------------------------
    bienvenida1=Label(usua,text='BIENVENIDO '+usuario[IDE]['nombre'],bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,ipadx=5)
    espacio=Label(usua,text='                            ',bg='green1')
    espacio.grid(row=0,column=0,padx=5,ipadx=5)
    menu1=Label(usua,text='MENU USUARIO',bg='green1',font=(70))
    menu1.grid(row=1,column=3,padx=5,ipadx=5)
    etiqueta_ide=Label(usua,text='Tu ide es: '+str(IDE)+'.',font=(50),bg='green1')
    etiqueta_ide.grid(row=2,column=3,padx=5,ipadx=5)
    botonPagos=Button(usua,text='PAGOS',command=abrirVentana_menu_Usuario_pagos_d,relief='solid',font=(50),bg='deep sky blue')
    botonPagos.grid(row=4,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonCobros=Button(usua,text='COBROS',command=abrirVentana_menu_Usuario_cobros_d,relief='solid',font=(50),bg='deep sky blue')
    botonCobros.grid(row=5,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonAhorros=Button(usua,text='AHORROS',command=abrirVentana_menu_Usuario_ahorros,relief='solid',font=(50),bg='deep sky blue')
    botonAhorros.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonInformacion=Button(usua,text='INFORMACION',command=abrirVentana_menu_Usuario_informacion,relief='solid',font=(50),bg='deep sky blue')
    botonInformacion.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(usua,text='SALIR',command=regresar,relief='solid',font=(50))
    botonDestruir.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_usuario=PhotoImage(file='usuario.gif')
    imagen_usuario_l=Label(usua,image=imagen_usuario).place(x=40,y=360)
    imagen_usuario_l.pack()

#---------------------------MENU EMPRESA----------------------------------------

def abrirVentana_menu_Empresa():
    global IDE
    empresa[IDE]['entradas'] += 1

    def regresar():
        guardarDatos()
        messagebox.showinfo('SALIR','GRACIAS POR ENTRAR!')
        empe.destroy()
        abrirVentana_raiz()

    def abrirVentana_menu_Empresa_pagos_d():
        empe.destroy()
        abrirVentana_menu_Empresa_pagos()
    def abrirVentana_menu_Empresa_cobros_d():
        empe.destroy()
        abrirVentana_menu_Empresa_cobros()

    empe=Toplevel()
    empe.iconbitmap('ide_a.ico')
    empe.geometry('450x530')
    barraMenu=Menu(empe)
    empe.config(background='green3',menu=barraMenu)
    #-----------------------BARRA---------------------------------
    def salirAplicacion():
        valor=messagebox.askokcancel('Cerrar','Deseas cerrar la Aplicacion')
        if valor == True:
            empe.destroy()

    def cerrarDocumento():
        valor=messagebox.askretrycancel('Reintentar','No es posible cerrar. Documento bloqueado')
        if valor == False:
            empe.destroy()

    archivoArchivo=Menu(barraMenu,tearoff=0)
    archivoArchivo.add_command(label='Nuevo')
    archivoArchivo.add_command(label='Guardar Datos',command=guardarDatos)
    archivoArchivo.add_separator()
    archivoArchivo.add_command(label='Cerrar',command=cerrarDocumento)
    archivoArchivo.add_command(label='Salir',command=salirAplicacion)

    archivoAyuda=Menu(barraMenu,tearoff=0)
    archivoAyuda.add_command(label='Licencia',command=avisoLicencia)
    archivoAyuda.add_command(label='Ayuda')
    archivoArchivo.add_separator()
    archivoAyuda.add_command(label='Acerca de IDE EcoUniversal',command=infoAdicional)

    barraMenu.add_cascade(label='Archivo',menu=archivoArchivo)
    barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)
    #-----------------------CODIGO---------------------------------
    bienvenida1=Label(empe,text='BIENVENIDO '+empresa[IDE]['nombre_empresa'],bg='green3',font=(30))
    bienvenida1.grid(row=0,column=3,padx=5,ipadx=5)
    espacio=Label(empe,text='                            ',bg='green3')
    espacio.grid(row=0,column=0,padx=5,ipadx=5)
    menu1=Label(empe,text='MENU EMPRESA',bg='green3',font=(70))
    menu1.grid(row=1,column=3,padx=5,ipadx=5)
    etiqueta_ide=Label(empe,text=' Tu ide es: '+str(IDE)+'.',font=(50),bg='green3')
    etiqueta_ide.grid(row=2,column=3,padx=5,ipadx=5)
    botonPagos=Button(empe,text='PAGOS',command=abrirVentana_menu_Empresa_pagos_d,relief='solid',font=(50),bg='deep sky blue')
    botonPagos.grid(row=4,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonCobros=Button(empe,text='COBROS',command=abrirVentana_menu_Empresa_cobros_d,relief='solid',font=(50),bg='deep sky blue')
    botonCobros.grid(row=5,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonAhorros=Button(empe,text='AHORROS',command=abrirVentana_menu_Empresa_ahorros,relief='solid',font=(50),bg='deep sky blue')
    botonAhorros.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonInformacion=Button(empe,text='INFORMACION',command=abrirVentana_menu_Empresa_informacion,relief='solid',font=(50),bg='deep sky blue')
    botonInformacion.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(empe,text='SALIR',command=regresar,relief='solid',font=(50))
    botonDestruir.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_empresa=PhotoImage(file='empresa.gif')
    imagen_empresa_l=Label(empe,image=imagen_empresa).place(x=40,y=360)
    imagen_empresa_l.pack()

#---------------------------MENU USUARIO----------------------------------------

def abrirVentana_menu_Usuario_pagos():
    def regresar():
        pagos.destroy()
        abrirVentana_menu_Usuario()

    def abrirVentana_menu_Usuario_pagos_a_d():
        pagos.destroy()
        abrirVentana_menu_Usuario_pagos_a()
    def abrirVentana_menu_Usuario_pagos_a_d():
        pagos.destroy()
        abrirVentana_menu_Usuario_pagos_a()
    def abrirVentana_menu_Usuario_pagos_e_d():
        pagos.destroy()
        abrirVentana_menu_Usuario_pagos_e()
    def abrirVentana_menu_Usuario_pagos_p_d():
        pagos.destroy()
        abrirVentana_menu_Usuario_pagos_p()
    def abrirVentana_menu_Usuario_pagos_tr_d():
        pagos.destroy()
        abrirVentana_menu_Usuario_pagos_tr()

    pagos=Toplevel()
    pagos.iconbitmap('ide_a.ico')
    pagos.geometry('550x390')
    pagos.config(background='green1')
    espacio=Label(pagos,text='   ',bg='green1')
    espacio.grid(row=0,column=0,padx=5,ipadx=5)
    bienvenida1=Label(pagos,text='PAGOS',bg='green1',font=(100))
    bienvenida1.grid(row=0,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    agua=Button(pagos,text='AGUA',command=abrirVentana_menu_Usuario_pagos_a_d,bg='deep sky blue',font=(50),relief='solid')
    agua.grid(row=1,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    telef=Button(pagos,text='TELEFONO',command=abrirVentana_menu_Usuario_pagos_a_d,bg='deep sky blue',font=(50),relief='solid')
    telef.grid(row=2,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    electricidad=Button(pagos,text='ELECTRICIDAD',command=abrirVentana_menu_Usuario_pagos_e_d,bg='deep sky blue',font=(50),relief='solid')
    electricidad.grid(row=3,column=4,padx=5,pady=5,ipadx=.5,ipady=5)
    predial=Button(pagos,text='PREDIAL',command=abrirVentana_menu_Usuario_pagos_p_d,bg='deep sky blue',font=(50),relief='solid')
    predial.grid(row=4,column=4,padx=4,pady=5,ipadx=5,ipady=5)
    transferencia=Button(pagos,text='TRANSFERENCIA',command=abrirVentana_menu_Usuario_pagos_tr_d,bg='deep sky blue',font=(50),relief='solid')
    transferencia.grid(row=5,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(pagos,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=7,column=5,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero=PhotoImage(file='dinero.gif')
    imagen_dinero_l=Label(pagos,image=imagen_dinero).place(x=210,y=70)
    imagen_dinero_l.pack()
def abrirVentana_menu_Usuario_cobros():
    def regresar():
        cobros.destroy()
        abrirVentana_menu_Usuario()

    def abrirVentana_menu_Usuario_cobros_h_d():
        cobros.destroy()
        abrirVentana_menu_Usuario_cobros_h()
    def abrirVentana_menu_Usuario_cobros_m_d():
        cobros.destroy()
        abrirVentana_menu_Usuario_cobros_m()

    cobros=Toplevel()
    cobros.iconbitmap('ide_a.ico')
    cobros.geometry('530x300')
    cobros.config(background='green1')
    bienvenida1=Label(cobros,text='COBROS',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=10,ipadx=5,ipady=10)
    hacer=Button(cobros,text='Hacer Cobro',command=abrirVentana_menu_Usuario_cobros_h_d,relief='solid',font=(50),bg='deep sky blue')
    hacer.grid(row=1,column=3,padx=5,pady=10,ipadx=5,ipady=10)
    mensaje=Button(cobros,text='Mensajes de Cobros',command=abrirVentana_menu_Usuario_cobros_m_d,relief='solid',font=(50),bg='deep sky blue')
    mensaje.grid(row=2,column=3,padx=5,pady=10,ipadx=5,ipady=10)
    botonDestruir=Button(cobros,text='ATRAS',command=regresar,relief='solid',font=(50))
    botonDestruir.grid(row=4,column=3,padx=5,pady=10,ipadx=5,ipady=10)
    imagen_cobrar=PhotoImage(file='cobrar.gif')
    imagen_cobrar_l=Label(cobros,image=imagen_cobrar).place(x=190,y=50)
    imagen_cobrar_l.pack()
def abrirVentana_menu_Usuario_ahorros():
    ahorros=Toplevel()
    ahorros.iconbitmap('ide_a.ico')
    ahorros.geometry('380x170')
    ahorros.config(background='green1')
    bienvenida1=Label(ahorros,text='AHORROS',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=2,padx=5,pady=5,ipadx=.5,ipady=5)
    ahorro=Label(ahorros,text='Tus ahorros totales son $'+str(usuario[IDE]['dinero'])+' M.N.',font=(50),bg='green1')
    ahorro.grid(row=2,column=2,padx=5,pady=5,ipadx=.5,ipady=5)
    botonDestruir=Button(ahorros,text='SALIR',command=ahorros.destroy,relief='solid',font=(50),bg='deep sky blue')
    botonDestruir.grid(row=4,column=2,padx=5,pady=5,ipadx=.5,ipady=5)
def abrirVentana_menu_Usuario_informacion():
    informacion=Toplevel()
    informacion.iconbitmap('ide_a.ico')
    informacion.geometry('610x480')
    informacion.config(background='green1')
    espacio=Label(informacion,text='                ',bg='green1')
    espacio.grid(row=0,column=0,padx=5,ipadx=5)
    bienvenida1=Label(informacion,text='INFORMACION',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=.5,ipady=5)

    nombre=Label(informacion,text='Tu nombre es: '+usuario[IDE]['nombre']+'.',font=(50),bg='deep sky blue')
    nombre.grid(row=1,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    apellido1=Label(informacion,text='Tu apellido paterno es: '+usuario[IDE]['apellido1']+'.',font=(50),bg='deep sky blue')
    apellido1.grid(row=2,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    apellido2=Label(informacion,text='Tu apellido materno es: '+usuario[IDE]['apellido2']+'.',font=(50),bg='deep sky blue')
    apellido2.grid(row=3,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    genero=Label(informacion,text='Tu genero es: '+usuario[IDE]['genero']+'.',font=(50),bg='deep sky blue')
    genero.grid(row=4,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    edad=Label(informacion,text='Tu edad es: '+usuario[IDE]['edad']+' años.',font=(50),bg='deep sky blue')
    edad.grid(row=5,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    telefono=Label(informacion,text='Tu numero telefonico es: '+usuario[IDE]['telefono']+'.',font=(50),bg='deep sky blue')
    telefono.grid(row=6,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    if usuario[IDE]['estado'] == 'cdmx':
        ubicacion=Label(informacion,text='Vives en la '+usuario[IDE]['estado']+' en la Delegacion de '+usuario[IDE]['municipio']+'.',font=(50),bg='deep sky blue')
    else:
        ubicacion=Label(informacion,text='Vives en el Estado de '+usuario[IDE]['estado']+' en el Municipio de '+usuario[IDE]['municipio']+'.',font=(50),bg='deep sky blue')
    ubicacion.grid(row=7,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    entrada=Label(informacion,text='Has entrado a la plataforma: '+str(usuario[IDE]['entradas'])+' veces.',font=(50),bg='deep sky blue')
    entrada.grid(row=8,column=3,padx=5,pady=5,ipadx=.5,ipady=5)

    botonDestruir=Button(informacion,text='SALIR',command=informacion.destroy,relief='solid',font=(50),bg='deep sky blue')
    botonDestruir.grid(row=10,column=5,padx=5,pady=5,ipadx=.5,ipady=5)

#---------------------------MENU EMPRESA----------------------------------------

def abrirVentana_menu_Empresa_pagos():
    ue = IntVar()
    def regresar():
        pagos_e.destroy()
        abrirVentana_menu_Empresa()
    def usua_empre():
        if ue.get() == 1:
            global y_e
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'
    pagos_e=Toplevel()
    pagos_e.iconbitmap('ide_a.ico')
    pagos_e.geometry('550x380')
    pagos_e.config(background='green3')
    bienvenida1=Label(pagos_e,text='PAGOS',bg='green3',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=.5,ipady=5)

    x_l=Label(pagos_e,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    x_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    x_e=Entry(pagos_e,bg='blue')
    x_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(pagos_e,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green3')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(pagos_e,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green3')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    z_l=Label(pagos_e,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    z_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    z_e=Entry(pagos_e,bg='blue')
    z_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonPagar=Button(pagos_e,text='PAGAR',command=lambda:Pagar_e(y_e,x_e.get(),z_e.get()),bg='deep sky blue',font=(50),relief='solid')
    botonPagar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(pagos_e,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=10,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero1=PhotoImage(file='dinero.gif')
    imagen_dinero1_l=Label(pagos_e,image=imagen_dinero1).place(x=210,y=70)
    imagen_dinero1_l.pack()
def abrirVentana_menu_Empresa_cobros():
    def regresar():
        cobros.destroy()
        abrirVentana_menu_Empresa()

    def abrirVentana_menu_Empresa_cobros_h_d():
        cobros.destroy()
        abrirVentana_menu_Empresa_cobros_h()
    def abrirVentana_menu_Empresa_cobros_m_d():
        cobros.destroy()
        abrirVentana_menu_Empresa_cobros_m()

    cobros=Toplevel()
    cobros.iconbitmap('ide_a.ico')
    cobros.geometry('530x300')
    cobros.config(background='green3')
    bienvenida1=Label(cobros,text='COBROS',bg='green3',font=(20))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    hacer=Button(cobros,text='Hacer Cobro',command=abrirVentana_menu_Empresa_cobros_h_d,bg='deep sky blue',font=(50),relief='solid')
    hacer.grid(row=1,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    mensaje=Button(cobros,text='Mensajes de Cobros',command=abrirVentana_menu_Empresa_cobros_m_d,bg='deep sky blue',font=(50),relief='solid')
    mensaje.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(cobros,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=4,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    imagen_cobrar=PhotoImage(file='cobrar.gif')
    imagen_cobrar_l=Label(cobros,image=imagen_cobrar).place(x=190,y=50)
    imagen_cobrar_l.pack()
def abrirVentana_menu_Empresa_ahorros():
    ahorros=Toplevel()
    ahorros.iconbitmap('ide_a.ico')
    ahorros.geometry('490x170')
    ahorros.config(background='green3')
    bienvenida1=Label(ahorros,text='AHORROS',bg='green3',font=(70))
    bienvenida1.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5)
    ahorro=Label(ahorros,text='Los activos de la empresa totales son $'+str(empresa[IDE]['dinero'])+' M.N.',bg='deep sky blue',font=(50))
    ahorro.grid(row=2,column=2,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(ahorros,text='SALIR',command=ahorros.destroy,bg='deep sky blue',font=(50),relief='solid')
    botonDestruir.grid(row=5,column=2,padx=5,pady=5,ipadx=5,ipady=5)
def abrirVentana_menu_Empresa_informacion():
    informacion=Toplevel()
    informacion.iconbitmap('ide_a.ico')
    informacion.geometry('700x480')
    informacion.config(background='green3')
    espacio=Label(informacion,text='                  ',bg='green3')
    espacio.grid(row=0,column=0,padx=5,ipadx=5)
    bienvenida1=Label(informacion,text='INFORMACION',bg='green3',font=(20))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    nombre=Label(informacion,text='El nombre de la Empresa es: '+empresa[IDE]['nombre_empresa']+'.',bg='deep sky blue',font=(50))
    nombre.grid(row=1,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    empleados=Label(informacion,text='La cantidad de empleados es: '+empresa[IDE]['empleados']+'.',bg='deep sky blue',font=(50))
    empleados.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    lider=Label(informacion,text='El lider de la empresa es: '+empresa[IDE]['lider']+'.',bg='deep sky blue',font=(50))
    lider.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    tipo=Label(informacion,text='Giro Empresarial : '+empresa[IDE]['lider']+'.',bg='deep sky blue',font=(50))
    tipo.grid(row=4,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    edad=Label(informacion,text='El tiempo de operacion de la empresa es: '+empresa[IDE]['edad_empresa']+' años.',bg='deep sky blue',font=(50))
    edad.grid(row=5,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    telefono=Label(informacion,text='El numero telefonico de la empresa es: '+empresa[IDE]['telefono_empresa']+'.',bg='deep sky blue',font=(50))
    telefono.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    if empresa[IDE]['estado_empresa'] == 'cdmx':
        ubicacion=Label(informacion,text='La empresa esta hubicada en la '+empresa[IDE]['estado_empresa']+' en la Delegacion de '+empresa[IDE]['municipio_empresa']+'.',bg='deep sky blue',font=(50))
    else:
        ubicacion=Label(informacion,text='La empresa esta hubicada en el Estado de '+empresa[IDE]['estado_empresa']+' en el Municipio de '+empresa[IDE]['municipio_empresa']+'.',bg='deep sky blue',font=(50))
    ubicacion.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    entrada=Label(informacion,text='Has entrado a la plataforma: '+str(empresa[IDE]['entradas'])+' veces.',bg='deep sky blue',font=(50))
    entrada.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    botonDestruir=Button(informacion,text='SALIR',command=informacion.destroy,bg='deep sky blue',font=(50),relief='solid')
    botonDestruir.grid(row=10,column=5,padx=5,pady=5,ipadx=5,ipady=5)

#---------------------------PAGOS USUARIO----------------------------------------

def abrirVentana_menu_Usuario_pagos_a():
    def regresar():
        ag.destroy()
        abrirVentana_menu_Usuario_pagos()
    ue = IntVar()
    def usua_empre():
        global y_e
        if ue.get() == 1:
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'

    ag=Toplevel()
    ag.iconbitmap('ide_a.ico')
    ag.geometry('550x380')
    ag.config(background='green1')
    bienvenida1=Label(ag,text='PAGO de Agua',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    x_l=Label(ag,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    x_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    x_e=Entry(ag,bg='blue')
    x_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(ag,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green1')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(ag,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green1')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    z_l=Label(ag,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    z_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    z_e=Entry(ag,bg='blue')
    z_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonPagar=Button(ag,text='PAGAR',command=lambda:Pagar_u(y_e,x_e.get(),z_e.get(),1),bg='deep sky blue',font=(50),relief='solid')
    botonPagar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(ag,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=10,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero=PhotoImage(file='dinero.gif')
    imagen_dinero_l=Label(ag,image=imagen_dinero).place(x=210,y=70)
    imagen_dinero_l.pack()
def abrirVentana_menu_Usuario_pagos_t():
    def regresar():
        te.destroy()
        abrirVentana_menu_Usuario_pagos()
    ue = IntVar()
    def usua_empre():
        global y_e
        if ue.get() == 1:
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'

    te=Toplevel()
    te.iconbitmap('ide_a.ico')
    te.geometry('550x380')
    te.config(background='green1')
    bienvenida1=Label(te,text='PAGO de Telefono',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    x_l=Label(te,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    x_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    x_e=Entry(te,bg='blue')
    x_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(te,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green1')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(te,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green1')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    z_l=Label(te,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    z_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    z_e=Entry(te,bg='blue')
    z_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonPagar=Button(te,text='PAGAR',command=lambda:Pagar_u(y_e,x_e.get(),z_e.get(),2),bg='deep sky blue',font=(50),relief='solid')
    botonPagar.grid(row=8,column=3,padx=5,pady=5,ipadx=.5,ipady=5)
    botonDestruir=Button(te,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=10,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero=PhotoImage(file='dinero.gif')
    imagen_dinero_l=Label(te,image=imagen_dinero).place(x=210,y=70)
    imagen_dinero_l.pack()
def abrirVentana_menu_Usuario_pagos_e():
    def regresar():
        el.destroy()
        abrirVentana_menu_Usuario_pagos()
    ue = IntVar()
    def usua_empre():
        global y_e
        if ue.get() == 1:
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'

    el=Toplevel()
    el.iconbitmap('ide_a.ico')
    el.geometry('550x380')
    el.config(background='green1')
    bienvenida1=Label(el,text='PAGO de Electricidad',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    x_l=Label(el,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    x_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    x_e=Entry(el,bg='blue')
    x_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(el,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green1')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(el,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green1')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    z_l=Label(el,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    z_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    z_e=Entry(el,bg='blue')
    z_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonPagar=Button(el,text='PAGAR',command=lambda:Pagar_u(y_e,x_e.get(),z_e.get(),3),bg='deep sky blue',font=(50),relief='solid')
    botonPagar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(el,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=10,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero=PhotoImage(file='dinero.gif')
    imagen_dinero_l=Label(el,image=imagen_dinero).place(x=210,y=70)
    imagen_dinero_l.pack()
def abrirVentana_menu_Usuario_pagos_p():
    def regresar():
        pr.destroy()
        abrirVentana_menu_Usuario_pagos()
    ue = IntVar()
    def usua_empre():
        global y_e
        if ue.get() == 1:
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'

    pr=Toplevel()
    pr.iconbitmap('ide_a.ico')
    pr.geometry('550x380')
    pr.config(background='green1')
    bienvenida1=Label(pr,text='PAGO de Predial',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    x_l=Label(pr,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    x_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    x_e=Entry(pr,bg='blue')
    x_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(pr,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green1')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(pr,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green1')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    z_l=Label(pr,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    z_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    z_e=Entry(pr,bg='blue')
    z_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonPagar=Button(pr,text='PAGAR',command=lambda:Pagar_u(y_e,x_e.get(),z_e.get(),4),bg='deep sky blue',font=(50),relief='solid')
    botonPagar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(pr,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=10,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero=PhotoImage(file='dinero.gif')
    imagen_dinero_l=Label(pr,image=imagen_dinero).place(x=210,y=70)
    imagen_dinero_l.pack()
def abrirVentana_menu_Usuario_pagos_tr():
    def regresar():
        tr.destroy()
        abrirVentana_menu_Usuario_pagos()
    ue = IntVar()
    def usua_empre():
        global y_e
        if ue.get() == 1:
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'

    tr=Toplevel()
    tr.iconbitmap('ide_a.ico')
    tr.geometry('550x380')
    tr.config(background='green1')
    bienvenida1=Label(tr,text='Transferencia',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    x_l=Label(tr,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    x_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    x_e=Entry(tr,bg='blue')
    x_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(tr,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green1')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(tr,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green1')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    z_l=Label(tr,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    z_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    z_e=Entry(tr,bg='blue')
    z_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonPagar=Button(tr,text='PAGAR',command=lambda:Pagar_u(y_e,x_e.get(),z_e.get(),5),bg='deep sky blue',font=(50),relief='solid')
    botonPagar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(tr,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=10,column=4,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_dinero=PhotoImage(file='dinero.gif')
    imagen_dinero_l=Label(tr,image=imagen_dinero).place(x=210,y=70)
    imagen_dinero_l.pack()

#---------------------------COBROS USUARIO----------------------------------------

def abrirVentana_menu_Usuario_cobros_h():
    def regresar():
        cobros_h.destroy()
        abrirVentana_menu_Usuario_cobros()
    ue = IntVar()
    def usua_empre():
        global y_e
        if ue.get() == 1:
            y_e = 'USUARIO'
        else:
            y_e = 'EMPRESA'

    cobros_h=Toplevel()
    cobros_h.iconbitmap('ide_a.ico')
    cobros_h.geometry('550x340')
    cobros_h.config(background='green1')
    bienvenida1=Label(cobros_h,text='COBROS',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    xa_l=Label(cobros_h,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    xa_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    xa_e=Entry(cobros_h,bg='blue')
    xa_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(cobros_h,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green1')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(cobros_h,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green1')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    za_l=Label(cobros_h,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    za_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    za_e=Entry(cobros_h,bg='blue')
    za_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonCobrar=Button(cobros_h,text='COBRAR',command=lambda:Cobrar_u(y_e,xa_e.get(),za_e.get()),bg='deep sky blue',font=(50),relief='solid')
    botonCobrar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(cobros_h,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=8,column=5,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_cobrar=PhotoImage(file='cobrar.gif')
    imagen_cobrar_l=Label(cobros_h,image=imagen_cobrar).place(x=210,y=70)
    imagen_cobrar_l.pack()
def abrirVentana_menu_Usuario_cobros_m():
    def regresar():
        cobros_m.destroy()
        abrirVentana_menu_Usuario_cobros()
    cobros_m=Toplevel()
    cobros_m.iconbitmap('ide_a.ico')
    cobros_m.geometry('1200x600')
    cobros_m.config(background='green1')
    bienvenida1=Label(cobros_m,text='BIENVENIDO A TUS MENSAJES',bg='green1',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    def codigoBoton_u(i):
        if len(usuario[IDE]['mensajes']) == 0:
            messagebox.showinfo('Mensajes','Sin Mensajes')
        else:
            if i == len(usuario[IDE]['mensajes']):
                miMensaje=Label(cobros_m,text='Mensaje #'+str(i+1)+': '+usuario[IDE]['mensajes'][i],font=(50))
                miMensaje.grid(row=i+2,column=3,padx=5,pady=0,ipadx=5,ipady=0)
            else:
                miMensaje=Label(cobros_m,text='Mensaje #'+str(i+1)+': '+usuario[IDE]['mensajes'][i],font=(50))
                miMensaje.grid(row=i+2,column=3,padx=5,pady=0,ipadx=5,ipady=0)
                codigoBoton_u(i+1)

    botonLeer=Button(cobros_m,text='Leer',command=lambda:codigoBoton_u(0),bg='deep sky blue',font=(50),relief='solid')
    botonLeer.grid(row=0,column=1,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(cobros_m,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=0,column=4,padx=5,pady=5,ipadx=5,ipady=5)
#---------------------------COBROS EMPRESA----------------------------------------

def abrirVentana_menu_Empresa_cobros_h():
    def regresar():
        cobros_he.destroy()
        abrirVentana_menu_Empresa_cobros()
    ue = IntVar()
    def usua_empre():
        global ya_e
        if ue.get() == 1:
            ya_e = 'USUARIO'
        else:
            ya_e = 'EMPRESA'

    cobros_he=Toplevel()
    cobros_he.iconbitmap('ide_a.ico')
    cobros_he.geometry('550x340')
    cobros_he.config(background='green3')
    bienvenida1=Label(cobros_he,text='COBROS',bg='green3',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    xa_l=Label(cobros_he,text='Ingresa IDE destino: ',bg='deep sky blue',font=(50),relief='solid')
    xa_l.grid(row=2,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    xa_e=Entry(cobros_he,bg='blue')
    xa_e.grid(row=3,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    opcion_u=Radiobutton(cobros_he,text='Usuario',variable=ue,value=1,command=usua_empre,font=(50),bg='green3')
    opcion_u.grid(row=4,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    opcion_e=Radiobutton(cobros_he,text='Empresa',variable=ue,value=2,command=usua_empre,font=(50),bg='green3')
    opcion_e.grid(row=5,column=3,padx=5,pady=1,ipadx=5,ipady=1)
    za_l=Label(cobros_he,text='Cantidad $: ',bg='deep sky blue',font=(50),relief='solid')
    za_l.grid(row=6,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    za_e=Entry(cobros_he,bg='blue')
    za_e.grid(row=7,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonCobrar=Button(cobros_he,text='COBRAR',command=lambda:Cobrar_e(ya_e,xa_e.get(),za_e.get()),bg='deep sky blue',font=(50),relief='solid')
    botonCobrar.grid(row=8,column=3,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(cobros_he,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=8,column=5,padx=5,pady=5,ipadx=5,ipady=5)
    imagen_cobrar=PhotoImage(file='cobrar.gif')
    imagen_cobrar_l=Label(cobros_he,image=imagen_cobrar).place(x=210,y=70)
    imagen_cobrar_l.pack()
def abrirVentana_menu_Empresa_cobros_m():
    def regresar():
        cobros_me.destroy()
        abrirVentana_menu_Empresa_cobros()
    cobros_me=Toplevel()
    cobros_me.iconbitmap('ide_a.ico')
    cobros_me.geometry('1200x600')
    cobros_me.config(background='green3')
    bienvenida1=Label(cobros_me,text='BIENVENIDO A TUS MENSAJES',bg='green3',font=(70))
    bienvenida1.grid(row=0,column=3,padx=5,pady=5,ipadx=5,ipady=5)

    def codigoBoton_e(i):
        if len(empresa[IDE]['mensajes']) == 0:
            messagebox.showinfo('Mensajes','Sin Mensajes')
        else:
            if i == len(empresa[IDE]['mensajes']):
                miMensaje=Label(cobros_me,text='Mensaje #'+str(i+1)+': '+empresa[IDE]['mensajes'][i],font=(50))
                miMensaje.grid(row=i+2,column=3,padx=5,pady=0,ipadx=5,ipady=0)
            else:
                miMensaje=Label(cobros_me,text='Mensaje #'+str(i+1)+': '+empresa[IDE]['mensajes'][i],font=(50))
                miMensaje.grid(row=i+2,column=3,padx=5,pady=0,ipadx=5,ipady=0)
                codigoBoton_e(i+1)

    botonLeer=Button(cobros_me,text='Leer',command=lambda:codigoBoton_e(0),bg='deep sky blue',font=(50),relief='solid')
    botonLeer.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5)
    botonDestruir=Button(cobros_me,text='ATRAS',command=regresar,font=(50),relief='solid')
    botonDestruir.grid(row=0,column=4,padx=5,pady=5,ipadx=5,ipady=5)
#--------------------------------VENTANA 1--------------------------------------
raiz = Tk()
raiz.iconbitmap('ide_a.ico')
raiz.title('IDE EcoUniversal')
raiz.geometry('710x390')
barraMenu=Menu(raiz)
#-----------------------BARRA---------------------------------
raiz.config(background='dark turquoise',menu=barraMenu)
def salirAplicacion():
    valor=messagebox.askokcancel('Cerrar','Deseas cerrar la Aplicacion')
    if valor == True:
        raiz.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel('Reintentar','No es posible cerrar. Documento bloqueado')
    if valor == False:
        raiz.destroy()

archivoArchivo=Menu(barraMenu,tearoff=0)
archivoArchivo.add_command(label='Nuevo')
archivoArchivo.add_command(label='Guardar Datos',command=guardarDatos)
archivoArchivo.add_separator()
archivoArchivo.add_command(label='Cerrar',command=cerrarDocumento)
archivoArchivo.add_command(label='Salir',command=salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label='Cortar')
archivoEdicion.add_command(label='Copiar')
archivoEdicion.add_command(label='Pegar')

archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoHerramientas.add_command(label='Extraer')
archivoHerramientas.add_command(label='Importar')
archivoHerramientas.add_command(label='Panel')

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label='Licencia',command=avisoLicencia)
archivoAyuda.add_command(label='Ayuda')
archivoArchivo.add_separator()
archivoAyuda.add_command(label='Acerca de IDE EcoUniversal',command=infoAdicional)

barraMenu.add_cascade(label='Archivo',menu=archivoArchivo)
barraMenu.add_cascade(label='Edicion',menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas',menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)
#-----------------------Grafico---------------------------------
bienvenida1=Label(raiz,text='  BIENVENIDO ',bg='green',font=('Comic Sans MS',30)).place(x=10,y=40)
bienvenida2=Label(raiz,text='A ',bg='green',font=('Comic Sans MS',30)).place(x=70,y=100)
bienvenida3=Label(raiz,text='IDE EcoUniversal',bg='green',font=('Comic Sans MS',30)).place(x=10,y=160)
imagen_raiz=PhotoImage(file='raiz.gif')
imagen_raiz_l=Label(raiz,image=imagen_raiz).place(x=340,y=40)
botonRegistrarse=Button(raiz,text='Registrarse',relief='solid',font=(80),command=abrirVentana_registrar).place(x=150,y=310)
botonIngresar=Button(raiz,text='Ingresar',relief='solid',font=(80),command=abrirVentana_ingresar).place(x=500,y=310)
messagebox.showinfo('Informacion','\t*IDE EcoUniversal:*\nEs una Plataforma Economica-Ecologica\nque busca disminuir la cantidad reciduos empleados\nen la procuccion de recibos y documentos.\nTodo esto para facilitar el pago en via remota\nde manera segura y eficiente para\n\tAyudar al Ambiente.')

raiz.mainloop()
