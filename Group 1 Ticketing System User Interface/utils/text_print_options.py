class Term:
    '''
    This class contains methods for displaying text in different colors
    '''
    # ANSI escape codes for colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'  # Reset to default color

    # ANSI escape codes for text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # ANSI escape codes for combinations of colors and styles
    RESET_BOLD = RESET + BOLD
    RED_BOLD = RED + BOLD
    GREEN_BOLD = GREEN + BOLD
    YELLOW_BOLD = YELLOW + BOLD
    BLUE_BOLD = BLUE + BOLD
    MAGENTA_BOLD = MAGENTA + BOLD
    RESET_UNDERLINE = RESET + UNDERLINE
    RED_UNDERLINE = RED + UNDERLINE
    GREEN_UNDERLINE = GREEN + UNDERLINE
    YELLOW_UNDERLINE = YELLOW + UNDERLINE
    BLUE_UNDERLINE = BLUE + UNDERLINE
    MAGENTA_UNDERLINE = MAGENTA + UNDERLINE
    RESET_BOLD_UNDERLINE = RESET + BOLD + UNDERLINE
    RED_BOLD_UNDERLINE = RED + BOLD + UNDERLINE
    GREEN_BOLD_UNDERLINE = GREEN + BOLD + UNDERLINE
    YELLOW_BOLD_UNDERLINE = YELLOW + BOLD + UNDERLINE
    BLUE_BOLD_UNDERLINE = BLUE + BOLD + UNDERLINE
    MAGENTA_BOLD_UNDERLINE = MAGENTA + BOLD + UNDERLINE
    




class PrintOptions:
    def __init__(self
                , alignment='center'
                , tab_spaces=0
                , screen_width=100
                , border_marker_char="|"
                , line_divider_char="*"
                , item_divider_char="|"
                , text_color=Term.RESET
                , border_marker_color=Term.RESET
                , line_divider_color=Term.RESET
                , item_divider_color=Term.RESET
                ):
        self.alignment = alignment
        self.tab_spaces = tab_spaces
        self.screen_width = screen_width
        self.border_marker_char = border_marker_char
        self.line_divider_char = line_divider_char
        self.item_divider_char = item_divider_char
        self.text_color = text_color
        self.border_marker_color = border_marker_color
        self.line_divider_color = line_divider_color
        self.item_divider_color = item_divider_color

    def copy(self):
        return PrintOptions(
            alignment=self.alignment,
            tab_spaces=self.tab_spaces,
            screen_width=self.screen_width,
            border_marker_char=self.border_marker_char,
            line_divider_char=self.line_divider_char,
            item_divider_char=self.item_divider_char,
            text_color=self.text_color,
            border_marker_color=self.border_marker_color,
            line_divider_color=self.line_divider_color,
            item_divider_color=self.item_divider_color
        )