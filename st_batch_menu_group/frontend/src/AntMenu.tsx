// AntMenu.tsx with configurable colors
import React, { useEffect, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";

interface MenuState {
  [key: string]: {
    label: string;
    options: string[];
    value: string;
  };
}

const BatchMenuGroup = (props: ComponentProps) => {
  // Ensure menu_state is defined with a default empty object
  const menu_state = props.args.menu_state || {};
  const [state, setState] = useState<MenuState>(menu_state);

  // Get color parameters with defaults
  const labelColor = props.args.label_color || "white";
  const menuBgColor = props.args.menu_bg_color || "#fff";
  const menuBorderColor = props.args.menu_border_color || "#d9d9d9";
  const menuHoverColor = props.args.menu_hover_color || "#40a9ff";
  const menuFocusShadowColor =
    props.args.menu_focus_shadow_color || "rgba(24, 144, 255, 0.2)";
  const menuTextColor = props.args.menu_text_color || "#333333";

  // Update component height when rendered - reduced height
  useEffect(() => {
    const element = document.getElementById("batch-menu-container");
    if (element) {
      // Even more reduced height
      Streamlit.setFrameHeight(element.offsetHeight + 5);
    }
  }, [state]);

  // Handle change in any select box
  const handleChange = (menuId: string, value: string) => {
    // Create a new state with the updated value
    const newState = {
      ...state,
      [menuId]: {
        ...state[menuId],
        value: value,
      },
    };

    // Update local state
    setState(newState);

    // Send the complete state back to Python
    Streamlit.setComponentValue(newState);
  };

  return (
    <div id="batch-menu-container" style={{ width: "100%" }}>
      <style>
        {`
          select {
            appearance: none;
            background-color: ${menuBgColor};
            border: 1px solid ${menuBorderColor};
            border-radius: 4px;
            padding: 5px 8px;
            padding-right: 25px;
            font-size: 14px;
            cursor: pointer;
            width: 100%;
            color: ${menuTextColor};
            background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23131313%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
            background-repeat: no-repeat;
            background-position: right 8px top 50%;
            background-size: 10px auto;
          }

          option {
            background-color: ${menuBgColor};
            color: ${menuTextColor};
          }

          select:hover {
            border-color: ${menuHoverColor};
          }

          select:focus {
            outline: none;
            border-color: ${menuHoverColor};
            box-shadow: 0 0 0 2px ${menuFocusShadowColor};
          }

          .menu-label {
            font-weight: 500;
            font-size: 12px;
            margin-bottom: 1px;
            color: ${labelColor};
          }

          .menu-container {
            margin-right: 10px;
            margin-bottom: 4px;
            min-width: 150px;
            max-width: 250px;
            flex: 1;
          }

          @media (max-width: 768px) {
            .menu-container {
              min-width: 120px;
            }
          }
        `}
      </style>
      <div
        style={{ display: "flex", flexWrap: "wrap", width: "100%", gap: "6px" }}
      >
        {Object.entries(state).map(([menuId, menuData]) => (
          <div key={menuId} className="menu-container">
            <label className="menu-label">{menuData.label}</label>
            <select
              value={menuData.value}
              onChange={(e) => handleChange(menuId, e.target.value)}
            >
              {(menuData.options || []).map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>
          </div>
        ))}
      </div>
    </div>
  );
};

export default withStreamlitConnection(BatchMenuGroup);
