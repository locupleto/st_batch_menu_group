import streamlit.components.v1 as components
import os

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_batch_menu_group",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_batch_menu_group", path=build_dir)


def st_batch_menu_group(
    menu_state,
    key=None,
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

    Returns
    -------
    dict
        The updated menu state after user interaction.
    """
    component_value = _component_func(
        menu_state=menu_state,
        key=key,
        default=menu_state
    )

    return component_value