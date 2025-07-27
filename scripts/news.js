fetch('../data/news.json')
  .then(res => res.json())
  .then(news => {
    const feed = document.getElementById('news-feed');
    feed.innerHTML = news.map(n => `
      <li><strong>[${n.date}]</strong> ${n.headline}</li>
    `).join('');
  });