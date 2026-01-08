# Visual Effects

## Glass Morphism Effect

```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}
```

## Gradient Backgrounds

### Linear Gradient

```css
.gradient-bg {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Radial Gradient

```css
.radial-gradient {
  background: radial-gradient(circle at center, #667eea 0%, #764ba2 100%);
}
```

## Scrollbar Hiding

```css
.scrollable {
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE 10+ */
}
.scrollable::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Edge */
}
```

## Hover Animations

```css
.hover-lift {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}
```

## Shadow Effects

```css
.shadow-soft {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.shadow-medium {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.shadow-strong {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}
```

## Border Radius

```css
.rounded-soft {
  border-radius: 8px;
}

.rounded-medium {
  border-radius: 12px;
}

.rounded-strong {
  border-radius: 16px;
}
```

## Image Resources

### Using Real Images

- **Unsplash**: `https://source.unsplash.com/800x600/?business`
- **Pexels API**: `https://images.pexels.com/photos/...`

### Example Usage

```html
<img src="https://source.unsplash.com/800x600/?technology" alt="Technology">
```

## Dark Mode Support

```css
.dark-mode {
  background-color: #1a1a1a;
  color: #ffffff;
}

.light-mode {
  background-color: #ffffff;
  color: #1a1a1a;
}
```

## Transition Effects

```css
.smooth-transition {
  transition: all 0.3s ease-in-out;
}

.fade-in {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

