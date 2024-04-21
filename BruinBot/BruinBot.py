import reflex as rx
from BruinBot import style
from BruinBot.state import TutorialState
from BruinBot.components import chat, navbar
from typing import Any, Dict
from BruinBot import login
from BruinBot import signup

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.chat_input_style), style={'text_align': 'right'}),
        rx.box(rx.text(answer, style=style.chat_messages_style), style={'text_align': 'left'}),
        style={'margin': '8px 0'}
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(TutorialState.chat_history, lambda messages: qa(messages[0], messages[1])),
        style=style.chat_box_style,
        py="8",
        flex="1",
        width="100%",
        max_width="50em",
        padding_x="4px",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    )


def action_bar() -> rx.Component:
    """
    Creates a centered horizontal stack layout with an input and button for user interactions.

    Returns:
        rx.Component: A reactive component representing the centered horizontal stack with input and button.
    """
    # Define styles if not globally available
    input_style: Dict[str, Any] = {'width': '70%', 'marginRight': '10px'}
    button_style: Dict[str, Any] = {'width': '30%'}

    # Adjust the stack style to center-align items
    stack_style: Dict[str, Any] = {
        'padding': '10px 0',
        'alignItems': 'center',  # Align items vertically in the center
        'justifyContent': 'center'  # Center-align items horizontally
    }

    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            value=TutorialState.question,  # Ensure TutorialState is properly defined and accessible
            on_change=TutorialState.set_question,
            style=input_style  # Use local or passed style configuration
        ),
        rx.button(
            "Ask",
            on_click=TutorialState.answer,  # Ensure TutorialState.answer is a callable function
            style=button_style  # Use local or passed style configuration
        ),
        style=stack_style  # Apply the new stack style with center alignment
    )
 

# @rx.page(route="/", title="Index Page")
# def index():
#     return rx.vstack(
#         GoogleOAuthProvider.create(
#             GoogleLogin.create(on_success=State.on_success),
#             client_id=CLIENT_ID,
#         )
#     )


@rx.page(route="/", title="Welcome to BruinBuddy")
def index() -> rx.Component:
    # Create a welcoming message with enhanced style
    greeting = rx.text(
        "Welcome to BruinBuddy!",
        style={
            "font-size": "24px",
            "font-weight": "bold",
            "color": "navy",
            "padding": "20px",
            "text-align": "center"  # Center-align the text
        }
    )

    # Subtext to describe BruinBuddy's purpose with refined style
    description = rx.text(
        "Your compassionate companion, here to listen, help, and empower you.",
        style={
            "font-size": "16px",
            "color": "darkgrey",
            "padding": "10px",
            "text-align": "center"  # Center-align the text
        }
    )

    # Stylish button that leads to the main page, with enhanced style
    login_button = rx.link(
        rx.button(
            "Log In",
            style={
                "background-color": "teal",  # Primary color for the button
                "color": "white",  # Text color for better contrast
                "border": "none",  # No border for a cleaner look
                "padding": "12px 24px",  # Comfortable padding for easier interaction
                "border-radius": "8px",  # Soft rounded corners for a modern look
                "cursor": "pointer",  # Cursor changes to pointer to indicate interactivity
                "font-weight": "bold",  # Bold text for better readability
                "margin-top": "20px",  # Margin top for spacing from other elements
                "button-align": "center",  # Text is centered within the button
                "transition": "background-color 0.3s, transform 0.3s",  # Smooth transition for color and transformation
            }
        ),
        href="/home/",
        on={
            "mouseover": {"background-color": "#005a5a"},  # Darker teal on hover for visual feedback
            "mouseout": {"background-color": "teal"},  # Revert to original color on mouse out
            "mousedown": {"transform": "scale(0.95)"},  # Slightly shrink on click
            "mouseup": {"transform": "scale(1.0)"}  # Return to normal size on release
        }

    )

    # Arrange components vertically with better spacing and alignment
    layout = rx.center(rx.vstack(rx.center(greeting, width = "100%"), description, rx.center(login_button, width="100%")))


    return layout





@rx.page(route="/home", title="Home Page")
def home() -> rx.Component:
    """The main app displayed as the home page."""

    return rx.chakra.vstack(
        navbar(),
        chat(),
        action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )

app = rx.App(

)

# app.add_page(signup)
# app.add_page(login)
# app.add_page(home, route="/", on_load=State.check_login())

