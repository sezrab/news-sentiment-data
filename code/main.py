import chart
import gitControl
import sentiment

while True:
    try:
        sentiment.main()
        chart.main()
        gitControl.update()
        break
    except:
        pass