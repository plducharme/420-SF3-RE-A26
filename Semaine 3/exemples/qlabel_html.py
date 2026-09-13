from PySide6.QtWidgets import QApplication, QLabel


class QLabelHtml(QLabel):

    def __init__(self):
        super().__init__()
        # l'attribut "style" des balises HTML permet de définir des styles CSS en ligne
        self.setText("""
        <h1 style="color:blue;">Titre principal</h1>
        <h2 style="color:green;">Sous-titre</h2>
        <p style="font-size:16px;">Ceci est un paragraphe avec du <b>texte en gras</b>, du <i>texte en italique</i>, et un 
        <a href="https://www.qt.io">lien vers Qt</a>.</p>
        <ul>
            <li>Premier élément de liste</li>
            <li>Deuxième élément de liste</li>
            <li>Troisième élément de liste</li>
        </ul>
        <ol>
            <li>Premier élément numéroté</li>
            <li>Deuxième élément numéroté</li>
            <li>Troisième élément numéroté</li>
        </ol>
        """)


app = QApplication()
html = QLabelHtml()
html.show()
app.exec()