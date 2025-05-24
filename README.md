# AI News Summarizer Chrome Extension

This Chrome extension fetches and summarizes trending news articles using an AI backend powered by FastAPI and OpenAI.

## Features
- Summarizes top headlines in real-time
- Highlights relevance scores
- Clean, simple popup UI

## How to Install

1. **Download this repository as a ZIP**
2. **Unzip the folder**
3. Go to `chrome://extensions` in your Chrome browser
4. Enable **Developer Mode** (top right toggle)
5. Click **Load Unpacked**
6. Select the unzipped folder containing the extension files

## Backend Setup

This extension connects to a FastAPI backend that:
- Parses RSS feeds
- Scrapes full articles
- Summarizes content using OpenAI

Check out the backend repo or deploy it on [Render.com](https://render.com).

Make sure to update the `popup.js` file with your actual deployed backend URL:
```js
fetch('https://your-api-url.onrender.com/news')
```

## Screenshots
*(Add screenshots here after installing the extension)*

## License
MIT