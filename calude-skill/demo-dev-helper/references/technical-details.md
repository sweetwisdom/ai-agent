# Technical Details

## HTML Structure Specification

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>页面标题</title>

    <!-- 1. Tailwind CSS（样式框架） -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- 2. FontAwesome（图标库） -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- 3. Vue 3（JS框架） -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

    <!-- 4. 其他库（按需） -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <!-- 5. 自定义样式（可选） -->
    <style>
        /* 复杂动画、自定义类 */
    </style>
</head>
<body class="bg-gray-100">
    <!-- Vue 挂载点 -->
    <div id="app">
        <!-- UI结构（使用Tailwind类） -->
    </div>

    <!-- Vue 逻辑 -->
    <script>
        const { createApp, ref, computed } = Vue;
        createApp({
            setup() {
                // 响应式数据和方法
                return { /* 暴露给模板 */ };
            }
        }).mount('#app');
    </script>
</body>
</html>
```

## Vue 3 Composition API Pattern

```javascript
setup() {
    // 1. 响应式数据
    const count = ref(0);
    const user = reactive({ name: '张三' });

    // 2. 计算属性
    const doubleCount = computed(() => count.value * 2);

    // 3. 方法
    const increment = () => {
        count.value++;
    };

    // 4. 生命周期
    onMounted(() => {
        console.log('组件已挂载');
    });

    // 5. 监听
    watch(count, (newVal) => {
        console.log('count变化:', newVal);
    });

    // 6. 返回（暴露给模板）
    return {
        count,
        user,
        doubleCount,
        increment
    };
}
```

## Tailwind CSS Common Classes

```html
<!-- 布局 -->
<div class="flex items-center justify-between">
<div class="grid grid-cols-3 gap-4">

<!-- 间距 -->
<div class="p-4 m-2">       <!-- padding: 1rem, margin: 0.5rem -->
<div class="px-6 py-3">     <!-- padding-x: 1.5rem, padding-y: 0.75rem -->

<!-- 颜色 -->
<div class="bg-blue-500 text-white">
<div class="bg-gray-100 text-gray-800">

<!-- 尺寸 -->
<div class="w-full h-screen">
<div class="max-w-4xl mx-auto">

<!-- 边框和圆角 -->
<div class="border border-gray-300 rounded-lg">
<div class="shadow-lg">

<!-- 响应式 -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
```

## Standard Template Structure

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[页面标题]</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Vue 3 -->
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

    <!-- 其他必要的库（按需引入） -->
    <!-- <script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script> -->

    <!-- 自定义样式（可选） -->
    <style>
        /* 复杂样式、动画、自定义类 */
    </style>
</head>
<body class="bg-gray-100">
    <!-- Vue 挂载点 -->
    <div id="app">
        <!-- 完整的UI结构，使用Tailwind类 -->
    </div>

    <script>
        const { createApp, ref, reactive, computed, watch } = Vue;

        createApp({
            setup() {
                // 响应式数据
                const data = ref([]);
                const state = reactive({
                    // 状态管理
                });

                // 计算属性
                const computed_value = computed(() => {
                    // 计算逻辑
                });

                // 方法
                const handleAction = () => {
                    // 事件处理
                };

                // 生命周期（如需要）
                watch(() => {
                    // 监听逻辑
                });

                // 返回暴露给模板的内容
                return {
                    data,
                    state,
                    computed_value,
                    handleAction
                };
            }
        }).mount('#app');
    </script>
</body>
</html>
```

