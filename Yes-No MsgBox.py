import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox, MessageBoxButtons
from System.Windows.Forms import DialogResult

#MessageBox.Show("The answer is YES")
dialogResult = MessageBox.Show("Some question", "Some Title", MessageBoxButtons.YesNo)
if(dialogResult == DialogResult.Yes):
	MessageBox.Show("The answer is YES")
else:
	MessageBox.Show("The answer is NO")