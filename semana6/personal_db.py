import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")
# Crear tabla de DEPARTAMENTOS
try :
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya existe")

# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO CARGOS (nombre,nivel,fecha_creacion) 
    VALUES ('Ingeniero', 5,2000-05-23)
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre,nivel,fecha_creacion) 
    VALUES ('Abogado', 4,'2001-05-26')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS (nombre,nivel,fecha_creacion) 
    VALUES ('Administrador', 4,'2001-05-26')
    """
)
# Consultar datos de    CARGOS
print("\nCARGOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)
#------------------------------------------------------------------------

try :
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya existe")

# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre,fecha_creacion) 
    VALUES ('sISTEMAS','2001-05-26')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre,fecha_creacion) 
    VALUES ('AdministRACION','2001-05-26')
    """
)

# Consultar datos de DEPARTAMENTOS
print("\nDEPARTAMENTOS:")
cursor = conn.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
    print(row)


#------------------------------------------------------------------------
try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno INTEGER NOT NULL,
        apellido_materno INTEGER NOT NULL,
        fecha_contratacion TEXT NOT NULL,
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla MATRICULAS ya existe")
# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO EMPLEADOS (DEPARTAMENTO_id, cargo_id) 
    VALUES ('andres', 'andres','paz', '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS (estudiante_id, carrera_id) 
    VALUES ('andres', 'andres','paz','2024-01-20')
    """
)
# Listar datos de Empleado
print("\nEMPLEADOS:")
cursor = conn.execute(
    "SELECT * FROM EMPLEADOS"
)


