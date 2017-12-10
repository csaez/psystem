import sys
from PyQt5 import QtWidgets
import psystem


class GraphicsView(QtWidgets.QGraphicsView):
    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if delta > 0:
            self.scale(1.1, 1.1)
        else:
            self.scale(0.9, 0.9)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *arg, **kwds):
        super().__init__(*arg, **kwds)

        # setup layout
        toolbar = self.addToolBar('mainToolbar')
        action = toolbar.addAction('Simulate')
        action.triggered.connect(self.simulate)

        self._scene = QtWidgets.QGraphicsScene()
        view = GraphicsView(self._scene)
        self.setCentralWidget(view)

        self.setMinimumSize(600, 800)

        # setup particles
        self._system = psystem.System()

        e = psystem.PointEmitter()
        e.position = [0.0, 40.0]
        self._system.emitters.append(e)

        g = [0.0, -0.098]
        self._system.forces.append(g)

    def simulate(self):
        self._system.simulate()
        self.draw()

    def draw(self):
        self._scene.clear()
        for p in self._system.particles:
            self._scene.addEllipse(p.position[0], -p.position[1], 1.0, 1.0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec_()
