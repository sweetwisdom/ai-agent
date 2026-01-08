# Best Practices

## Common Mistakes to Avoid

### 1. ❌ Don't Use Pseudo-code

**Wrong:**
```javascript
const fetchData = async () => {
    // TODO: 实现API调用
    ...
}
```

**Correct:**
```javascript
const fetchData = async () => {
    // 模拟API调用，实际开发时替换为真实API
    const mockData = [
        { id: 1, name: '示例数据' }
    ];
    data.value = mockData;
}
```

### 2. ❌ Don't Over-nest DOM

**Wrong:**
```html
<div><div><div><div><div><span>内容</span></div></div></div></div></div>
```

**Correct:**
```html
<div class="container">
    <span class="content">内容</span>
</div>
```

### 3. ❌ Don't Mix Technology Stacks

**Wrong:**
```html
<script src="jquery.min.js"></script>
<script>$('#btn').click(() => {...})</script>
```

**Correct:**
```html
<button @click="handleClick">按钮</button>
```

## Layout Best Practices

### 1. Prioritize Flexbox and Grid

```html
<div class="flex items-center justify-between">
<div class="grid grid-cols-3 gap-4">
```

### 2. Use Tailwind Color Palette

```html
<div class="bg-blue-500 text-white">
<button class="bg-green-600 hover:bg-green-700">
```

### 3. Use Unified Spacing Scale

```html
<div class="p-4 m-2">  <!-- 4=1rem=16px, 2=0.5rem=8px -->
<div class="space-y-4">  <!-- 子元素之间垂直间距 -->
```

### 4. Use FontAwesome Icons

```html
<i class="fas fa-user"></i>
<i class="far fa-heart"></i>
```

### 5. Form Styling

```html
<input class="border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
```

### 6. Button Styling

```html
<button class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded transition duration-200">
```

### 7. Card Components

```html
<div class="bg-white rounded-lg shadow p-6">
```

### 8. Responsive Design

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
```

## Input Handling Best Practices

### Provide Clear Requirements

**✅ Good:**
```
创建一个商品列表页面，要求：
- 顶部有搜索框和分类筛选
- 商品以卡片形式展示（3列布局）
- 每个卡片显示图片、名称、价格、评分
- 支持点击查看详情
- 底部有分页
- 整体采用蓝色主题
```

**❌ Bad:**
```
做个商品页面
```

### Upload High-Quality Screenshots

- Screenshots should be clear and complete
- Include main functional areas
- If multiple states exist, provide separate screenshots
- Explain special interaction effects

### Provide Real Data Structures

```json
{
  "users": [
    {
      "id": 1,
      "name": "张三",
      "avatar": "https://...",
      "role": "admin",
      "email": "zhang@example.com",
      "createdAt": "2025-01-15"
    }
  ]
}
```

### Specify Technical Requirements

- What special effects are needed (animations, transitions)
- Whether complex functionality is needed (drag and drop, charts)
- Responsive requirements (which devices to prioritize)
- Performance requirements (how to handle large amounts of data)

## Code Quality Guidelines

1. **Completeness**: Complete HTML structure, all features implemented
2. **Runnable**: Can open directly in browser, no build steps required
3. **No pseudo-code**: No `...`, `TODO`, `// implementation code` placeholders
4. **Semantic**: Proper use of HTML5 semantic tags
5. **Responsive**: Use Tailwind responsive classes, adapt to different screens
6. **Modern**: Use Vue 3 Composition API, modern code style
7. **Well-commented**: Key logic has comments, mock parts have explanations
8. **Beautiful**: Follow modern UI design trends, reasonable color scheme, comfortable spacing

