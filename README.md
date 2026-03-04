# RRHH-
# ERP RRHH – Sprint 1

#Descripción del Proyecto

Este proyecto corresponde al desarrollo inicial de un módulo de Recursos Humanos para un ERP, implementado bajo metodología Scrum y trabajando 100% en la nube.

Durante el Sprint 1 se desarrolló:

- Una API REST para la gestión de empleados.
- Un proceso ETL para limpieza y transformación de datos salariales.
- Un modelo predictivo base utilizando Regresión Logística.
- Documentación arquitectónica bajo el estándar arc42.

El objetivo principal fue integrar backend, análisis de datos y fundamentos de MLOps dentro de una arquitectura clara y modular.

---

#Integrantes

- Maria Luisa Silva Santiago – Rol Product Owner
- Juan Sebastian Muñoz Melo – Rol Desarrolador

---

#Arquitectura del Proyecto

El sistema está dividido en tres componentes principales:

#API REST (Backend)
- Framework: FastAPI
- Endpoints para creación y consulta de empleados
- Validación de datos mediante modelos

#Pipeline ETL
- Limpieza de datos salariales
- Transformación y cálculo de salario anual
- Preparación de datos para análisis

#Modelo Predictivo (MLOps Base)
- Regresión Logística
- División entrenamiento/prueba
- Evaluación con métricas de clasificación

# 🔹 Enfoque Arquitectónico
Se implementó una separación clara entre:

- Capa transaccional (API)
- Capa analítica (ETL + ML)
- Documentación arquitectónica (arc42)

---

#Enlaces del Proyecto

📘 Documentación arc42 (Notion):  
👉 https://www.notion.so/1256511918ed411a8919b2d2b0076bf4?v=5f046c0c505f40e3abedb3fb8584cbf9&source=copy_link 

🎨 Diseño UI/UX (Figma):  
👉 https://www.figma.com/design/YVeR5lCisH376KmUf9Yaf0/Sin-t%C3%ADtulo?node-id=0-1&t=O5hLbpXpGCqsYDyf-0

📊 Notebook ETL y Modelo (Colab):  
👉 https://colab.research.google.com/drive/1Ih6a5tgj9achIRgs8lmuXdqyMajbl4hk?usp=sharing


#Estado del Sprint

- API funcional ✔
- ETL implementado ✔
- Modelo predictivo base ✔
- Base de datos NoSQL ❌ (Planificado para siguiente Sprint)

---

#Notas

Este proyecto representa la base inicial del sistema ERP y será extendido en futuros Sprints con persistencia en base de datos, automatización DevOps y procesamiento distribuido.

POR FAVOR Revisar el kanban y el collab a profundidad para denotar la realizacion de lo propuesto gracias.
