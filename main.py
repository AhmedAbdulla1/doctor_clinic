import random
from queue import Queue


class Doctor:
    def __init__(self, time):
        self.time = time
        self.exist_patient = False
        self.time_remaining = 0

    def isFree(self):
        return not self.exist_patient

    def start(self, nextPatient):
        patient_time = nextPatient.getPatientAge() / self.time
        self.time_remaining = patient_time
        self.exist_patient = True

    def tick(self):
        if self.exist_patient:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining == 0:
                self.exist_patient = False
        return


class Patient:
    def __init__(self, buildTime):
        self.buildTime = buildTime
        self.patientAge = random.randrange(20, 61)

    def getBuildTime(self):
        return self.buildTime

    def getPatientAge(self):
        return self.patientAge

    def waitingTime(self, currentTime):
        return currentTime - self.buildTime


def simulation(numOfMinutes, patientTime):
    doctor = Doctor(patientTime)
    patient_queue = Queue()
    waiting_list_times = []
    for currentTime in range(numOfMinutes):
        if random.randrange(1, 25) == 24:
            patient = Patient(currentTime)
            patient_queue.put(patient)
        if doctor.isFree() and not patient_queue.empty():
            next_patient = patient_queue.get()
            waiting_list_times.append(next_patient.waitingTime(currentTime))
            doctor.start(next_patient)
        doctor.tick()
    average_wait = sum(waiting_list_times) / len(waiting_list_times)
    print("Average Wait ", average_wait, " secs", patient_queue.qsize(), " tasks remaining.")


# start this program
for i in range(10):
    simulation(240, 5)
print("finished")
