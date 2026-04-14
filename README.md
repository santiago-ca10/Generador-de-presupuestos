# Generador de Presupuestos

Aplicación de escritorio desarrollada en Python que permite generar presupuestos en formato PDF de manera rápida y sencilla mediante una interfaz gráfica.

---

## 🚀 Problema

Muchos profesionales y freelancers necesitan crear presupuestos de forma rápida, pero:

- Usan herramientas manuales (Word, Excel)
- Pierden tiempo formateando documentos
- No tienen una solución automatizada simple

---

## 💡 Solución

Esta aplicación permite:

- Ingresar datos del proyecto (nombre, horas, valor, duración)
- Generar automáticamente un PDF profesional
- Elegir dónde guardar el archivo desde el sistema

Todo desde una interfaz gráfica simple y directa.

---

## 🖥️ Características

- Interfaz gráfica con Tkinter
- Generación automática de PDF
- Selector de ruta para guardar archivo
- Cálculo automático del costo total
- Validación básica de datos

---

## 🏗️ Estructura del proyecto

```
📁 generador_presupuestos
├── 📁 app
│ ├── 📁 core
│ │ ├── models.py
│ │ └── pdf_service.py
│ │
│ └── 📁 gui
│ └── app.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación

```bash
git clone https://github.com/tu-usuario/generador_presupuestos.git
```
```bash
cd generador_presupuestos
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

Tkinter

fpdf2

## 📌 Estado del proyecto

En desarrollo 🚧
Se planean mejoras en la interfaz y funcionalidades.