import math

from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# GitHub repository name: a8-sprite-previewer-Luke_Bode

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

        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        #current_frame = 0
        self.current_image = QLabel()
        #current_image.setPixmap(self.frames[current_frame])

        self.fps_slider = QSlider()
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(100)
        self.fps_slider.setFixedHeight(200)
        self.fps_slider.setFixedWidth(30)
        self.fps_slider.setTickInterval(20)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)

        self.fps_label_words = QLabel("Frames per second")
        self.fps_label_words.setFixedWidth(100)
        self.fps_label_words.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.fps_label_number = QLabel("1")
        self.fps_label_number.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.animate_button = QPushButton("Start")
        self.animate_button.setFixedWidth(300)
        self.animate_button.clicked.connect(self.animate)


        secondary_frame = QFrame()
        secondary_frame_layout = QHBoxLayout()
        secondary_frame_layout.addWidget(self.current_image)
        secondary_frame_layout.addWidget(self.fps_slider)
        secondary_frame.setLayout(secondary_frame_layout)

        fps_frame = QFrame()
        fps_frame_layout = QHBoxLayout()
        fps_frame_layout.addWidget(self.fps_label_words)
        fps_frame_layout.addWidget(self.fps_label_number)
        fps_frame.setLayout(fps_frame_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(secondary_frame)
        main_layout.addWidget(fps_frame)
        main_layout.addWidget(self.animate_button)
        #main_layout.setContentsMargins(20, 20, 320, 320)
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        self.fps_slider.valueChanged.connect(self.update_fps)

    def update_fps(self, fps_value):
        self.fps_amount = fps_value
        print(self.fps_amount)
        self.fps_label_number.setNum(self.fps_amount)

    def animate(self):
        if self.animate_button.text() == "Start":
            # start timer
            self.animate_button.setText("Stop")
        if self.animate_button.text() == "Stop":
            # stop timer
            self.animate_button.setText("Start")

    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
