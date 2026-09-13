# Resume

Edit `Abdul-Manan-Resume.tex`, then compile with Tectonic (or upload to Overleaf and use XeLaTeX).

From the repository root:

```sh
mkdir -p output/pdf
tectonic --outdir output/pdf resume/Abdul-Manan-Resume.tex
cp output/pdf/Abdul-Manan-Resume.pdf docs/assets/Abdul-Manan-Resume.pdf
```

Review the PDF layout and clickable links before committing. The published PDF lives in `docs/assets`; `output/` is an ignored local delivery folder. Keep `docs/resume.md` in sync with factual edits. The resume is adapted from Jake's Resume; see `TEMPLATE-LICENSE`.
