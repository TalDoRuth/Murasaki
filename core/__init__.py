import datetime
now = datetime.datetime.now()

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        awnser = 'São {} horas e {} minutos'.format(now.hour, now.minute)
        return awnser
      