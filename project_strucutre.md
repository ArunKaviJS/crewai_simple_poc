advanced_agent/
│
├── .env
├── .gitignore
├── requirements.txt
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── llm/
│   ├── __init__.py
│   └── azure_llm.py
│
├── orchestrator/
│   ├── __init__.py
│   ├── main_agent.py
│   └── prompts.py
│
├── agents/
│   ├── __init__.py
│   │
│   ├── document_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── tools.py
│   │
│   ├── data_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── tools.py
│   │
│   └── report_agent/
│       ├── __init__.py
│       ├── agent.py
│       ├── prompts.py
│       └── tools.py
│
├── data/
│   ├── sales.csv
│   └── documents/
│       └── company_info.txt
│
└── outputs/
    └── reports/