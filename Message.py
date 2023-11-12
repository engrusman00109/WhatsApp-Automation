import pywhatkit

# Send a WhatsApp Message to a Contact at 8:35 PM
pywhatkit.sendwhatmsg("+923126857109", "Hello I am Usman Akram", 20, 35)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+923126857109", "Hello I am Usman Akram", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("Friends group", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+923126857109", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("Friends group", "Hey All!  I am Usman Akram", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("Friends group", "Hey All !I am Usman Akram")

# Play a Video on YouTube
#pywhatkit.playonyt("PyWhatKit")