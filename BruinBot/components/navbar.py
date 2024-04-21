import reflex as rx
from BruinBot.state import TutorialState

def sidebar_chat(chat: str) -> rx.Component:
    """A sidebar chat item.

    Args:
        chat: The chat item.
    """
    return  rx.drawer.close(rx.hstack(
        rx.button(
            chat, on_click=lambda: TutorialState.set_chat(chat), width="80%", variant="surface"
        ),
        rx.button(
            rx.icon(
                tag="trash",
                on_click=TutorialState.delete_chat,
                stroke_width=1,
            ),
            width="20%",
            variant="surface",
            color_scheme="red",
        ),
        width="100%",
    ))


def sidebar(trigger) -> rx.Component:
    """Enhanced sidebar component with improved aesthetics."""
    # Sidebar styles
    sidebar_style = {
        'top': 'auto',
        'right': 'auto',
        'height': '100%',
        'width': '20em',
        'padding': '2em',
        'background_color': rx.color("mauve", 2),
        'outline': 'none',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
        'borderRight': f'1px solid {rx.color("mauve", 3)}'
    }
    
    # Heading style
    heading_style = {
        'color': rx.color("mauve", 12),
        'fontSize': '1.25em',
        'fontWeight': 'bold',
        'marginBottom': '0.5em'
    }
    
    # Divider style
    divider_style = {
        'margin': '1em 0'
    }

    return rx.drawer.root(
        rx.drawer.trigger(trigger),
        rx.drawer.overlay(),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.heading("Chats", style=heading_style),
                    rx.divider(style=divider_style),
                    align_items="stretch",
                    width="100%",
                ),
                style=sidebar_style
            ),
            direction="left"
        )
    )



def modal(trigger) -> rx.Component:
    """A modal to create a new chat."""
    return rx.dialog.root(
        rx.dialog.trigger(trigger),
        rx.dialog.content(
            rx.hstack(
                rx.input(
                    placeholder="Type something...",
                    width=["15em", "20em", "30em", "30em", "30em", "30em"],
                ),
                rx.dialog.close(
                    rx.button(
                        "Create chat",
                    ),
                ),
                background_color=rx.color("mauve", 1),
                spacing="2",
                width="100%",
            ),
        ),
    )

def navbar():
    """Generates a soothing and visually appealing navigation bar."""
    # Styles
    navbar_style = {
        'padding': '12px 24px',
        'backdropFilter': 'auto',
        'backdropBlur': 'lg',
        'borderBottom': f"1px solid {rx.color('mauve', 3)}",
        'backgroundColor': rx.color("sky", 2),
        'position': 'sticky',
        'top': '0',
        'zIndex': '100',
        'alignItems': 'center'
    }

    avatar_style = {
        'marginRight': '8px',
        'backgroundImage': 'url(https://example.com/avatar.png)',  # Placeholder image URL
        'backgroundSize': 'cover'
    }

    heading_style = {
        'fontWeight': 'bold',
        'fontSize': '18px',
        'color': rx.color("cyan", 9)
    }

    tooltip_badge_style = {
        'marginLeft': '12px'
    }

    button_style = {
        'fontWeight': 'bold',
        'marginLeft': '12px',
        'boxShadow': '0 2px 4px rgba(0, 120, 255, 0.3)'
    }

    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.avatar(fallback="BB", variant="solid", style=avatar_style),
                rx.heading("Your Friendly Neighbourhood BruinBot", style=heading_style),
                rx.desktop_only(
                    rx.badge(
                        rx.tooltip(rx.icon("info", size=16), content="The current selected chat."),
                        variant="soft",
                        style=tooltip_badge_style
                    )
                ),
                align_items="center",
            ),
            rx.hstack(
                modal(rx.button("+ New chat", style=button_style)),
                sidebar(
                    rx.button(
                        rx.icon(
                            tag="messages-square",
                            color=rx.color("blue", 12),
                        ),
                        background_color=rx.color("blue", 6),
                        style=button_style
                    )
                ),
                rx.desktop_only(
                    rx.button(
                        rx.icon(
                            tag="sliders-horizontal",
                            color=rx.color("green", 12),
                        ),
                        background_color=rx.color("green", 6),
                        style=button_style
                    )
                ),
                align_items="center",
            ),
            justify_content="space-between",
            align_items="center",
        ),
        style=navbar_style
    )
