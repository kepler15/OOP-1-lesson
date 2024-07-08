class Time:
    def __init__(self, hour, minute, second):
        if not (0 <= hour <= 23):
            raise ValueError("soat 0 bilan 23 orasida bo'lishi kerak")
        if not (0 <= minute <= 59):
            raise ValueError("minut 0 bilan 59 orasida bo'lishi kerak")
        if not (0 <= second <= 59):
            raise ValueError("sekund 0 bilan 59 orasida bo'lishi kerak")
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def set_hour(self, hour):
        if not (0 <= hour <= 23):
            raise ValueError("soat 0 bilan 23 orasida bo'lishi kerak")
        self.hour = hour

    def set_minute(self, minute):
        if not (0 <= minute <= 59):
            raise ValueError("minut 0 bilan 59 orasida bo'lishi kerak")
        self.minute = minute

    def set_second(self, second):
        if not (0 <= second <= 59):
            raise ValueError("sekund 0 bilan 59 orasida bo'lishi kerak")
        self.second = second

    def set_time(self, hour, minute, second):
        if not (0 <= hour <= 23):
            raise ValueError("soat 0 bilan 23 orasida bo'lishi kerak")
        if not (0 <= minute <= 59):
            raise ValueError("minut 0 bilan 59 orasida bo'lishi kerak")
        if not (0 <= second <= 59):
            raise ValueError("sekund 0 bilan 59 orasida bo'lishi kerak")
        self.hour = hour
        self.minute = minute
        self.second = second
        

    def to_string(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def next_second(self):
        if self.second == 59:
            self.second = 0
            if self.minute == 59:
                self.minute = 0
                self.hour = (self.hour + 1) % 24
            else:
                self.minute += 1
        else:
            self.second += 1
        return self

    def previous_second(self):
        if self.second == 0:
            self.second = 59
            if self.minute == 0:
                self.minute = 59
                self.hour = (self.hour - 1) % 24
            else:
                self.minute -= 1
        else:
            self.second -= 1
        return self
    
try:
    soat = int(input("Soat kiriting: "))
    min = int(input("Minut kiriting: "))
    sek = int(input("Sekund kiriting: "))
    time1 = Time(23, 59, 59)
    time1.set_time(soat, min, sek)
    print(time1.to_string())
except ValueError as e:
    print(f"Hato: {e}")
    


# ishlatib korish uchun misollar



# try:
#     time1 = Time(23, 59, 59)
#     print("Boshlang'ich vaqt:", time1.to_string()) 
#     time1.next_second()
#     print("Keyingi soniya:", time1.to_string())  

#     time2 = Time(0, 0, 0)
#     print("Boshlang'ich vaqt:", time2.to_string())  
#     time2.previous_second()
#     print("Oldingi soniya:", time2.to_string())  

# except ValueError as e:
#     print(e)
