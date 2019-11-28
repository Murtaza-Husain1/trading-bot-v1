from appJar import gui
VERSION="0.1"
SIZE="500x300"

def buy(btn):
	print(btn)

def sell(btn):
	print(btn)


app = gui("Trading Bot V"+VERSION, SIZE)

app.startFrameStack("MAIN")

app.startTabbedFrame("DB-PS")
app.startTab("Dashboard")
app.setTabbedFrameTabExpand("DB-PS", expand=True)

app.startPanedFrameVertical("p1")
app.addLabel("l1", "Current Position")

app.startPanedFrame("p2")
app.addLabelEntry("Price")
app.addLabelEntry("Amount")

app.startPanedFrame("p5")
app.addLabel("l7", "Open Order")
app.stopPanedFrame()

app.stopPanedFrame()

app.startPanedFrame("p3")
app.addLabel("l3", "Buy/Sell")
app.addButton("Buy", buy)
app.addButton("Sell", sell)
app.stopPanedFrame()

app.startPanedFrame("p4")
app.addLabel("l4", "BTC Ticker")

app.stopPanedFrame()

app.stopPanedFrame()
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