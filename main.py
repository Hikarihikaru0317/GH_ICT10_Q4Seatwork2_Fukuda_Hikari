from pyscript import document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I name is {self.name}. I am from {self.section}. My most favorite subject is {self.favorite_subject}."

subjects = ["math", "science", "philosopht", "english", "social studies", "Filipino"]
sections = ["Amethyst", "Sapphire", "Liberty", "Emerald", "Diamond"]

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
    Classmate("abayon", "Amethyst", "math"),
    Classmate("antes", "Sapphire", "science"),
    Classmate("apostol", "Liberty", "philosopht"),
    Classmate("banaag", "Emerald", "english"),
    Classmate("barrientos", "Diamond", "social studies"),
    Classmate("casal", "Amethyst", "Filipino"),
    Classmate("coeli", "Sapphire", "math"),
    Classmate("david", "Liberty", "science"),
    Classmate("de mata", "Emerald", "philosopht"),
    Classmate("dela cruz f", "Diamond", "english"),
    Classmate("dela cruz j", "Amethyst", "social studies"),
    Classmate("dellejero", "Sapphire", "Filipino"),
    Classmate("fukuda", "Liberty", "math"),
    Classmate("gozum", "Emerald", "science"),
    Classmate("ibay", "Diamond", "philosopht"),
    Classmate("lim", "Amethyst", "english"),
    Classmate("lozano", "Sapphire", "social studies"),
    Classmate("mamauag", "Liberty", "Filipino"),
    Classmate("navarro", "Emerald", "math"),
    Classmate("precones", "Diamond", "science"),
    Classmate("ramos", "Amethyst", "philosopht"),
    Classmate("sidhu", "Sapphire", "english"),
    Classmate("tiu", "Liberty", "social studies"),
    Classmate("villamayor", "Emerald", "Filipino"),
    Classmate("zaragoza", "Diamond", "math")
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