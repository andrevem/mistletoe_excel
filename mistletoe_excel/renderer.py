from dataclasses import dataclass
from functools import singledispatchmethod
from typing import Any, Iterable

from mistletoe import block_token, span_token
from mistletoe.block_token import BlockToken
from mistletoe.base_renderer import BaseRenderer

from openpyxl.cell.rich_text import TextBlock, CellRichText
from openpyxl.worksheet.cell_range import CellRange
from 

@dataclass
class ExcelRendererOptions: # TODO complete this
    pass

# super().__init__ also create a map for polyformism that is not gonna be used

class ExcelRenderer(BaseRenderer):
    """Excel renderer for mistletoe.
    """
    def __init__(self, *extras, **ExcelRendererOptions):
        super().__init__(*extras) # this also create a map for polyformism that is not gonna be used
        self.options = ExcelRendererOptions       

    # As this is a stateful renderer we dont have to return anything
    # By convenction we return the log of the state change
    
    def render(self, token) -> str: # we return the range as a string
        return self._render(token)

    @singledispatchmethod
    def _render(self, token) -> str:
        return ''

    @_render.register
    def __render(self, token: span_token.Strong) -> str:
        return ''
    def render_emphasis(self, token):
        pass
    def render_inline_code(self, token):
        pass
    def render_raw_text(self, token):
        pass
    def render_strikethrough(self, token):
        pass
    def render_image(self, token):
        pass
    def render_link(self, token):
        pass
    def render_auto_link(self, token):
        pass
    def render_escape_sequence(self, token):
        pass
    def render_heading(self, token):
        pass
    def render_heading(self, token):
        pass
    def render_quote(self, token):
        pass
    def render_paragraph(self, token):
        pass
    def render_block_code(self, token):
        pass
    def render_block_code(self, token):
        pass
    def render_list(self, token):
        pass
    def render_list_item(self, token):
        pass
    def render_table(self, token):
        pass
    def render_table_row(self, token):
        pass
    def render_table_cell(self, token):
        pass
    def render_thematic_break(self, token):
        pass
    def render_line_break(self, token):
        pass
    def render_document(self, token):
        pass
    }