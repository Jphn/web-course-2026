# Exercício 15 - Polimento e Deploy

## Objetivo

Implementar UMA melhoria à escolha.

## Opções (escolher uma)

### A) Paginação

- `models.py`: `list_items(page=1, per_page=10, search=None)` com `LIMIT ? OFFSET ?`
- `routes/items.py`: `page = request.args.get('page', 1, type=int)`
- Template: links Anterior/Próximo com `url_for('items.list', page=..., q=search)`

### B) Colunas Ordenáveis

- Headers: `<a href="{{ url_for('items.list', sort='name', dir='asc') }}">Nome</a>`
- Model: `ORDER BY {{coluna}} {{direcao}}` (validar colunas permitidas)
- Ícone de seta indicando direção atual

### C) Filtro por Categoria

- Dropdown no topo da listagem: `<select name="categoria">...`
- Model: `WHERE categoria = ?` quando filtro ativo
- Badge mostrando filtro ativo + botão "Limpar"

### D) Contador na Navbar

- Usar `count_items()` existente do Exercício 12
- `base.html`: `<a href="{{ url_for('items.list') }}">Itens <span class="badge">{{ total }}</span></a>`
- Context processor para disponibilizar `total` globalmente

## Entrega

- Commit no GitHub com feature branch
- README atualizado com descrição da feature

## Critério de Sucesso

- Feature funciona corretamente
- Código segue padrões do projeto
- Nenhuma funcionalidade existente quebrada
