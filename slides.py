from manim import *
from manim_slides import Slide

from PIL import Image
import numpy as np
import requests
from pathlib import Path

import numpy as np

class EmojiImageMobject(ImageMobject):
    def __init__(self, emoji, **kwargs):
        emoji_code = "-".join(f"{ord(c):x}" for c in emoji)
        emoji_code = emoji_code.upper()  # <-  needed for openmojis
        url = f"https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/618x618/{emoji_code}.png"
        im = Image.open(requests.get(url, stream=True).raw)
        emoji_img = np.array(im.convert("RGBA"))
        ImageMobject.__init__(self, emoji_img, **kwargs)

class Slide1(Slide):
    def construct(self):

        title_old = Tex(r"CMS", font_size=50).shift(DOWN*1.3)
        author = Tex("Andres Rios-Tascon", font_size=40).next_to(title_old, DOWN, buff=0.6)
        info = Tex("RSE Group Meeting. Jul 10th, 2024", font_size=30).next_to(author, DOWN, buff=0.6)

        cms_detector = ImageMobject("./images/cms_detector.jpeg").scale_to_fit_height(4).next_to(title_old, UP, buff=0.5)
        line_cross = Line(start=cms_detector.get_center()+LEFT*3 + DOWN*2, end=cms_detector.get_center()+RIGHT*3 + UP*2, stroke_width=50).set_color(PURE_RED)

        mirror_symmetry = ImageMobject("./images/mirror_symmetry.png").scale_to_fit_height(4).next_to(title_old, UP, buff=0.5)
        title_new = Tex(r"Computational Mirror Symmetry", font_size=50).shift(DOWN*1.3)

        self.add(title_old, author, info, cms_detector)
        self.wait(0.1)
        self.next_slide()
        self.play(Create(line_cross))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(line_cross), FadeOut(cms_detector))
        self.play(FadeIn(mirror_symmetry), ReplacementTransform(title_old, title_new))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title_new, author, info, mirror_symmetry]], run_time=0.5)

class Slide2(Slide):
    def construct(self):
        title = Tex(r"{{Brief History}}", font_size=50).to_edge(UP, buff=0.5)

        text1 = Tex(r"In the late 1980's, mathematicians were studying enumerative geometry.\\(The counting of certain objects/solutions in geometry.)", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP)
        text2 = Tex(r"They were working with geometric spaces called Calabi-Yau (CY)\\manifolds.", font_size=40, tex_environment="flushleft").next_to(text1, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text3 = Tex(r"Why?", font_size=40, tex_environment="flushleft").next_to(text2, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text4 = Tex(r"They're mathematicians.", font_size=40, tex_environment="flushleft").next_to(text3, RIGHT, buff=0.5)
        text5 = Tex(r"This is how it went.", font_size=40, tex_environment="flushleft").next_to(text3, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)

        self.play(Write(title))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text4))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text5))
        self.wait(0.1)
        self.next_slide()

        title_new = Tex(r"{{Brief History}} (dramatization)", font_size=50).to_edge(UP, buff=0.5)

        mathematician = ImageMobject("./images/mathematician.png").scale_to_fit_height(2).to_corner(DL, buff=0.5)
        physicist = ImageMobject("./images/physicist.jpg").scale_to_fit_height(2).to_corner(DR, buff=0.5)

        mathematician_text = Tex(r"(mathematicians)", font_size=40).next_to(mathematician, UP, buff=0.5)
        physicist_text = Tex(r"(some physicists)", font_size=40).next_to(physicist, UP, buff=0.5)

        bubble_l1 = ImageMobject("./images/chat_bubble_gray.png").scale_to_fit_height(1.5).stretch_to_fit_width(7).to_edge(DOWN, buff=0.5).shift(LEFT*0.5)
        text_l1 = Tex(r"We spent spent a long time computing\\these few invariants.", font_size=30, tex_environment="flushleft").move_to(bubble_l1.get_center()).set_color(BLACK)

        bubble_l2 = ImageMobject("./images/chat_bubble_gray.png").scale_to_fit_height(1.5).stretch_to_fit_width(7).to_edge(DOWN, buff=0.5).shift(LEFT*0.5)
        text_l2 = Tex(r"It's too hard to compute more of them.", font_size=30, tex_environment="flushleft").move_to(bubble_l2.get_center()).set_color(BLACK)
        
        bubble_r1 = ImageMobject("./images/chat_bubble_blue.png").scale_to_fit_height(1.5).stretch_to_fit_width(7).to_edge(DOWN, buff=0.5).shift(RIGHT*0.5)
        text_r1 = Tex(r"We computed a bunch more.", font_size=30, tex_environment="flushleft").move_to(bubble_r1.get_center()).set_color(BLACK)

        bubble_r2 = ImageMobject("./images/chat_bubble_blue.png").scale_to_fit_height(1.5).stretch_to_fit_width(7).to_edge(DOWN, buff=0.5).shift(RIGHT*0.5)
        text_r2 = Tex(r"We used physics.", font_size=30, tex_environment="flushleft").move_to(bubble_r2.get_center()).set_color(BLACK)

        bubble_l3 = ImageMobject("./images/chat_bubble_gray.png").scale_to_fit_height(1.5).stretch_to_fit_width(7).to_edge(DOWN, buff=0.5).shift(LEFT*0.5)
        text_l3 = Tex(r"wat", font_size=30, tex_environment="flushleft").move_to(bubble_l3.get_center()).set_color(BLACK)

        bubble_l4 = ImageMobject("./images/chat_bubble_gray.png").scale_to_fit_height(1.5).stretch_to_fit_width(7).to_edge(DOWN, buff=0.5).shift(LEFT*0.5)
        text_l4 = Tex(r"wow ur right", font_size=30, tex_environment="flushleft").move_to(bubble_l4.get_center()).set_color(BLACK)

        self.play(*[FadeOut(o) for o in [text1, text2, text3, text4, text5]], TransformMatchingTex(title, title_new), run_time=0.5)
        self.play(FadeIn(mathematician), Write(mathematician_text))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(bubble_l1), FadeIn(text_l1))
        self.wait(0.1)
        self.next_slide()
        self.play(*[o.animate.shift(UP*1.5) for o in [bubble_l1, text_l1]], run_time=0.5)
        self.play(FadeIn(bubble_l2), FadeIn(text_l2), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(physicist), Write(physicist_text))
        self.wait(0.1)
        self.next_slide()
        self.play(*[o.animate.shift(UP*1.5) for o in [bubble_l1, text_l1, bubble_l2, text_l2]], run_time=0.5)
        self.play(FadeIn(bubble_r1), FadeIn(text_r1), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(*[o.animate.shift(UP*1.5) for o in [bubble_l1, text_l1, bubble_l2, text_l2, bubble_r1, text_r1]], run_time=0.5)
        self.play(FadeIn(bubble_r2), FadeIn(text_r2), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(*[o.animate.shift(UP*1.5) for o in [bubble_l2, text_l2, bubble_r1, text_r1, bubble_r2, text_r2]], FadeOut(bubble_l1), FadeOut(text_l1), run_time=0.5)
        self.play(FadeIn(bubble_l3), FadeIn(text_l3), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(*[o.animate.shift(UP*1.5) for o in [bubble_r1, text_r1, bubble_r2, text_r2, bubble_l3, text_l3]], FadeOut(bubble_l2), FadeOut(text_l2), run_time=0.5)
        self.play(FadeIn(bubble_l4), FadeIn(text_l4), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [mathematician, physicist, bubble_r1, bubble_r2, bubble_l3, bubble_l4]], *[Unwrite(o) for o in [title_new, mathematician_text, physicist_text, text_r1, text_r2, text_l3, text_l4]], run_time=0.5)

class Slide3(Slide):
    def construct(self):
        title = Tex(r"How did they do this?", font_size=50).to_edge(UP, buff=0.5)
        
        t2a = Tex(r"IIA", font_size=40).next_to(title, DOWN, buff=0.6).shift(LEFT*3.5)
        t2b = Tex(r"IIB", font_size=40).next_to(title, DOWN, buff=0.6).shift(RIGHT*3.5)
        t_string = Tex("String Theory", font_size=40).next_to(title, DOWN, buff=0.6)
        t_mirror = Tex(r"different (mirror) CYs\\used as extra dimensions", font_size=30).next_to(title, DOWN, buff=2.5)
        t_physics = Tex("same physics", font_size=40).to_edge(DOWN, buff=1.5)
        
        cy1 = ImageMobject("images/CY_image.png")
        cy1.scale_to_fit_height(2.5)
        cy1.next_to(t2a, DOWN, buff=1.5)
        
        cy2 = ImageMobject("images/CY_image2.png")
        cy2.scale_to_fit_height(2.5)
        cy2.next_to(t2b, DOWN, buff=1.5)

        t_credit = Tex("[Images by Geoffrey Fatin]", font_size=15).to_edge(RIGHT, buff=0.2)

        t_ms = Tex("This is a very profound relationship called Mirror Symmetry", font_size=40).to_edge(DOWN, buff=0.5)
        
        a1 = Arrow(start=t2a.get_center()+DOWN*t2a.height/2, end=cy1.get_center()+UP*cy1.height/2)
        a2 = Arrow(start=t2b.get_center()+DOWN*t2b.height/2, end=cy2.get_center()+UP*cy2.height/2)
        
        a3 = Arrow(start=cy1.get_center()+RIGHT*cy1.width/2, end=t_physics.get_center()+UP*t_physics.height/2)
        a4 = Arrow(start=cy2.get_center()+LEFT*cy2.width/2, end=t_physics.get_center()+UP*t_physics.height/2)

        self.play(Write(title), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(t_string), FadeIn(t2a), FadeIn(t2b))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(a1), Create(a2), run_time=0.5)
        self.play(FadeIn(t_mirror), FadeIn(cy1), FadeIn(cy2), FadeIn(t_credit))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(a3), Create(a4), run_time=0.5)
        self.play(FadeIn(t_physics))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(t_ms))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [t_string, t2a, t2b, a1, a2, a3, a4, t_mirror, cy1, cy2, t_credit, t_physics, t_ms]],run_time=0.5)

        text1 = Tex(r"Quantum computations (very hard) on one side correspond to\\classical computations (much easier) on the other side.", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*1.5)
        text2 = Tex(r"Some quantum computations were related to the counting that\\mathematicians were doing.", font_size=40, tex_environment="flushleft").next_to(text1, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text3 = Tex(r"Mirror symmetry can be used as a computational tool!", font_size=40, tex_environment="flushleft").next_to(text2, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text4 = Tex(r"Strategy: do computations on the easy(-ish) side to\\find the answer of a computation on the hard side.", font_size=40, tex_environment="flushleft").next_to(text3, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)

        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text4))
        self.wait(0.1)
        self.next_slide()

        title_new = Tex(r"Why is this important?", font_size=50).to_edge(UP, buff=0.5)

        text5 = Tex(r"For physicists:", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*1.5)
        text6 = Tex(r"Some important topological invariants can be computed in this way,\\called Gopakumar-Vafa (GV) and Gromov-Witten (GW) invariants.\\The provide deep insights into the geometry and the resulting physics\\from string theory.", font_size=40, tex_environment="flushleft").next_to(text5, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        text7 = Tex(r"For mathematicians:", font_size=40, tex_environment="flushleft").next_to(text6, DOWN, buff=0.8).to_edge(LEFT, buff=0.5)
        text8 = Tex(r"They're mathematicians.", font_size=40, tex_environment="flushleft").next_to(text7, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        self.play(ReplacementTransform(VGroup(title, text1, text2, text3, text4), title_new))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text5))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text6))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text7))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text8))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title_new, text5, text6, text7, text8]], run_time=0.5)

class Slide4(Slide):
    def construct(self):
        title = Tex(r"Let's look at the actual computation", font_size=50).to_edge(UP, buff=0.5)
        subtitle = Tex(r"(skipping many details and hours of math)", font_size=30).next_to(title, DOWN, buff=0.2)

        text1 = Tex(r"In general, even the classical computation is still too hard.\\For CYs arising from toric varieties, Hosono, Klemm, Theisen and Yau\\(HKTY) devised a procedure.", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*1.5)
        text2 = Tex(r"After a hard integral and lots of math, the task boils down to rewriting\\a series with a change of variables and extracting the coefficients.", font_size=40, tex_environment="flushleft").next_to(text1, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text3 = MathTex(r"\frac{1}{2}\tilde{\kappa}_{abc}(\beta^{bc}(\vec{x}) - \alpha^b(\vec{x})\alpha^c(\vec{x}))=\sum_{\vec{n}\in\mathcal{M}}n_a\ \text{GV}_{\vec{n}}\ \text{Li}_2\left(e^{2\pi i\ \vec{n}\cdot\vec{t}}\right)", font_size=40).next_to(text2, DOWN, buff=0.5)
        text4 = MathTex(r"\text{using } t^a=\frac{\log x^a}{2\pi i} + \frac{\alpha^a(\vec{x})}{2\pi i}", font_size=40).next_to(text3, DOWN, buff=0.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3), FadeIn(text4))
        self.wait(0.1)
        self.next_slide()
        self.play(text3.animate.shift(UP*3), *[FadeOut(o) for o in [text1, text2, text4]], run_time=0.5)

        text5 = Tex(r"infinite series", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=1)
        a1 = Arrow(start=text5.get_center()+UP*text5.height/2, end=text3.get_center()+DOWN*text3.height/2+LEFT*3.8+UP*0.4)
        a2 = Arrow(start=text5.get_center()+UP*text5.height/2, end=text3.get_center()+DOWN*text3.height/2+LEFT*2.2+UP*0.4)

        text6 = Tex(r"invariants we want", font_size=40, tex_environment="flushleft").to_edge(RIGHT, buff=1)
        a3 = Arrow(start=text6.get_center()+UP*text6.height/2, end=text3.get_center()+DOWN*text3.height/2+RIGHT*2.3+UP*0.4)

        text7 = Tex(r"terms organized in a cone", font_size=40, tex_environment="flushleft").to_edge(DOWN, buff=2)
        a4 = Arrow(start=text7.get_center()+UP*text7.height/2, end=text5.get_center()+DOWN*text5.height/2)
        a5 = Arrow(start=text7.get_center()+UP*text7.height/2, end=text3.get_center()+DOWN*text3.height/2+RIGHT*1)

        text8 = Tex(r"GV invariants are integer due to miraculous cancellations.\\Even a tiny mistake in input/algorithm results in non-integer results.", font_size=40, tex_environment="flushleft").to_edge(DOWN, buff=0.5)

        self.play(Create(a1), Create(a2), FadeIn(text5), runtime=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(Create(a3), FadeIn(text6))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(a4), Create(a5), FadeIn(text7))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text8))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [text3, text5, text6, text7, text8, a1, a2, a3, a4, a5]], run_time=0.5)

        mori_pts = []
        for x in range(11):
            for y in range(11):
                if y <= 3*x:
                    mori_pts.append((x,y))
        mori_pts.sort(key=lambda p: (p[0]+p[1],p[1],p[0]))
        axes0 = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=5,
            y_length=5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            tips=False,
        ).shift(DOWN*0.2).to_edge(LEFT, buff=2).set_z_index(5)
        y_label0 = axes0.get_y_axis_label(Tex(r"$x_2$").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.2)
        x_label0 = axes0.get_x_axis_label(Tex(r"$x_1$"), edge=DOWN, direction=DOWN, buff=0.4)
        plot_labels0 = VGroup(x_label0, y_label0).set_z_index(5)
        dots_eff = [Dot(point=axes0.c2p(*pt)).set_z_index(10) for pt in mori_pts]
        gen1 = Line(start=axes0.c2p(0,0), end=axes0.c2p(10/3, 10), color=BLUE).set_z_index(6)
        gen2 = Line(start=axes0.c2p(0,0), end=axes0.c2p(10,0), color=BLUE).set_z_index(6)
        m_cone = Polygon(axes0.c2p(0,0), axes0.c2p(10,0), axes0.c2p(10,10), axes0.c2p(10/3, 10), stroke_opacity=0, fill_opacity=0.5, fill_color=BLUE)
        t_m_cone = Tex(r"$\mathcal{M}$", font_size=35).move_to(axes0.c2p(1.5,7))
        gen1_trunc = Line(start=axes0.c2p(0, 0), end=axes0.c2p(9/4,3*9/4), color=BLUE).set_z_index(6)
        gen2_trunc = Line(start=axes0.c2p(0, 0), end=axes0.c2p(9, 0), color=BLUE).set_z_index(6)
        m_cone_trunc = Polygon(axes0.c2p(0,0), axes0.c2p(9/4,3*9/4), axes0.c2p(9, 0), stroke_opacity=0, fill_opacity=0.5, fill_color=BLUE)

        text1 = MathTex(r"\omega(\vec{x})=", font_size=40).to_edge(RIGHT, buff=4).shift(UP*2)
        text2 = MathTex(r"\sum_{\vec{n}\in\mathcal{M}} c(\vec{n})\vec{x}^{\vec{n}}", font_size=40).next_to(text1, RIGHT, buff=0.1)
        text3 = MathTex(r"c((0,0))", font_size=40).next_to(text1, RIGHT, buff=0.1).shift(DOWN*0)
        text4 = MathTex(r"+\ c((1,0))\ x_1", font_size=40).next_to(text1, RIGHT, buff=0.1).shift(DOWN*0.7)
        text5 = MathTex(r"+\ c((2,0))\ x_1^2", font_size=40).next_to(text1, RIGHT, buff=0.1).shift(DOWN*0.7*2)
        text6 = MathTex(r"+\ c((1,1))\ x_1x_2", font_size=40).next_to(text1, RIGHT, buff=0.1).shift(DOWN*0.7*3)
        text7 = MathTex(r"+\ \cdots", font_size=40).next_to(text1, RIGHT, buff=0.1).shift(DOWN*0.7*4)

        text8 = Tex(r"Need to truncate to do computations.", font_size=30, tex_environment="flushleft").to_edge(RIGHT, buff=0.5).shift(DOWN*2)
        text9 = Tex(r"Now we're working with polynomials.", font_size=30, tex_environment="flushleft").next_to(text8, DOWN, buff=0.5)

        self.play(Create(axes0), Write(plot_labels0), Write(t_m_cone), Create(gen1), Create(gen2), FadeIn(m_cone),
                 AnimationGroup(*[Create(d) for d in dots_eff], lag_ratio=0.05, run_time=1))
        self.wait(0.1)
        self.next_slide()
        self.play(Write(text1), Write(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(text2), run_time=0.5)
        self.play(dots_eff[0].animate.set_color(PURE_RED), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[0].animate.set_color(WHITE), ReplacementTransform(dots_eff[0].copy(), text3))
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[1].animate.set_color(PURE_RED), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[1].animate.set_color(WHITE), ReplacementTransform(dots_eff[1].copy(), text4))
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[2].animate.set_color(PURE_RED), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[2].animate.set_color(WHITE), ReplacementTransform(dots_eff[2].copy(), text5))
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[3].animate.set_color(PURE_RED), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(dots_eff[3].animate.set_color(WHITE), ReplacementTransform(dots_eff[3].copy(), text6))
        self.wait(0.1)
        self.next_slide()
        self.play(*[d.animate.set_color(PURE_RED) for d in dots_eff[4:]])
        self.play(*[d.animate.set_color(WHITE) for d in dots_eff[4:]], ReplacementTransform(VGroup(*[d.copy() for d in dots_eff[4:]]), text7))
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(gen1, gen1_trunc), ReplacementTransform(gen2, gen2_trunc), ReplacementTransform(m_cone, m_cone_trunc),
                 *[FadeOut(o) for o in dots_eff[40:]], FadeIn(text8))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text9))
        self.wait(0.1)
        self.next_slide()
        self.play(*[Uncreate(o) for o in dots_eff[:40]+[gen1_trunc, gen2_trunc, m_cone_trunc, axes0]], *[FadeOut(o) for o in [text1, text3, text4, text5, text6, text7, text8, text9, plot_labels0, t_m_cone]], run_time=0.5)
        
        text1 = Tex(r"The whole problem boils down to efficiently manipulating polynomials.", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*1.5)
        text2 = Tex(r"What makes it hard?", font_size=40, tex_environment="flushleft").next_to(text1, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        blist = BulletedList(
            r"Many terms ($> 10^6$)",
            r"Many variables ($> 10^2$)",
            r"Huge coefficients ($> 10^{100}$), requires multiprecision floats or rationals\\with abitrary-precision integers",
            font_size=35, buff=0.4
        ).next_to(text2, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        text3 = Tex(r"I couldn't find any existing software that could handle these requirements.", font_size=40, tex_environment="flushleft").next_to(blist, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)

        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[0]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[2]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [text1, text2, blist, text3, title, subtitle]])
        
class Slide5(Slide):
    def construct(self):
        title = Tex(r"The difficulty of polynomial operations", font_size=50).to_edge(UP, buff=0.5)

        text1 = Tex(r"Operation", font_size=40, tex_environment="flushleft").to_edge(LEFT, buff=3).shift(UP*2)
        text2 = Tex(r"Difficulty", font_size=40, tex_environment="flushleft").to_edge(RIGHT, buff=3).shift(UP*2)
        text3 = MathTex(r"p(\vec{x})+q(\vec{x}),\ p(\vec{x})-q(\vec{x}),\ p(\vec{x})\cdot s", font_size=40).next_to(text1, DOWN, buff=0.5)
        text4 = MathTex(r"p(\vec{x})\cdot q(\vec{x})", font_size=40).next_to(text3, DOWN, buff=0.5)
        text5 = MathTex(r"p(\vec{x})^n", font_size=40).next_to(text4, DOWN, buff=0.5)
        text6 = MathTex(r"e^{p(\vec{x})},\ p(\vec{x})^{-1},\ \text{Li}_2(p(\vec{x}))", font_size=40).next_to(text5, DOWN, buff=0.5)

        e1 = EmojiImageMobject("😊").scale_to_fit_height(text3.height*1.5).next_to(text3).to_edge(RIGHT, buff=3.5)
        e2 = EmojiImageMobject("😨").scale_to_fit_height(text3.height*1.5).next_to(text4).to_edge(RIGHT, buff=3.5)
        e3 = EmojiImageMobject("😭").scale_to_fit_height(text3.height*1.5).next_to(text5).to_edge(RIGHT, buff=3.5)
        e4 = EmojiImageMobject("💀").scale_to_fit_height(text3.height*1.5).next_to(text6).to_edge(RIGHT, buff=3.5)

        text7 = Tex(r"Everything relies on efficient polynomial multiplication.", font_size=40).to_edge(DOWN, buff=0.5)

        self.play(Write(title))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text1), FadeIn(text2), run_time=0.5)
        self.play(FadeIn(text3), FadeIn(e1), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text4), FadeIn(e2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text5), FadeIn(e3))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text6), FadeIn(e4))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text7))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title, text1, text2, text3, text4, text5, text6, e1, e2, e3, e4, text7]], run_time=0.5)

        title = Tex(r"My approach", font_size=50).to_edge(UP, buff=0.5)

        text1 = Tex(r"Construct auxiliary list $\mathfrak{L}$ with all $\vec{n}$, i.e. representing all possible monomials.\\Improves memory efficiency.", font_size=35, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*1.5)
        text2 = Tex(r"Construct auxiliary hash map $\mathfrak{M}$ that maps $\vec{n}$ to its index in $\mathfrak{L}$.\\Allows for fast multiplication of monomials.", font_size=35, tex_environment="flushleft").next_to(text1, DOWN, buff=1).to_edge(LEFT, buff=0.5)
        text3 = Tex(r"Polynomials are represented as a struct with a hash map that maps the index\\of nonzero coefficients to their value, and a sorted list of nonzero coefficient\\indices (redundant, but helps for faster multiplication).", font_size=35, tex_environment="flushleft").next_to(text2, DOWN, buff=1).to_edge(LEFT, buff=0.5)

        self.play(FadeIn(title))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title, text1, text2, text3]], run_time=0.5)

class Slide6(Slide):
    def construct(self):
        title = Tex(r"Making the code public", font_size=50).to_edge(UP, buff=0.5)

        text0 = Tex(r"The only existing software to perform this computation was a mathematica\\package written by Klemm and Kreuzer.", font_size=35, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*2)
        text1 = Tex(r"During my PhD, I wrote C++ code for this, but it has remained closed-source.", font_size=35, tex_environment="flushleft").next_to(text0, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text2 = Tex(r"In my free time, I have been rewriting it in Rust (with Python bindings) as a\\learning exercise.", font_size=35, tex_environment="flushleft").next_to(text1, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text3 = Tex(r"I also put into practice the many things I've learned from Henry and others.", font_size=35, tex_environment="flushleft").next_to(text2, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text4 = Tex(r"It's now available at https://github.com/ariostas/cygv.", font_size=35, tex_environment="flushleft").next_to(text3, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        text5 = Tex(r"Still a lot of cleanup and improvements to be done, but it works pretty well.", font_size=35, tex_environment="flushleft").next_to(text4, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)

        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text0))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text4))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text5))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title, text0, text1, text2, text3, text4, text5]], run_time=0.5)
    
class Slide7(Slide):
    def construct(self):
        title = Tex(r"{{Performance comparison at}} $d=2$", font_size=50).to_edge(UP, buff=0.5)

        axes1 = Axes(
            x_range=[0, 200, 50],
            y_range=[-3, 5, 1],
            x_length=9,
            y_length=5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN, "numbers_to_include": range(0, 201, 50)},
            y_axis_config={"numbers_to_include": range(-6, 11, 2), "numbers_to_exclude": [], "exclude_origin_tick": False, "scaling": LogBase()},
            tips=False,
        ).shift(DOWN*0.2)
        y_label1 = axes1.get_y_axis_label(Tex("Time (s)").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.4)
        x_label1 = axes1.get_x_axis_label(Tex("Degree"), edge=DOWN, direction=DOWN, buff=0.4)
        plot_labels1 = VGroup(x_label1, y_label1)
        with open("data/timings_rust.txt", "r") as f:
            gv_timings_rust = np.array([eval(l) for l in f.readlines()])
        with open("data/timings_cpp.txt", "r") as f:
            gv_timings_cpp = np.array([eval(l) for l in f.readlines()])
        with open("data/timings_inst_klemm.txt", "r") as f:
            gv_timings_k = np.array([eval(l) for l in f.readlines()])
        with open("data/timings_inst_klemm_kreuzer.txt", "r") as f:
            gv_timings_kk = np.array([eval(l) for l in f.readlines()])
        plot1 = axes1.plot_line_graph(x_values=gv_timings_k[:,0], y_values=gv_timings_k[:,1], line_color=BLUE, add_vertex_dots=False)
        plot2 = axes1.plot_line_graph(x_values=gv_timings_kk[:,0], y_values=gv_timings_kk[:,1], line_color=ORANGE, add_vertex_dots=False)
        plot3 = axes1.plot_line_graph(x_values=gv_timings_cpp[:,0], y_values=gv_timings_cpp[:,1], line_color=PURE_GREEN, add_vertex_dots=False)
        plot4 = axes1.plot_line_graph(x_values=gv_timings_rust[:,0], y_values=gv_timings_rust[:,1], line_color=YELLOW, add_vertex_dots=False)
        t_plot1 = Tex(r"Klemm", color=BLUE, font_size=40).move_to(axes1.c2p(25, 1e5))
        t_plot2 = Tex(r"Klemm+Kreuzer", color=ORANGE, font_size=40).move_to(axes1.c2p(70, 1e4))
        t_plot3 = Tex(r"C++ code", color=PURE_GREEN, font_size=40).move_to(axes1.c2p(150, 5e4))
        t_plot4 = Tex(r"Rust code", color=YELLOW, font_size=40).move_to(axes1.c2p(200, 1e3))

        self.play(Write(title), Create(axes1), Write(plot_labels1))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(plot1), Write(t_plot1))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(plot2), Write(t_plot2))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(plot3), Write(t_plot3))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(plot4), Write(t_plot4))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [plot1, plot2, plot3, plot4, t_plot1, t_plot2, t_plot3, t_plot4]], run_time=0.5)
        
        axes2 = Axes(
            x_range=[0, 200, 50],
            y_range=[0, 200, 50],
            x_length=5.5,
            y_length=5.5,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            tips=False,
        ).shift(DOWN*0.3).to_edge(LEFT, buff=1.5).set_z_index(5)
        y_label2 = axes2.get_y_axis_label(Tex(r"$x_2$").rotate(PI/2), edge=LEFT, direction=LEFT, buff=0.2)
        x_label2 = axes2.get_x_axis_label(Tex(r"$x_1$"), edge=RIGHT, direction=DOWN, buff=0.2).shift(RIGHT*0.5)
        plot_labels2 = VGroup(x_label2, y_label2)
        pts_comp = []
        with open("data/11169_output_200.txt", "r") as f:
            for l in f.readlines():
                dd = eval(l)
                pts_comp.append(list(dd[0]))
        pts_comp.sort(key=lambda p: (p[0]+p[1],p[1],p[0]))
        pts_new = [pt for pt in pts_comp if pt[0]+pt[1]>30]
        pts_klemm = [pt for pt in pts_comp if pt[0]+pt[1]<=24]
        pts_klemmkreuzer = [pt for pt in pts_comp if 24<pt[0]+pt[1]<=30]
        dots_new = [Dot(point=axes2.c2p(*pt), color=PURE_GREEN, radius=0.01) for pt in pts_new]
        dots_kk = [Dot(point=axes2.c2p(*pt), color=ORANGE, radius=0.01) for pt in pts_klemmkreuzer]
        dots_k = [Dot(point=axes2.c2p(*pt), color=BLUE, radius=0.01) for pt in pts_klemm]
        with open("data/large_gv.txt", "r") as f:
            large_gv_str = f.read()
        large_gv = Tex(large_gv_str, font_size=20).to_edge(RIGHT, buff=1).shift(UP*1.2)
        gv_arrow = Arrow(start=large_gv.get_center()+UP*(large_gv.height/2-0.2)+LEFT*large_gv.width/2, end=axes2.c2p(43,157))
        t_k = Tex(r"Klemm", color=BLUE, font_size=40).to_edge(RIGHT, buff=2.5).to_edge(DOWN, buff=1)
        t_kk = Tex(r"Klemm+Kreuzer", color=ORANGE, font_size=40).next_to(t_k, UP, buff=0.7)
        t_new = Tex(r"C++/Rust code", color=PURE_GREEN, font_size=40).next_to(t_kk, UP, buff=0.7)

        self.play(ReplacementTransform(axes1, axes2), ReplacementTransform(plot_labels1, plot_labels2), run_time=0.5)
        self.play(AnimationGroup(*[Create(d) for d in dots_k], lag_ratio=0.05, run_time=1), Write(t_k))
        self.wait(0.1)
        self.next_slide()
        self.play(AnimationGroup(*[Create(d) for d in dots_kk], lag_ratio=0.05, run_time=1), Write(t_kk))
        self.wait(0.1)
        self.next_slide()
        self.play(AnimationGroup(*[Create(d) for d in dots_new], lag_ratio=0.05, run_time=1), Write(t_new))
        self.wait(0.1)
        self.next_slide()
        self.play(Write(large_gv), Create(gv_arrow))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [axes2,plot_labels2, t_k, t_kk, t_new,large_gv,gv_arrow]+dots_k+dots_kk+dots_new], run_time=0.5)

        title_new = Tex(r"{{Performance comparison at}} $d=101$", font_size=50).to_edge(UP, buff=0.5)

        text1 = Tex(r"Klemm + Kreuzer:", font_size=35, tex_environment="flushleft").to_edge(LEFT, buff=0.5).shift(UP*1.5)
        text2 = Tex(r"Can't do anything.", font_size=35, tex_environment="flushleft").next_to(text1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        text3 = Tex(r"New code:", font_size=35, tex_environment="flushleft").next_to(text2, DOWN, buff=1.5).to_edge(LEFT, buff=0.5)
        text4 = Tex(r"Have tried using up to 360,378,676 terms, finding 2,500 nonzero GV invariants.", font_size=35, tex_environment="flushleft").next_to(text3, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        text5 = Tex(r"(Partially) beats even recent efforts by mathematicians to compute these invariants with new techniques.", font_size=35, tex_environment="flushleft").next_to(text4, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        self.play(TransformMatchingTex(title, title_new), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text1))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text2))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text3))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text4))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(text5))
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title_new, text1, text2, text3, text4, text5]], run_time=0.5)

class Slide8(Slide):
    def construct(self):
        title = Tex(r"Summary and conclusions", font_size=50).to_edge(UP, buff=0.5)

        blist = BulletedList(
            r"Mirror Symmetry is a powerful computational tool.",
            r"There is a lack of computational software for string theory.",
            r"The basics of computing GV invariants is easy to understand, but hard to\\make efficient.\\(I would be curious to hear if you have suggestions.)",
            r"Rust is cool.",
            r"Big numbers are cool.",
            font_size=35, buff=0.4
        ).next_to(title, DOWN, buff=1.5).to_edge(LEFT, buff=1)

        thank_you = Tex(r"Thank you!", font_size=60)

        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[0]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[1]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[2]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[3]))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeIn(blist.submobjects[4]))
        self.wait(0.1)
        self.next_slide()
        self.play(ReplacementTransform(VGroup(title, blist), thank_you))
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(thank_you), run_time=0.5)

class Slide9(Slide):
    def construct(self):
        backup = Tex(r"Backup slides", font_size=60)

        title = Tex(r"Toy example", font_size=50).to_edge(UP, buff=0.5)
        
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{blkarray}")
        text1 = MathTex(
        r"""
\mathfrak{L}=\begin{blockarray}{ccc}
& x_0 & x_1 \\
\begin{block}{c(cc)}
  0 & 0 & 0 \\
  1 & 0 & 1 \\
  2 & 1 & 0 \\
  3 & 0 & 2 \\
  4 & 1 & 1 \\
  5 & 2 & 0\\
\end{block}
\end{blockarray}
        """, tex_template=myTemplate, font_size=40).shift(UP*1.).to_edge(LEFT, buff=2)

        text2 = MathTex(
        r"""
\mathfrak{M}=\begin{Bmatrix}
    (0,0) \rightarrow 0\\
    (0,1) \rightarrow 1\\
    (1,0) \rightarrow 2\\
    (0,2) \rightarrow 3\\
    (1,1) \rightarrow 4\\
    (2,0) \rightarrow 5\\
\end{Bmatrix}
        """, font_size=40).shift(UP*1.).to_edge(RIGHT, buff=2)

        text3 = MathTex(r"p(\vec{x})=2x_2+4x_1x_2\equiv\{3\rightarrow 2,\ 4\rightarrow 4\}", font_size=40).to_edge(LEFT, buff=1.5).shift(DOWN*1.5)
        text4 = MathTex(r"q(\vec{x})=3+x_1+3x_2^2\equiv\{0\rightarrow 3,\ 2\rightarrow 1,\ 3\rightarrow 3\}", font_size=40).next_to(text3, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)
        text5 = MathTex(r"p(\vec{x})\cdot q(\vec{x})=6x_2+14x_1x_2\equiv\{1\rightarrow 6,\ 4\rightarrow 14\}", font_size=40).next_to(text4, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(backup), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(backup), run_time=0.5)
        self.play(*[FadeIn(o) for o in [title, text1, text2, text3, text4, text5]], run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(*[FadeOut(o) for o in [title, text1, text2, text3, text4, text5]])

class CombinedSlides(Slide):
    def construct(self):
        slideClasses = [Slide1, Slide2, Slide3, Slide4, Slide5, Slide6, Slide7, Slide8, Slide9]
        for sc in slideClasses:
            sc.construct(self)