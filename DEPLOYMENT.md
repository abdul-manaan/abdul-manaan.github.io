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
6. After the domain works, update the link in `tools/build_resume.py` from the GitHub URL to the custom domain and regenerate the resume if desired.

The custom domain is intentionally not activated by a local CNAME before DNS setup: doing that would redirect the existing working GitHub URL too early.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Resume maintenance

`tools/resume_data.json` contains the experience used by `tools/build_resume.py`. The PDF is generated with ReportLab, with the download copied to `assets/Abdul-Manan-Resume.pdf`; the delivery copy is in `output/pdf`. Keep `resume.md` in sync after edits. The publication and project sections are in the builder.

Corrections confirmed by the owner: Siemens June-August 2022 (three-month internship), Brown research ended May 2023, LUMS research ended May 2020. Cloudflare is shown as November 2025-present based on the current role; Brown's Sc.M. degree title is supported by the existing website. The incomplete patent reference and inconsistent Code Jam round label in the source were omitted rather than expanded into unsupported claims.
