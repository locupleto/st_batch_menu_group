import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_batch_menu_group",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_batch_menu_group", path=build_dir)


def st_batch_menu_group(
    menu_state,
    key=None,
    label_color="white",
    menu_bg_color="#fff",
    menu_border_color="#d9d9d9",
    menu_hover_color="#40a9ff",
    menu_focus_shadow_color="rgba(24, 144, 255, 0.2)",
    menu_text_color="#333333",
):
    """
    Create a batch menu group component that handles multiple select boxes as a single unit.

    This component is designed to reduce Streamlit page reruns by handling all menu
    interactions in a single component. When any menu changes, the entire state is
    returned to Python for processing.

    Parameters
    ----------
    menu_state : dict
        A dictionary containing the complete state of all menus.
        Format: {
            "menu_id": {
                "label": "Menu Label",
                "options": ["Option 1", "Option 2", ...],
                "value": "Selected Option"
            },
            ...
        }
    key : str
        An optional key that uniquely identifies this component.
    label_color : str
        Color for the menu labels (default: "white")
    menu_bg_color : str
        Background color for the menu dropdowns (default: "#fff")
    menu_border_color : str
        Border color for the menu dropdowns (default: "#d9d9d9")
    menu_hover_color : str
        Border color when hovering over a menu (default: "#40a9ff")
    menu_focus_shadow_color : str
        Shadow color when a menu is focused (default: "rgba(24, 144, 255, 0.2)")
    menu_text_color : str
        Text color for the menu items (default: "#333333")

    Returns
    -------
    dict
        The updated menu state after user interaction.
    """
    component_value = _component_func(
        menu_state=menu_state,
        label_color=label_color,
        menu_bg_color=menu_bg_color,
        menu_border_color=menu_border_color,
        menu_hover_color=menu_hover_color,
        menu_focus_shadow_color=menu_focus_shadow_color,
        menu_text_color=menu_text_color,
        key=key,
        default=menu_state
    )

    return component_value