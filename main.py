# created by Nader 
#            Elkholy
#            Elabassy

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
            if self.time_remaining <= 0:  # التركاية هنا ==>
                self.exist_patient = False
        return


class Patient:
    def __init__(self, buildTime):
        self.buildTime = buildTime
        self.patientAge = random.randrange(20, 61)

    def getPatientAge(self):
        return self.patientAge

    def waitingTime(self, currentTime):
        return currentTime - self.buildTime


def simulation(numOfMinutes, patientTime):
    doctor = Doctor(patientTime)
    patient_queue = Queue()
    waiting_list_times = []
    num_of_patients = 0
    for currentTime in range(numOfMinutes):
        r = random.randrange(0, 6)
        if r == 5:
            num_of_patients = num_of_patients + 1  # number of patient
            patient = Patient(currentTime)
            patient_queue.put(patient)
        if doctor.isFree() and not patient_queue.empty():
            next_patient = patient_queue.get()
            waiting_list_times.append(next_patient.waitingTime(currentTime))
            doctor.start(next_patient)
        doctor.tick()
    print("Number of patient in this day is ", num_of_patients)
    average_wait = sum(waiting_list_times) / len(waiting_list_times)
    print("Average Wait ", average_wait, " min and ", patient_queue.qsize(), " patient remaining.")


# start this program
print("Start\nin this part patient time with doctor = (Age/5)\n")
for i in range(10):
    simulation(240, 5)  # in this part patient time with doctor = (Age/5)
    print()
print("finished this part\n")
print("In this part patient time with doctor = (Age/10)\n")
for i in range(10):
    simulation(240, 10)  # in this part patient time with doctor = (Age/10)
    print()
print("finished")
