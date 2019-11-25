from appJar import gui
VERSION="0.1"
SIZE="500x500"

app = gui("Trading Bot V"+VERSION, SIZE)

app.startFrame("TOP", row=0, column=0)
app.addLabel("TOP")
app.setLabelBg("TOP", "green")
app.stopFrame()

app.startFrame("BOTTOM", row=1, column=0)
app.addLabel("BOTTOM")
app.setLabelBg("BOTTOM", "blue")
app.stopFrame()

app.go()