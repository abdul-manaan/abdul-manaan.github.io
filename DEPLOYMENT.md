# Website and Cloudflare setup

The site remains on GitHub Pages. Cloudflare provides DNS and a Worker-backed public page-view counter.

## Deploy the counter

From `cloudflare/counter`:

```sh
npm ci
npx wrangler login
npm run deploy
```

Wrangler creates the SQLite-backed Durable Object and prints the Worker URL. No API keys belong in the website. Set `_config.yml`:

```yaml
counter_endpoint: "https://abdul-manan-page-views.YOUR-SUBDOMAIN.workers.dev/views"
```

Use the actual URL from deployment, append `/views`, commit the config, and push to `master`. Until configured, the counter stays hidden. If the service fails, it stays hidden rather than displaying a fabricated number. `GET /views` reads the total; each successful browser `POST /views` increments it. Both domains share one durable counter. It starts at zero; the old CountAPI total has not been migrated.

This counts page loads, including reloads, not unique people. It stores only the aggregate count. Origin checks restrict browser callers but are not authentication: scripts can spoof the Origin header. For abuse control, add a Cloudflare rate-limit rule on a Worker custom domain. Request failures and blocked JavaScript can undercount. There is no automatic POST retry, to avoid double-counting.

Reference: https://developers.cloudflare.com/durable-objects/examples/build-a-counter/

## Point fnuabdulmanan.org at GitHub Pages

1. In GitHub **profile Settings → Pages → Add a domain**, enter `fnuabdulmanan.org`. Copy GitHub's verification TXT name/value into Cloudflare DNS, then verify in GitHub. Keep that TXT record.
2. In the repository **Settings → Pages**, set the custom domain to `fnuabdulmanan.org`. For this branch-based site GitHub creates `CNAME`; pull that change before pushing further edits.
3. In Cloudflare DNS for this zone, replace only conflicting apex website A/AAAA/CNAME records with these records. Preserve MX, email TXT, verification TXT, and unrelated subdomains.

| Type | Name | Target | Proxy status |
| --- | --- | --- | --- |
| A | @ | 185.199.108.153 | DNS only |
| A | @ | 185.199.109.153 | DNS only |
| A | @ | 185.199.110.153 | DNS only |
| A | @ | 185.199.111.153 | DNS only |
| CNAME | www | abdul-manaan.github.io | DNS only |

4. Wait for GitHub's DNS check and certificate provisioning. Enable **Enforce HTTPS** in repository Pages settings when available. GitHub redirects `www` to the apex domain.
5. Verify `https://fnuabdulmanan.org`, `https://www.fnuabdulmanan.org`, the resume download, and the counter. Keep DNS-only during initial certificate provisioning; it is sufficient for this setup.
6. After the domain works, update the website link in `resume-source/Abdul-Manan-Resume.tex` to the custom domain and recompile the resume.

The custom domain is intentionally not activated by a local CNAME before DNS setup: doing that would redirect the existing working GitHub URL too early.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Resume maintenance

The editable resume is `resume-source/Abdul-Manan-Resume.tex`, adapted from Jake's Resume (https://github.com/jakegut/resume). The template license is alongside the source. Compile with Tectonic or upload the source to Overleaf and select XeLaTeX:

```sh
tectonic --outdir output/pdf resume-source/Abdul-Manan-Resume.tex
cp output/pdf/Abdul-Manan-Resume.pdf assets/Abdul-Manan-Resume.pdf
```

Keep `resume.md` in sync after edits. Confirmed corrections: Siemens June-August 2022, Brown research ended May 2023, LUMS research ended May 2020. Cloudflare is shown as November 2025-present based on the current role; Brown's Sc.M. degree title comes from the existing website. The incomplete patent reference and inconsistent Code Jam round label were omitted. tinyOS-rs details come from the local project README.
