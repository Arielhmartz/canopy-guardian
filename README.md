# Canopy GuardIAn

Landing page del proyecto **Canopy GuardIAn** — sistema de detección acústica de tala ilegal mediante IA embebida y hardware de bajo costo, orientado a la industria forestal y áreas protegidas de Chile.

## Estado del proyecto

- MVP en fase de pruebas de laboratorio
- Postulación en curso a **CORFO Semilla Inicia Biobío 2026**
- Equipo basado en la Región del Biobío, Chile

## Estructura

```
guardian-forestal/
├── index.html              # Landing principal (versión CORFO)
├── comercial.html          # Versión comercial alternativa
├── images/                 # Imágenes optimizadas (webp + jpg fallback)
├── optimize_images.py      # Script para regenerar versiones webp/jpg
└── .gitignore
```

## Desarrollo local

Para previsualizar el sitio:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Y abrir `http://localhost:8000/` en el navegador.

## Optimización de imágenes

Las imágenes originales en alta resolución se guardan localmente en `images/originals/` (excluidas del repo) y se generan versiones `.webp` (principal) + `.jpg` (fallback) con:

```bash
python optimize_images.py
```

## Stack

- HTML5 + CSS embebido (variables CSS) + JavaScript mínimo (sin frameworks)
- Tipografías: Space Grotesk (display) + DM Sans (body) vía Google Fonts
- Diseño responsive (desktop + tablet + mobile)
- Accesibilidad: ARIA labels, `prefers-reduced-motion`, focus visible, skip link
- Sin backend: el formulario de contacto está pendiente de conectar a un servicio (Formspree o similar)

## Deploy

Sitio estático, desplegado en DigitalOcean App Platform (Static Site, plan gratuito).

## Contacto

**Ariel Herrera** · Ingeniero en Conservación de Recursos Naturales
[aherrera@marfutura.org](mailto:aherrera@marfutura.org)
