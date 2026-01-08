# Platform Templates

## File Organization

### PC Desktop / Admin System

```
ui-design-output/
├── index.html           # Main entry, iframe tiled display
├── dashboard.html       # Dashboard
├── user-management.html # User management
├── data-management.html # Data management
├── settings.html        # Settings
└── [other pages].html
```

### Mobile App

```
ui-design-output/
├── index.html          # Main entry, Tab switching display
├── home.html           # Home
├── discover.html       # Discover
├── messages.html       # Messages
├── profile.html        # Profile
└── [feature pages].html
```

### Responsive Web

```
ui-design-output/
├── index.html          # Homepage (responsive)
├── about.html          # About page
├── products.html       # Products page
├── contact.html        # Contact page
└── [other pages].html
```

## HTML Templates

### Mobile Template (375px width)

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>[Page Title]</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
      body { width: 375px; margin: 0 auto; }
      /* Touch optimization, gesture support */
    </style>
  </head>
  <body class="bg-gray-50">
    <!-- Top status bar -->
    <header class="sticky top-0 z-50">...</header>

    <!-- Main content area -->
    <main class="pb-20">...</main>

    <!-- Bottom Tab navigation -->
    <nav class="fixed bottom-0 left-0 right-0">...</nav>
  </body>
</html>
```

### PC Desktop Template (1920px width)

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>[Page Title]</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  </head>
  <body>
    <header>...</header>
    <div class="flex">
      <aside class="w-64">...</aside>
      <main class="flex-1">...</main>
    </div>
  </body>
</html>
```

## Layout Requirements

### PC Desktop

- Top navigation bar: System logo, search box, notifications, user info, settings
- Sidebar: Navigation menu (collapsible)
- Main content area: Multi-column layout, data tables, charts
- Interface size: 1920x1080 or 1440x900
- Mouse hover effects, tooltips

### Mobile

- Top navigation bar: Title, back button, right-side actions
- Bottom Tab bar: 3-5 main function entries
- Single-column content layout, card design
- Interface size: 375x667 (iPhone SE) or 390x844 (iPhone 12)
- Pull-to-refresh, pull-up load, swipe gestures

### Tablet

- Collapsible sidebar + top navigation
- Dual or triple-column layout (master-detail structure)
- Interface size: 768x1024 (iPad) or 1024x768 (landscape)
- Split-screen operations, drag support

### Responsive Web

- Fluid layout, use Tailwind breakpoints (sm/md/lg/xl)
- Mobile: Hamburger menu + single column
- Tablet: Dual-column layout
- Desktop: Multi-column layout + sidebar

## index.html Structure

### PC Desktop: iframe Tiled Display

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Overview</title>
    <style>
        body { margin: 0; padding: 20px; background: #f5f5f5; }
        .page-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
            gap: 20px;
        }
        iframe {
            width: 100%;
            height: 800px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background: white;
        }
    </style>
</head>
<body>
    <h1>System Pages Overview</h1>
    <div class="page-grid">
        <div>
            <h2>Dashboard</h2>
            <iframe src="dashboard.html"></iframe>
        </div>
        <div>
            <h2>User Management</h2>
            <iframe src="user-management.html"></iframe>
        </div>
        <!-- More pages -->
    </div>
</body>
</html>
```

### Mobile: Tab Switching

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body x-data="{ activeTab: 'home' }">
    <!-- Tab content -->
    <div x-show="activeTab === 'home'">
        <!-- Home content -->
    </div>
    
    <!-- Bottom Tab bar -->
    <nav class="fixed bottom-0 left-0 right-0">
        <button @click="activeTab = 'home'">Home</button>
        <!-- More tabs -->
    </nav>
</body>
</html>
```

