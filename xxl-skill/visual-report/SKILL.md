---
name: visual-report
description: Generate beautiful, interactive single-file HTML reports with Mermaid diagrams, a sticky sidebar table of contents, code blocks, and rich visual formatting. Use this skill whenever the user wants to visualize, summarize, or present information as an HTML page — including technical documentation, architecture overviews, code analysis reports, data exploration results, process walkthroughs, system design docs, or any content that benefits from structured visual presentation. Trigger whenever the user says things like "generate an HTML report", "visualize this", "make a readable summary page", "create a doc with diagrams", "show me the architecture", or asks for any kind of formatted, browsable output with diagrams or interactive elements.
---

# Visual Report

Generate polished, interactive, single-file HTML reports that are a pleasure to read. Every report is a self-contained `.html` file the user can open in any browser — no build step, no dependencies to install.

## Why this skill exists

Raw text and markdown are fine for quick notes, but when the user needs to present, share, or deeply understand something — an architecture, a codebase walkthrough, a data analysis — a well-structured visual report is dramatically more effective. This skill bridges the gap between "I have information" and "I can see and navigate it clearly."

## Output format

Every report is a **single `.html` file** that includes:
- All CSS inlined in a `<style>` block
- All JS inlined in `<script>` blocks
- Google Fonts loaded via `<link>` (Inter + Noto Sans SC + JetBrains Mono)
- Mermaid loaded via CDN (`https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js`)
- No other external dependencies

The file should open correctly by double-clicking in any modern browser.

## Page structure

The layout is a **centered card** with sidebar + scrollable content:

```
┌─ page background (#f8fafc) ──────────────────┐
│                                               │
│   ┌────────────┬──────────────────────────┐   │
│   │            │  Title + description     │   │
│   │  Sidebar   │  ───────────────────     │   │
│   │  (fixed,   │                          │   │
│   │   its own  │  Content sections        │   │
│   │   scroll)  │  (max-width ~50rem)      │   │
│   │            │                          │   │
│   │  - Label   │  Diagrams, code blocks,  │   │
│   │  - TOC     │  tables, callouts...     │   │
│   │            │                          │   │
│   └────────────┴──────────────────────────┘   │
│                                [ ↑ Back to top]│
└───────────────────────────────────────────────┘
```

### No dark header
Don't use a large dark header. Instead, put the title and description directly in the content area as the first elements — a bold h1 followed by a muted description paragraph with a bottom border. This keeps the page clean and lightweight.

### Centered layout
The sidebar + content card (`max-width: 1260px`) is horizontally centered on the page with `justify-content: center` on the container, and has left/right borders to define its edges. This means on wide screens the sidebar is near the center of the page, not flush to the far left.

### Sidebar
- Width 272px, light background (`#fafbfc`)
- "目录导航" uppercase label in small muted text
- TOC items with numbered badges (`.toc-num`) for top-level sections
- Active state: blue gradient background + blue left border + blue number badge
- On narrow screens (< 900px), collapses to sticky top bar

### Content area
- Centered with `max-width: 50rem`
- Smooth scroll-spy that highlights the current TOC item
- "Back to top" floating button
- Each section wrapped in `<section id="...">`

## Section headings

Use **plain numbers** for h2 headings — no emoji icons, no special containers. Just clean text:

```html
<h2>1. 架构总览</h2>
<h2>2. 路由设计</h2>
<h2>3. 鉴权机制</h2>
```

This keeps the document professional and easy to scan. The numbered format naturally creates hierarchy and is universally readable.

## Visual components

### 1. Mermaid diagrams

Every report should include at least one Mermaid diagram — typically a **flowchart** showing the logical flow. Include a **sequence diagram** when the content involves multi-actor interactions. Skip the sequence diagram when it wouldn't add value.

Diagram container features:
- A **rainbow gradient top border** (3px, blue → purple → pink) via `::before` pseudo-element
- Clean white card with subtle shadow
- Centered title (`.diagram-title`)
- Use `%%{init: {...}}%%` to customize Mermaid theme
- Use `classDef` to color-code different node categories
- Keep diagrams to ~15 nodes max; use subgraphs for complex flows

Read `references/mermaid-guide.md` for detailed Mermaid patterns and common pitfalls.

### 2. Code blocks (macOS-style dark window)

Display code inside a styled dark window:

```html
<div class="code-window">
    <div class="code-header">
        <div class="code-dots">
            <span class="code-dot red"></span>
            <span class="code-dot yellow"></span>
            <span class="code-dot green"></span>
        </div>
        <span class="code-title">filename.py</span>
        <span class="code-lang">python</span>
    </div>
    <div class="code-content">
        <pre><code>your code here</code></pre>
    </div>
</div>
```

Key details:
- Background: `#0f172a` (deeper than Tokyo Night for better contrast)
- Header: gradient `#1e293b` → `#1a2332` with red/yellow/green dots
- Center area for **filename**, right side for **language badge** in a pill
- Use `<span>` classes for manual syntax highlighting:
  - `.tk-kw` (purple `#c084fc`) — keywords
  - `.tk-fn` (blue `#60a5fa`) — functions
  - `.tk-str` (green `#34d399`) — strings
  - `.tk-cm` (gray italic `#64748b`) — comments
  - `.tk-num` (orange `#fb923c`) — numbers
  - `.tk-dec` (pink `#f472b6`) — decorators
  - `.tk-type` (cyan `#38bdf8`) — types
  - `.tk-const` (yellow `#fbbf24`) — constants
  - `.tk-op` (muted `#94a3b8`) — operators
- Font: JetBrains Mono (loaded via Google Fonts)

### 3. Callout boxes

Four types, each with a colored icon badge on the left:

```html
<div class="callout info">
    <div class="callout-icon">i</div>
    <div>Content here</div>
</div>
```

| Type | Class | Icon bg | Border | Use for |
|------|-------|---------|--------|---------|
| Info | `.callout.info` | `#3b82f6` | `#bfdbfe` | Context, tips, explanations |
| Warning | `.callout.warning` | `#f59e0b` | `#fde68a` | Caveats, gotchas |
| Success | `.callout.success` | `#22c55e` | `#bbf7d0` | Key takeaways, wins |
| Danger | `.callout.danger` | `#ef4444` | `#fecaca` | Critical issues, anti-patterns |

### 4. Metric cards

Use a grid of metric cards for key numbers:

```html
<div class="metrics">
    <div class="metric-card">
        <div class="metric-value">99.99%</div>
        <div class="metric-label">Availability</div>
    </div>
</div>
```

- Grid layout with `auto-fit, minmax(180px, 1fr)`
- Values use gradient text (blue → purple) with large bold font
- Labels in uppercase small muted text
- Hover: subtle lift + shadow

### 5. Tags / badges

Inline colored pills for categorization:

```html
<span class="tag tag-blue">Path</span>
<span class="tag tag-green">Header</span>
<span class="tag tag-purple">Weight</span>
```

### 6. Step lists

Numbered step-by-step lists with a vertical timeline:

```html
<ol class="step-list">
    <li><strong>Step title</strong> — description</li>
    <li><strong>Step title</strong> — description</li>
</ol>
```

Each step gets a gradient circle number and a connecting vertical line.

### 7. Tables

- Rounded corners (`border-radius: 12px`)
- Header: uppercase small text, 2px bottom border
- Rows: subtle hover background
- Clean padding

### 8. Typography

- **Fonts**: Inter (headings + body) + Noto Sans SC (Chinese) + JetBrains Mono (code) — loaded via Google Fonts. This gives sharper, more modern typography than system fonts.
- **h2**: 1.375rem, plain numbered text (e.g., "1. 架构总览"), bottom border separator
- **h3**: 1.125rem, bold, tight letter-spacing
- Body text: 15px, color `#475569`, line-height 1.8
- Inline code: `#6366f1` (indigo) on `#f1f5f9` with 1px border

## When to use Python scripts

If the task involves **data processing** — parsing logs, aggregating CSV data, computing statistics, transforming JSON — write a Python script to do the heavy lifting, then embed the results into the HTML report.

Don't use Python unnecessarily — if the content is purely conceptual or documentary, just write the HTML directly.

## Responsive design

Three breakpoints:
- **Desktop** (> 1200px): full sidebar + content layout
- **Tablet** (901–1200px): narrower sidebar (240px), reduced padding
- **Mobile** (< 900px): single column, sidebar becomes sticky top nav

## Key scripts

Two inline scripts are required:

1. **Mermaid init** — `mermaid.initialize(...)` with custom theme variables
2. **Scroll-spy + Back to top** — IntersectionObserver for TOC highlighting, scroll listener for the back-to-top button

## Style reference

Read `references/style-guide.md` for the complete CSS reference. The template at `assets/template.html` provides the full HTML skeleton — use it as a starting point.

## Checklist before delivering

Before handing the HTML file to the user, verify:

- [ ] Self-contained file (only CDN for Mermaid + Google Fonts)
- [ ] Dark header with badge, title, description, meta
- [ ] Sidebar TOC matches all sections; scroll-spy works
- [ ] At least one Mermaid diagram with valid syntax
- [ ] Code blocks use dark window style with syntax highlighting spans
- [ ] Important points use callout boxes (info/warning/success/danger)
- [ ] Back-to-top button is present and functional
- [ ] Responsive layout works at desktop + mobile widths
- [ ] Chinese and English text render well (Inter + Noto Sans SC)

## Example workflow

**User says:** "帮我分析一下这个项目的架构，生成一个可视化的 HTML 文档"

**What you do:**
1. Explore the codebase to understand the architecture
2. Plan the report structure (which sections, what diagrams)
3. Write the HTML file following this skill's design system
4. Save the file and open it for the user

**User says:** "把这份数据分析的结果做成一个好看的报告"

**What you do:**
1. Write a Python script to process/analyze the data
2. Run the script to get results
3. Build an HTML report with metric cards, tables, and key findings
4. Include a flowchart of the analysis pipeline
5. Save and deliver
