from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    Source_of_Hire = models.CharField(max_length=100, choices=[(
        'Agency', 'Agency'), ('Reference', 'Reference'), ('Portal', 'Portal')], default='Agency')

    Name_of_Agency = models.CharField(max_length=100, blank=True, null=True)

    Name_of_Referral_Emp = models.CharField(
        max_length=100, blank=True, null=True)

    Full_Name = models.CharField(
        max_length=100, blank=True, null=True)

    Grade = models.CharField(
        max_length=100, blank=True, null=True)

    Employee_Type = models.CharField(
        max_length=100, blank=True, null=True)

    Department = models.CharField(
        max_length=100, blank=True, null=True)

    Main_Sub_Department_Mapping = models.CharField(
        max_length=100, blank=True, null=True)

    Job = models.TextField(blank=True, null=True)

    Title = models.CharField(
        max_length=100, blank=True, null=True)

    Location = models.CharField(
        max_length=100, blank=True, null=True)

    Appraiser_Ecode = models.CharField(
        max_length=100, blank=True, null=True)

    Appraiser_Name = models.CharField(
        max_length=100, blank=True, null=True)

    DOJ = models.CharField(
        max_length=100, blank=True, null=True)

    Date_of_Birth = models.CharField(
        max_length=100, blank=True, null=True)

    Category = models.CharField(
        max_length=100, blank=True, null=True)

    Email_Address = models.EmailField(blank=True, null=True)

    Gender = models.CharField(
        max_length=100, blank=True, null=True)

    KLI_RHRM = models.CharField(
        max_length=100, blank=True, null=True)

    Confirmation_Date = models.DateField(blank=True, null=True)

    Town_Or_City = models.CharField(
        max_length=100, blank=True, null=True)

    Notice_Period = models.CharField(
        max_length=100, blank=True, null=True)

    Served = models.BooleanField(blank=True, null=True, default=False)

    System_LWD = models.CharField(
        max_length=100, blank=True, null=True)

    DOJ_Group = models.CharField(
        max_length=100, blank=True, null=True)

    Status = models.CharField(
        max_length=100, choices=[('(Active)', 'Active'), ('Exit', 'Exit'), ('Absconding', 'Absconding')], default='Active')

    Last_attendance_marked = models.CharField(
        max_length=100, blank=True, null=True)

    BGV_Status = models.CharField(
        max_length=100, blank=True, null=True)

    Laptop_or_Desktop = models.CharField(
        max_length=100, blank=True, null=True)

    Data_card = models.CharField(
        max_length=100, blank=True, null=True)

    Any_other_IT_gadget = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Full_Name


class LD (models.Model):
    Employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    Training_done = models.BooleanField(blank=True, null=True, default=False)
    Training_done_Date = models.DateField(blank=True, null=True)
    Training_in_Calendar = models.BooleanField(
        blank=True, null=True, default=False)
    Training_in_Calendar_Date = models.DateField(blank=True, null=True)
    Any_Training_Requirement = models.TextField(blank=True, null=True)
    Employee_Raised_or_Employer_Raised = models.CharField(max_length=100, choices=[(
        'Employee Raised', 'Employee Raised'), ('Employer Raised', 'Employer Raised')], default='Employee Raised')


class Compensation_and_Benefit (models.Model):
    Employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    CTC = models.CharField(max_length=100, blank=True, null=True)
    Car_Scheme = models.BooleanField(blank=True, null=True, default=False)
    LTBP = models.BooleanField(blank=True, null=True, default=False)
    Bonus_or_Incentive = models.TextField(blank=True, null=True)
    PF = models.CharField(max_length=100, blank=True, null=True)
    ESIC = models.CharField(max_length=100, blank=True, null=True)
    Gratuity = models.CharField(max_length=100, blank=True, null=True)
    Mediclaim = models.CharField(max_length=100, blank=True, null=True)
    GTL = models.CharField(max_length=100, blank=True, null=True)
    GPA = models.CharField(max_length=100, blank=True, null=True)
    Meal_Pass = models.CharField(max_length=100, blank=True, null=True)
    Garden_Leave = models.CharField(max_length=100, blank=True, null=True)
    Leave_General = models.CharField(max_length=100, blank=True, null=True)
    Maternity_or_Paternity = models.CharField(
        max_length=100, blank=True, null=True)
    Sabbatical_Leave = models.CharField(max_length=100, blank=True, null=True)
    Extended_Sick_Leave = models.CharField(
        max_length=100, blank=True, null=True)


class Discipline (models.Model):
    Employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    SCN_Disciplinary_Action = models.TextField(blank=True, null=True)
    Warning_or_Caution = models.TextField(blank=True, null=True)
    Other_action = models.TextField(blank=True, null=True)


class HR_Letter	(models.Model):
    Employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    Confirmation_Letter = models.TextField(blank=True, null=True)
    PMS_Letter = models.TextField(blank=True, null=True)
    Any_Other_Letter = models.TextField(blank=True, null=True)
    Recognition = models.TextField(blank=True, null=True)


class Rating (models.Model):
    Employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    PMS_rating_FY_21 = models.CharField(blank=True, null=True, max_length=100)
    PMS_rating_FY_20 = models.CharField(blank=True, null=True, max_length=100)
    PMS_rating_FY_19 = models.CharField(blank=True, null=True, max_length=100)


class Onboarding_documents (models.Model):
    Employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True)
    Education_Certificate = models.TextField(blank=True, null=True)
    Relieving_Letter = models.TextField(blank=True, null=True)
    Joining_Form = models.TextField(blank=True, null=True)
    Adhaar = models.TextField(blank=True, null=True)
    PAN = models.TextField(blank=True, null=True)
    Any_Other_document = models.TextField(blank=True, null=True)
    CIBIL_rating = models.TextField(blank=True, null=True)
