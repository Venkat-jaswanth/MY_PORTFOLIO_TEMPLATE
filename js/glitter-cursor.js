// Glitter cursor effect
document.addEventListener('mousemove', function(e) {
  const dot = document.createElement('div');
  dot.className = 'glitter-cursor-dot';
  dot.style.left = (e.clientX - 5) + 'px';
  dot.style.top = (e.clientY - 5) + 'px';
  document.body.appendChild(dot);
  setTimeout(() => {
    dot.remove();
  }, 500);
});

if (!document.querySelector('.glitter-cursor-ring')) {
  const ring = document.createElement('div');
  ring.className = 'glitter-cursor-ring';
  document.body.appendChild(ring);

  document.addEventListener('mousemove', function(e) {
    ring.style.left = (e.clientX - 18) + 'px';
    ring.style.top = (e.clientY - 18) + 'px';
  });
}