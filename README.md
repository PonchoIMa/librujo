# lubrijo API
**A Headless Metadata Engine for EPUB/PDF Library Management.**
_now in full-Esperanto_

## Vision
**librujo** (esperanto for 'library') is a lightweight, local-first REST API designed to organize large-scale document collections (.epub, .pdf). It prioritizes data integrity and system observability, moving away from bloated library managers toward a "Bare-Metal" data layer.

## Tech Stack
- **Language:** Python 3.12+
- **Framework:** FastAPI
- **Database:** SQLite (SQLAlchemy ORM)
- **Parsing:** EbookLib (EPUB), PyMuPDF (PDF)
- **Interface:** Future TUI (Textual/Rich)

## Current Layout
### ER-Diagram
```mermaid
erDiagram
    BOOK ||--o{ BOOK_TAG : "categorized by"
    TAG ||--o{ BOOK_TAG : "applied to"
    AUTHOR ||--o{ BOOK : "applied to"

    BOOK {
        int    id PK
        text   title
        text   subtitle
        int    author_id FK
        text   synopsis
        text   file_path
        text   file_type
        text   isbn
        datetime date_added
        int    status
    }
    
    AUTHOR {
        int    id PK
        text   last_name
        text   first_name
        text   biography
    }

    TAG {
        int    id PK
        text   name
    }

    BOOK_TAG {
        int id PK
        int book_id FK
        int tag_id FK
    }
```

### Git Progress ([see full diagram](#))
```mermaid
gitGraph
    commit id: "Initial Commit"
    commit id: "Initial Setup"
    branch develop
    checkout develop
    branch feature/parser-logic
    checkout feature/parser-logic
    commit id: "Add EPUB parser"
    commit id: "Add PDF parser"
    checkout develop
    merge feature/parser-logic
    checkout develop
    checkout main
    merge develop tag: "v0.1.0-alpha"
```
## Project Milestones
For a more precise status report on the library, visit [the Backlog](https://github.com/users/PonchoIMa/projects/1)
- [ ] Phase 1: File System Ingestion & Metadata Extraction
- [ ] Phase 2: SQLite Schema Implementation
- [ ] Phase 3: REST API Endpoint Development
- [ ] Phase 4: TUI Client for Terminal Management
