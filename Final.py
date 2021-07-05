import mysql.connector #Importamos el conector para la base de datos
import cv2
import mediapipe as mp
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import DoubleVar
from skimage import feature
from tkinter import Canvas
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import Menu
from tkinter import Tk
from tkinter import NW
from tkinter import Button
from tkinter import *
from PIL import Image
import pandas as pd
import PySimpleGUI as sg
from mttkinter import *
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_drawing.DrawingSpec

#Datos necesarios para nuestra conexion con la base de datos
dbConnect = {
    'host':'localhost',
    'user':'root',
    'password':'admin',
    'database':'python'
    }

conexion = mysql.connector.connect(**dbConnect) ##Establece la conexion

cursor = conexion.cursor() #Nos permite enviar comandos al servidor y recibir los resultados

##Consultar registros

def consultar():
    sql = "select * from angulocaderaizquierda" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta
    
    #Forzar el guardado del cache
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()

def graficacaderaderecha(name_text):
    
    sql = "select * from angulocaderaderecha" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta

    contador = []
    angulo = []
    for datos in resultados:
        contador.append(datos[0])
        angulo.append(datos[1])
    #print (contador)
    #listas = []
    #df1 = pd.DataFrame(listas, columns=[])
    #df1['IdAngulo'] = pd.Series(contador)
    #df1['Angulo'] = pd.Series(angulo)
    #print(df1)
    
    plt.plot(contador,angulo)
    plt.title('Cadera Derecha')
    plt.savefig("Imagenes\{}\CaderaDerecha.jpg".format(name_text.split('.')[0]))
    plt.show()
    return angulo, contador
    
def graficacaderaizquierda(name_text):
    
    sql = "select * from angulocaderaizquierda" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta
    
    contador = []
    angulo = []
    for datos in resultados:
        contador.append(datos[0])
        angulo.append(datos[1])
    
    plt.plot(contador,angulo)
    plt.title('Cadera Izquierda')
    plt.savefig("Imagenes\{}\CaderaIzquierda.jpg".format(name_text.split('.')[0]))
    plt.show()
    return angulo
    
def graficarodillaizquierda(name_text):
    
    sql = "select * from angulorodillaizquierda" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta
    
    contador = []
    angulo = []
    for datos in resultados:
        contador.append(datos[0])
        angulo.append(datos[1])
    
    plt.plot(contador,angulo)
    plt.title('Rodilla Izquierda')
    plt.savefig("Imagenes\{}\RodillaIzquierda.jpg".format(name_text.split('.')[0]))
    plt.show()
    return angulo
    
def graficarodilladerecha(name_text):
    
    sql = "select * from angulorodilladerecha" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta
    contador = []
    angulo = []
    for datos in resultados:
        contador.append(datos[0])
        angulo.append(datos[1])
    
    plt.plot(contador,angulo)
    plt.title('Rodilla Derecha')
    plt.savefig("Imagenes\{}\RodillaDerecha.jpg".format(name_text.split('.')[0]))
    plt.show()
    return angulo
    
def graficatobilloizquierdo(name_text):
    
    sql = "select * from angulotobilloizquierdo" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta

    contador = []
    angulo = []
    for datos in resultados:
        contador.append(datos[0])
        angulo.append(datos[1])
    
    plt.plot(contador,angulo)
    plt.title('Tobillo Izquierdo')
    plt.savefig("Imagenes\{}\TobilloIzquierdo.jpg".format(name_text.split('.')[0]))
    plt.show()
    return angulo
    
def graficatobilloderecho(name_text):
    
    sql = "select * from angulotobilloderecho" #Variable que contiene la consulta de sql
    
    cursor.execute(sql) #Enviar la consulta
    
    resultados = cursor.fetchall() #Recibimos los resultados de la consulta
    
    contador = []
    angulo = []
    for datos in resultados:
        contador.append(datos[0])
        angulo.append(datos[1])
    
    plt.plot(contador,angulo)
    plt.title('Tobillo Derecho')
    plt.savefig("Imagenes\{}\TobilloDerecho.jpg".format(name_text.split('.')[0]))
    plt.show()
    return angulo
    
def insertarangulorodillaizquierda(angulo):
    
    #sqlInsertar = "insert into angulorodillaizquierda(id,angulo)values(%s,%s)"
    
    cursor.execute(f"insert into angulorodillaizquierda (angulo) values ({angulo})")
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()

def insertarangulorodilladerecha(angulo):
    
    #sqlInsertar = "insert into angulorodillaizquierda(id,angulo)values(%s,%s)"
    
    cursor.execute(f"insert into angulorodilladerecha (angulo) values ({angulo})")
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()
    
def insertarangulotobilloizquierdo(angulo):
    
    #sqlInsertar = "insert into angulotobilloizquierdo(id,angulo)values(%s,%s)"
    
    cursor.execute(f"insert into angulotobilloizquierdo (angulo) values ({angulo})")
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()
    
def insertarangulotobilloderecho(angulo):
    
    #sqlInsertar = "insert into angulotobilloderecho(id,angulo)values(%s,%s)"
    
    cursor.execute(f"insert into angulotobilloderecho (angulo) values ({angulo})")
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()

def insertarangulocaderaizquierda(angulo):
    
    #sqlInsertar = "insert into angulocaderaizquierda(id,angulo)values(%s,%s)"
    
    cursor.execute(f"insert into angulocaderaizquierda (angulo) values ({angulo})")
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()
    
def insertarangulocaderaderecha(angulo):
    
    #sqlInsertar = "insert into angulocaderaderecha(id,angulo)values(%s,%s)"
    
    cursor.execute(f"insert into angulocaderaderecha (angulo) values ({angulo})")
    
    #conexion.commit()
    
    #cursor.close()
    
    #conexion.close()
##################################

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

def inicio(archivo, name_text):
    ##Podriamos recibir el nombre del usuario y el nombre del documento a guardar
    cap = cv2.VideoCapture(archivo)#Dar la opcion de subir el video de manera manual
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            if ret == True:
            
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
              
                # Make detection
                results = pose.process(image)
            
                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Coordenadas pierna izquierda
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                    ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                    foot = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                    
                    #Coordenadas pierna derecha 
                    shoulder_der = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    hip_der = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    knee_der = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                    ankle_der = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                    foot_der = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
                    
                    # Calcular angulo rodilla izquierda
                    angle = calculate_angle(hip, knee, ankle)
                    #print(angle)
                    # Visualize angle
                    cv2.putText(image, str(angle), 
                                   tuple(np.multiply(knee, [640, 480]).astype(int)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    #insertarangulorodillaizquierda(angle)
                    # Calcular angulo rodilla derecha
                    #contador = contador + 1
                    angle_der = calculate_angle(hip_der, knee_der, ankle_der)
                    #print(angle_der)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle_der), 
                                   tuple(np.multiply(knee_der, [640, 480]).astype(int)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Calcular angulo cadera izquierda
                    angle_izq_hip = calculate_angle(shoulder, hip, knee)
                    #print(angle_izq_hip)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle_izq_hip), 
                                   tuple(np.multiply(hip, [640, 480]).astype(int)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Calcular angulo cadera derecho
                    angle_der_hip = calculate_angle(shoulder_der, hip_der, knee_der)
                    #print(angle_der_hip)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle_der_hip), 
                                   tuple(np.multiply(hip_der, [640, 480]).astype(int)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Calcular angulo tobillo izquierdo
                    angle_foot_izq = calculate_angle(knee, ankle, foot)
                    #print(angle_foot_izq)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle_foot_izq), 
                                   tuple(np.multiply(ankle, [640, 480]).astype(int)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    # Calcular angulo tobillo derecho
                    angle_foot_der = calculate_angle(knee_der, ankle_der, foot_der)
                    #print(angle_foot_der)
                    
                    # Visualize angle
                    cv2.putText(image, str(angle_foot_der), 
                                   tuple(np.multiply(ankle_der, [640, 480]).astype(int)), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                        )
                    insertarangulocaderaizquierda(angle_izq_hip)
                    insertarangulorodilladerecha(angle_der)
                    insertarangulorodillaizquierda(angle)
                    insertarangulocaderaderecha(angle_der_hip)
                    insertarangulotobilloizquierdo(angle_foot_izq)
                    insertarangulotobilloderecho(angle_foot_der)
                    if cv2.waitKey(30) & 0xFF == ord('s'):
                        break
                except:
                    pass
        
         
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                         )               
                
                cv2.imshow('Mediapipe Feed', image)
            else:
                break
        conexion.commit()
        cap.release()
        cv2.destroyAllWindows()
        consultar()
        angulo1, contador = graficacaderaderecha(name_text)
        angulo2 = graficacaderaizquierda(name_text)
        angulo3 = graficarodilladerecha(name_text)
        angulo4 = graficarodillaizquierda(name_text)
        angulo5 = graficatobilloderecho(name_text)
        angulo6 = graficatobilloizquierdo(name_text)
        listas = [contador, angulo1, angulo2, angulo3, angulo4, angulo5, angulo6]
        df = pd.DataFrame(listas).transpose()
        df.columns = ['IdAngulo','Cadera Derecha','Cadera Izquierda','Rodilla Derecha','Rodilla Izquierda','Tobillo Derecho','Tobillo Izquierdo']
        print(df)
        df.to_excel("Imagenes/{}/{}".format(name_text.split('.')[0],name_text), index=False)
        truncate()
        
        
    
        
    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

def cerrarventana():
    ventana2.destroy()
    #inicio()
##Insertar video
def insertvideo():
    import os
    archivo = filedialog.askopenfilename(title = 'abrir')
    name_text = archivo.split('/')[-1].split('.')[0]+'.xlsx'
    os.mkdir("Imagenes/{}".format(name_text.split('.')[0]))
    inicio(archivo, name_text)
def truncate():
    sql = "truncate python.angulocaderaderecha"  
    cursor.execute(sql) #Enviar la consulta
    sql = "truncate python.angulocaderaizquierda"  
    cursor.execute(sql) #Enviar la consulta
    sql = "truncate python.angulorodilladerecha"  
    cursor.execute(sql) #Enviar la consulta
    sql = "truncate python.angulorodillaizquierda"  
    cursor.execute(sql) #Enviar la consulta
    sql = "truncate python.angulotobilloderecho"  
    cursor.execute(sql) #Enviar la consulta
    sql = "truncate python.angulotobilloizquierdo"  
    cursor.execute(sql) #Enviar la consulta
    
    
    
##Inicio
w = 1000
h = 700
ventana2 = Tk();
extraW=ventana2.winfo_screenwidth() - w
extraH=ventana2.winfo_screenheight() - h
ventana2.geometry("%dx%d%+d%+d" % (w, h, extraW / 3-300, extraH / 3))
ventana2.title("BIOELECTRONICA")
Label(text = "UNIVERSIDAD DEL AZUAY ", font= ("Times New Roman",12)).place(x=750, y=20)
Label(text = "INGENIERIA ELECTRONICA", font= ("Times New Roman",12)).place(x=750, y=60)
Label(text = "BIOELECTRONICA ", font= ("Times New Roman",12)).place(x=780, y=100)
Label(text = "PROYECTO ASINCRONICO", font= ("Times New Roman",12)).place(x=755, y=140)
Label(text = "ANALISIS DE LA MARCHA", font= ("Times New Roman",12)).place(x=755, y=180)
imagen2L = PhotoImage(file="Imagenes/arbol.png")
lblImagen2=Label(ventana2,image=imagen2L).place(x=0,y=0)
buton = Button(ventana2,text = "Acceder al Proyecto",font=("ARIEL", 12, "bold"), command = cerrarventana).place(x=780, y=300)
ventana2.resizable(width=False, height=False)
ventana2.mainloop()
#################################

#######Segunda Ventana
root = mtTkinter.Tk()
root.geometry('500x300+500+175')
root.configure(background="white")
root.title("ANALISIS DE LA MARCHA")
root.resizable(False, False)
frame = Frame(root, width=600, height=750)
#frame.config(bg="blue")
frame.pack()
Label(text = "ANALISIS DE LA MARCHA ", font= ("Times New Roman",20)).place(x=90, y=20)

# c.pack()
button1 = Button(frame, text="INSERTAR VIDEO", fg="black", font=("ARIEL", 9, "bold"), command = insertvideo)
# button2 = Button(frame, text="QUIT", fg="black", font=("Ariel", 9, "bold"), bg="cyan")
# button3 = Button(frame, text="COMPARE", fg="black", font=("Ariel", 9, "bold"), bg="cyan")
# button4 = Button(frame, text="INSERT TESTING VIDEO", fg="black", font=("Ariel", 9, "bold"), bg="cyan")
# button5 = Button(frame, text="RESULT", fg="black", font=("Ariel", 9, "bold"), bg="cyan")

button1.place(relheight=0.1, relwidth=0.332, relx=0.5, rely=0.4, anchor=CENTER)
# button2.place(relheight=0.05, relwidth=0.332, relx=0.995, rely=1, anchor=SE)
# button3.place(relheight=0.1, relwidth=0.332, relx=0.5, rely=0.6, anchor=CENTER)
# button5.place(relheight=0.1, relwidth=0.332, relx=0.5, rely=0.7, anchor=CENTER)
# button4.place(relheight=0.1, relwidth=0.332, relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()