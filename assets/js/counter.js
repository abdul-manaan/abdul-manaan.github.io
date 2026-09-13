(() => {
  const endpoint = document.currentScript.dataset.counterEndpoint;
  if (!endpoint) return;
  fetch(endpoint, { method: 'POST', credentials: 'omit', cache: 'no-store', signal: AbortSignal.timeout(5000) })
    .then(response => { if (!response.ok) throw new Error('Counter unavailable'); return response.json(); })
    .then(({ count }) => {
      if (!Number.isSafeInteger(count) || count < 0) return;
      document.getElementById('visits').textContent = count.toLocaleString();
      document.getElementById('page-views').hidden = false;
    }).catch(() => {});
})();
