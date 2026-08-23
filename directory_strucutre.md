topic
  │
  ▼
Research Analyst
  │
  ├── SerperDevTool → web research
  ├── plan research
  ├── extract evidence
  └── produce 5 structured insights
  │
  ▼
Content Writer
  │
  ├── receives research context
  ├── validates claims against research
  └── produces ArticleDraft
  │
  ▼
Social Editor
  │
  ├── receives ArticleDraft
  ├── LinkedIn adaptation
  └── X adaptation
  │
  ▼
PUBLISH GATE
  │
  ├── human approves → optional webhook
  └── human rejects → stop

# ========================================
  agentic-content-pipeline/
│
├── .env
├── .env.example
├── requirements.txt
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── brain/
│   ├── __init__.py
│   └── llm.py
│
├── schemas/
│   ├── __init__.py
│   ├── research.py
│   ├── article.py
│   └── social.py
│
├── tools/
│   ├── __init__.py
│   ├── research_tools.py
│   └── publishing.py
│
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   ├── content_agent.py
│   └── social_agent.py
│
├── prompts/
│   ├── research.md
│   ├── content_writer.md
│   └── social_editor.md
│
├── tasks/
│   ├── __init__.py
│   ├── research_task.py
│   ├── article_task.py
│   └── social_task.py
│
├── orchestration/
│   ├── __init__.py
│   └── crew.py
│
├── gates/
│   ├── __init__.py
│   └── publish_gate.py
│
└── output/