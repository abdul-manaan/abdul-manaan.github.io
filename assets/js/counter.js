(() => {
  const script = document.currentScript;
  const target = document.getElementById('visits');
  if (!target) return;
  const endpoint = script && script.dataset.counterEndpoint;
  if (!endpoint) { target.textContent = 'Unavailable'; return; }

  // Keep the footer visible, even when the service is slow or blocked.
  const controller = typeof AbortController === 'function' ? new AbortController() : null;
  const timeout = setTimeout(() => {
    target.textContent = 'Temporarily unavailable';
    if (controller) controller.abort();
  }, 10000);
  const options = { method: 'POST', credentials: 'omit', cache: 'no-store' };
  if (controller) options.signal = controller.signal;
  Promise.resolve().then(() => fetch(endpoint, options))
    .then(response => {
      if (!response.ok) throw new Error('Counter unavailable');
      return response.json();
    })
    .then(({ count }) => {
      if (!Number.isSafeInteger(count) || count < 0) throw new Error('Invalid count');
      target.textContent = count.toLocaleString();
    })
    .catch(() => { target.textContent = 'Temporarily unavailable'; })
    .finally(() => clearTimeout(timeout));
})();
