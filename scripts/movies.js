fetch('../data/movies.json')
  .then(res => res.json())
  .then(movies => {
    const container = document.getElementById('movie-list');
    container.innerHTML = movies.map(movie => `
      <div class="movie-card">
        <img src="${movie.poster}" alt="${movie.title}" />
        <h3>${movie.title}</h3>
        <p>🎬 ${movie.genre}<br>📅 ${movie.release}</p>
      </div>
    `).join('');
  });