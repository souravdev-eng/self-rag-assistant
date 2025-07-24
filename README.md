# Self-RAG PDF Assistant (LangGraph + Pinecone)

An AI-powered assistant that lets you upload a PDF, ask questions about its content, and get smart, LLM-generated answers — all built using LangGraph, Pinecone, and OpenAI.

This project uses a structured LangGraph workflow to enable retrieval-augmented generation (RAG) with confidence evaluation, dynamic query handling, and a scalable vector database setup.

---

## Features

- Upload and parse PDFs using LangChain
- Chunk, embed, and store content in Pinecone vector DB
- Ask natural language questions about the document
- RAG pipeline: vector search → context → LLM answer
- LangGraph logic to evaluate confidence and retry if needed
- Looping flow: Rephrase low-confidence queries and reattempt
- Optional: Document summarization and follow-up questions

---

## Tech Stack

- **LangGraph** — Workflow orchestration and branching
- **LangChain** — Document loaders and embedding utilities
- **Pinecone** — Vector database for semantic search
- **OpenAI** — LLM for answers and reasoning
- **Python** — Main backend logic

---

## How It Works

1. **Upload PDF** → Load & chunk text
2. **Embed + Store** → Save in Pinecone
3. **Ask Question** → LangGraph runs RAG flow
4. **Evaluate** → If low confidence → rephrase & retry
5. **Respond** → Final answer is streamed back to user

---

## Future Ideas

- Handle multiple documents in memory
- Integrate document summarization with question generator
- Add conversation memory and follow-up context
- Deploy as a SaaS tool (e.g., legal contracts Q&A, policy docs)

---

## Author

Built by **Sourav Majumdar** — a self-taught Tech Lead passionate about AI workflows, system design, and building impactful software.
