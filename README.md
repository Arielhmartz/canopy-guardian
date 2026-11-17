# Soundscape Sentinel

Landing page de **Soundscape Sentinel** — nodos IoT de monitoreo acústico pasivo con IA en el borde que entregan, 24/7, riqueza y ocurrencia de aves, índices de paisaje sonoro (NDSI, ACI, ADI) y variables ambientales, con reportes listos para expedientes SEIA/RCA. Dirigido a consultoras ambientales y titulares de proyectos de energía, minería e infraestructura en Chile y LATAM.

## Estado del proyecto

- Idea validada → MVP; reutiliza la plataforma acústica desarrollada para Canopy GuardIAn
- Postulación en curso a **Start-Up Chile Build (BIG13), 2026**
- Sitio en inglés (requisito de la convocatoria y foco LATAM)

> El proyecto anterior, **Canopy GuardIAn** (detección de tala ilegal, CORFO Semilla Inicia Biobío), se conserva en `canopy-guardian.html` y `comercial.html`.

## Estructura

```
canopy-guardian/
├── index.html              # Landing principal — Soundscape Sentinel (EN)
├── canopy-guardian.html    # Landing anterior — Canopy GuardIAn (versión CORFO)
├── comercial.html          # Canopy GuardIAn — versión comercial alternativa
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
[arielmar.upv@gmail.com](mailto:arielmar.upv@gmail.com)
