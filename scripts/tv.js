fetch('../data/tvshows.json')
  .then(res => res.json())
  .then(shows => {
    const list = document.getElementById('tv-list');
    list.innerHTML = shows.map(show => `
      <div class="tv-card">
        <h3>${show.title}</h3>
        <p>📺 ${show.platform}</p>
      </div>
    `).join('');
  });