# Dashboard en Power BI – Tienda Aurelion

Este directorio contiene el dashboard desarrollado como parte del proyecto final del curso  
**Fundamentos en Inteligencia Artificial – IBM + Guayerd (2025)**.

El proyecto integra análisis de datos, visualización, diseño del modelo de datos y presentación de resultados en Power BI.

---

## Contenido de la carpeta

- **Aurelion_Dashboard_powerbi.pdf**  
  Exportación completa del dashboard, con todas las páginas del informe listas para visualizar sin necesidad de Power BI.

- **vista_modelo_powerBI.png**  
  Imagen del modelo de datos utilizado en Power BI, basado en un esquema de estrella.

---

## Estructura del modelo de datos

El modelo relacional incluye:

- **fact_detalleVentas**: tabla de hechos con transacciones de venta  
- **dim_cliente**: información de clientes (ciudad, nombre, email, fecha de alta)  
- **dim_producto**: productos y categorías  
- **dim_medioPago**: medios de pago utilizados  
- **calendario**: tabla de fechas con jerarquías temporales  
- **Medidas**: tabla con KPIs calculados

Las relaciones están definidas mediante claves foráneas, y el modelo permite realizar análisis por ciudad, categoría, medio de pago y temporalidad.

---

## Secciones del dashboard

El informe está organizado en varias páginas temáticas:

### General
- Ventas totales  
- Ticket promedio  
- Cantidad total vendida  
- Evolución temporal  
- Distribución por categoría y medio de pago  

### Clientes
- Importe total por ciudad  
- Top 10 de clientes  
- Ticket promedio por cliente  
- Frecuencia de compra  
- Vista del modelo relacional  

### Productos y categorías
- Top 5 productos más vendidos  
- Mapa de calor por ciudad y categoría  
- Evolución de ventas por categoría  

### Medios de pago
- Participación de cada medio de pago  
- Evolución mensual  
- Cantidad vendida por categoría y medio de pago  

---

## Objetivo del dashboard

El dashboard fue diseñado para:

- Facilitar la interpretación de los datos comerciales  
- Identificar patrones de compra y comportamiento de clientes  
- Analizar el rendimiento por ciudad, categoría y medio de pago  
- Proveer métricas clave (KPIs) para la toma de decisiones  

---

## Herramientas utilizadas

- Power BI Desktop  
- Lenguaje DAX para medidas y KPIs  
- Modelo relacional con esquema de estrella  

---

## Nota

Los datos utilizados corresponden a un caso práctico provisto en el marco del curso y se emplean exclusivamente con fines educativos.
