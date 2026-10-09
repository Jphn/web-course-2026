# Exercício 10 - Tratamento de Formulários

## Objetivo

Adicionar campo description ao formulário de item.

## Instruções

1. No `templates/items/form.html`, adicionar após categoria:

```html
{{ render_field('description', 'Descrição', 'textarea', description or '',
false, rows=4) }}
```

2. No `app/routes/items.py`, atualizar validação:

```python
description = request.form.get('description', '').strip()
if description and len(description) > 500:
    errors.append('Descrição muito longa (máx 500 chars)')
```

3. Incluir nas chamadas create_item/update_item:

```python
create_item(name, category, description)
update_item(id, name, category, description)
```

4. Exibir na tabela da listagem:

```html
<td>{{ item.description or '-' }}</td>
```

## Teste

Criar item com descrição, verificar se aparece na tabela.

## Critério de Sucesso

- Campo description no formulário
- Validação: opcional, máx 500 chars
- Armazenado no banco
- Exibido na listagem
