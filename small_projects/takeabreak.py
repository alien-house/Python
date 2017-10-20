
import webbrowser
import time

break_count = 0
total_breaks = 3

print("This program  started on ", time.ctime())

while ( break_count  < total_breaks ):
  time.sleep(5)
  webbrowser.open("https://www.youtube.com/watch?v=enw3gQJmwuc&t=10s")
  break_count = break_count + 1






