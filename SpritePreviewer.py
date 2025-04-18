import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# GitHub repository url: https://github.com/University-of-Utah-CS3505/a8-sprite-previewer-Luke_Bode
# There's some warnings about converting float to int and how it-
# might be removed in future pycharm updates, but who cares

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)
        self.fps_amount = 1
        self.current_frame_num = 0

        self.setupUI()


    def setupUI(self):

        # menu stuff
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')

        pause_action = QAction('&Pause', self)
        pause_action.triggered.connect(self.pause)
        file_menu.addAction(pause_action)

        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        file_menu.addAction(exit_action)

        frame = QFrame()
        # main image
        self.image = QLabel()
        self.image.setPixmap(self.frames[self.current_frame_num])
        self.image.setFixedSize(50,50)

        # fps slider
        self.fps_slider = QSlider()
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(100)
        self.fps_slider.setFixedHeight(200)
        self.fps_slider.setFixedWidth(30)
        self.fps_slider.setTickInterval(20)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)

        # fps label, words and number
        self.fps_label_words = QLabel("Frames per second")
        self.fps_label_words.setFixedWidth(100)
        self.fps_label_words.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.fps_label_number = QLabel("1")
        self.fps_label_number.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # start/stop button
        self.animate_button = QPushButton("Start")
        self.animate_button.setFixedWidth(200)
        self.animate_button.clicked.connect(self.animate)

        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)
        self.timer.setInterval(1000/self.fps_amount)

        # main image and fps slider frame and layout
        secondary_frame = QFrame()
        secondary_frame_layout = QHBoxLayout()
        secondary_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        secondary_frame_layout.setSpacing(50)
        secondary_frame_layout.addWidget(self.image)
        secondary_frame_layout.addWidget(self.fps_slider)
        secondary_frame.setLayout(secondary_frame_layout)

        # fps words and number frame and layout
        fps_frame = QFrame()
        fps_frame_layout = QHBoxLayout()
        fps_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fps_frame_layout.addWidget(self.fps_label_words)
        fps_frame_layout.addWidget(self.fps_label_number)
        fps_frame.setLayout(fps_frame_layout)

        # main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(secondary_frame)
        main_layout.addWidget(fps_frame)
        main_layout.addWidget(self.animate_button)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        self.fps_slider.valueChanged.connect(self.update_fps)

    def update_fps(self, fps_value):
        self.fps_amount = fps_value
        self.fps_label_number.setNum(self.fps_amount)
        self.timer.setInterval(1000/self.fps_amount)

    def animate(self):
        if self.animate_button.text() == "Start":
            self.timer.start()
            self.animate_button.setText("Stop")
        elif self.animate_button.text() == "Stop":
            self.timer.stop()
            self.animate_button.setText("Start")
        else:
            print("button state error")

    def next_frame(self):
        self.current_frame_num += 1
        if self.current_frame_num >= len(self.frames):
            self.current_frame_num = 0
        self.image.setPixmap(self.frames[self.current_frame_num])

    def pause(self):
        self.timer.stop()
        self.animate_button.setText("Start")

    def quit_program(self):
        QApplication.quit()



def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
