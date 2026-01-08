# Best Practices

## Design Principles

- 🎯 **User-centered**: PC focuses on efficiency, mobile on convenience, tablet on comfort
- 🎨 **Balance beauty and practicality**: Don't over-design, maintain restraint
- 📐 **Maintain design consistency**: Follow target platform design specifications
- ♿ **Accessibility**: Consider needs of different user groups
- 📱 **Platform characteristics first**: Leverage platform-unique interaction methods

## Technical Limitations

- ⚠️ Avoid using Tailwind's `list-item` class name
- ⚠️ iframe embedding may affect some interactions (only use for PC display)
- ⚠️ CDN resources require network connection
- ⚠️ Large code files need to be written in batches
- ⚠️ Mobile requires testing touch event compatibility
- ⚠️ Responsive design requires testing multiple breakpoints

## Best Practices

- ✅ **Prioritize Tailwind utility classes**, reduce custom CSS
- ✅ **Icon library selection**: FontAwesome / Iconify / Heroicons
- ✅ **Third-party libraries on demand**: Intelligently select based on functional requirements
- ✅ **Add code comments**: Facilitate subsequent modifications
- ✅ **Clear file structure**: Unified naming conventions
- ✅ **Multi-platform testing**: Verify display effects at different sizes
- ✅ **Performance optimization**: Image lazy loading, CDN acceleration
- ✅ **Progressive enhancement**: Ensure basic functionality works on low-end devices

## Common Questions

**Q: How to determine which platform to use?**
A: AI automatically identifies based on keywords. If uncertain, will actively ask user to select platform type.

**Q: Why use iframe tiling for PC desktop?**
A: Only for prototype display, convenient for viewing all interfaces at once. Actual development can be changed to single-page application or multi-page navigation.

**Q: How to simulate touch interactions on mobile?**
A: Use CSS `:active` pseudo-class and JavaScript `touchstart/touchend` events to simulate touch feedback.

**Q: How to handle large code files?**
A: AI automatically detects code volume, will write in batches when exceeding 500 lines, create framework first then fill content.

**Q: Can generated code be used directly in production?**
A: This is a high-fidelity prototype, suitable for demonstrations and early development reference. Production environment needs further optimization (componentization, state management, API integration, etc.).

**Q: Can specific design styles be specified?**
A: Yes! Specify desired style in requirements (minimalist, tech-savvy, business-like, etc.), AI will adjust design accordingly.

**Q: Which third-party libraries are supported?**
A: Supports all popular libraries that can be introduced via CDN, such as Vue, React, Alpine.js, Chart.js, GSAP, etc. AI intelligently selects the most appropriate library based on functional requirements.

**Q: How to switch between mobile and PC?**
A: Simply specify platform in requirement description, or use relevant keywords (e.g., "App", "admin system"), AI will automatically identify and adapt.

## Providing Clear Requirements

❌ **Not recommended**:
```
帮我做一个后台系统
```

✅ **Recommended**:
```
设计一个内容管理系统后台，需要：
- 文章管理（创建、编辑、发布）
- 分类和标签管理
- 评论审核
- 媒体库（图片上传和管理）
- 站点设置
```

## Specifying Design Style

If you have specific design preferences, please specify:
```
设计风格：科技感、深色主题、使用蓝紫色渐变
```

## Specifying Key Functions

If there are particularly important functions, please emphasize:
```
重点：数据统计仪表盘需要展示实时数据图表
```

