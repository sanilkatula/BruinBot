# """Shared auth layout."""

# import reflex as rx

# def container(*children, **props):
#     """A fixed container based on a 960px grid."""
#     # Enable override of default props.
#     props = (
#         dict(
#             width="100%",
#             max_width="960px",
#             background="white",
#             height="100%",
#             px="9",
#             margin="0 auto",
#             position="relative",
#         )
#         | props
#     )
#     return rx.stack(*children, **props)

# def auth_layout(*args):
#     """The shared layout for the login and sign up pages."""
#     return rx.box(
#         container(
#             rx.vstack(
#                 rx.heading("Welcome to PySocial!", size="8"),
#                 rx.heading("Sign in or sign up to get started.", size="8"),
#                 align="center",
#             ),
#             rx.text(
#                 "See the source code for this demo app ",
#                 rx.link(
#                     "here",
#                     href="https://github.com/reflex-dev/reflex-examples/tree/main/twitter",
#                 ),
#                 ".",
#                 color="gray",
#                 font_weight="medium",
#             ),
#             *args,
#             border_top_radius="10px",
#             box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
#             display="flex",
#             flex_direction="column",
#             align_items="center",
#             padding_top="36px",
#             padding_bottom="24px",
#             spacing="4",
#         ),
#         height="100vh",
#         padding_top="40px",
#         background="url(bg.svg)",
#         background_repeat="no-repeat",
#         background_size="cover",
#     )