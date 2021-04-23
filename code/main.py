import chart
import gitControl
import sentiment

while True:
    try:
        print("sentiment.main()")
        sentiment.main()
        print("chart.main()")
        chart.main()
        print("gitControl.update()")
        gitControl.update()
        break
    except Exception as e:
        print(e)
