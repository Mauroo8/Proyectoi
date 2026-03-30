import mysql.connector

def crear_tablas():
    """Crea la base de datos y tablas necesarias para el sistema"""
    conexion = obtener_conexion()
    if conexion is None:
        print("❌ No se pudo conectar a MySQL")
        return False
    
    cursor = conexion.cursor()
    
    try:
        # 1. CREAR LA BASE DE DATOS si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS inventario")
        print("✅ Base de datos 'inventario' creada/verificada")
        
        # 2. Usar la base de datos
        cursor.execute("USE inventario")
        
        # 3. Crear tabla de consumibles
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consumibles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                stock INT DEFAULT 0,
                estado VARCHAR(50) DEFAULT 'disponible'
            )
        ''')
        print("✅ Tabla 'consumibles' creada/verificada")
        
        # 4. Crear tabla de periféricos desechables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS perifericos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                stock INT DEFAULT 0,
                estado VARCHAR(50) DEFAULT 'disponible',
                tipo VARCHAR(50) DEFAULT 'generico'
            )
        ''')
        print("✅ Tabla 'perifericos' creada/verificada")
        
        # 5. Crear tabla de componentes internos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS componentes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                fecha_compra DATE,
                estado VARCHAR(50) DEFAULT 'disponible',
                especificaciones TEXT
            )
        ''')
        print("✅ Tabla 'componentes' creada/verificada")
        
        # 6. Crear tabla de activos (ejemplo: PCs, impresoras, etc.)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                descripcion TEXT,
                estado VARCHAR(50) DEFAULT 'activo',
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("✅ Tabla 'activos' creada/verificada")
        
        conexion.commit()
        print("🎉 ¡Base de datos y tablas configuradas correctamente!")
        return True
        
    except mysql.connector.Error as err:
        print(f"❌ Error creando base de datos: {err}")
        return False
    finally:
        conexion.close()

def obtener_conexion():
    """Crea y devuelve una conexión a la base de datos inventario"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sql1234T",   # ⚠️ Ajusta según tu entorno
            database="inventario"
        )
        print("✅ Conexión a base de datos 'inventario' exitosa")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error conectando a inventario: {err}")
        return None

# Crear tablas automáticamente al importar
crear_tablas()