# Interfaces (small, specific)
class Teachable:
    def teach(self):
        raise NotImplementedError("Subclasses must implement teach()")

class Researchable:
    def research(self):
        raise NotImplementedError("Subclasses must implement research()")

class MedicalPractitioner:
    def treat_patient(self):
        raise NotImplementedError("Subclasses must implement treat_patient()")


# Classes implementing relevant interfaces

class ProfessorResearcher(Teachable, Researchable):
    def teach(self):
        print("Professor Researcher is teaching students.")
    def research(self):
        print("Professor Researcher is conducting research.")


class FullTimeResearcher(Researchable):
    def research(self):
        print("Full-time Researcher is focusing entirely on research.")


class ProfessorHospitalResearcher(Teachable, Researchable, MedicalPractitioner):
    def teach(self):
        print("Professor Hospital Researcher is teaching medical students.")
    def research(self):
        print("Professor Hospital Researcher is conducting medical research.")
    def treat_patient(self):
        print("Professor Hospital Researcher is treating patients in the hospital.")


# Main program
if __name__ == '__main__':
    prof_res = ProfessorResearcher()
    researcher = FullTimeResearcher()
    hospital_prof = ProfessorHospitalResearcher()

    prof_res.teach()
    prof_res.research()

    researcher.research()

    hospital_prof.teach()
    hospital_prof.research()
    hospital_prof.treat_patient()
