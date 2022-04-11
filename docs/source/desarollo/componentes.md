# Componentes

El proyecto está basado en Django, que permite usar módulos de python como *apps* que construirán la aplicación final.
Esos módulos serán los componentes que hemos logrado identificar en clases.

| Nº | Componentes del sistema | Funcionalidad principal                                                                                                             | Actor/es relacionado/s                                                                    |
|----|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1  | Cuentas de usuarios     | Se encarga de registrar, modificar y eliminar las cuentas de usuario además de validar el inicio de sesión y el cierre de la misma. | Administrador de sistema \| Administrador de ventas \| Administrador de bodega \| Cliente |
| 2  | Inventario              | Se encarga de gestionar todo el inventario registrado en la base de datos (Registro, modificación, eliminación).                    | Administrador de bodega \| Administrador de ventas                                        |
| 3  | Catálogo                | Se encarga de gestionar el front end del catálogo además de la propia publicación de los mangas, productos destacados y ofertas.    | Administrador de ventas                                                                   |
| 4  | Ventas                  | Se encarga de registrar las acciones del cliente con el carrito de compra (agregar producto, eliminar producto, comprar)            | Cliente                                                                                   |
| 5  | Analitica               | Se encarga de formular los gráficos para la toma de decisiones.                                                                     | Administrador de ventas                                                                   |
| 6  | Notificaciones          | Se encarga de mandar notificaciones a los clientes con los cambios de estado que sucedan con sus pedidos.                           | Cliente                                                                                   |
| 7  | Despacho                | Se encarga de gestionar el registro de los despachos y su modificación.                                                             | Administrador de ventas                                                                   |
| 8  | Contacto                | Se encarga de recibir y dar soluciones a las dudas o reclamos de los clientes.                                                      | Administrador de ventas                                                                   |