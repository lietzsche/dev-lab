import unittest

from pptx import Presentation
from pptx.enum.text import MSO_AUTO_SIZE
from pptx.util import Inches

from ppt_module import add_textbox, validate


class TextboxSafetyTests(unittest.TestCase):
    def _slide(self):
        prs = Presentation()
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)
        return prs, prs.slides.add_slide(prs.slide_layouts[6])

    def test_explicit_newline_is_separate_text_shapes(self):
        _, slide = self._slide()
        result = add_textbox(slide, 1, 1, 4, "첫 줄\n둘째 줄", 18)
        self.assertEqual([shape.text for shape in result.shapes], ["첫 줄", "둘째 줄"])
        first, second = result.shapes
        self.assertLess(first.top + first.height, second.top)

    def test_fixed_multiline_box_keeps_headroom(self):
        _, slide = self._slide()
        result = add_textbox(
            slide, 1, 1, 4, "첫 줄\n둘째 줄", 22,
            height=1.0, margin_in=0.02, min_size_pt=7,
        )
        for shape in result.shapes:
            fit_ratio, line_count = validate._text_fit_ratio(shape)
            self.assertEqual(line_count, 1)
            self.assertLessEqual(fit_ratio, 1.0)
            self.assertEqual(shape.text_frame.auto_size, MSO_AUTO_SIZE.NONE)
        self.assertLess(result.shapes[0].top + result.shapes[0].height, result.shapes[1].top)

    def test_validator_reports_overlapping_split_lines(self):
        _, slide = self._slide()
        result = add_textbox(
            slide, 1, 1, 4, "첫 줄\n둘째 줄", 20,
            height=1.0, margin_in=0.01,
        )
        result.shapes[1].top = result.shapes[0].top + result.shapes[0].height - Inches(0.1)
        warnings = validate.check_slide(slide, index=1)
        self.assertTrue(any("overlaps text" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
