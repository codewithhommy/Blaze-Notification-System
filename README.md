# Blaze-Notification-System (Sentinel-AML)

Este proyecto simula un entorno de trabajo real de **Ciberseguridad y Prevención de Fraude** en entidades Fintech/Bancarias. Automatiza la detección de alertas y protege la integridad de la evidencia digital, utilizando una metodología de documentación profesional.

## Propósito Profesional
- **Simulación Real:** En la industria bancaria, el análisis se escala mediante scripts automáticos, no procesos manuales en Excel.
- **Portafolio de Ciberseguridad:** Demostración práctica de habilidades en Python, Linux y Hardening de archivos.
- **Eficiencia Operativa:** Transformación de procesos lentos y propensos a error en ejecuciones precisas y constantes.

## Componentes del Sistema

### 1. El Motor de Datos (Python + Pandas)
Utiliza lógica de reglas de negocio para procesar transacciones y detectar desvíos de límites autorizados.
- **Procesamiento ETL:** Lee de `/data`, transforma la información y genera salidas limpias.
- **Generación de ROS:** Crea archivos JSON automáticos (estándar de la industria) para auditoría legal.

### 2. Blindaje y Hardening (Bash Scripting)
El script `deploy_sentinel.sh` actúa como orquestador de seguridad:
- **Automatización de Despliegue:** Ejecuta el entorno completo con un solo comando.
- **Integridad de Evidencia:** Aplica `chmod 400` a los reportes para "cristalizarlos", volviéndolos de solo lectura e inalterables.

 ## Metodología de Documentación (Obsidian)
Para este proyecto, se implementó un sistema de notas en **Obsidian** siguiendo estándares de investigación:
- **Bitácora de Incidentes:** Registro detallado de cada alerta detectada para trazabilidad.
- **Análisis de Patrones:** Documentación de por qué una transacción se considera fraude (exceso de límites, comportamiento inusual).
- **Gestión del Conocimiento:** Uso de la terminal como "mejor amiga" para ver datos crudos, garantizando que el análisis no tenga filtros que oculten errores.

## 🧠 Conocimientos Aplicados
- **Lógica de Reglas de Negocio:** Traducción de políticas bancarias a código ejecutable.
- **Infraestructura como Código:** Comunicación entre lenguajes y scripts de administración.
- **Troubleshooting Crítico:** Resolución de errores de entorno, sintaxis y permisos de kernel.
- **Estándares Financieros:** Uso de JSON para el intercambio de datos seguro.

