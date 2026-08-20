/* JAYVI — Estúdio vintage: reveal on scroll + contadores animados */

(function () {
  'use strict';

  // Reveal on scroll
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }
      });
    },
    { threshold: 0.15 }
  );
  reveals.forEach((el) => observer.observe(el));

  // Contadores animados (com separador de milhar em pt-BR)
  const nums = document.querySelectorAll('.stat-num[data-target]');
  const counterObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = Number(el.dataset.target);
        const dur = 1600;
        const start = performance.now();

        function fmt(n) {
          return n.toLocaleString('pt-BR');
        }

        function step(now) {
          const p = Math.min((now - start) / dur, 1);
          const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
          el.textContent = fmt(Math.round(target * eased));
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        counterObs.unobserve(el);
      });
    },
    { threshold: 0.5 }
  );
  nums.forEach((n) => counterObs.observe(n));
})();
