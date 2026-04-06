# Mermaid Diagram Best Practices

## General principles

- Always use `%%{init: {...}}%%` to set theme variables — don't rely on Mermaid defaults
- Use `classDef` to color-code different node categories for quick visual parsing
- Keep individual diagrams to 15 nodes or fewer; use subgraphs for complex flows
- Always test that Mermaid syntax is valid before embedding — common pitfalls below

## Flowchart patterns

### Basic structure
```
%%{init: {'theme': 'base', 'themeVariables': {
    'primaryColor': '#dbeafe',
    'primaryBorderColor': '#3b82f6',
    'primaryTextColor': '#1e293b',
    'lineColor': '#64748b',
    'fontSize': '14px'
}}}%%
flowchart TD
    A[Start] --> B{Decision?}
    B -->|Yes| C[Action A]
    B -->|No| D[Action B]
    C --> E[End]
    D --> E
```

### Using classDef for color categories
```
flowchart TD
    A[Input] --> B[Process]
    B --> C[Output]
    B --> D[(Database)]

    classDef input fill:#dbeafe,stroke:#3b82f6,color:#1e40af
    classDef process fill:#f0fdf4,stroke:#22c55e,color:#166534
    classDef output fill:#fef3c7,stroke:#f59e0b,color:#92400e
    classDef storage fill:#f3e8ff,stroke:#a855f7,color:#6b21a8

    class A input
    class B process
    class C output
    class D storage
```

### Subgraphs for grouping
```
flowchart TD
    subgraph Frontend
        A[React App] --> B[API Client]
    end
    subgraph Backend
        C[API Server] --> D[Service Layer]
        D --> E[(Database)]
    end
    B --> C
```

## Sequence diagram patterns

### When to include
- API call chains between services
- Request/response patterns
- Multi-actor workflows (user → frontend → backend → DB)
- Authentication/authorization flows

### Basic structure
```
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant A as API Server
    participant D as Database

    U->>F: Click submit
    F->>A: POST /api/data
    A->>D: INSERT INTO table
    D-->>A: OK
    A-->>F: 200 {id: 1}
    F-->>U: Show success
```

### Styling tips
- Use `participant ... as ...` for readable aliases
- Use `->>` for solid arrows (requests) and `-->>` for dashed arrows (responses)
- Use `Note over A,B: text` for annotations
- Use `rect rgb(...)` blocks to highlight sections
- Use `activate/deactivate` for lifecycle spans

## Common Mermaid syntax pitfalls

1. **Special characters in node text**: Wrap in quotes if text contains `()`, `[]`, `{}`, or special chars
   ```
   A["Function call()"] --> B["Array[0]"]
   ```

2. **Parentheses in labels**: Use `["text"]` instead of `(text)` for labels with parens
   ```
   A["getData(id)"]  ✅
   A(getData(id))    ❌ will break
   ```

3. **Semicolons**: Don't end lines with `;` — Mermaid doesn't use them

4. **Long labels**: Use `<br/>` for line breaks inside node text
   ```
   A["Line 1<br/>Line 2"]
   ```

5. **Arrow labels with special chars**: Wrap in quotes
   ```
   A -->|"response (200)"| B
   ```

## Recommended color palettes

### Blue-focused (default, professional)
```
primaryColor: '#dbeafe'
primaryBorderColor: '#3b82f6'
primaryTextColor: '#1e293b'
lineColor: '#64748b'
secondaryColor: '#f0fdf4'
tertiaryColor: '#fef3c7'
```

### Warm (for business/strategy docs)
```
primaryColor: '#fef3c7'
primaryBorderColor: '#f59e0b'
primaryTextColor: '#78350f'
lineColor: '#a16207'
secondaryColor: '#fce7f3'
tertiaryColor: '#ede9fe'
```

### Dark-accent (for technical architecture)
```
primaryColor: '#e0e7ff'
primaryBorderColor: '#6366f1'
primaryTextColor: '#312e81'
lineColor: '#4f46e5'
secondaryColor: '#dcfce7'
tertiaryColor: '#fef9c3'
```
