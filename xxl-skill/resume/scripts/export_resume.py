#!/usr/bin/env python3
"""
Export an HTML resume to PDF and/or PNG.

Usage:
    python export_resume.py resume.html                  # Export both PDF and PNG
    python export_resume.py resume.html --pdf            # PDF only
    python export_resume.py resume.html --png            # PNG only
    python export_resume.py resume.html -o ~/Desktop     # Custom output directory

Requirements:
    pip install playwright && playwright install chromium
"""

import argparse
import asyncio
import os
import sys
import subprocess
import shutil
from pathlib import Path


def ensure_playwright():
    """Check if playwright is available; if not, install it."""
    try:
        import playwright
        return True
    except ImportError:
        print("[info] playwright not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        return True


async def export(html_path: str, output_dir: str, do_pdf: bool, do_png: bool):
    from playwright.async_api import async_playwright

    html_path = os.path.abspath(html_path)
    if not os.path.isfile(html_path):
        print(f"[error] File not found: {html_path}")
        sys.exit(1)

    stem = Path(html_path).stem
    os.makedirs(output_dir, exist_ok=True)

    file_url = "file://" + html_path

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Set viewport to A4 width in pixels (210mm ≈ 794px)
        await page.set_viewport_size({"width": 794, "height": 1123})
        await page.goto(file_url, wait_until="networkidle")

        # Wait for fonts to load
        await page.wait_for_timeout(1500)

        if do_pdf:
            pdf_path = os.path.join(output_dir, f"{stem}.pdf")
            await page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            print(f"[done] PDF → {pdf_path}")

        if do_png:
            png_path = os.path.join(output_dir, f"{stem}.png")

            # Get the .page element's bounding box for a precise screenshot
            page_el = await page.query_selector(".page")
            if page_el:
                await page_el.screenshot(
                    path=png_path,
                    type="png",
                    scale="device",
                )
            else:
                # Fallback: full page screenshot
                await page.screenshot(
                    path=png_path,
                    full_page=True,
                    type="png",
                )
            print(f"[done] PNG → {png_path}")

        await browser.close()


def main():
    parser = argparse.ArgumentParser(description="Export HTML resume to PDF / PNG")
    parser.add_argument("html", help="Path to the HTML resume file")
    parser.add_argument("-o", "--output", default=".", help="Output directory (default: current dir)")
    parser.add_argument("--pdf", action="store_true", help="Export PDF only")
    parser.add_argument("--png", action="store_true", help="Export PNG only")
    args = parser.parse_args()

    # If neither flag is set, export both
    do_pdf = args.pdf or (not args.pdf and not args.png)
    do_png = args.png or (not args.pdf and not args.png)

    ensure_playwright()
    asyncio.run(export(args.html, args.output, do_pdf, do_png))


if __name__ == "__main__":
    main()
