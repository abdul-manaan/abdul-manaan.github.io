import { DurableObject } from 'cloudflare:workers';

export class PageViews extends DurableObject {
  async read() {
    return (await this.ctx.storage.get('count')) ?? 0;
  }
  async increment() {
    return this.ctx.storage.transaction(async txn => {
      const count = ((await txn.get('count')) ?? 0) + 1;
      await txn.put('count', count);
      return count;
    });
  }
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin');
    const allowed = env.ALLOWED_ORIGINS.split(',').map(value => value.trim());
    const headers = { 'Cache-Control': 'no-store', 'Vary': 'Origin' };
    if (origin && !allowed.includes(origin)) return new Response('Forbidden', { status: 403, headers });
    if (origin) headers['Access-Control-Allow-Origin'] = origin;
    if (new URL(request.url).pathname !== '/views') return new Response('Not found', { status: 404, headers });
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: { ...headers, 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Max-Age': '86400' } });
    }
    if (!['GET', 'POST'].includes(request.method)) return new Response('Method not allowed', { status: 405, headers: { ...headers, Allow: 'GET, POST, OPTIONS' } });
    if (request.method === 'POST' && !origin) return new Response('Origin required', { status: 403, headers });
    const counter = env.PAGE_VIEWS.getByName('abdul-manan-site');
    try {
      const count = request.method === 'POST' ? await counter.increment() : await counter.read();
      return Response.json({ count }, { headers });
    } catch {
      return new Response('Counter unavailable', { status: 503, headers });
    }
  }
};
