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

# def index() -> rx.Component:

#     return rx.link(rx.button("Log In"), href="/home/")


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
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
    ),
)

# app.add_page(signup)
# app.add_page(login)
# app.add_page(home, route="/", on_load=State.check_login())

