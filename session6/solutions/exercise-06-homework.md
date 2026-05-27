# Session 6 Homework

## Capstone repository

Link: https://github.com/sotomarcos24/bda-capstone-1

## New YouTube URLs

1. https://www.youtube.com/watch?v=5hPtU8Jbpg0
2. https://www.youtube.com/watch?v=PpH_mi923_A
3. https://www.youtube.com/watch?v=zBjJUV-lzHo
4. https://www.youtube.com/watch?v=TkYElDbuvnw
5. https://www.youtube.com/watch?v=YhvLXwmCO4E

## What I changed

I created a new dowload_file_semaphore function with the dowload_limit semaphore as an argument to enable parallel downloads with a limit of 5 downloads.
I executed this in a new file called semaphore.py so it was all clear and not mixed with the pool and the serial execution.

## Semaphore design

I implemented the download_limit into a new dowload_file_semaphore function and the result_file_guard to wirte the resutls in the semaphore_results.txt file one line at a time

## Result file format

Url: https://www.youtube.com/watch?v=jNQXAC9IVRw, status: success, error: , timestamp: 2026-05-27 10:24:05
Url: https://www.youtube.com/watch?v=BB49x_uMlGA, status: success, error: , timestamp: 2026-05-27 10:24:05
Url: https://www.youtube.com/watch?v=Hm5ieMoxc4c, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=LeAltgu_pbM, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=tCDvOQI3pco, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=5hPtU8Jbpg0, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=PpH_mi923_A, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=zBjJUV-lzHo, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=TkYElDbuvnw, status: success, error: , timestamp: 2026-05-27 10:24:06
Url: https://www.youtube.com/watch?v=YhvLXwmCO4E, status: success, error: , timestamp: 2026-05-27 10:24:06

## Testing

With download_limit = threading.Semaphore(5) i set the limit to only 5 downloads at once

## Reflection

I found both equaly harder
