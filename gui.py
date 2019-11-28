from appJar import gui
VERSION="0.1"
SIZE="500x500"

app = gui("Trading Bot V"+VERSION, SIZE)

app.startFrameStack("MAIN")

app.startTabbedFrame("DB-PS")
app.startTab("Dashboard")
app.setTabbedFrameTabExpand("DB-PS", expand=True)
app.addLabel("TEST2","TEST2LABEL")
app.stopTab()

app.startTab("Pick Strategies")
app.addLabel("TEST3","TEST3LABEL")
app.stopTab()
app.stopTabbedFrame()

# app.startFrame("BOTTOM", row=1, column=0)
# app.addLabel("BOTTOM")
# app.setLabelBg("BOTTOM", "blue")
# app.stopFrame()
app.stopFrameStack()

app.go()

