# Actividad-9

## Descripcion de Pruebas

Este código realiza pruebas automatizadas en una página web de ejemplo utilizando Selenium y pytest. Define funciones para esperar y localizar elementos en la página, como por XPATH, ID o clase. Contiene tres pruebas: una para iniciar sesión verificando que la URL cambie correctamente, otra para interactuar con un checkbox y asegurarse de que se pueda seleccionar, y una más para probar un menú desplegable seleccionando una opción y verificando la elección.

## Pruebas Realizadas

* Prueba de Login: Inicia sesión en la página introduciendo un nombre de usuario y contraseña, luego verifica que la URL cambie a la página de éxito, asegurando que el login fue exitoso.

* Prueba de Checkbox: Accede a la página con los checkboxes, selecciona uno de ellos y verifica que esté marcado correctamente, asegurándose de que la interacción funcione como se espera.

* Prueba de Dropdown: Interactúa con un menú desplegable, selecciona una opción y verifica que la opción seleccionada sea la correcta, asegurando que el menú funcione adecuadamente.

## Reporte de Pruebas

Allure se utiliza en este código para generar informes detallados y visuales de las pruebas automatizadas. Es una herramienta que facilita la visualización de los resultados de las pruebas, proporcionando un formato más accesible y comprensible para los desarrolladores y equipos de calidad.
