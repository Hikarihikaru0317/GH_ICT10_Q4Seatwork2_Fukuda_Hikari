from pyscript import document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I name is {self.name}. I am from {self.section}. My most favorite subject is {self.favorite_subject}."

subjects = ["math", "science", "philosophy", "english", "social studies", "filipino"]
sections = ["Emerald"]

names = [
    "abayon",
    "antes",
    "apostol",
    "banaag",
    "barrientos",
    "casal",
    "coeli",
    "david",
    "de mata",
    "dela cruz f",
    "dela cruz j",
    "dellejero",
    "fukuda",
    "gozum",
    "ibay",
    "lim",
    "lozano",
    "mamauag",
    "navarro",
    "precones",
    "ramos",
    "sidhu",
    "tiu",
    "villamayor",
    "zaragoza"
]

classmates_list = [
    Classmate("abayon", "Emerald", "math"),
    Classmate("antes", "Emerald", "science"),
    Classmate("apostol", "Emerald", "philosophy"),
    Classmate("banaag", "Emerald", "english"),
    Classmate("barrientos", "Emerald", "social studies"),
    Classmate("casal", "Emerald", "filipino"),
    Classmate("coeli", "Emerald", "math"),
    Classmate("david", "Emerald", "science"),
    Classmate("de mata", "Emerald", "philosophy"),
    Classmate("dela cruz f", "Emerald", "english"),
    Classmate("dela cruz j", "Emerald", "social studies"),
    Classmate("dellejero", "Emerald", "filipino"),
    Classmate("fukuda", "Emerald", "math"),
    Classmate("gozum", "Emerald", "science"),
    Classmate("ibay", "Emerald", "philosophy"),
    Classmate("lim", "Emerald", "english"),
    Classmate("lozano", "Emerald", "social studies"),
    Classmate("mamauag", "Emerald", "filipino"),
    Classmate("navarro", "Emerald", "math"),
    Classmate("precones", "Emerald", "science"),
    Classmate("ramos", "Emerald", "philosophy"),
    Classmate("sidhu", "Emerald", "english"),
    Classmate("tiu", "Emerald", "social studies"),
    Classmate("villamayor", "Emerald", "filipino"),
    Classmate("zaragoza", "Emerald", "math")
]

def show_list(event):
    message_p = document.getElementById("message")
    
    final_output = ""
    for student in classmates_list:
        final_output += student.introduce() + "<br>"
        
    message_p.innerHTML = final_output


def add_classmate(event):
    name_input = document.getElementById("nameInput")
    section_input = document.getElementById("sectionInput")
    subject_input = document.getElementById("subjectInput")
    
    if name_input.value != "" and section_input.value != "" and subject_input.value != "":
        
        new_student = Classmate(name_input.value, section_input.value, subject_input.value)
        classmates_list.append(new_student)
        
        
        name_input.value = ""
        section_input.value = ""
        subject_input.value = ""
        
        
        show_list(0)
    else:
        document.getElementById("message").innerHTML = "Please fill out all fields before adding."
