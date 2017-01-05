# smile_more
How much do you smile when you work? How about your posture?
Using Google API and OpenCV, this program will check it for you and show you information.
If you get too close to your monitor (turtleneck), it will beep.

![image](https://cloud.githubusercontent.com/assets/901975/21677274/79aed7fc-d374-11e6-9a08-25456b3af3df.png)

## Run
```bsh
python main.py
```

## Output example
```bsh
('Distance: ', 28.0, 'Joy: ', 75, 'Anger: ', 0)
('Distance avg: ', 28.0, 'Joy avg: ', 75, 'Anger avg: ', 0) count:  1

Cannot find your face!

('Distance: ', 21.0, 'Joy: ', 0, 'Anger: ', 0)
('Distance avg: ', 68.66666666666667, 'Joy avg: ', 25, 'Anger avg: ', 0) count:  3

Too close! (with beep)
```

## Example output (need to be improved)
## Requirements
- Webcam
- OpenCV
- apscheduler
- Google API (key)

## TODO
- Improve output (icon and/or status icon update)
- More classification (facial expression and posture detection)

## Contributions
We always welcome your contributions, PRs.
