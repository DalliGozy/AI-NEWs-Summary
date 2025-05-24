document.addEventListener('DOMContentLoaded', () => {
  const list = document.getElementById('news-list');

  fetch('https://your-ai-news.onrender.com/news')
    .then(response => response.json())
    .then(data => {
      data.forEach(news => {
        const item = document.createElement('div');
        item.className = 'news-item';
        item.innerHTML = `
          <div class="news-title">${news.title}</div>
          <div class="news-summary">${news.summary}</div>
          <div class="relevance-score">Relevance Score: ${news.relevance.toFixed(2)}</div>
        `;
        list.appendChild(item);
      });
    })
    .catch(error => {
      list.innerHTML = `<p style="color: red;">Error loading news: ${error}</p>`;
    });
});