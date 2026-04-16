# ImgSearchEngine
ImgSearchEngine is a lightweight local image search engine that lets you find photos and screenshots using natural language queries instead of filenames or tags.
It runs completely offline on your machine — no APIs, no cloud services, and no internet required.

---

## 🔍 How it works
- Images are encoded into 500-dimensional vectors using CLIP's image encoder
- When you search, your text query is encoded using CLIP's text encoder into the same 512-dimensional space
- The system compares your query vector against all image vectors using cosine similarity
- Results are ranked by similarity and returned to the user

---

## 📁 Supported file types
- `.jpg` / `.jpeg` / `.jfif`
- `.png`
- `.webp`
- `.bmp`

---

## ⚙️ Features
- Fully local search engine
- Semantic search using natural language (not filename or tag based)
- Powered by OpenAI CLIP — image and text live in the same vector space
- Returns top-K most relevant results
- Simple GUI built with Tkinter
- No external APIs required

---

## 🖥️ Interface
A simple Tkinter GUI allows you to:
- Search your image library using plain English queries
- View matching image paths
- Preview the top results directly in the interface

---

## 📌 Notes
This project indexes all images in a folder into a local JSON vector store, enabling fast semantic similarity search across your local image library.

> **Note:** JSON storage works well for small to medium collections. For large image libraries, serializing high-dimensional float vectors as plain text is not storage-efficient — migration to a binary format or a dedicated vector store such as ChromaDB is recommended at scale.
