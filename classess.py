import copy
import sys
import heapq
sys.setrecursionlimit(10**7)

instructors = ["Ranjbar", "Bidoki", "Ahmadi", "Baghbani", "Mohammadi", "Asad", "Kaboudjai", "Sajjadi", "Badakhshan"]

Courses = ['Advanced Programming', 'Advanced Programming Workshop', 'Algorithm Design', 'Andishe 2', 'Automata', 'CEH', 'Computer Architecture', 'Data Mining',
    'Diff eq', 'Digtial Design lab', 'Discrete math', 'Electrical Circuit', 'Especial Content 1', 'MicroProcessors lab',
    'Network', 'Network lab', 'OS lab', 'Physic 1', 'Physic 2', 'Physic 2 lab', 'Programming Languages', 'Signals',
    'Software Engineering 2', 'Stats', 'Way of Research', 'math2']

can_teach = {
    "Ranjbar" : ["Advanced Programming Workshop", "Advanced Programming", "Programming Languages", "Data Mining", "Way of Research"],
    "Bidoki" : ["Algorithm Design", "Especial Content 1", "Way of Research", "Software Engineering 2"],
    "Ahmadi" : ["OS lab", "Network lab", "Digtial Design lab", "CEH", "Computer Architecture","Network","Discrete math"],
    "Baghbani" : ["Discrete math", "Automata"],
    "Mohammadi" : ["Signals", "Electrical Circuit", "MicroProcessors lab"],
    "Asad" : ["math2", "Discrete math", "Diff eq", "Stats"],
    "Kaboudjai" : ["Network","Automata"],
    "Sajjadi" : ["Andishe 2"],
    "Badakhshan" : ["Physic 1", "Physic 2", "Physic 2 lab"]
}

schedule = {}

instructor_free_times ={

    "Ranjbar" : ['sat - 8 to 10', 'sat - 10 to 12', 'sat - 14 to 16', 'sat - 16 to 18', 'sat - 18 to 20',
        'mon - 8 to 10', 'mon - 10 to 12', 'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20',
        'wed - 8 to 10', 'wed - 10 to 12', 'wed - 14 to 16', 'wed - 16 to 18', 'wed - 18 to 20'],

    "Bidoki" : ['mon - 8 to 10', 'mon - 10 to 12', 'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20',
        'tue - 8 to 10', 'tue - 10 to 12', 'tue - 14 to 16', 'tue - 16 to 18', 'tue - 18 to 20',
        'wed - 8 to 10', 'wed - 10 to 12', 'wed - 14 to 16', 'wed - 16 to 18', 'wed - 18 to 20'],

    "Ahmadi" : ['sat - 8 to 10', 'sat - 10 to 12', 'sat - 14 to 16', 'sat - 16 to 18', 'sat - 18 to 20',
        'sun - 8 to 10', 'sun - 10 to 12', 'sun - 14 to 16', 'sun - 16 to 18', 'sun - 18 to 20',
        'mon - 8 to 10', 'mon - 10 to 12', 'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20',
        'tue - 8 to 10', 'tue - 10 to 12', 'tue - 14 to 16', 'tue - 16 to 18', 'tue - 18 to 20'],

    "Baghbani" : ['sat - 14 to 16', 'sat - 16 to 18', 'sat - 18 to 20',
        'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20'],

    "Mohammadi" : ['sat - 14 to 16', 'sat - 16 to 18', 'sat - 18 to 20',
        'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20'],

    "Asad" : ['sun - 8 to 10', 'sun - 10 to 12', 'sun - 14 to 16', 'sun - 16 to 18', 'sun - 18 to 20',
        'tue - 8 to 10', 'tue - 10 to 12', 'tue - 14 to 16', 'tue - 16 to 18', 'tue - 18 to 20'
    ],

    "Kaboudjai" : ['mon - 8 to 10', 'mon - 10 to 12', 'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20',
        'thu - 8 to 10', 'thu - 10 to 12', 'thu - 14 to 16', 'thu - 16 to 18', 'thu - 18 to 20'],

    "Sajjadi" : ['tue - 14 to 16', 'tue - 16 to 18', 'tue - 18 to 20'
        'thu - 14 to 16', 'thu - 16 to 18', 'thu - 18 to 20'],

    "Badakhshan" : ['sun - 8 to 10', 'sun - 10 to 12', 'sun - 14 to 16', 'sun - 16 to 18', 'sun - 18 to 20',
        'wed - 8 to 10', 'wed - 10 to 12', 'wed - 14 to 16', 'wed - 16 to 18', 'wed - 18 to 20',
        'mon - 8 to 10', 'mon - 10 to 12', 'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20']
}
days = ["sat", "sun", "mon", "tue", "wed", "thu"]
class_times = ["8","10","14","16","18"]

times= ['sat - 8 to 10', 'sat - 10 to 12', 'sat - 14 to 16', 'sat - 16 to 18', 'sat - 18 to 20',
    'sun - 8 to 10', 'sun - 10 to 12', 'sun - 14 to 16', 'sun - 16 to 18', 'sun - 18 to 20',
    'mon - 8 to 10', 'mon - 10 to 12', 'mon - 14 to 16', 'mon - 16 to 18', 'mon - 18 to 20',
    'tue - 8 to 10', 'tue - 10 to 12', 'tue - 14 to 16', 'tue - 16 to 18', 'tue - 18 to 20',
    'wed - 8 to 10', 'wed - 10 to 12', 'wed - 14 to 16', 'wed - 16 to 18', 'wed - 18 to 20',
    'thu - 8 to 10', 'thu - 10 to 12', 'thu - 14 to 16', 'thu - 16 to 18', 'thu - 18 to 20']

Courses_semester = {
    'Advanced Programming': 2,
    'Advanced Programming Workshop' : 2,
    'Algorithm Design' : 4,
    'Andishe 2':2,
    'Automata':4,
    'CEH':8,
    'Computer Architecture':4,
    'Data Mining':8,
    'Diff eq':2,
    'Digtial Design lab':4,
    'Discrete math':2, 
    'Electrical Circuit':4,
    'Especial Content 1':6,
    'MicroProcessors lab':6,
    'Network':6,
    'Network lab':6,
    'OS lab':6,
    'Physic 1':2,
    'Physic 2':2,
    'Physic 2 lab':4,
    'Programming Languages':8,
    'Signals':6,
    'Software Engineering 2':6,
    'Stats':4,
    'Way of Research':6,
    'math2':2
}


def find_available_times(course,ins_free_time,sched):
    times = []
    inses = who_can_teach(course)
    for ins in inses:
        availabes = when_can_teach(ins, ins_free_time)
        for available in availabes:
            if no_sem_problem(available,course,sched):
                times.append([available,ins])
    return times


def who_can_teach(course):
    instructor = []
    for key, value in can_teach.items():
        if value.__contains__(course):
            instructor.append(key)
    return instructor

def when_can_teach(person, ins_free_time):
    times = []
    for key, value in ins_free_time.items():
                if person == key:
                    times.extend(value)
    return times

def make_time_dict():
    for time in times:
        schedule[time] = []
    return schedule

def no_sem_problem(time, course,sched):
    for key, values in sched.items():
        if key == time:
            sems = []
            for value in values:
                sems.append(Courses_semester.get(value[0]))
            return not sems.__contains__(Courses_semester.get(course))
    return True

#select            
def get_mrv(the_courses, ins_free_time, sched):
    result = []
    for course in the_courses:
        ava_times = find_available_times(course, ins_free_time,sched)
        result.append([len(ava_times),course,ava_times]) 

    heapq.heapify(result)
    return result

def get_lcv(course,ava_times,sched,ins_time, remaining_courses):
    result = []
    for ava_time in ava_times:
        for ava_time2 in ava_times:
            if ava_time[1] == ava_time2[1]:
                if ava_time2[0].split(" - ")[0] != ava_time[0].split(" - ")[0] and ava_time[0].split(" - ")[1] == ava_time2[0].split(" - ")[1]: #same hour not the same day
                    new_ins_time=copy.deepcopy(ins_time)
                    new_ins_time[ava_time[1]].remove(ava_time[0])
                    new_ins_time[ava_time2[1]].remove(ava_time2[0])


                    new_sched = copy.deepcopy(sched)
                    new_sched[ava_time[0]].append([course,ava_time[1]])
                    new_sched[ava_time2[0]].append([course,ava_time2[1]])

                    total = 0
                    if len(remaining_courses)>0:
                        for rcs in remaining_courses:
                            x = find_available_times(rcs,ins_time,new_sched)
                            total += len(x)
                            flag = True
                            if len(x)<2: #forward_checking
                                    flag = False
                            
                            if flag:
                                result.append([total,new_ins_time,new_sched])
                    else:
                        result.append([0,new_ins_time,new_sched])
            
    result.sort(key=lambda x:x[0],reverse=True)
    return result




make_time_dict()
def go_for_it(rem_courses, sched,ins_time ):
    if len(rem_courses)==0:
        schedule = sched
        instructor_free_times = ins_time
        return schedule
    
    mrv = get_mrv(rem_courses,ins_time, sched)
    for case in mrv:
        remaining = copy.deepcopy(rem_courses)
        remaining.remove(case[1])

        lcv = get_lcv(case[1],case[2],sched,ins_time,remaining)
        for oppurtunity in lcv:
            status = go_for_it(remaining,oppurtunity[2],oppurtunity[1])
            if status == None:
                continue
            else:
                return status



schedule=go_for_it(Courses,schedule,instructor_free_times)
total = 0
for key,value in schedule.items():
    print(f"day = {key}\t\t courses ={value}")
    total+=len(value)
print(total)


    
    

