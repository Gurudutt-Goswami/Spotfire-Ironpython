#these are neccessary imports required to show messagebox
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox, MessageBoxButtons
from System.Windows.Forms import DialogResult

import clr 
clr.AddReference("Microsoft.Office.Interop.Outlook")
emailid=Document.Properties["EmailId"];
mailsub=Document.Properties["MailSubject"];
MailContent=Document.Properties["MailContent"];

from System.Runtime.InteropServices import Marshal
mail= Marshal.GetActiveObject("Outlook.Application").CreateItem(0)
mail.Recipients.Add(emailid)
mail.Subject = mailsub
mail.Body = MailContent
joker=mail.Send();
#print joker
if(joker==True):
	MessageBox.Show("Your message sent Successfully!");