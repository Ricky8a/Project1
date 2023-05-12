from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys


class TVRemoteApp(QMainWindow):
    """A class that represents a simple TV remote application.

        Attributes:
            channel_images (list[str]): A list of channel images filenames.
            current_channel_index (int): An integer representing the current channel index.
            volume_level (int): An integer representing the current volume level.
            muted (bool): A boolean value indicating if the TV is muted.
            __status (bool): A private boolean value indicating if the TV is on or off.
        """

    def __init__(self):
        """Initializes the TVRemoteApp instance."""
        super(TVRemoteApp, self).__init__()
        loadUi("view.ui", self)
        self.channel_images = ["Disney.png", "Mtv.png", "Univision.png"]
        self.tvDisplay.setPixmap(QPixmap())
        self.current_channel_index = 0
        self.volume_level = 0
        self.muted = False
        self.__status = False

        self.on_offButton.clicked.connect(self.on_off_clicked)
        self.channelUp.clicked.connect(self.channel_up_clicked)
        self.channelDown.clicked.connect(self.channel_down_clicked)
        self.volumeUp.clicked.connect(self.volume_up_clicked)
        self.volumeDown.clicked.connect(self.volume_down_clicked)
        self.mute.clicked.connect(self.mute_clicked)
        self.channel0.clicked.connect(self.channel0_clicked)
        self.channel1.clicked.connect(self.channel1_clicked)
        self.channel2.clicked.connect(self.channel2_clicked)

    def on_off_clicked(self):
        """Turns the TV on or off and updates the UI accordingly."""
        if self.__status == False:
            self.__status = True
            self.tvDisplay.setEnabled(True)
            self.channelUp.setEnabled(True)
            self.channelDown.setEnabled(True)
            self.volumeUp.setEnabled(True)
            self.volumeDown.setEnabled(True)
            self.mute.setEnabled(True)
            image = QPixmap(self.channel_images[self.current_channel_index]).scaled(250, 150)
            self.tvDisplay.setPixmap(image)
            self.volumeDisplay.setText("Vol: " + str(self.volume_level))
            self.show_volume_display_for_1_seconds()
            self.channelDisplay.setText("Channel: " + str(self.current_channel_index))
            self.show_channel_display_for_1_seconds()
        else:
            self.__status = False
            self.tvDisplay.setEnabled(False)
            self.channelUp.setEnabled(False)
            self.channelDown.setEnabled(False)
            self.volumeUp.setEnabled(False)
            self.volumeDown.setEnabled(False)
            self.mute.setEnabled(False)
            self.tvDisplay.setPixmap(QPixmap())
            self.volumeDisplay.setText("")
            self.channelDisplay.setText("")

    def channel_up_clicked(self):
        """Switches to the next channel and updates the UI accordingly."""
        if self.tvDisplay.isEnabled():
            self.current_channel_index = (self.current_channel_index + 1) % len(self.channel_images)
            image = QPixmap(self.channel_images[self.current_channel_index]).scaled(250, 150)
            self.tvDisplay.setPixmap(image)
            self.channelDisplay.setText("Channel: " + str(self.current_channel_index))
            self.show_channel_display_for_1_seconds()
    def channel_down_clicked(self):
        """Switches to the previous channel and updates the UI accordingly."""
        if self.tvDisplay.isEnabled():
            self.current_channel_index = (self.current_channel_index - 1) % len(self.channel_images)
            image = QPixmap(self.channel_images[self.current_channel_index]).scaled(250, 150)
            self.tvDisplay.setPixmap(image)
            self.channelDisplay.setText("Channel: " + str(self.current_channel_index))
            self.show_channel_display_for_1_seconds()

    def volume_up_clicked(self):
        """Increase the volume level by one if the TV is enabled and not muted."""
        if self.tvDisplay.isEnabled():
            if not self.muted:
                self.volume_level = min(self.volume_level + 1, 3)
                self.volumeDisplay.setText("Vol: " + str(self.volume_level))
            else:
                self.volumeDisplay.setText("MUTE")
            self.show_volume_display_for_1_seconds()
    def volume_down_clicked(self):
        """Decrease the volume level by one if the TV is enabled and not muted."""
        if self.tvDisplay.isEnabled():
            if not self.muted:
                self.volume_level = max(self.volume_level - 1, 0)
                self.volumeDisplay.setText("Vol: " + str(self.volume_level))
            else:
                self.volumeDisplay.setText("MUTE")
            self.show_volume_display_for_1_seconds()
    def mute_clicked(self):
        """Toggle mute on/off and update the volume display accordingly if the TV is enabled."""
        if self.tvDisplay.isEnabled():
            if not self.muted:
                self.muted = True
                self.volumeDisplay.setText("MUTE")
                self.show_volume_display_for_1_seconds()
            else:
                self.muted = False
                self.volumeDisplay.setText("Vol: " + str(self.volume_level))
                self.show_volume_display_for_1_seconds()

    def show_volume_display_for_1_seconds(self):
        """Show the volume display for 1 second and then hide it."""
        self.volumeDisplay.show()
        QTimer.singleShot(1000, self.volumeDisplay.hide)

    def show_channel_display_for_1_seconds(self):
        """Show the channel display for 1 second and then hide it."""
        self.channelDisplay.show()
        QTimer.singleShot(1000, self.channelDisplay.hide)

    def channel0_clicked(self):
        """Changes the TV to channel 0 and updates the UI accordingly."""
        if self.tvDisplay.isEnabled():
            self.current_channel_index = 0
            image = QPixmap(self.channel_images[self.current_channel_index]).scaled(250, 150)
            self.tvDisplay.setPixmap(image)
            self.channelDisplay.setText("Channel: " + str(self.current_channel_index))
            self.show_channel_display_for_1_seconds()

    def channel1_clicked(self):
        """Changes the TV to channel 1 and updates the UI accordingly."""
        if self.tvDisplay.isEnabled():
            self.current_channel_index = 1
            image = QPixmap(self.channel_images[self.current_channel_index]).scaled(250, 150)
            self.tvDisplay.setPixmap(image)
            self.channelDisplay.setText("Channel: " + str(self.current_channel_index))
            self.show_channel_display_for_1_seconds()

    def channel2_clicked(self):
        """Changes the TV to channel 2 and updates the UI accordingly."""
        if self.tvDisplay.isEnabled():
            self.current_channel_index = 2
            image = QPixmap(self.channel_images[self.current_channel_index]).scaled(250, 150)
            self.tvDisplay.setPixmap(image)
            self.channelDisplay.setText("Channel: " + str(self.current_channel_index))
            self.show_channel_display_for_1_seconds()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TVRemoteApp()
    window.show()
    sys.exit(app.exec_())