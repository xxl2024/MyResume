# Visual Report Style Guide — Complete CSS & JS Reference

> This document is a complete reference for reproducing the visual design of the HTML report template.
> It contains every CSS rule, JavaScript snippet, and HTML structure pattern extracted from the
> canonical `visual-report-demo.html`. An LLM can use this file alone to generate pixel-accurate reports.

---

## Table of Contents

1. [External Dependencies](#1-external-dependencies)
2. [Color Palette](#2-color-palette)
3. [Reset & Base Styles](#3-reset--base-styles)
4. [Layout Structure](#4-layout-structure)
5. [Header](#5-header)
6. [Sidebar / Table of Contents](#6-sidebar--table-of-contents)
7. [Content Area](#7-content-area)
8. [Typography](#8-typography)
9. [Code Blocks (Code Window)](#9-code-blocks-code-window)
10. [Syntax Highlight Tokens](#10-syntax-highlight-tokens)
11. [Mermaid Diagram Containers](#11-mermaid-diagram-containers)
12. [Tables](#12-tables)
13. [Callout Boxes](#13-callout-boxes)
14. [Tags](#14-tags)
15. [Metric Cards](#15-metric-cards)
16. [Step Lists](#16-step-lists)
17. [Back-to-Top Button](#17-back-to-top-button)
18. [Scrollbar](#18-scrollbar)
19. [Responsive Breakpoints](#19-responsive-breakpoints)
20. [Scroll-Spy JavaScript](#20-scroll-spy-javascript)
21. [Mermaid Init Script](#21-mermaid-init-script)

---

## 1. External Dependencies

### Fonts (Google Fonts)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
```

| Font             | Weights Used       | Purpose                        |
|------------------|--------------------|--------------------------------|
| Inter            | 400, 500, 600, 700, 800 | Primary UI / body font    |
| JetBrains Mono   | 400, 500, 600      | Code blocks & inline code      |
| Noto Sans SC     | 400, 500, 600, 700 | CJK (Chinese) fallback         |

### Mermaid.js

```html
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
```

---

## 2. Color Palette

### Core Neutrals (Slate scale)

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| slate-950     | `#0f172a` | Darkest bg (header, code blocks), strong text, h2 color |
| slate-800     | `#1e293b` | Header gradient mid, code header bg, h3 color |
| slate-700     | `#334155` | Header gradient end, body text color, th color |
| slate-600     | `#475569` | Paragraph text, td text, li text, tag-gray text |
| slate-500     | `#64748b` | Meta item color, sidebar TOC default, code title, operator token |
| slate-400     | `#94a3b8` | Sidebar label, metric label, li marker, scrollbar thumb hover, mermaid line color |
| slate-200     | `#e2e8f0` | Borders, h2 border-bottom, toc-num bg, step-list left border, table header border, inline code border |
| slate-100     | `#f1f5f9` | TOC hover bg, inline code bg, tag-gray bg, td hover bg, table row border |
| slate-50      | `#f8fafc` | Page background, sidebar bg, metric card bg, th bg |
| white         | `#ffffff` | Content area bg, diagram bg, table bg       |

### Brand / Primary (Blue scale)

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| blue-600      | `#2563eb` | Active TOC link text & border, active toc-num bg |
| blue-500      | `#3b82f6` | Header badge dot, section-icon gradient start, metric gradient start, mermaid primary border, callout info icon bg, step number gradient start |
| blue-400      | `#60a5fa` | Syntax token `.tk-fn` (function)            |
| blue-300      | `#93c5fd` | Header badge text color                     |
| blue-200      | `#bfdbfe` | Callout info border                         |
| blue-100      | `#dbeafe` | Tag-blue bg, mermaid primary fill, active TOC link bg start |
| blue-50       | `#eff6ff` | Callout info background, active TOC gradient start |

### Violet / Indigo

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| indigo-500    | `#6366f1` | Inline code text, section-icon gradient end, step number gradient end |
| violet-500    | `#8b5cf6` | Metric gradient end, diagram top-bar gradient mid |
| violet-400    | `#a855f7` | Mermaid service node border                 |
| violet-800    | `#6b21a8` | Mermaid service node text                   |
| violet-700    | `#7c3aed` | Tag-purple text                             |
| purple-400    | `#c084fc` | Syntax token `.tk-kw` (keyword)             |

### Green

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| green-500     | `#22c55e` | Code dot green, callout success icon bg     |
| green-400     | `#34d399` | Syntax token `.tk-str` (string)             |
| green-300     | `#bbf7d0` | Callout success border                      |
| green-200     | `#dcfce7` | Tag-green bg                                |
| green-50      | `#f0fdf4` | Callout success background                  |
| green-700     | `#166534` | Callout success text                        |
| green-600     | `#16a34a` | Tag-green text                              |

### Amber / Yellow / Orange

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| amber-500     | `#f59e0b` | Callout warning icon bg, mermaid note border |
| amber-400     | `#fbbf24` | Syntax token `.tk-const` (constant)         |
| amber-300     | `#fde68a` | Callout warning border                      |
| amber-100     | `#fef3c7` | Callout warning background, mermaid note bg |
| amber-800     | `#92400e` | Callout warning text                        |
| yellow-500    | `#eab308` | Code dot yellow                             |
| orange-400    | `#fb923c` | Syntax token `.tk-num` (number)             |
| orange-200    | `#ffedd5` | Tag-orange bg                               |
| orange-700    | `#c2410c` | Tag-orange text                             |

### Red / Pink

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| red-500       | `#ef4444` | Code dot red, callout danger icon bg        |
| red-300       | `#fecaca` | Callout danger border                       |
| red-50        | `#fef2f2` | Callout danger background                   |
| red-900       | `#991b1b` | Callout danger text                         |
| pink-500      | `#ec4899` | Diagram top-bar gradient end                |
| pink-400      | `#f472b6` | Syntax token `.tk-dec` (decorator)          |

### Cyan

| Token         | Hex       | Usage                                       |
|---------------|-----------|---------------------------------------------|
| cyan-400      | `#38bdf8` | Syntax token `.tk-type` (type)              |

---

## 3. Reset & Base Styles

```css
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    height: 100%;
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #f8fafc;
    color: #334155;
    line-height: 1.75;
    height: 100%;
    margin: 0;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
```

---

## 4. Layout Structure

The page uses a **centered card** layout: a `.page-container` centers its child horizontally, then a `.main-body` flex row contains a **sidebar** and a **content-wrapper** within a max-width boundary.

```
+--- page bg (#f8fafc) ----------------+
|                                       |
|   +----------+--------------------+   |
|   | .sidebar |  .content-wrapper  |   |
|   | (272px)  |  (flex: 1, scroll) |   |
|   |          |   .main-content    |   |
|   |          |   (max-w: 50rem)   |   |
|   +----------+--------------------+   |
|                                       |
+---------------------------------------+
```

**No dark header.** Title and description go directly in `.main-content` as inline elements.

```css
/* Page container -- centers the main card */
.page-container {
    height: 100%;
    display: flex;
    justify-content: center;
    min-height: 0;
}

/* Main body -- centered card with max-width */
.main-body {
    flex: 1;
    min-height: 0;
    display: flex;
    overflow: hidden;
    background: #ffffff;
    max-width: 1260px;
    width: 100%;
    border-left: 1px solid #e2e8f0;
    border-right: 1px solid #e2e8f0;
}

/* Content scroll area */
.content-wrapper {
    flex: 1;
    min-width: 0;
    min-height: 0;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 44px 56px 80px;
    background: #ffffff;
}

/* Content max-width container */
.main-content {
    max-width: 50rem;   /* 800px */
    margin: 0 auto;
}

/* Sections get scroll-margin for anchor links */
section {
    scroll-margin-top: 24px;
}
```

---

## 5. Title Area (in-content)

Instead of a separate header component, the title and description are placed directly inside `.main-content` as the first elements:

```html
<main class="main-content">
    <h1 style="font-size: 1.75rem; color: #0f172a; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 8px; padding-bottom: 0; border-bottom: none;">Report Title</h1>
    <p style="color: #94a3b8; font-size: 14px; margin-bottom: 32px; padding-bottom: 16px; border-bottom: 1px solid #e2e8f0;">Brief description of the report.</p>
    <!-- sections follow -->
</main>
```

This keeps the page lightweight — no dark gradient, no badge, no meta bar.

---

## 6. Sidebar / Table of Contents

### CSS

```css
.sidebar {
    width: 272px;
    background: #fafbfc;
    border-right: 1px solid #e2e8f0;
    padding: 20px 0;
    overflow-x: hidden;
    overflow-y: auto;
    flex-shrink: 0;
    align-self: stretch;
}

.sidebar-label {
    padding: 0 20px;
    margin-bottom: 16px;
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.toc {
    list-style: none;
    padding: 0 12px;
}

.toc li {
    margin: 2px 0;
}

.toc a {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 7px 12px;
    color: #64748b;
    text-decoration: none;
    font-size: 13px;
    font-weight: 500;
    border-radius: 8px;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    border-left: 2px solid transparent;
    line-height: 1.4;
}

.toc a:hover {
    background: #f1f5f9;
    color: #334155;
}
```

### TOC Heading Levels

```css
/* H1-level TOC items -- bold, with section number badge */
.toc .toc-h1 {
    font-weight: 700;
    font-size: 13px;
    color: #334155;
    margin-top: 12px;
}

.toc .toc-h1:first-child {
    margin-top: 0;
}

/* H2-level TOC items -- indented */
.toc .toc-h2 {
    padding-left: 24px;
    font-size: 12.5px;
    font-weight: 500;
}

/* H3-level TOC items -- more indented, muted */
.toc .toc-h3 {
    padding-left: 36px;
    font-size: 12px;
    color: #a1a1aa;
    font-weight: 400;
}
```

### Active State (scroll-spy)

```css
.toc a.active {
    background: linear-gradient(135deg, #eff6ff 0%, #f0f4ff 100%);
    color: #2563eb;
    border-left-color: #2563eb;
    font-weight: 600;
}
```

### TOC Section Number Badge

```css
.toc-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
    background: #e2e8f0;
    color: #64748b;
    border-radius: 5px;
    font-size: 11px;
    font-weight: 700;
    flex-shrink: 0;
    transition: all 0.2s ease;
}

.toc a.active .toc-num {
    background: #2563eb;
    color: #ffffff;
}
```

### HTML Structure

```html
<nav class="sidebar">
    <div class="sidebar-label">Table of Contents</div>
    <ul class="toc">
        <li><a href="#section1" class="toc-h1"><span class="toc-num">1</span> Section Title</a></li>
        <li><a href="#subsection" class="toc-h2">Subsection Title</a></li>
        <li><a href="#subsubsection" class="toc-h3">Sub-subsection</a></li>
    </ul>
</nav>
```

---

## 7. Content Area

```css
.content-wrapper {
    flex: 1;
    min-width: 0;
    min-height: 0;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 44px 56px 80px;
    background: #ffffff;
}

.main-content {
    max-width: 50rem;
    margin: 0 auto;
}

section {
    scroll-margin-top: 24px;
}
```

---

## 8. Typography

### Headings

```css
h2 {
    font-size: 1.375rem;       /* 22px */
    color: #0f172a;
    margin-top: 56px;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e2e8f0;
    font-weight: 700;
    letter-spacing: -0.02em;
}

/* Remove top margin for the first section */
section:first-of-type h2 {
    margin-top: 0;
}

h3 {
    font-size: 1.125rem;       /* 18px */
    color: #1e293b;
    margin-top: 36px;
    margin-bottom: 16px;
    font-weight: 700;
    letter-spacing: -0.01em;
}

h4 {
    font-size: 1rem;           /* 16px */
    color: #334155;
    margin-top: 28px;
    margin-bottom: 12px;
    font-weight: 600;
}
```

### Section Headings — Plain Numbers

Use plain numbered text for h2 headings. No emoji, no `.section-icon` containers:

```html
<h2>1. Section Title</h2>
<h2>2. Another Section</h2>
```

### Body Text

```css
p {
    margin-bottom: 16px;
    color: #475569;
    font-size: 15px;
    line-height: 1.8;
}

ul, ol {
    margin-bottom: 20px;
    padding-left: 24px;
}

li {
    margin-bottom: 8px;
    color: #475569;
    font-size: 15px;
    line-height: 1.7;
}

li::marker {
    color: #94a3b8;
}

strong {
    color: #0f172a;
    font-weight: 700;
}
```

### Inline Code

```css
:not(pre) > code {
    background: #f1f5f9;
    color: #6366f1;
    padding: 2px 7px;
    border-radius: 5px;
    font-size: 13.5px;
    font-weight: 500;
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid #e2e8f0;
}
```

### Horizontal Rule

```css
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #e2e8f0, transparent);
    margin: 48px 0;
}
```

---

## 9. Code Blocks (Code Window)

The code block is a macOS-style "window" with a header bar (traffic light dots + filename + language badge) and a dark code content area.

### CSS

```css
.code-window {
    margin: 24px 0;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #1e293b;
    background: #0f172a;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
                0 10px 15px -3px rgba(0, 0, 0, 0.08);
}

.code-header {
    background: linear-gradient(180deg, #1e293b 0%, #1a2332 100%);
    padding: 12px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.code-dots {
    display: flex;
    gap: 7px;
}

.code-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.code-dot.red    { background: #ef4444; }
.code-dot.yellow { background: #eab308; }
.code-dot.green  { background: #22c55e; }

.code-title {
    flex: 1;
    text-align: center;
    color: #64748b;
    font-size: 12px;
    font-weight: 500;
    font-family: 'JetBrains Mono', monospace;
}

.code-lang {
    color: #64748b;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    background: rgba(255, 255, 255, 0.06);
    padding: 3px 8px;
    border-radius: 4px;
}

.code-content {
    background: #0f172a;
    padding: 20px 24px;
    overflow-x: auto;
}

.code-content pre {
    margin: 0;
    background: transparent;
    color: #e2e8f0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13.5px;
    line-height: 1.75;
    tab-size: 4;
}

.code-content code {
    font-family: 'JetBrains Mono', monospace;
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
}
```

### HTML Structure

```html
<div class="code-window">
    <div class="code-header">
        <div class="code-dots">
            <span class="code-dot red"></span>
            <span class="code-dot yellow"></span>
            <span class="code-dot green"></span>
        </div>
        <span class="code-title">filename.ext</span>
        <span class="code-lang">LANG</span>
    </div>
    <div class="code-content">
        <pre><code><!-- syntax-highlighted code here --></code></pre>
    </div>
</div>
```

---

## 10. Syntax Highlight Tokens

Use `<span class="tk-XX">` inside `<code>` blocks. These are the token classes and their exact colors:

```css
.tk-kw    { color: #c084fc; }                        /* keyword -- purple */
.tk-fn    { color: #60a5fa; }                        /* function -- blue */
.tk-str   { color: #34d399; }                        /* string -- green */
.tk-cm    { color: #64748b; font-style: italic; }    /* comment -- gray italic */
.tk-num   { color: #fb923c; }                        /* number -- orange */
.tk-op    { color: #94a3b8; }                        /* operator -- muted */
.tk-dec   { color: #f472b6; }                        /* decorator/annotation -- pink */
.tk-type  { color: #38bdf8; }                        /* type name -- cyan */
.tk-const { color: #fbbf24; }                        /* constant -- yellow */
```

### Token Summary Table

| Class      | Color     | Hex       | Used For                           |
|------------|-----------|-----------|-------------------------------------|
| `.tk-kw`   | Purple    | `#c084fc` | Keywords (`class`, `if`, `return`)  |
| `.tk-fn`   | Blue      | `#60a5fa` | Function/method names               |
| `.tk-str`  | Green     | `#34d399` | String literals                     |
| `.tk-cm`   | Gray      | `#64748b` | Comments (italic)                   |
| `.tk-num`  | Orange    | `#fb923c` | Numeric literals                    |
| `.tk-op`   | Muted     | `#94a3b8` | Operators (`=`, `+`, `->`)          |
| `.tk-dec`  | Pink      | `#f472b6` | Decorators / annotations (`@`)      |
| `.tk-type` | Cyan      | `#38bdf8` | Type names (`String`, `Mono`)       |
| `.tk-const`| Yellow    | `#fbbf24` | Constants                           |

### Usage Example

```html
<pre><code><span class="tk-dec">@Component</span>
<span class="tk-kw">public class</span> <span class="tk-type">MyService</span> {
    <span class="tk-kw">private</span> <span class="tk-type">String</span> name <span class="tk-op">=</span> <span class="tk-str">"hello"</span>;
    <span class="tk-cm">// count of items</span>
    <span class="tk-kw">private int</span> count <span class="tk-op">=</span> <span class="tk-num">42</span>;
}</code></pre>
```

---

## 11. Mermaid Diagram Containers

### CSS

```css
.diagram-container {
    background: #ffffff;
    padding: 28px 32px 36px;
    border-radius: 14px;
    margin: 32px 0;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04),
                0 8px 32px rgba(15, 23, 42, 0.06);
    position: relative;
}

/* Rainbow gradient top accent bar */
.diagram-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
    border-radius: 14px 14px 0 0;
}

.diagram-title {
    margin-top: 4px;
    margin-bottom: 24px;
    color: #0f172a;
    text-align: center;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: -0.01em;
}

.mermaid {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    min-height: 200px;
}

.mermaid svg {
    max-width: 100% !important;
    height: auto !important;
}
```

### Flowchart Variant (larger diagrams)

```css
.diagram-container.diagram-flowchart .mermaid {
    min-height: 350px;
    max-height: min(78vh, 800px);
    overflow: auto;
    padding: 8px 4px 16px;
}
```

### HTML Structure

```html
<!-- Standard diagram -->
<div class="diagram-container">
    <div class="diagram-title">Diagram Title</div>
    <div class="mermaid">
        sequenceDiagram
            ...
    </div>
</div>

<!-- Flowchart (large, scrollable) -->
<div class="diagram-container diagram-flowchart">
    <div class="diagram-title">Flowchart Title</div>
    <div class="mermaid">
        flowchart TD
            ...
    </div>
</div>
```

### Mermaid Theme Variables (inline per diagram)

For flowcharts:

```text
%%{init: {'theme': 'base', 'themeVariables': {
    'primaryColor': '#dbeafe',
    'primaryBorderColor': '#3b82f6',
    'primaryTextColor': '#1e293b',
    'lineColor': '#94a3b8',
    'fontSize': '13px'
}}}%%
```

For sequence diagrams:

```text
%%{init: {'theme': 'base', 'themeVariables': {
    'actorBkg': '#dbeafe',
    'actorBorder': '#3b82f6',
    'actorTextColor': '#1e293b',
    'signalColor': '#475569',
    'signalTextColor': '#1e293b',
    'noteBkgColor': '#fef3c7',
    'noteBorderColor': '#f59e0b',
    'noteTextColor': '#92400e',
    'activationBkgColor': '#eff6ff',
    'activationBorderColor': '#3b82f6',
    'fontSize': '13px'
}}}%%
```

### Mermaid classDef Color Schemes

```text
classDef client   fill:#fef3c7, stroke:#f59e0b, color:#92400e
classDef gateway  fill:#dbeafe, stroke:#3b82f6, color:#1e40af
classDef filter   fill:#f0fdf4, stroke:#22c55e, color:#166534
classDef service  fill:#f3e8ff, stroke:#a855f7, color:#6b21a8
classDef infra    fill:#fce7f3, stroke:#ec4899, color:#9d174d
classDef metrics  fill:#dcfce7, stroke:#22c55e, color:#166534
classDef tracing  fill:#e0e7ff, stroke:#6366f1, color:#312e81
classDef logging  fill:#fef3c7, stroke:#f59e0b, color:#92400e
classDef gw       fill:#dbeafe, stroke:#3b82f6, color:#1e40af
```

---

## 12. Tables

```css
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 24px 0;
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

th {
    background: #f8fafc;
    padding: 11px 18px;
    text-align: left;
    font-weight: 700;
    color: #334155;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    border-bottom: 2px solid #e2e8f0;
}

td {
    padding: 13px 18px;
    border-bottom: 1px solid #f1f5f9;
    font-size: 14px;
    color: #475569;
}

tr:last-child td {
    border-bottom: none;
}

tr:hover td {
    background: #f8fafc;
}
```

### HTML Structure

```html
<table>
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data</td>
            <td>Data</td>
        </tr>
    </tbody>
</table>
```

---

## 13. Callout Boxes

Four types: `info`, `warning`, `success`, `danger`.

### Base CSS

```css
.callout {
    border-radius: 10px;
    padding: 16px 20px;
    margin: 24px 0;
    display: flex;
    gap: 12px;
    align-items: flex-start;
    font-size: 14px;
    line-height: 1.7;
}

.callout-icon {
    flex-shrink: 0;
    width: 22px;
    height: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 6px;
    font-size: 13px;
    margin-top: 1px;
}
```

### Type-Specific Styles

| Type      | Background | Border      | Text Color | Icon BG   | Icon Text | Icon Character |
|-----------|------------|-------------|------------|-----------|-----------|----------------|
| `info`    | `#eff6ff`  | `#bfdbfe`   | `#1e40af`  | `#3b82f6` | `white`   | `i`            |
| `warning` | `#fffbeb`  | `#fde68a`   | `#92400e`  | `#f59e0b` | `white`   | `!`            |
| `success` | `#f0fdf4`  | `#bbf7d0`   | `#166534`  | `#22c55e` | `white`   | `&#10003;` (checkmark) |
| `danger`  | `#fef2f2`  | `#fecaca`   | `#991b1b`  | `#ef4444` | `white`   | `&#10005;` (x-mark) |

```css
.callout.info {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1e40af;
}
.callout.info .callout-icon {
    background: #3b82f6;
    color: white;
}

.callout.warning {
    background: #fffbeb;
    border: 1px solid #fde68a;
    color: #92400e;
}
.callout.warning .callout-icon {
    background: #f59e0b;
    color: white;
}

.callout.success {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #166534;
}
.callout.success .callout-icon {
    background: #22c55e;
    color: white;
}

.callout.danger {
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #991b1b;
}
.callout.danger .callout-icon {
    background: #ef4444;
    color: white;
}
```

### HTML Structure

```html
<div class="callout info">
    <div class="callout-icon">i</div>
    <div>Callout content with <strong>bold</strong> and <code>code</code>.</div>
</div>

<div class="callout warning">
    <div class="callout-icon">!</div>
    <div>Warning message.</div>
</div>

<div class="callout success">
    <div class="callout-icon">&#10003;</div>
    <div>Success message.</div>
</div>

<div class="callout danger">
    <div class="callout-icon">&#10005;</div>
    <div>Danger message.</div>
</div>
```

---

## 14. Tags

Small colored pill badges for labeling items (often used inside table cells).

```css
.tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 10px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.02em;
}

.tag-blue   { background: #dbeafe; color: #1d4ed8; }
.tag-green  { background: #dcfce7; color: #16a34a; }
.tag-purple { background: #f3e8ff; color: #7c3aed; }
.tag-orange { background: #ffedd5; color: #c2410c; }
.tag-gray   { background: #f1f5f9; color: #475569; }
```

### Tag Color Table

| Class         | Background | Text Color |
|---------------|------------|------------|
| `.tag-blue`   | `#dbeafe`  | `#1d4ed8`  |
| `.tag-green`  | `#dcfce7`  | `#16a34a`  |
| `.tag-purple` | `#f3e8ff`  | `#7c3aed`  |
| `.tag-orange` | `#ffedd5`  | `#c2410c`  |
| `.tag-gray`   | `#f1f5f9`  | `#475569`  |

### HTML Structure

```html
<span class="tag tag-blue">Label</span>
<span class="tag tag-green">Label</span>
<span class="tag tag-purple">Label</span>
<span class="tag tag-orange">Label</span>
<span class="tag tag-gray">Label</span>
```

---

## 15. Metric Cards

A responsive grid of KPI cards with gradient-text values.

### CSS

```css
.metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin: 24px 0;
}

.metric-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: all 0.2s ease;
}

.metric-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    transform: translateY(-1px);
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.metric-label {
    font-size: 12px;
    color: #94a3b8;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-top: 4px;
}
```

### HTML Structure

```html
<div class="metrics">
    <div class="metric-card">
        <div class="metric-value">&lt; 5ms</div>
        <div class="metric-label">P99 Latency</div>
    </div>
    <div class="metric-card">
        <div class="metric-value">50K</div>
        <div class="metric-label">Peak QPS</div>
    </div>
    <div class="metric-card">
        <div class="metric-value">99.99%</div>
        <div class="metric-label">Availability SLA</div>
    </div>
    <div class="metric-card">
        <div class="metric-value">12</div>
        <div class="metric-label">Downstream Services</div>
    </div>
</div>
```

---

## 16. Step Lists

Ordered lists with numbered circle badges connected by a vertical timeline line.

### CSS

```css
.step-list {
    list-style: none;
    padding: 0;
    counter-reset: step-counter;
}

.step-list li {
    counter-increment: step-counter;
    position: relative;
    padding-left: 48px;
    padding-bottom: 24px;
    margin-bottom: 0;
    border-left: 2px solid #e2e8f0;
    margin-left: 14px;
}

.step-list li:last-child {
    border-left-color: transparent;
    padding-bottom: 0;
}

.step-list li::before {
    content: counter(step-counter);
    position: absolute;
    left: -15px;
    top: 0;
    width: 28px;
    height: 28px;
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: 700;
}
```

### HTML Structure

```html
<ol class="step-list">
    <li>
        <strong>Step Title</strong> &mdash; Step description text.
    </li>
    <li>
        <strong>Step Title</strong> &mdash; Step description text.
    </li>
    <li>
        <strong>Step Title</strong> &mdash; Step description text.
    </li>
</ol>
```

---

## 17. Back-to-Top Button

A fixed-position button that fades in when the user scrolls down.

### CSS

```css
.back-to-top {
    position: fixed;
    bottom: 32px;
    right: 32px;
    width: 40px;
    height: 40px;
    background: #0f172a;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 50;
}

.back-to-top.visible {
    opacity: 1;
    transform: translateY(0);
}

.back-to-top:hover {
    background: #1e293b;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}
```

### HTML Structure

```html
<button class="back-to-top" id="backToTop"
        onclick="document.querySelector('.content-wrapper').scrollTo({top: 0, behavior: 'smooth'})">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M18 15l-6-6-6 6"/>
    </svg>
</button>
```

---

## 18. Scrollbar

Custom WebKit scrollbar styling (applies to all scrollable areas).

```css
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
```

---

## 19. Responsive Breakpoints

### Breakpoint: max-width 900px (mobile / narrow)

The sidebar becomes a sticky horizontal strip at the top; the layout switches from row to column.

```css
@media (max-width: 900px) {
    html, body {
        height: auto;
        overflow: auto;
    }

    .page-container {
        height: auto;
        min-height: 100vh;
    }

    .main-body {
        flex-direction: column;
        min-height: auto;
        overflow: visible;
        border-left: none;
        border-right: none;
    }

    .sidebar {
        width: 100%;
        position: sticky;
        top: 0;
        z-index: 20;
        max-height: min(40vh, 280px);
        border-right: none;
        border-bottom: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    .content-wrapper {
        overflow: visible;
        padding: 24px 20px 48px;
    }

    .metrics {
        grid-template-columns: repeat(2, 1fr);
    }
}
```

### Breakpoint: 901px - 1200px (medium / tablet)

Sidebar narrows slightly; content padding is reduced.

```css
@media (max-width: 1200px) and (min-width: 901px) {
    .sidebar {
        width: 240px;
    }

    .content-wrapper {
        padding: 36px 36px 64px;
    }
}
```

---

## 20. Scroll-Spy JavaScript

This script handles three things:
1. Smooth-scrolling when a TOC link is clicked.
2. Highlighting the active TOC link as the user scrolls (IntersectionObserver-based scroll-spy).
3. Showing/hiding the back-to-top button based on scroll position.

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const tocLinks = document.querySelectorAll('.toc a');
    const sections = document.querySelectorAll('section[id]');
    const contentWrapper = document.querySelector('.content-wrapper');
    const backToTop = document.getElementById('backToTop');

    // 1. Smooth scroll on TOC click
    tocLinks.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const target = document.getElementById(targetId);
            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    // 2. Scroll spy via IntersectionObserver
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocLinks.forEach(l => l.classList.remove('active'));
                const activeLink = document.querySelector(`.toc a[href="#${entry.target.id}"]`);
                if (activeLink) activeLink.classList.add('active');
            }
        });
    }, {
        root: contentWrapper,
        rootMargin: '-5% 0px -85% 0px',
        threshold: 0
    });

    sections.forEach(section => observer.observe(section));

    // 3. Back-to-top visibility toggle
    contentWrapper.addEventListener('scroll', () => {
        backToTop.classList.toggle('visible', contentWrapper.scrollTop > 300);
    });
});
```

### Key IntersectionObserver Settings

| Parameter    | Value                   | Purpose                                      |
|--------------|-------------------------|----------------------------------------------|
| `root`       | `.content-wrapper`      | Observe within the scrollable content area   |
| `rootMargin` | `'-5% 0px -85% 0px'`   | Only a narrow band near the top triggers activation |
| `threshold`  | `0`                     | Fire as soon as any part enters the band     |

### Back-to-Top Trigger

The button gains the `.visible` class (opacity: 1, translateY(0)) when `contentWrapper.scrollTop > 300`.

---

## 21. Mermaid Init Script

Global Mermaid initialization (runs before DOMContentLoaded; the library renders on load).

```javascript
mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
        primaryColor: '#dbeafe',
        primaryBorderColor: '#3b82f6',
        primaryTextColor: '#1e293b',
        lineColor: '#94a3b8',
        secondaryColor: '#f0fdf4',
        tertiaryColor: '#fef3c7',
        fontSize: '13px'
    },
    flowchart: {
        curve: 'basis',
        useMaxWidth: true
    },
    sequence: {
        useMaxWidth: true,
        wrap: true,
        mirrorActors: false
    }
});
```

### Mermaid Theme Variables Reference

| Variable              | Value     | Maps To                        |
|-----------------------|-----------|--------------------------------|
| `primaryColor`        | `#dbeafe` | Node fill (blue-100)           |
| `primaryBorderColor`  | `#3b82f6` | Node border (blue-500)         |
| `primaryTextColor`    | `#1e293b` | Node text (slate-800)          |
| `lineColor`           | `#94a3b8` | Arrow/edge color (slate-400)   |
| `secondaryColor`      | `#f0fdf4` | Secondary node fill (green-50) |
| `tertiaryColor`       | `#fef3c7` | Tertiary node fill (amber-100) |
| `fontSize`            | `13px`    | Diagram text size              |

### Flowchart Config

| Option       | Value   | Purpose                              |
|--------------|---------|--------------------------------------|
| `curve`      | `basis` | Smooth curved edges (B-spline)       |
| `useMaxWidth`| `true`  | SVG scales to fit container width    |

### Sequence Diagram Config

| Option        | Value   | Purpose                                  |
|---------------|---------|------------------------------------------|
| `useMaxWidth` | `true`  | SVG scales to container width            |
| `wrap`        | `true`  | Long text wraps inside boxes             |
| `mirrorActors`| `false` | Do NOT repeat actor labels at bottom     |

---

## Complete HTML Skeleton

For reference, here is the minimal complete page skeleton combining all sections above:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Title</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Paste ALL CSS from sections 3-18 here */
    </style>
</head>
<body>
    <div class="page-container">
        <div class="main-body">
            <nav class="sidebar">
                <div class="sidebar-label">目录导航</div>
                <ul class="toc">
                    <li><a href="#s1" class="toc-h1"><span class="toc-num">1</span> Section</a></li>
                    <li><a href="#s1a" class="toc-h2">Subsection</a></li>
                </ul>
            </nav>

            <div class="content-wrapper">
                <main class="main-content">
                    <h1 style="font-size: 1.75rem; color: #0f172a; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 8px; padding-bottom: 0; border-bottom: none;">Report Title</h1>
                    <p style="color: #94a3b8; font-size: 14px; margin-bottom: 32px; padding-bottom: 16px; border-bottom: 1px solid #e2e8f0;">Brief description.</p>

                    <section id="s1">
                        <h2>1. Section Title</h2>
                        <p>Content...</p>
                    </section>

                    <hr>

                    <section id="s1a">
                        <h3>Subsection</h3>
                        <p>More content...</p>
                    </section>

                </main>
            </div>
        </div>
    </div>

    <button class="back-to-top" id="backToTop"
            onclick="document.querySelector('.content-wrapper').scrollTo({top:0,behavior:'smooth'})">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 15l-6-6-6 6"/>
        </svg>
    </button>

    <script>
        /* Mermaid init + Scroll-spy -- paste from sections 20-21 */
    </script>
</body>
</html>
```

---

*End of style guide.*
