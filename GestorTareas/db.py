from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

#El engine permite a SQLalchemy comunicarse con la base de datos
engine= create_engine("sqlite:///database/tareas.db",
                      connect_args= {"check_same_thread": False})
#Crear el engine no conecta inmediatamente a la base de  datos

#Ahora crearemos la sesion,lo que nos permite realizar transacciones dentro de la base de datos
Session= sessionmaker(bind= engine)
session= Session()

#esta clase se encarga de mapear la info de las clases que hereda y vincular
#su informacion a la base de datos
Base= declarative_base()