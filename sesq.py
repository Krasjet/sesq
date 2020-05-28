from pygments.style import Style
from pygments.formatters import HtmlFormatter
from pygments.token import *

white = "#f4f7f7"
gray06 = "#909494"
gray05 = "#7c8080"
gray04 = "#5c6060"
gray03 = "#545858"
gray02 = "#404444"
gray01 = "#222626"
black = "#081212"

lightblue = "#74A3B7"
blue = "#507585"
purple = "#818AC2"

select = "#dce0e0"
error = "#FF6363"


class Sesq(Style):
    """
    Sesquichromatic syntax highlighting, for karasu.
    """
    background_color = white
    highlight_color = select

    default_style = ""

    styles = {
        Comment: gray06,
        Comment.Preproc: "italic " + gray06,
        Comment.PreprocFile: blue,
        Comment.Hashbang: "italic " + gray06,

        Keyword: "italic " + gray01,
        Keyword.Type: "bold " + black,

        Punctuation: "italic " + gray01,
        Operator: "italic " + black,

        Name: gray01,
        Name.Function: "italic underline " + gray04,

        Name.Variable: "italic " + gray04,
        Name.Builtin: "italic " + gray04,
        Name.Attribute: "italic " + gray05,
        Name.Namespace: gray04,

        Name.Decorator: "bold " + gray02,
        Name.Tag: "italic " + gray02,
        Name.Class: "bold " + gray03,
        Name.Constant: "bold " + gray03,

        String: blue,
        String.Symbol: "italic " + lightblue,
        String.Backtick: "" + lightblue,

        Number: "bold " + purple,

        Generic.Heading: "bold " + black,
        Generic.Subheading: "italic " + black,
        Generic.Output: "bold " + gray05,
        Generic.Prompt: "italic " + gray02,
        Generic.Emph: "italic " + black,
        Generic.Strong: "bold " + black,

        Error: error
    }


if __name__ == '__main__':
    print(HtmlFormatter(style=Sesq).get_style_defs(['.sourceCode']))
