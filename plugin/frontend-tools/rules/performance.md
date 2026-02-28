# 前端性能优化准则

## 核心策略

- **先测后优**：用 Lighthouse、Chrome DevTools 等定位真实瓶颈，再针对性优化
- **关注关键路径**：首屏渲染、核心交互路径优先
- **包体与加载**：控制 bundle 体积、按需与懒加载

## 包体与依赖

- 避免引入巨型库（整库引用），优先 tree-shake 友好或按需引入
- 路由与弹窗等非首屏组件使用动态 `import()` 懒加载
- 定期用 `pnpm build` 或 `vite-bundle-visualizer` 查看产物与 chunk 划分

## 渲染与资源

- 列表长数据使用虚拟滚动或分页，避免一次渲染过多 DOM
- 图片：合适尺寸、现代格式（WebP/AVIF）、懒加载（loading="lazy" 或 IntersectionObserver）
- 避免在组件内定义大对象/大数组导致每次渲染重新创建，可提到模块级或 useMemo/useRef

## Core Web Vitals

- **LCP**：关键资源预加载、服务端渲染或骨架屏、减少主线程阻塞
- **FID/INP**：减少长任务、拆分逻辑或使用 Web Worker
- **CLS**：图片/媒体设置尺寸、字体避免 FOIT/FOUT、动态内容预留占位

## 框架相关

- React：避免在渲染中创建新函数/对象导致子组件无效重渲染，合理使用 memo/useMemo/useCallback
- Vue：避免在模板中写复杂表达式，计算属性与响应式粒度适中
- 状态更新批量、按需，避免过于细粒度导致频繁更新

## 检查清单

- [ ] 首屏路由与重组件已懒加载
- [ ] 图片有尺寸与懒加载
- [ ] 无明显的重复打包或过大的单 chunk
- [ ] 关键交互无长时间主线程阻塞
