from django.test import TestCase
from viewer.models import Employment, Duty, Project, Domain, Experience, Education, Reference, Employee

test_company_name = "AB Corp"
test_job_title = "Button Smasher"
test_start_date = "2020-01-01"
test_end_date = "2020-01-02"
test_leave_reason = "Another button smashing job."
test_duty = "Push buttons in the right order."
test_project = "Improved button pushing processes."
test_domain = "Systems Administration"
test_experience = "Button Pushing"
test_edu = "Foo High School"
test_edu_level = "Diploma"
test_edu_year = "2019-01-01"
test_employee = "Rusty Shackleford"
test_email = "rustyshack@example.com"
test_phone = "1234567890"
test_ref = "Johnny Doh"
test_ref_contact = "Available Upon Request"

class DutyTestCase(TestCase):
	def setUp(self):
		self.duty = Duty.objects.create(description=test_duty)

	def test_duty(self):
		self.assertEqual(self.duty.description, test_duty)

class ProjectTestCase(TestCase):
	def setUp(self):
		self.project = Project.objects.create(description=test_project)

	def test_project(self):
		self.assertEqual(self.project.description, test_project)

class EmploymentTestCase(TestCase):
	def setUp(self):
		Duty.objects.create(description=test_duty)
		Project.objects.create(description=test_project)
		self.employment = Employment.objects.create(company_name=test_company_name,
			job_title=test_job_title,
			start_date=test_start_date,
			end_date=test_end_date,
			leave_reason=test_leave_reason,
			)
		my_duties = [Duty.objects.get(description=test_duty)]
		self.employment.duties.set(my_duties)
		my_projects = [Project.objects.get(description=test_project)]
		self.employment.projects.set(my_projects)

	def test_employment(self):
		self.assertEqual(self.employment.job_title, test_job_title)
		self.assertEqual(self.employment.start_date, test_start_date)
		self.assertEqual(self.employment.end_date, test_end_date)
		self.assertEqual(self.employment.leave_reason, test_leave_reason)

	def test_employment_duty(self):
		self.assertEqual(self.employment.duties.get().description, test_duty)

	def test_employment_project(self):
		self.assertEqual(self.employment.projects.get().description, test_project)

class DomainsTestCase(TestCase):
	def setUp(self):
		self.domain = Domain.objects.create(name=test_domain)
		Experience.objects.create(name=test_experience)
		my_xps = [Experience.objects.get(name=test_experience)]
		self.domain.experiences.set(my_xps)

	def test_domain(self):
		self.assertEqual(self.domain.name, test_domain)

class ExperienceTestCase(TestCase):
	def setUp(self):
		self.xp = Experience.objects.create(name=test_experience)

	def test_experience(self):
		self.assertEqual(self.xp.name, test_experience)

class EducationTestCase(TestCase):
	def setUp(self):
		self.edu = Education.objects.create(name=test_edu, level=test_edu_level, year=test_edu_year)

	def test_education(self):
		self.assertEqual(self.edu.name, test_edu)
		self.assertEqual(self.edu.level, test_edu_level)
		self.assertEqual(self.edu.year, test_edu_year)

class ReferenceTestCase(TestCase):
	def setUp(self):
		employer = Employment.objects.create(company_name=test_company_name,
			job_title=test_job_title,
			start_date=test_start_date,
			end_date=test_end_date,
			leave_reason=test_leave_reason,
		)
		self.reference = Reference.objects.create(name=test_ref, contact=test_ref_contact, employment=employer)
		
		#self.reference.employment.set([employer])

	def test_reference(self):
		self.assertEqual(self.reference.name, test_ref)
		self.assertEqual(self.reference.contact, test_ref_contact)
		self.assertEqual(self.reference.employment.company_name, test_company_name)
		self.assertEqual(self.reference.employment.leave_reason, test_leave_reason)

class EmployeeTestCase(TestCase):
	def setUp(self):
		self.employee = Employee.objects.create(name=test_employee, email=test_email, phone=test_phone)
		Experience.objects.create(name=test_experience)
		my_xps = [Experience.objects.get(name=test_experience)]
		Domain.objects.create(name=test_domain)
		my_domain = Domain.objects.get(name=test_domain)
		my_domain.experiences.set(my_xps)
		self.employee.domains.set([my_domain])
		Education.objects.create(name=test_edu, level=test_edu_level, year=test_edu_year)
		my_edu = [Education.objects.get(name=test_edu)]
		self.employee.education.set(my_edu)
		employer = Employment.objects.create(company_name=test_company_name,
			job_title=test_job_title,
			start_date=test_start_date,
			end_date=test_end_date,
			leave_reason=test_leave_reason,
		)
		my_refs = [Reference.objects.create(name=test_ref, contact=test_ref_contact, employment=employer)]
		self.employee.reference.set(my_refs)


	def test_employee(self):
		self.assertEqual(self.employee.name, test_employee)
		self.assertEqual(self.employee.email, test_email)
		self.assertEqual(self.employee.phone, test_phone)

	def test_employee_domains(self):
		self.assertEqual(self.employee.domains.get(name=test_domain).name, test_domain)
		self.assertEqual(self.employee.domains.get(name=test_domain).experiences.get(name=test_experience).name, test_experience)
		

	def test_employee_education(self):
		self.assertEqual(self.employee.education.get(name=test_edu).name, test_edu)

	def test_employee_reference(self):
		self.assertEqual(self.employee.reference.get(name=test_ref).name, test_ref)


