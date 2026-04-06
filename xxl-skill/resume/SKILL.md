---
name: resume
description: "Generate beautiful, professional single-file HTML resumes with A4 layout, left sidebar, and responsive design that keeps the sidebar visible on all devices. Use this skill whenever the user wants to create a resume, CV, update their resume, generate a resume from their experience, convert resume content to HTML, or asks about resume formatting. Trigger on any mention of: resume, CV, curriculum vitae, job application document, personal profile page, or when users provide career/education info and want it formatted professionally."
---

# Resume Generator

Generate professional, visually polished single-file HTML resumes. The output is a self-contained HTML file that looks great on desktop, mobile, and print — all at A4 paper dimensions with a persistent left sidebar.

## Design Philosophy

The resume uses a two-column layout: a narrower left sidebar for personal info, contact, education, and skills; and a wider main area for work experience and projects. The design prioritizes:

- **Readability**: Clean typography with good contrast and spacing
- **Consistency**: A4 dimensions (210mm x 297mm) maintained across all viewports
- **Multi-device**: The sidebar stays on the left even on mobile — it scales down proportionally rather than stacking vertically, because a stacked sidebar on mobile breaks the resume's visual identity and wastes an entire screen of vertical space on contact info
- **Print-ready**: Clean output when printed or saved as PDF
- **Light color palette**: Soft, professional colors that feel modern without being distracting

## How to Use This Skill

1. Read the HTML template at `assets/template.html` within this skill's directory
2. Customize the template based on the user's information
3. Replace all placeholder content with the user's actual data
4. Save as a single `.html` file

## Content Structure

The resume has these sections (all customizable):

### Sidebar (left column)
- **Avatar**: Placeholder with initials (first character of surname), or an actual photo if provided
- **Name**: Chinese name (large) + English name (small, uppercase)
- **Motto/Tagline**: A short personal statement (italic)
- **Contact Info**: Job objective, email, phone — each with a Font Awesome icon
- **Education**: School, degree, major, dates — displayed in a compact table with icons
- **Skills**: Skill name with icon + progress bar showing proficiency level

### Main Area (right column)
- **Work Experience**: Company name, job title (as a colored badge), date range
  - Work summary as bullet points
- **Projects**: Project title, date range, then a card containing:
  - Background: Why the project existed
  - Responsibilities: What the person did
  - Results: Measurable outcomes
- **Company Divider**: A decorative line separating different employers

## Color Palette

Use a light, warm color scheme. The default palette is:

```
Background:        #f0f2f7 (light blue-gray page background)
Paper:             #ffffff (white paper)
Sidebar BG:        linear-gradient(175deg, #f8f6fd 0%, #f1f4fa 38%, #f3faf6 100%)
Sidebar border:    #e4e8f0
Primary accent:    #6C7BD8 (soft indigo)
Secondary accent:  #9BA6EF (lighter indigo)
Strong accent:     #5264D0 (deeper indigo for emphasis)
Title text:        #1a1f2e
Body text:         #404656
Muted text:        #8a90a0
Hairline/borders:  #e8ecf4
Accent dim:        rgba(108,123,216,0.10) (for badge backgrounds)
```

The sidebar has a subtle left-edge gradient stripe (purple → blue → green, 50% opacity) for visual interest. Project cards cycle through three tint variations (lavender, mint, peach) to add visual rhythm without being distracting.

Feel free to adjust these colors slightly for the user's preference, but keep them in the light/pastel family.

## Responsive Strategy

This is the most important technical requirement. The sidebar must remain on the left side at all screen sizes. Here's how:

```css
.page {
  width: 210mm;
  min-height: 297mm;
  display: grid;
  grid-template-columns: 62mm 1fr;
}

/* Mobile: scale the entire page down instead of reflowing */
@media screen and (max-width: 820px) {
  body {
    background: #f0f2f7;
  }
  .page {
    width: 210mm;              /* Keep A4 width */
    grid-template-columns: 62mm 1fr;  /* Keep two columns */
    transform-origin: top center;
    transform: scale(var(--mobile-scale));
    margin: 0 auto;
  }
}
```

Use JavaScript to calculate the scale factor:

```javascript
function adjustScale() {
  var page = document.querySelector('.page');
  if (!page) return;
  var vw = window.innerWidth;
  if (vw < 820) {
    var scale = vw / (210 * 3.7795275591); // 210mm to px
    page.style.setProperty('--mobile-scale', Math.min(scale, 1));
    page.style.transform = 'scale(' + Math.min(scale, 1) + ')';
    page.style.transformOrigin = 'top center';
    // Adjust body height to match scaled content
    var h = page.scrollHeight * Math.min(scale, 1);
    document.body.style.minHeight = h + 'px';
  } else {
    page.style.transform = 'none';
    document.body.style.minHeight = '';
  }
}
window.addEventListener('resize', adjustScale);
window.addEventListener('DOMContentLoaded', adjustScale);
```

This approach scales the entire A4 page down proportionally on small screens, preserving the exact same layout — sidebar stays on the left, text stays readable, and the visual structure is identical to desktop.

## Typography

Use this font stack:
```css
font-family: "Plus Jakarta Sans", "Noto Sans SC", "PingFang SC",
  "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
```

Load from Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

Icons from Font Awesome 6:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
```

## Print Styles

For `@media print`:
- Remove page background, box shadows, border-radius
- Keep the two-column grid layout (same as screen)
- Set `@page { size: A4 portrait; margin: 0; }`
- Enable `print-color-adjust: exact` for backgrounds
- Prevent page breaks inside project cards and after headings

## Adapting for Different Users

When a user provides their resume content:

1. **Parse their information** into the sections above (sidebar info, work experience, projects)
2. **Choose appropriate Font Awesome icons** for their skills (e.g., `fa-brands fa-react` for React, `fa-solid fa-database` for databases)
3. **Set skill bar widths** based on the user's described proficiency or years of experience
4. **Adjust the avatar placeholder** to show the first character of their surname
5. **Scale content to fit A4**: If there's a lot of content, reduce font sizes slightly or split into multiple pages. Each page should be a separate `.page` div.

## Multi-page Support

If the resume content exceeds one A4 page:
- Create additional `.page` divs
- The sidebar only appears on the first page
- Subsequent pages use full-width layout with a thin left accent bar for visual continuity
- Add a subtle page number at the bottom

## Exporting to PNG

The template includes a built-in "导出图片" (Export Image) button in the top-right corner. It uses [html2canvas](https://html2canvas.hertzen.com/) loaded from CDN to capture the `.page` element at 2x resolution, producing a crisp PNG image.

How it works:
- Clicking the button temporarily removes any mobile scaling transform
- html2canvas renders the `.page` element at 2x scale for retina-quality output
- The PNG is automatically downloaded with the document title as filename
- The button shows a spinner during export and restores after completion
- The export button is hidden when printing (`@media print`)

This approach requires zero local tool installation — it works entirely in the browser. The exported PNG preserves all colors, gradients, fonts (loaded via CDN), and layout exactly as displayed.

When generating a resume, this export button is always included in the template. If the user asks to "export", "save as image", "download as PNG", or "screenshot" their resume, point them to the button in the top-right corner of the page.

For PDF export: users can use the browser's built-in Print → Save as PDF function. The template's `@media print` styles ensure clean A4 output with correct colors.

## Template Location

Read the full HTML template from `assets/template.html` in this skill's directory. The template contains the complete HTML with all CSS inline, ready to be customized with user data.
