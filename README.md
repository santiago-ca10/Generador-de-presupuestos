# Generador de Presupuestos

Aplicación de escritorio desarrollada en Python que permite generar presupuestos en formato PDF de manera rápida y sencilla mediante una interfaz gráfica moderna.

---

## 🚀 Problema

Muchos profesionales y freelancers necesitan crear presupuestos de forma rápida, pero:

- Usan herramientas manuales (Word, Excel)
- Pierden tiempo formateando documentos
- No tienen una solución rápida y reutilizable

---

## 💡 Solución

Esta aplicación permite:

- Ingresar datos del proyecto (nombre, horas, valor, duración)
- Generar automáticamente un PDF profesional
- Elegir dónde guardar el archivo desde el sistema

Todo desde una aplicación de escritorio intuitiva.

---

## 🖥️ Características

- Interfaz gráfica con CustomTkinter
- Generación automática de PDF
- Selector de ruta para guardar archivo
- Cálculo automático del costo total
- Validación básica de datos
- Arquitectura modular (core / gui / i18n)

---

## 🏗️ Estructura del proyecto

```
📁 generador_presupuestos
├── 📁 app
│ ├── 📁 core
│ │ ├── config.py
│ │ ├── models.py
│ │ └── pdf_service.py
│ │
│ ├── 📁 gui
│ │ ├── app.py
│ │ ├── main_window.py
│ │ └── settings_window.py
│ │
│ ├── 📁 i18n
│ │ ├── en.json
│ │ └── es.json
│ │
│ └── init.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación

```bash
git clone https://github.com/santiago-ca10/Generador-de-presupuestos.git
```
```bash
cd Generador-de-presupuestos
```

```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
▶️ Uso
```bash
python main.py
```
### Tecnologías utilizadas
Python

CustomTkinter

fpdf2

## 📌 Estado del proyecto

En desarrollo 🚧

- Próximas mejoras:
- Diseño de interfaz más avanzado
- Plantillas de presupuesto
- Inclusión de datos de cliente
- Exportación en otros formatos
- Generación de ejecutable (.exe)