from PySide6.QtCore import QObject, Signal
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from functools import cached_property
from PySide6.QtGui import QImage

# Classe permettant de télécharger une image à partir d'une URL.

class ImageDownloader(QObject):
    # Créer un signal qui sera émis lorsqu'une image a été téléchargée.
    finished = Signal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager.finished.connect(self.handle_finished)

    # Une propriété cached est une propriété qui est calculée une seule fois et qui est ensuite mise en cache.
    # Ne pas oublier que "property" est un décorateur qui permet de définir une méthode comme une propriété.
    # Donc la méthode sera exécutée une seule fois et le résultat sera mis en cache.
    @cached_property
    def manager(self):
        return QNetworkAccessManager()

    def start_download(self, url):
        self.manager.get(QNetworkRequest(url))

    def handle_finished(self, reply):
        if reply.error() != QNetworkReply.NetworkError.NoError:
            print("error: ", reply.errorString())
            return
        image = QImage()
        image.loadFromData(reply.readAll())
        self.finished.emit(image)

