# Documentación de Uso de Inteligencia Artificial EVALUACION 3

Durante el desarrollo de la Evaluación Sumativa 3, utilicé herramientas de Inteligencia Artificial (ChatGPT) como apoyo para la codificación. Sin embargo, el código final es el resultado de un proceso de refinamiento técnico propio, aplicando un análisis crítico sobre las sugerencias de la IA para cumplir con los criterios de seguridad y estabilidad.

### 1. Generación de fragmentos de código y análisis
**Prompt utilizado:** *"Genera un método en Python para insertar un nuevo proyecto en una base de datos SQLite, y otro método para insertar un departamento"*.

**Propuesta de la IA:** La IA entregó métodos básicos de inserción (`INSERT`) que tomaban los datos y los guardaban directamente en la base de datos sin ningún tipo de revisión previa.

### 2. Identificación de vulnerabilidades y ajustes técnicos
Al analizar la propuesta de la IA frente a los criterios de la evaluación y la problemática de la empresa, detecté y corregí lo siguiente:

*   **Decisión 1 (Modificación - Validación de Entradas):** La IA no validaba los datos ingresados por el usuario. Para cumplir con el criterio 3.1.2 (Seguridad), **agregué** validaciones en los DAOs (`ProyectoDAO` y `DepartamentoDAO`). Justificación: Evitar que se ingresen nombres vacíos, demasiado cortos (menos de 3 caracteres) o con símbolos extraños (como `@`, `#`, `*`). Se exige que el nombre sea alfanumérico y permita espacios.
*   **Decisión 2 (Modificación - Manejo de Excepciones):** La IA no manejaba qué pasaba si la base de datos rechazaba la inserción o si fallaba la validación. Para cumplir con el criterio 3.1.3, **modifiqué** el archivo `menu_admin.py` para envolver la llamada a los DAOs en bloques `try/except ValueError`. Justificación: Evitar que el programa se cierre abruptamente (traceback) ante un error de tipeo del usuario, permitiendo que el sistema continúe funcionando de forma controlada.
*   **Decisión 3 (Rechazo - Manejo de Excepciones Genéricas):** La IA sugirió usar `except Exception:` de forma genérica para capturar cualquier fallo. **Rechacé** esta sugerencia y en su lugar utilicé excepciones específicas (`ValueError`). Justificación: Capturar todo de forma genérica oculta errores de programación, dificulta la depuración y no permite entregar un mensaje claro y seguro al usuario.
*   **Decisión 4 (Adaptación - Validación de Tipos):** La IA no verificaba si el ID del empleado ingresado por teclado era realmente un número. **Modifiqué** el código para forzar la conversión con `int()` dentro de un bloque `try`. Justificación: Prevenir que el programa falle con un `ValueError` no controlado si el administrador escribe letras en lugar de números al asignar un proyecto.

**Conclusión:**
El código generado por la IA sirvió como un punto de partida, pero las decisiones de seguridad (validación de caracteres), manejo específico de errores y estabilidad del sistema fueron implementadas de manera consciente y justificada por mi parte para cumplir con los estándares de la asignatura.