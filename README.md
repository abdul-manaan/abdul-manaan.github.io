# Abdul Manan · Personal website

Portfolio, research publications, and resume for Abdul Manan, Systems Engineer at Cloudflare.

**[Visit the website](https://abdul-manaan.github.io/)** · **[Resume](https://abdul-manaan.github.io/assets/Abdul-Manan-Resume.pdf)** · **[LinkedIn](https://www.linkedin.com/in/fnu-abdul-manan)**

## Project structure

```text
docs/       Jekyll website, pages, theme, images, and published PDF
infra/      Cloudflare page-view counter and deployment guide
resume/     Editable LaTeX resume and build instructions
.github/    Dependency update configuration
```

The website source is grouped under `docs/` because GitHub Pages supports publishing directly from that folder. The folders beginning with `_` inside it are Jekyll conventions.

## Common changes

| Change | File |
| --- | --- |
| Homepage and projects | `docs/index.md` |
| Experience and education | `docs/resume.md` |
| Site title, biography, counter URL | `docs/_config.yml` |
| Publications and blog posts | `docs/_posts/` |
| Footer and navigation | `docs/_includes/` |
| Theme styling | `docs/_sass/` |
| PDF resume | `resume/Abdul-Manan-Resume.tex` |
| Counter backend | `infra/counter/src/index.js` |

## Local website preview

With Ruby and Bundler installed:

```sh
cd docs
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000`. The production counter accepts only the configured public origins, so local previews display its unavailable state. To test counting locally, use Wrangler:

```sh
cd infra/counter  # from the repository root
npm ci
npm run dev
```

In another terminal, run `node infra/counter/test-counter.mjs`. These tests target local port 8787 and do not change the production count.

## Publishing

Push website changes to `master`. GitHub Pages builds from **`/docs`**. Existing public URLs stay unchanged.

- [Counter deployment and custom-domain setup](infra/README.md)
- [LaTeX resume build instructions](resume/README.md)

The counter records aggregate page loads, including refreshes, rather than unique visitors. Its backend is a Cloudflare Worker with a SQLite-backed Durable Object. Never commit account tokens or credentials.

## Maintenance

Dependency updates are proposed by Dependabot. Review and test them before merging. Existing dependency advisories are not resolved by reorganizing this repository.

Generated website builds, local PDF delivery copies, dependency folders, and LaTeX intermediates are ignored. The downloadable resume PDF is intentionally tracked for GitHub Pages.

## Credits and license

The website uses Jekyll Academic, based on Minimal Mistakes. The original MIT notice is preserved in [LICENSE](LICENSE). The LaTeX template's license is in [resume/TEMPLATE-LICENSE](resume/TEMPLATE-LICENSE).
