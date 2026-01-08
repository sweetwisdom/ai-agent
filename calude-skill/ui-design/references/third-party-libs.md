# Third-party Libraries

## Library Selection Guide

| Functionality | Recommended Library | CDN Link |
|--------------|-------------------|-----------|
| **Light Interactions** | Alpine.js | `<script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>` |
| **Complex State Management** | Vue 3 | `<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>` |
| **React Components** | React + ReactDOM | `<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>` |
| **Data Visualization** | Chart.js / ECharts | `<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>` |
| **Animation Effects** | GSAP / Anime.js | `<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>` |
| **Form Validation** | Zod / Yup | `<script src="https://cdn.jsdelivr.net/npm/zod@latest"></script>` |
| **Date Picker** | Flatpickr | `<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>` |
| **Rich Text Editor** | Quill / TinyMCE | `<script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>` |
| **Drag and Sort** | SortableJS | `<script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script>` |
| **Notifications** | Toastify / Notyf | `<script src="https://cdn.jsdelivr.net/npm/toastify-js"></script>` |
| **Image Lazy Loading** | Lozad.js | `<script src="https://cdn.jsdelivr.net/npm/lozad"></script>` |
| **Scroll Animation** | AOS (Animate On Scroll) | `<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>` |

## When to Use Third-party Libraries

| Scenario | Recommended Solution | Reason |
|----------|---------------------|--------|
| Simple button click | Native JavaScript | No additional dependencies needed |
| Simple state toggle | Alpine.js | Lightweight (15KB), low learning curve |
| Complex forms, multi-step flows | Vue 3 | Mature reactive system |
| Data visualization | Chart.js / ECharts | Professional chart library, powerful features |
| Complex animations | GSAP | Excellent performance, clean API |
| Rich text editing | Quill / TinyMCE | Ready-made complete solution |

## Prohibited Libraries

- ❌ jQuery (outdated, Tailwind + Alpine.js can replace)
- ❌ Large UI frameworks (Bootstrap, Element UI) conflict with Tailwind
- ❌ Libraries requiring build tools (npm packages), only use CDN versions

## Selection Principles

- ✅ Prefer native JavaScript or Alpine.js for simple functionality
- ✅ Use Vue/React for complex interactions (multi-step forms, state synchronization)
- ✅ Must introduce chart library for data visualization needs
- ✅ All libraries via CDN, ensuring immediate use

