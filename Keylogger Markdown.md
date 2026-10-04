Hi. This is **Rishabh Dev Malhotra** from **CSDA** branch; and my first project at EHAX is "**Keylogger**".



After the reading the project description, I marked out what my main aim is and what extra features should I go for.

I need to-: 1) Record keyboard input with timestamps

&#x20;           2) Also translate special characters to \[SPACE], \[SHIFT] etc.

&#x20;           3) A sequence to stop recording input

&#x20;           4) Display total keystrokes and active runtime

&#x20;           5) Calculate WPM and error rates

&#x20;           6) Display frequency table for top-5 most used keys



I decided to use **Python** since I am more comfortable with it.



\***Note**-: Following text is me coding and yapping side by side so please excuse the unnecessary stuff I may write or if I miss something to mention.



**Day 1:**



After shortlisting my targets, I first installed pynput library and then checked the commands it offered. I imported the keyboard functions into my code since that is what I am gonna use. With the help of AI, I found out what commands help me to do what and how to use them. The function keyboard.Listener() is the way to track the keyboard inputs. My plan is to track the keys and and get them inside the file keystrokes.log, ignoring the timestamps for the time being. The first that problem arose was how to deal with special characters like "!", ",", "''" etc. I was using isalnum() to sort alphanumeric characters and Space, Shift type characters but it fails due to them. So I used AI and found out about the function "hasattr(object , type )"    which checks the object and looks for the property mentioned in place of type in it and returns True or False. This solves my first problem.

After writing the code by myself, I got to run the code for the first time and was immediately hit by errors since I misunderstood how Listener function works. I made 'key' the parameter instead of my\_press\_function which gave me an error.
As soon as I fixed the problem and ran the code again, I found out that only one of my keyboard input was being taken and then the code just stopped on it's own thereafter. As of now, I am using Escape key as my method to stop the listening process. Turns out it was a silly error. I didn't write key==keyboard.Key.esc while checking if condition and that gave me the error.
Hence, my basic portion of the project is done where I can get my inputs to the file and then stop the listening using escape key.



**Day 2:**



It is now time to expand on the basics and add the timestamps in it and then try to implement a new finishing sequence to the program instead of escape key. I started by looking the documentation of the "time" library and soon found out the function that will help me here; localtime(). On printing it, I found it gave a tuple like thing but with time.struct\_time outside the bracket with all the necessary info that I needed for timestamps. My original idea here was to brute force slice it after converting to a string and then restructure it into my desired format before sending it in the log file. But the problem with my brute force was not only time waste, but also that days like "1" would not be written as "01" which basically fails my slicing. I could have brute forced by applying several if-else but it would have also been waste of time. My next plan was to somehow convert it into a dictionary and then use it to structure my formatted string to do the job. Before I went for this approach, I went to read more from the documentation and found that what I received from function was a "object with a named tuple interface" and index value is sufficient to retrieve what we want from it. So after that, the timestamps were done.

The next task is to count the total keystrokes and active runtime. I experimented a lot by taking a variable outside the function and then calling it in the function despite knowing it won't work the normal way. I tried to mess around with the listener.join as well for that. Finally I decided to check google for that and found out I can just declare the variable as global variable inside the function and it is sufficient enough to count the keystrokes.
Coming to active runtime, my initial plan was to take a localtime before listener statements and a localtime when I click escape(for the time being) and then subtract hours with hours, minutes with minutes etc to get the runtime. Ofc it has flaws of being negative in some quantities so I had to look for another approach. I check the documentation of time library for a function which could help and found perf\_counter() function; which is basically a stopwatch of the program. It gives me runtime in seconds upto a lot of decimals. I can modify it to a good format(HH:MM:SS) but I am lazy so I am gonna keep it in seconds upto 2 decimals(centi-second that is).



**Day 3:**



Time to finish the left over tasks. Starting off with WPM. I googled the formulae for Gross WPM, Net WPM and Backspace Error rates and then implemented them all in the code. The formattable string was giving TypeError int can't multiply with float when I was trying to not use variables for WPMs and print them directly. Ended up taking variables and that too with int version of runtime to get simple, good enough output. Then was time for hotkey sequence which I had to use ChatGPT for since I couldn't understand the simple thing from documentation alone(self-depreciation is good). Defined a function 'exc' and then used GlobalHotKeys function to finally implement the clean exit sequence. Now I had no idea how to map the top 5 used keys. So I went to GPT once more and it gave me the idea of using dictionaries. After implementation, the project is done. I was thinking of getting the last brownie point but then I got lazy which thus ended the project.

**Hence, the project was done with minimal AI, library documentations other than my brain power.** 

*(Thanks for the project though, was a good learning experience even though short. Excited for more)*

