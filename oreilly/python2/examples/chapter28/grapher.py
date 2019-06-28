from pawt import swing, awt, colors, GridBag
RIGHT = swing.JLabel.RIGHT
APPROVE_OPTION = swing.JFileChooser.APPROVE_OPTION
import java.io
import pickle, os

default_setup = """from math import *
def squarewave(x,order):
    total = 0.0
    for i in range(1, order*2+1, 2):
        total = total + sin(x*i/10.0)/(float(i))
    return total
"""
default_expression = "squarewave(x, order=3)"

class Chart(awt.Canvas):
    color = colors.darkturquoise
    style = 'Filled'

    def getPreferredSize(self):
        return awt.Dimension(600,300)

    def paint(self, graphics):
        clip = self.bounds
        graphics.color = colors.white
        graphics.fillRect(0, 0, clip.width, clip.height)

        width = int(clip.width * .8)
        height = int(clip.height * .8)
        x_offset = int(clip.width * .1)
        y_offset = clip.height - int(clip.height * .1)

        N = len(self.data); xs = [0]*N; ys = [0]*N

        xmin, xmax = 0, N-1
        ymax = max(self.data)
        ymin = min(self.data)

        zero_y = y_offset - int(-ymin/(ymax-ymin)*height)
        zero_x = x_offset + int(-xmin/(xmax-xmin)*width)

        for i in range(N):
            xs[i] = int(float(i)*width/N) + x_offset
            ys[i] = y_offset - int((self.data[i]-ymin)/(ymax-ymin)*height)
        graphics.color = self.color
        if self.style == "Line":
            graphics.drawPolyline(xs, ys, len(xs))
        else:
            xs.insert(0, xs[0]); ys.insert(0, zero_y)
            xs.append(xs[-1]); ys.append(zero_y)
            graphics.fillPolygon(xs, ys, len(xs))

        # draw axes
        graphics.color = colors.black
        graphics.drawLine(x_offset,zero_y, x_offset+width, zero_y)
        graphics.drawLine(zero_x, y_offset, zero_x, y_offset-height)

        # draw labels
        leading = graphics.font.size
        graphics.drawString("%.3f" % xmin, x_offset, zero_y+leading)
        graphics.drawString("%.3f" % xmax, x_offset+width, zero_y+leading)
        graphics.drawString("%.3f" % ymin, zero_x-50, y_offset)
        graphics.drawString("%.3f" % ymax, zero_x-50, y_offset-height+leading)

class GUI:
    def __init__(self):
        self.numelements = 100
        self.frame = swing.JFrame(windowClosing=self.do_quit)

        # build menu bar
        menubar = swing.JMenuBar()
        file = swing.JMenu("File")
        file.add(swing.JMenuItem("Load", actionPerformed = self.do_load))
        file.add(swing.JMenuItem("Save", actionPerformed = self.do_save))
        file.add(swing.JMenuItem("Quit", actionPerformed = self.do_quit))
        menubar.add(file)
        self.frame.JMenuBar = menubar

        # create widgets
        self.chart = Chart(visible=1)
        self.execentry = swing.JTextArea(default_setup, 8, 60)
        self.evalentry = swing.JTextField(default_expression,
                                          actionPerformed = self.update)

        # create options panel
        optionsPanel = swing.JPanel(awt.FlowLayout(
            alignment=awt.FlowLayout.LEFT))

        # whether the plot is a line graph or a filled graph
        self.filled = swing.JRadioButton("Filled",
                                         actionPerformed=self.set_filled)
        optionsPanel.add(self.filled)
        self.line = swing.JRadioButton("Line",
                                       actionPerformed=self.set_line)
        optionsPanel.add(self.line)
        styleGroup = swing.ButtonGroup()
        styleGroup.add(self.filled)
        styleGroup.add(self.line)

        # color selection
        optionsPanel.add(swing.JLabel("Color:", RIGHT))
        colorlist = filter(lambda x: x[0] != '_', dir(colors))
        self.colorname = swing.JComboBox(colorlist)
        self.colorname.itemStateChanged = self.set_color
        optionsPanel.add(self.colorname)

        # number of points
        optionsPanel.add(swing.JLabel("Number of Points:", RIGHT))
        self.sizes = [50, 100, 200, 500]
        self.numpoints = swing.JComboBox(self.sizes)
        self.numpoints.selectedIndex = self.sizes.index(self.numelements)
        self.numpoints.itemStateChanged = self.set_numpoints
        optionsPanel.add(self.numpoints)

        # do the rest of the layout in a GridBag
        self.do_layout(optionsPanel)

    def do_layout(self, optionsPanel):
        bag = GridBag(self.frame.contentPane, fill='BOTH',
                      weightx=1.0, weighty=1.0)
        bag.add(swing.JLabel("Setup Code: ", RIGHT))
        bag.addRow(swing.JScrollPane(self.execentry), weighty=10.0)
        bag.add(swing.JLabel("Expression: ", RIGHT))
        bag.addRow(self.evalentry, weighty=2.0)
        bag.add(swing.JLabel("Output: ", RIGHT))
        bag.addRow(self.chart, weighty=20.0)
        bag.add(swing.JLabel("Options: ", RIGHT))
        bag.addRow(optionsPanel, weighty=2.0)
        self.update(None)  
        self.frame.visible = 1
        self.frame.size = self.frame.getPreferredSize()

        self.chooser = swing.JFileChooser()
        self.chooser.currentDirectory = java.io.File(os.getcwd())

    def do_save(self, event=None):
        self.chooser.rescanCurrentDirectory()
        returnVal = self.chooser.showSaveDialog(self.frame)
        if returnVal == APPROVE_OPTION:
            object = (self.execentry.text,  self.evalentry.text,
                      self.chart.style,
                      self.chart.color.RGB,
                      self.colorname.selectedIndex, 
                      self.numelements)
            file = open(os.path.join(self.chooser.currentDirectory.path,
                        self.chooser.selectedFile.name), 'w')
            pickle.dump(object, file)
            file.close()

    def do_load(self, event=None):
        self.chooser.rescanCurrentDirectory()    
        returnVal = self.chooser.showOpenDialog(self.frame)
        if returnVal == APPROVE_OPTION:
            file = open(os.path.join(self.chooser.currentDirectory.path,
                     self.chooser.selectedFile.name))
            (setup, each, style, color, 
             colorname, self.numelements) = pickle.load(file)
            file.close()
            self.chart.color = java.awt.Color(color)
            self.colorname.selectedIndex = colorname
            self.chart.style = style
            self.execentry.text = setup
            self.numpoints.selectedIndex = self.sizes.index(self.numelements)
            self.evalentry.text = each
            self.update(None)

    def do_quit(self, event=None): 
        import sys
        sys.exit(0)

    def set_color(self, event):
        self.chart.color = getattr(colors, event.item)
        self.chart.repaint()

    def set_numpoints(self, event):
        self.numelements = event.item
        self.update(None)

    def set_filled(self, event):
        self.chart.style = 'Filled'
        self.chart.repaint()

    def set_line(self, event):
        self.chart.style = 'Line'
        self.chart.repaint()

    def update(self, event):
        context = {}
        exec self.execentry.text in context
        each = compile(self.evalentry.text, '<input>', 'eval')
        numbers = [0]*self.numelements
        for x in xrange(self.numelements):
            context['x'] = float(x)
            numbers[x] = eval(each, context)
        self.chart.data = numbers
        if self.chart.style == 'Line':
            self.line.setSelected(1)
        else:
            self.filled.setSelected(1)
        self.chart.repaint()

GUI()
