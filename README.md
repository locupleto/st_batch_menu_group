# Streamlit Batch Menu Group Component

This custom Streamlit component provides a solution for handling multiple related dropdown menus as a single unit, significantly reducing the number of page reruns in Streamlit applications. It's particularly useful for implementing cascading menus where the options in one menu depend on the selection in another.

## Problem Solved

Standard Streamlit dropdown menus trigger a page rerun whenever their value changes. In applications with multiple interdependent menus (like Exchange → Type → Symbol), this leads to multiple consecutive reruns, causing inefficient rendering and a poor user experience.

This component solves the problem by:
1. Handling all menus as a single component
2. Processing all state changes in a batch
3. Updating dependent menus in a single rerun

## Features

- **Batch State Management**: All menu changes are processed together, reducing Streamlit reruns  
- **Dependency Handling**: Python-side logic handles menu dependencies  
- **Native HTML Elements**: Uses native select elements for maximum compatibility  
- **Compact Design**: Minimal vertical space usage  
- **Responsive Layout**: Adapts to different screen sizes  

## Installation

To install this component, run:

```bash
pip install st_batch_menu_group
```

## Usage

First, import the component:

```python
from st_batch_menu_group import st_batch_menu_group
```

Then, create a menu state dictionary and use the component:

```python
# Define your menu state
menu_state = {
    "exchange_select": {
        "label": "Exchanges",
        "options": ["Binance", "Coinbase", "Kraken"],
        "value": "Binance"
    },
    "type_select": {
        "label": "Types",
        "options": ["Spot", "Futures", "Options"],
        "value": "Spot"
    },
    "symbol_select": {
        "label": "Symbols",
        "options": ["BTC/USDT", "ETH/USDT", "SOL/USDT"],
        "value": "BTC/USDT"
    }
}

# Use the component
updated_state = st_batch_menu_group(
    menu_state,
    key="my_menu_group"
)

# Handle state changes
if updated_state != menu_state:
    st.session_state.menu_state = updated_state
    st.rerun()
```

## Handling Dependencies

To handle dependencies between menus, implement logic in your Python code:

```python
if updated_state != st.session_state.menu_state:
    changed_menu = None
    for menu_id in st.session_state.menu_state:
        if st.session_state.menu_state[menu_id]["value"] != updated_state[menu_id]["value"]:
            changed_menu = menu_id
            break

    valid_state = dict(updated_state)

    if changed_menu == "exchange_select":
        exchange = valid_state["exchange_select"]["value"]
        new_types = get_types_for_exchange(exchange)
        valid_state["type_select"]["options"] = new_types
        valid_state["type_select"]["value"] = new_types[0]

        new_symbols = get_symbols_for_type(exchange, new_types[0])
        valid_state["symbol_select"]["options"] = new_symbols
        valid_state["symbol_select"]["value"] = new_symbols[0]

    elif changed_menu == "type_select":
        exchange = valid_state["exchange_select"]["value"]
        type_val = valid_state["type_select"]["value"]
        new_symbols = get_symbols_for_type(exchange, type_val)
        valid_state["symbol_select"]["options"] = new_symbols
        valid_state["symbol_select"]["value"] = new_symbols[0]

    st.session_state.menu_state = valid_state
    st.rerun()
```

## Dynamic Key Approach

For more reliable re-rendering when state changes, you can use a dynamic key based on the current state:
```python
# Use a unique key for the component based on the state
component_key = f"menu_group_{hash(str(st.session_state.menu_state))}"

# Use the component with dynamic key
updated_state = st_batch_menu_group(
    st.session_state.menu_state,
    key=component_key
)
```
This approach ensures that when the menu state changes, Streamlit creates a new component instance with a different key, forcing a complete re-render with the updated options.

## API Reference

### `st_batch_menu_group(menu_state, key=None)`

**Parameters**:

- `menu_state (dict)`: A dictionary containing the complete state of all menus. Format:
```python
{
    "menu_id": {
        "label": "Menu Label",
        "options": ["Option 1", "Option 2", ...],
        "value": "Selected Option"
    },
    ...
}
```

- `key (str, optional)`: An optional key that uniquely identifies this component.

**Returns**:
- `dict`: The updated menu state after user interaction.

## Appearance Customization

The component's appearance can be customized using color parameters:

```python
updated_state = st_batch_menu_group(
    menu_state,
    key="my_menu_group",
    label_color="#ffffff",           # Color for menu labels
    menu_bg_color="#1e1e1e",         # Background color for menus
    menu_border_color="#444444",     # Border color for menus
    menu_hover_color="#1890ff",      # Border color on hover
    menu_focus_shadow_color="rgba(24, 144, 255, 0.3)",  # Shadow when focused
    menu_text_color="#ffffff"        # Text color for menu items
)
```

### Theme Examples

You can define themes and apply them to the component:

```python
# Define theme color schemes
themes = {
    "Light": {
        "label_color": "#333333",
        "menu_bg_color": "#ffffff",
        "menu_border_color": "#d9d9d9",
        "menu_hover_color": "#40a9ff",
        "menu_focus_shadow_color": "rgba(24, 144, 255, 0.2)",
        "menu_text_color": "#333333"
    },
    "Dark": {
        "label_color": "#ffffff",
        "menu_bg_color": "#1e1e1e",
        "menu_border_color": "#444444",
        "menu_hover_color": "#1890ff",
        "menu_focus_shadow_color": "rgba(24, 144, 255, 0.3)",
        "menu_text_color": "#ffffff"
    }
}

# Apply theme colors to the component
current_theme = "Dark"
theme_colors = themes[current_theme]

updated_state = st_batch_menu_group(
    menu_state,
    key="my_menu_group",
    **theme_colors
)
```

## Example

See the included `app.py` for a complete example of implementing cascading menus with Exchange → Type → Symbol dependencies as well as optional themed coloring of the menus.

## How It Works

- The JavaScript component renders all menus based on the provided state  
- When a user changes a menu, the entire state is sent back to Python  
- Python code identifies which menu changed and updates dependent menus  
- The updated state is sent back to the component in a single rerun  
- This process ensures only one page rerun per user interaction  

## License

MIT
