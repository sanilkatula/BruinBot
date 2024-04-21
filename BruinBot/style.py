import reflex as rx

# Enhanced color palette
background_color = '#f0f2f5'
primary_color = '#0056b3'
secondary_color = '#e9ecef'
text_color = '#343a40'
button_hover_color = '#004494'

# Common styles
common_style = {
    'border_radius': '8px',
    'box_shadow': '0 2px 12px rgba(0,0,0,0.15)',
    'font_family': 'Arial, sans-serif',
    'color': text_color,
}

# Define styles
chat_header_style = {
    **common_style,
    'padding': '12px',
    'background_color': primary_color,
    'color': 'white',
    'text_align': 'center',
}

chat_box_style = {
    **common_style,
    'width': '350px',
    'height': '500px',
    'background_color': secondary_color,
    'border': '1px solid #ccc',
    'flex_direction': 'column',
}

chat_messages_style = {
    'flex': 1,
    'padding': '10px',
    'overflow_y': 'auto',
    'background_color': background_color,
}

chat_input_style = {
    **common_style,
    'display': 'flex',
    'padding': '10px',
    'background_color': secondary_color,
}

input_style = {
    'flex': 1,
    'padding': '8px 12px',
    'border': '1px solid #bbb',
    'margin_right': '5px',
    'background_color': 'white',
}

button_style = {
    **common_style,
    'padding': '8px 16px',
    'background_color': primary_color,
    'hover': {
        'background_color': button_hover_color,
    },
    'cursor': 'pointer',
}

