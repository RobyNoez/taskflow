# ***Parte 1. Analizar el problema***

*Antes de escribir código, identifica las entidades importantes del problema.*

*Completa una tabla como esta:*

| Posible objeto | ¿Por qué existe? | ¿Qué información necesita? |
| --- | --- | --- |
| Proyecto | Para crear el proyecto a gestionar | Identificador del proyecto. Titulo. Responsable. Descripción Estado. Fechas |
| Tarea | Para crear las tareas de un proyecto | Identificador de la tarea. Titulo. Estado de la tarea. Responsable de la tarea. Descripción de la tarea. |
| Usuario | Para trabajar sobre las tareas | Identificador del usuario. Nombre. Departamento. Puesto. Datos personales |


\*\*\*en color verde, atributos opcionales, no necesarios.

***Después responde:***

- **¿Qué otras entidades podrían existir?**

- Departamento: para conocer a que departamento pertenecen los usuarios, los cuales estarán agrupados por departamentos. Existiría la posibilidad de asignar la tarea a un departamento y dentro de este a usuarios. Podría ser un atributo también.

- **¿Cuáles son realmente necesarias?**

- Proyecto, tarea y usuario.

- **¿Cuáles son solamente datos o características de otras entidades?**

- Título, estado, responsable de las tareas, y otros como fecha inicio, fecha fin. Nombre del usuario, y otros posibles atributos, como departamento, puesto. Nombre del proyecto, responsable, fechas inicio y fin, estado.

*No busques todavía una única respuesta correcta.*

*Lo importante es justificar tus decisiones.*

# ***Parte 2. Identificar el estado***

*Para cada objeto que hayas identificado, determina qué información necesita conocer.*

**Proyecto**: Identificador del proyecto – Responsable – Titulo -   Descripción - Estado

**Se podrían almacenar en una estructura de datos el conjunto de tareas del proyecto.
Esta sería util para control de errores** 

**Tarea:** Identificador de la tarea – Título - Estado de la tarea - Responsable de la tarea. Descripción de la tarea

**Usuario:** Identificador del usuario - Nombre

# ***Parte 3. Identificar el comportamiento***

*Queremos saber qué se puede hacer con cada objeto:*

**Proyecto:** Añadir tarea – Asignar – Reasignar - Cerrar

**Tarea:** Asignar – Iniciar – Reasignar – Finalizar

**Usuario:** Modificar nombre

# ***Parte 4. Responsabilidades***

| Acción | Objeto responsable | ¿Por qué? |
| --- | --- | --- |
| Completar una tarea | Tarea | Almacena el estado y puede cambiarlo a “completada” |
| Iniciar una tarea | Tarea | Controla el estado puede cambiar su valor a “en progreso” |
| Asignar responsable | Tarea | Almacena el valor del usuario asignado como responsable. |
| Crear proyecto | main.py | Se pueden crear nuevos objetos desde el programa principal |
| Añadir tarea al proyecto | Proyecto | El proyecto contiene las tareas de las que se compone |


# ***Parte 5. Diseñar el modelo***

*Ahora reúne tus decisiones.*

*Construye un primer modelo conceptual:*

*Añade la información y comportamientos que hayas decidido.*

- **Proyecto** (identificador, responsable, titulo, descripción, estado)

Contiene

**Tareas** (identificador, responsable, descripción, título, estado)

Se asignan a

**Usuario** (identificador, nombre)

# ***Parte 9. ******Respuesta al “******prompt******”***

## **Análisis del diseño de ****TaskFlow**

Tu diseño está bastante bien delimitado para una primera aplicación de gestión de proyectos. Has identificado tres clases principales: Proyecto, Tarea y Usuario, con sus atributos y comportamientos.

Voy a analizarlo desde el punto de vista de la Programación Orientada a Objetos (POO), respetando tu propuesta y sin rediseñarla.

### **1. ¿Qué decisiones parecen coherentes?**

| Decisión | Valoración |
| --- | --- |
| Identificar Proyecto, Tarea y Usuario | Correcto. Son las tres entidades principales que necesitas. |
| Utilizar identificadores únicos | Adecuado, porque permite diferenciar proyectos, tareas y usuarios aunque tengan nombres iguales. |
| Incluir título y descripción | Coherente. Permite identificar y explicar el contenido de proyectos y tareas. |
| Incluir un responsable | Correcto si cada proyecto y tarea tienen una persona encargada. |
| Incluir un estado en Proyecto y Tarea | Adecuado para controlar su situación. |
| Añadir tareas desde Proyecto | Correcto, porque el proyecto organiza las tareas que contiene. |
| Iniciar y finalizar desde Tarea | Correcto, porque la tarea es responsable de controlar su propio estado. |
| Modificar nombre desde Usuario | Coherente, porque el usuario gestiona uno de sus propios atributos. |


Valoración: Has separado correctamente las entidades y has asignado la mayoría de los comportamientos al objeto que posee la información que se modifica.

### **2. ¿Qué responsabilidades podrían estar mal asignadas?**

En general, las responsabilidades están bien distribuidas, pero hay algunos aspectos que conviene aclarar.

#### Proyecto: Asignar y Reasignar

Estos métodos tienen sentido si sirven para cambiar el responsable del proyecto.

Sin embargo, si los utilizas para asignar tareas a usuarios, estarías introduciendo una responsabilidad que también podría corresponder a Tarea.

Es importante diferenciar ambas operaciones.

#### Tarea: Asignar y Reasignar

Estos métodos están correctamente situados en Tarea, ya que es el objeto que guarda la información sobre su responsable.

No obstante, debes distinguir entre el objeto que realiza el cambio y el usuario que tiene permiso para solicitarlo.

#### Proyecto: Cerrar

Es correcto que Proyecto se encargue de cambiar su propio estado a cerrado.

Pero debes decidir si se puede cerrar un proyecto que todavía tiene tareas pendientes.

#### Usuario: Modificar nombre

Está correctamente asignado, ya que afecta a un atributo del propio usuario.

No encuentro ninguna responsabilidad claramente mal asignada con la información que has proporcionado.

### **3. ¿Qué información podría faltar?**

| Objeto | Posible información ausente | Justificación |
| --- | --- | --- |
| Proyecto | Lista de tareas | Si el proyecto debe añadir tareas, necesita alguna manera de conocer cuáles tiene asociadas. |
| Proyecto | Valores posibles del estado | Debes definir si puede estar abierto, cerrado o en otras situaciones. |
| Tarea | Proyecto al que pertenece | Puede ser necesario para conocer a qué proyecto está asociada. |
| Tarea | Valores posibles del estado | Conviene establecer qué estados puede tener y cómo cambia entre ellos. |
| Usuario | Ningún atributo imprescindible adicional | El identificador y el nombre pueden ser suficientes para esta primera versión. |


Hay una cuestión especialmente importante: la relación entre Proyecto y Tarea.

Has definido el comportamiento añadir_tarea() en Proyecto, pero todavía no has indicado cómo se almacenan o relacionan esas tareas.

No es obligatorio que tanto Proyecto como Tarea guarden esta relación. Depende de cómo decidas organizar el modelo.

### **4. ¿Qué información podría sobrar?**

No veo ningún atributo claramente innecesario.

Sin embargo, revisaría tres aspectos:

- Descripción de Proyecto: es útil, pero debes decidir si realmente la necesitas o si es información opcional.

Responsable de Proyecto: tiene sentido si todos los proyectos necesitan una persona responsable.

Asignar y Reasignar: podrías considerar un único método que permita cambiar el responsable, aunque mantener dos métodos también es válido si quieres diferenciar la primera asignación de las posteriores.

No eliminaría información sin conocer primero los requisitos concretos de la aplicación.

### **5. ¿Qué preguntas deberías hacerte antes de programar?**

Estas preguntas te ayudarán a definir mejor el funcionamiento de TaskFlow.

| Pregunta | ¿Por qué es importante? |
| --- | --- |
| ¿Un proyecto puede contener varias tareas? | Para definir la relación entre Proyecto y Tarea. |
| ¿Una tarea puede pertenecer a varios proyectos? | Para establecer cómo se relacionan ambas clases. |
| ¿Puede existir una tarea sin responsable? | Para saber si la asignación es obligatoria. |
| ¿Qué estados puede tener un proyecto? | Para definir correctamente el comportamiento cerrar(). |
| ¿Qué estados puede tener una tarea? | Para controlar los métodos iniciar() y finalizar(). |
| ¿Puede finalizarse una tarea sin haberla iniciado? | Para establecer reglas de cambio de estado. |
| ¿Se puede reasignar una tarea finalizada? | Para definir las restricciones de sus métodos. |
| ¿Puede cerrarse un proyecto con tareas pendientes? | Para determinar cuándo se permite cerrar un proyecto. |
| ¿Quién puede asignar o reasignar responsables? | Para diferenciar las responsabilidades de las clases de los permisos de los usuarios. |
| ¿Qué ocurre si se elimina un usuario responsable? | Para evitar que proyectos o tareas queden con referencias inválidas. |


## **Valoración final**

Puntos fuertes

Las tres clases están bien identificadas. Sus atributos son razonables y los comportamientos principales están asignados a los objetos adecuados.

Aspectos que debes aclarar

La relación entre proyectos y tareas, los posibles estados de cada objeto y las condiciones para asignar, finalizar o cerrar.

Recomendación

Mantendría tus tres clases originales. Antes de programar, definiría las reglas de los cambios de estado y aclararía cómo se relacionan las tareas con sus proyectos.

Conclusión: Tu diseño es coherente para una primera versión de TaskFlow. No necesita una reorganización completa, pero sí concretar algunas reglas para que los métodos tengan un comportamiento claro y predecible.

El siguiente paso lógico sería utilizar estas decisiones para elaborar el diagrama de clases UML y después implementar los módulos Python, procurando que el análisis, el diagrama y el código sean consistentes.
