import streamlit as st
from st_batch_menu_group import st_batch_menu_group

st.set_page_config(layout="wide")

st.title("Batch Menu Group Demo")
st.markdown("### Demonstrating cascading menus with reduced page reruns")

# Define theme color schemes
themes = {
    "Light": {
        "label_color": "#aaaaaa",  # Gray text for labels in Light theme
        "menu_bg_color": "#ffffff",
        "menu_border_color": "#d9d9d9",
        "menu_hover_color": "#40a9ff",
        "menu_focus_shadow_color": "rgba(24, 144, 255, 0.2)",
        "menu_text_color": "#333333"  # Dark text for menu items in Light theme
    },
    "Dark": {
        "label_color": "#ffffff",  # White text for labels in Dark theme
        "menu_bg_color": "#1e1e1e",
        "menu_border_color": "#444444",
        "menu_hover_color": "#1890ff",
        "menu_focus_shadow_color": "rgba(24, 144, 255, 0.3)",
        "menu_text_color": "#ffffff"  # White text for menu items in Dark theme
    },
    "Custom": {
        "label_color": "#ffd700",  # Gold
        "menu_bg_color": "#2c3e50",  # Dark blue
        "menu_border_color": "#3498db",  # Blue
        "menu_hover_color": "#e74c3c",  # Red
        "menu_focus_shadow_color": "rgba(231, 76, 60, 0.3)",
        "menu_text_color": "#ffffff"  # White text for menu items in Custom theme
    }
}

# Mock data for demonstration
exchange_types = {
    "Binance": ["Spot", "Futures", "Options"],
    "Coinbase": ["Spot"],
    "Kraken": ["Spot", "Futures"]
}

# Exchange symbols with many options
exchange_symbols = {
    "Binance": {
        "Spot": [
            "BTC/USDT", "ETH/USDT", "SOL/USDT", "ADA/USDT", "DOT/USDT", 
            "AVAX/USDT", "MATIC/USDT", "LINK/USDT", "XRP/USDT", "LTC/USDT",
            "UNI/USDT", "DOGE/USDT", "SHIB/USDT", "ATOM/USDT", "ETC/USDT",
            "FIL/USDT", "AAVE/USDT", "ALGO/USDT", "XLM/USDT", "VET/USDT",
            "EOS/USDT", "TRX/USDT", "XMR/USDT", "CAKE/USDT", "AXS/USDT",
            "SAND/USDT", "MANA/USDT", "ENJ/USDT", "CHZ/USDT", "BAT/USDT",
            "COMP/USDT", "DASH/USDT", "NEO/USDT", "IOTA/USDT", "ZEC/USDT",
            "THETA/USDT", "FTM/USDT", "EGLD/USDT", "NEAR/USDT", "ONE/USDT",
            "HBAR/USDT", "KSM/USDT", "WAVES/USDT", "ICX/USDT", "ZIL/USDT",
            "RVN/USDT", "ONT/USDT", "DGB/USDT", "SC/USDT", "ZRX/USDT"
        ],
        "Futures": [
            "BTC/USDT-PERP", "ETH/USDT-PERP", "SOL/USDT-PERP", "ADA/USDT-PERP",
            "DOT/USDT-PERP", "AVAX/USDT-PERP", "MATIC/USDT-PERP", "LINK/USDT-PERP",
            "XRP/USDT-PERP", "LTC/USDT-PERP", "UNI/USDT-PERP", "DOGE/USDT-PERP",
            "SHIB/USDT-PERP", "ATOM/USDT-PERP", "ETC/USDT-PERP"
        ],
        "Options": [
            "BTC-25MAR22-40000-C", "ETH-25MAR22-3000-C", "BTC-25MAR22-45000-C",
            "ETH-25MAR22-3500-C", "BTC-25MAR22-50000-C", "ETH-25MAR22-4000-C",
            "BTC-25MAR22-55000-C", "ETH-25MAR22-4500-C", "BTC-25MAR22-60000-C",
            "ETH-25MAR22-5000-C"
        ]
    },
    "Coinbase": {
        "Spot": ["BTC/USD", "ETH/USD", "SOL/USD"]
    },
    "Kraken": {
        "Spot": ["XBT/USD", "ETH/USD", "DOT/USD"],
        "Futures": ["XBT/USD-PERP", "ETH/USD-PERP"]
    }
}

# Track if we need to update the component
if "needs_update" not in st.session_state:
    st.session_state.needs_update = False

# Track which menu changed
if "changed_menu" not in st.session_state:
    st.session_state.changed_menu = None

# Track current theme
if "current_theme" not in st.session_state:
    st.session_state.current_theme = "Dark"

# Initial menu state setup
if "menu_state" not in st.session_state:
    default_exchange = "Binance"
    default_type = "Spot"

    st.session_state.menu_state = {
        "exchange_select": {
            "label": "Exchanges",
            "options": ["Binance", "Coinbase", "Kraken"],
            "value": default_exchange
        },
        "type_select": {
            "label": "Types",
            "options": exchange_types[default_exchange],
            "value": default_type
        },
        "symbol_select": {
            "label": "Symbols",
            "options": exchange_symbols[default_exchange][default_type],
            "value": exchange_symbols[default_exchange][default_type][0]
        },
        "interval_select": {
            "label": "Interval",
            "options": ["1m", "5m", "15m", "1h", "4h", "1d"],
            "value": "1h"
        },
        "indicator_select": {
            "label": "Indicator",
            "options": ["None", "MA", "EMA", "RSI"],
            "value": "None"
        },
        "theme_select": {
            "label": "Theme",
            "options": ["Dark", "Light", "Custom"],
            "value": st.session_state.current_theme
        }
    }

# Use a unique key for the component based on the state
component_key = f"price_chart_menus_{hash(str(st.session_state.menu_state))}"

# Get current theme colors
theme_colors = themes[st.session_state.current_theme]

# Use the batch menu component with theme colors
updated_state = st_batch_menu_group(
    st.session_state.menu_state,
    key=component_key,
    label_color=theme_colors["label_color"],
    menu_bg_color=theme_colors["menu_bg_color"],
    menu_border_color=theme_colors["menu_border_color"],
    menu_hover_color=theme_colors["menu_hover_color"],
    menu_focus_shadow_color=theme_colors["menu_focus_shadow_color"],
    menu_text_color=theme_colors["menu_text_color"]
)

# Check if state has changed
if updated_state != st.session_state.menu_state:
    # Find which menu changed
    changed_menu = None
    for menu_id in st.session_state.menu_state:
        if st.session_state.menu_state[menu_id]["value"] != updated_state[menu_id]["value"]:
            changed_menu = menu_id
            break

    # Store which menu changed
    st.session_state.changed_menu = changed_menu

    # Create a new valid state based on the change
    valid_state = dict(updated_state)

    # Handle dependencies to ensure a valid state
    if changed_menu == "exchange_select":
        # Update types based on new exchange
        exchange = valid_state["exchange_select"]["value"]

        # Ensure the exchange exists in our data
        if exchange in exchange_types:
            new_types = exchange_types[exchange]
            valid_state["type_select"]["options"] = new_types

            # Ensure the selected type is valid for this exchange
            if valid_state["type_select"]["value"] not in new_types:
                valid_state["type_select"]["value"] = new_types[0]

            # Update symbols based on new type
            type_val = valid_state["type_select"]["value"]
            if type_val in exchange_symbols[exchange]:
                new_symbols = exchange_symbols[exchange][type_val]
                valid_state["symbol_select"]["options"] = new_symbols

                # Ensure the selected symbol is valid for this exchange/type
                if valid_state["symbol_select"]["value"] not in new_symbols:
                    valid_state["symbol_select"]["value"] = new_symbols[0]

    elif changed_menu == "type_select":
        # Update symbols based on new type
        exchange = valid_state["exchange_select"]["value"]
        type_val = valid_state["type_select"]["value"]

        # Ensure the exchange and type exist in our data
        if exchange in exchange_symbols and type_val in exchange_symbols[exchange]:
            new_symbols = exchange_symbols[exchange][type_val]
            valid_state["symbol_select"]["options"] = new_symbols

            # Ensure the selected symbol is valid for this exchange/type
            if valid_state["symbol_select"]["value"] not in new_symbols:
                valid_state["symbol_select"]["value"] = new_symbols[0]

    elif changed_menu == "theme_select":
        # Update the current theme
        st.session_state.current_theme = valid_state["theme_select"]["value"]

    # Update session state with the new valid state
    st.session_state.menu_state = valid_state
    st.session_state.needs_update = True

    # Force a rerun to apply the changes immediately
    st.rerun()

# Display the current selections
st.subheader("Current Selections")
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.metric("Exchange", st.session_state.menu_state["exchange_select"]["value"])
with col2:
    st.metric("Type", st.session_state.menu_state["type_select"]["value"])
with col3:
    st.metric("Symbol", st.session_state.menu_state["symbol_select"]["value"])
with col4:
    st.metric("Interval", st.session_state.menu_state["interval_select"]["value"])
with col5:
    st.metric("Indicator", st.session_state.menu_state["indicator_select"]["value"])
with col6:
    st.metric("Theme", st.session_state.menu_state["theme_select"]["value"])

# Display current theme colors
st.subheader("Current Theme Colors")
theme_colors = themes[st.session_state.current_theme]
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.color_picker("Label Color", theme_colors["label_color"], disabled=True)
with col2:
    st.color_picker("Background", theme_colors["menu_bg_color"], disabled=True)
with col3:
    st.color_picker("Border", theme_colors["menu_border_color"], disabled=True)
with col4:
    st.color_picker("Hover", theme_colors["menu_hover_color"], disabled=True)
with col5:
    st.text("Focus Shadow")
    st.code(theme_colors["menu_focus_shadow_color"])

# Simulate chart display
st.subheader("Price Chart")
st.info(f"This is where your chart would be displayed for {st.session_state.menu_state['symbol_select']['value']} on {st.session_state.menu_state['exchange_select']['value']} ({st.session_state.menu_state['type_select']['value']}) with {st.session_state.menu_state['interval_select']['value']} interval")

# Explanation
st.markdown("---")
st.markdown("""
### How This Works

1. **Single Component**: All menus are wrapped in a single Streamlit component
2. **Batch Updates**: When any menu changes, the entire state is sent back to Python
3. **Dependency Handling**: Python code handles dependencies between menus
4. **Reduced Reruns**: The page only reruns once per user interaction
5. **Theme Customization**: The component's appearance can be customized with color parameters

This approach significantly reduces the number of page reruns compared to using individual Streamlit select boxes.
""")