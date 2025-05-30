from Model.User import User
import datetime
from Model.Product import Product
from db.Connection import ConnectionSQLite
from Model.Category import Category

class Admin(User):

    def __init__(self, id_user, username , email, password, date, role):
    
        super().__init__(id_user, username , email, password, date, role)
        self.cnx = ConnectionSQLite()



    def menu(self):

        while True:
            print("\nMenú:")
            print("1. Agregar Producto")
            print("2. Agregar Usuarios")
            print("3. Editar Producto")
            print("4. Editar Usuario")
            print("5. Eliminar Producto")
            print("6. Eliminar Usuario")
            print("7. Agregar Categoria")
            print("8. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                product = self.ingresar_datos_productos()
                try:
                    self.cnx.insert_product(product)
                    print("Plato agregado con éxito.")
                except Exception as e:
                    print("Error al agregar el plato.")
                pass
            elif opcion == '2':
                print("2")
            elif opcion == '3':
                self.view_prdutcs()
                id = int(input("Ingrese el ID del plato que desea editar: "))
                product = self.ingresar_datos_productos()
                try:
                    self.cnx.edit(id, product)
                    print("Plato editado con éxito.")
                except Exception as e:
                    print("Error al editar el plato.")               
                pass

            elif opcion == '4':
                self.edit_users()

            elif opcion == '5':
                self.view_prdutcs()
                id = int(input("Ingrese el ID del plato que desea eliminar: "))
                self.cnx.delete(id)
                print("El producto se elimino con exito")
            elif opcion == '6':
                self.view_users()
                id = int(input("Ingrese el ID del usuario a eliminar: "))
                self.cnx.delete_user(id)
                print("El usuario fue eliminado con exito")
            elif opcion == '7':
                self.insert_category()
            elif opcion == '8':
                print("Programa finalizado.")
                break
            else:
                print(
                    "Opción no válida. Por favor, selecciona una opción válida del menú."
                )


    
    def ingresar_datos_productos(self):
        print("(*) Campos Obligatorios")
        name = input("Nombre del Plato: ")
        description = input("Descripcion del Plato: ")
        ingredients = input("Ingredientes del plato: ")
        inf_nutrition = input("Informacion Nutricional: ")
        price = input("*Precio: ")
        stock = input("*Stock: ")
        ranking = input("*Ranking: ")
        self.view_categorys()
        category = input("Categoria ID: ")
        #agregar id_product
        product = Product(None, name, description, ingredients, inf_nutrition, price, stock, datetime.date.today(), ranking, category)
        return product
   

    
    #VER CATEGORIAS
    def view_categorys(self):
        list_categorys = self.cnx.category_findall()
        if len(list_categorys) > 0:
            for category in list_categorys:
                print(f"ID: {category[0]}, nombre: {category[1]}")
        else:
            print("No se encontraron registros de categorias en la Base de Datos")


    #VER PRODUCTOS
    def view_prdutcs(self):
        list_products = self.cnx.product_findall()
        if len(list_products) > 0:
            for product in list_products:
                print(
                            f"ID: {product[0]}, nombre: {product[1]}, Descripcion: {product[2]}"
                        )
        else:
            print("No se encontraron registros de productos en la Base de Datos")
    


    #VER USUARIOS REGISTRADOS
    def view_users(self):
        list_users = self.cnx.view_users()
        if len(list_users) > 0:
            for user in list_users:
                print(
                            f"ID: {user[0]}, Nombre Usuario: {user[1]}, Email: {user[2]}"
                        )
        else:
            print("No se encontraron registros de usuarios en la Base de Datos")

   
    #INSERTAR CATEGORIA
    def insert_category(self):
        name = input("Ingrese el nombre de la Categoria: ")
        category = Category(None, name)
        self.cnx.insert_category(category)



    def edit_users(self):
        self.view_users()
        id = int(input("Ingrese el ID del usuario a Editar: "))
        current_date = datetime.date.today()
        username = input("Nombre de Usuario: ")
        email = input("Correo Electronico: ")
        passw = input("Contraseña: ")
        rol = input("Tipos de Rol:\n1. Admin\n0. Cliente\nRol: ")
       
        res = input("\n\n¿Desea guardar cambios si/no?")

        if res == "si":
            try:
                self.cnx.edit_user(id, User(None, username, email, passw, current_date, rol))      
                print("Edicion ejecutada con exito")
            except Exception as e:
                print("Error al registrar usuario" + str(e))
       

        