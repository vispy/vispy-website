from sphinx.writers import html


def setup(app):
    app.set_translator('html', HTMLTranslator)


class HTMLTranslator(html.HTMLTranslator):

    # Get rid of the 'container' class
    def visit_container(self, node):
        self.body.append(self.starttag(node, 'div', CLASS=''))
