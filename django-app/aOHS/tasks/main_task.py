from background_task import background


@background(schedule=60)
def mainTask():
    pass

