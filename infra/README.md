# Website and Cloudflare setup

The site remains on GitHub Pages. Cloudflare provides DNS and a Worker-backed public page-view counter.

## Deploy the counter

From `infra/counter`:

```sh
npm ci
npx wrangler login
npm run deploy
```

Wrangler creates the SQLite-backed Durable Object and prints the Worker URL. No API keys belong in the website. Set `docs/_config.yml`:

```yaml
counter_endpoint: "https://abdul-manan-page-views.YOUR-SUBDOMAIN.workers.dev/views"
```

Use the actual URL from deployment, append `/views`, commit the config, and push to `master`. Until configured, the counter is omitted. Once configured, it shows a loading state and a temporary-unavailability message on failure. `GET /views` reads the total; each successful browser `POST /views` increments it. Both domains share one durable counter. It starts at zero; the old CountAPI total has not been migrated.

This counts page loads, including reloads, not unique people. It stores only the aggregate count. Origin checks restrict browser callers but are not authentication: scripts can spoof the Origin header. For abuse control, add a Cloudflare rate-limit rule on a Worker custom domain. Request failures and blocked JavaScript can undercount. There is no automatic POST retry, to avoid double-counting.

Reference: https://developers.cloudflare.com/durable-objects/examples/build-a-counter/

## Point fnuabdulmanan.org at GitHub Pages

1. In GitHub **profile Settings → Pages → Add a domain**, enter `fnuabdulmanan.org`. Copy GitHub's verification TXT name/value into Cloudflare DNS, then verify in GitHub. Keep that TXT record.
2. In the repository **Settings → Pages**, set the custom domain to `fnuabdulmanan.org`. For this branch-based site GitHub creates `docs/CNAME`; pull that change before pushing further edits.
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
6. After the domain works, update the website link in `resume/Abdul-Manan-Resume.tex` to the custom domain and recompile the resume.

The custom domain is intentionally not activated by a local CNAME before DNS setup: doing that would redirect the existing working GitHub URL too early.

Reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site


## GitHub Pages publishing

The publishing source is `master` → `/docs`. Jekyll reads `docs/_config.yml`. Public URLs remain rooted at `/`, not `/docs/`.
