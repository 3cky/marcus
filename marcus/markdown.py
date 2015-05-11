import re
import mistune

class MarcusRenderer(mistune.Renderer):
    def image(self, src, title, text):
        """Rendering a image with title and text

        :param src: source link of the image with optional dimensions qualifier in format ' =<width>x[height]'.
        :param title: title text of the image.
        :param text: alt text of the image.
        """
        if src.startswith('javascript:'):
            src = ''
        dimensions = ''
        if ' ' in src:
            src, ext = src.split(' ', 1)
            size = re.search(r"=(?P<width>\d+)x(?P<height>\d*)", ext)
            if size:
                dimensions = ' width="%d"' % int(size.group('width'))
                if size.group('height'):
                    dimensions += ' height="%d"' % int(size.group('height'))
        text = mistune.escape(text, quote=True)
        if title:
            title = mistune.escape(title, quote=True)
            html = '<img src="%s" alt="%s" title="%s"%s' % (src, text, title, dimensions)
        else:
            html = '<img src="%s" alt="%s"%s' % (src, text, dimensions)
        if self.options.get('use_xhtml'):
            return '%s />' % html
        return '%s>' % html

def render(value, renderer=MarcusRenderer()):
    md = mistune.Markdown(renderer=renderer)
    return md.render(value)
