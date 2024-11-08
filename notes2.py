import string
import time
text = "On October 21, 1957, Queen Elizabeth II delivered a speech to the General Assembly of the United Nations to make a statement that was characterized by the Cold War and actions of decolonization. The purpose of her speech was to reassure the support of British citizens in their efforts to preserve peace and cooperation in the face of tensions on a global scale. An example of a speech that combines formal regal power with a personal idea to common human ideals is the one that is being given"

temp = ''
for ch in text:
    for i in string.printable:
      if i == ch or ch == '':
        time.sleep(0.03)
        print(temp + i)
        temp +=ch
        break
    else:
       time.sleep(0.02)
       print(temp+i)
