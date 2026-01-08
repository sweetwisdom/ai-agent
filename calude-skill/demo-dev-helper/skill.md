---
name: demo-dev-helper
description: Generate complete, runnable single-page HTML applications using Vue 3 + Tailwind CSS + FontAwesome (all via CDN) based on screenshots, structure descriptions, or text requirements. Use when users need to quickly create high-fidelity UI prototypes or demo pages that can run directly in a browser without any build tools. Perfect for prototyping, demonstrations, or learning Vue 3 and Tailwind CSS.
---

# Demo开发助手 (Demo Dev Helper)

Generate complete, runnable single-page HTML applications using **HTML + Vue 3 + Tailwind CSS + FontAwesome** (all via CDN) based on screenshots, structure descriptions, or text requirements.

## Core Workflow

When users provide input, follow these steps:

1. **Analyze requirements** - Identify page type, core functionality, UI components needed
2. **Design HTML structure** - Use semantic HTML tags, plan Vue data binding and event handling
3. **Implement styles** - Prioritize Tailwind CSS utility classes, use inline `<style>` for complex styles
4. **Implement interaction logic** - Define reactive data in `<script setup>`, implement event handlers
5. **Complete details** - Add reasonable mock data, code comments, ensure all interactions work
6. **Output complete code** - Generate full HTML file with all CDN imports, formatted code, usage instructions

## Input Processing

Handle different input types:

- **Screenshot provided**: Analyze layout, colors, fonts, spacing, UI elements, icons, interaction states. Use Tailwind CSS utility classes to restore styles.
- **Structure description**: Understand page structure and functional requirements from text. Reference common design patterns and best practices.
- **JSON data**: Infer page type from data structure, design appropriate data display, implement necessary data operations.
- **No input provided**: Prompt user to provide screenshot, description, or requirements. Do not generate code without input.

## Technical Stack Requirements

**Required stack:**
- **Framework**: Vue 3 (`<script setup>` + Composition API) via CDN
- **UI library**: No specific UI library; icons via **FontAwesome** (CDN)
- **Styling**: **Tailwind CSS** utility classes (via CDN), inline `<style>` for complex styles
- **All dependencies**: Introduced via `<script>` and `<link>` CDN in `<head>`

**Optional libraries** (introduce as needed):
- Drag and drop: `https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js`
- Charts: `https://cdn.jsdelivr.net/npm/chart.js`
- Date handling: `https://cdn.jsdelivr.net/npm/dayjs`
- Animation: `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js`

## Output Requirements

Generated HTML files must meet these standards:

1. **Completeness**: Full `<!DOCTYPE html>` declaration, `<head>` (CDN imports, meta tags, title), `<body>` (Vue mount point + complete UI), `<script setup>` (Vue logic), `<style>` (if necessary)
2. **Runnable**: Can run directly in browser, no pseudo-code (`...`, `TODO`, `// implementation code`, etc.), all features have actual implementation or mock data
3. **Code quality**: Clean, semantic code, proper HTML semantic tags, Tailwind CSS utility classes, Vue Composition API (ref, reactive, computed, watch)
4. **Data handling**: Use mock data + comments for uncertain interactions (API requests, state management), mock data should be realistic and complete
5. **Responsive design** (optional but recommended): Use Tailwind responsive classes (`sm:`, `md:`, `lg:`, `xl:`)

## Code Quality Standards

Generated code must satisfy:
- ✅ **Completeness**: Complete HTML structure, all features implemented
- ✅ **Runnable**: Can open directly in browser, no build steps required
- ✅ **No pseudo-code**: No `...`, `TODO`, `// implementation code` placeholders
- ✅ **Semantic**: Proper use of HTML5 semantic tags
- ✅ **Responsive**: Use Tailwind responsive classes, adapt to different screens
- ✅ **Modern**: Use Vue 3 Composition API, modern code style
- ✅ **Well-commented**: Key logic has comments, mock parts have explanations
- ✅ **Beautiful**: Follow modern UI design trends, reasonable color scheme, comfortable spacing

## Best Practices

- **Layout**: Prioritize Flexbox and Grid
- **Colors**: Use Tailwind color palette
- **Spacing**: Use unified scale
- **Icons**: Use FontAwesome
- **Forms**: Proper input styling with focus states
- **Buttons**: Include hover and transition effects
- **Cards**: Use white background, rounded corners, shadows
- **Responsive**: Use Tailwind responsive classes

For detailed implementation guidelines, examples, and common patterns, see:
- [Technical Details](references/technical-details.md) - HTML structure, Vue patterns, Tailwind usage
- [Best Practices](references/best-practices.md) - Detailed guidelines and common mistakes to avoid

## Error Handling

- **Unclear user input**: Ask for more details, provide 2-3 design options
- **Complex functionality**: Prioritize referencing mature lightweight libraries (from CDN), don't hand-write complex logic
- **Unclear or partially obscured screenshots**: Infer complete design from visible parts, reference common design patterns
- **Technology stack conflicts**: Strictly adhere to Vue 3 + Tailwind CSS + FontAwesome stack
- **Performance**: Avoid excessive DOM nesting, use v-if and v-show appropriately

