# RAG Confluence

Confluence 문서를 활용한 RAG (Retrieval-Augmented Generation) 시스템

## 프로젝트 구조

```
src/
├── api/
│   └── __init__.py
│
├── application/
│   ├── __init__.py
│   ├── data-processing/
│   │   └── __init__.py
│   └── retriever/
│       └── __init__.py
│
├── domain/
│   └── __init__.py
│
└── store/
    ├── __init__.py
    ├── confluence/
    │   └── __init__.py
    └── vector/
        └── __init__.py
```

## 모듈 설명

### API
외부에서 호출 가능한 API Controller 입니다. application 모듈의 비즈니스 로직을 호출하여 사용자 요청을 처리합니다.

### Application
실제 비즈니스 로직을 구현합니다.

#### Data Processing
Confluence 문서를 가져와 벡터로 임베딩한 후 벡터 DB에 저장합니다.

#### Retriever
사용자의 질문을 받아 벡터 DB에서 가장 적합한 데이터를 검색하고, 이를 기반으로 프롬프트를 작성하여 LLM API로 답변을 생성합니다.

### Domain
도메인 모델을 관리합니다.

### Store
외부 API나 DB에서 데이터를 가져옵니다

#### Confluence
Confluence API를 통해 문서 데이터를 가져옵니다.

#### Vector
벡터 DB에서 데이터를 저장하고 검색합니다.

