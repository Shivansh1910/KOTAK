from django.contrib import admin
from django.http import HttpResponse
import csv
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class EmployeeAdmin(ImportExportModelAdmin):
    models = models.Employee


admin.site.register(models.Employee, EmployeeAdmin)


class LDAdmin(ImportExportModelAdmin):
    models = models.LD


admin.site.register(models.LD, LDAdmin)


class Compensation_and_BenefitAdmin(ImportExportModelAdmin):
    models = models.Compensation_and_Benefit


admin.site.register(models.Compensation_and_Benefit,
                    Compensation_and_BenefitAdmin)


class DisciplineAdmin(ImportExportModelAdmin):
    models = models.Discipline


admin.site.register(models.Discipline, DisciplineAdmin)


class HR_LetterAdmin(ImportExportModelAdmin):
    models = models.HR_Letter


admin.site.register(models.HR_Letter, HR_LetterAdmin)


class RatingAdmin(ImportExportModelAdmin):
    models = models.Rating


admin.site.register(models.Rating, RatingAdmin)


class Onboarding_documentsAdmin(ImportExportModelAdmin):
    models = models.Onboarding_documents


admin.site.register(models.Onboarding_documents, Onboarding_documentsAdmin)


def export_as_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow([
        'Employees Id',
        'Source of Hire (Agency/Reference/Portal)'	,
        'Name of Agency',
        'Name of Referral Emp',
        'Full Name',
        'Grade',
        'Employee Type',
        'Department',
        'Main Sub Department Mapping',
        'Job',
        'Title',
        'Location',
        'Appraiser Ecode'	,
        'Appraiser Name'	,
        'DOJ',
        'Date of Birth	',
        'Category',
        '	Email Address',
        'Gender',
        'KLI RHRM',
        'Confirmation Date',
        'Town Or City',
        'Notice Period',
        'Served(Y/N)',
        ' System LWD',
        '	DOJ Group	Status (Active/Exit/Absconding)',
        'Last attendance marked' 	,
        'BGV Status',
        'Labtop/Desktop',
        'Data card'	,
        'Any other IT gadget',
        'Training done',
        'Date',
        'Training in Calendar'	,
        'Date',
        'Any Training Requirement',
        'Employee Raised/Employer Raised',
        'CTC',
        'Car Scheme (Y/N)',
        'LTBP (Y/N)',
        'Bonus/Incentive'	,
        'PF',
        'ESIC',
        'Gratuity',
        'Mediclaim'	,
        'GTL',
        'GPA',
        'Meal Pass',
        'Garden Leave',
        'Leave General',
        'Maternity/Paternity',
        'Sabbatical Leave',
        'Extended Sick Leave',
        'SCN- Disciplinary Action',
        'Warning/Caution',
        'Other action',
        '	Confirmation Letter',
        'PMS Letter',
        'Any Other Letter ',
        'Recognition (Value Cheeque)',
        'PMS rating',
        'FY 21-22',
        'PMS rating FY 20-21',
        'PMS rating FY 19-20',
        'Education Certificate',
        'Relieving Letter',
        'Joining Form',
        'Adhaar',
        'PAN',
        'Any Other document'	,
        'CIBIL rating'
    ])

    users = models.Employee.objects.all()
    employee = users.values_list('id', 'Source_of_Hire', 'Name_of_Agency', 'Name_of_Referral_Emp', 'Full_Name', 'Grade', 'Employee_Type', 'Department', 'Main_Sub_Department_Mapping', 'Job', 'Title', 'Location', 'Appraiser_Ecode', 'Appraiser_Name', 'DOJ',
                                 'Date_of_Birth', 'Category', 'Email_Address', 'Gender', 'KLI_RHRM', 'Confirmation_Date', 'Town_Or_City', 'Notice_Period', 'Served', 'System_LWD', 'DOJ_Group', 'Status', 'Last_attendance_marked', 'BGV_Status', 'Laptop_or_Desktop', 'Data_card', 'Any_other_IT_gadget')
    for index, user in enumerate(users):
        LD = list(models.LD.objects.filter(Employee=user).values_list('Training_done', 'Training_done_Date', 'Training_in_Calendar',
                                                                      'Training_in_Calendar_Date', 'Any_Training_Requirement', 'Employee_Raised_or_Employer_Raised'))
        Compensation_and_Benefit = list(models.Compensation_and_Benefit.objects.filter(
            Employee=user).values_list('CTC', 'Car_Scheme', 'LTBP', 'Bonus_or_Incentive', 'PF', 'ESIC', 'Gratuity', 'Mediclaim', 'GTL', 'GPA', 'Meal_Pass', 'Garden_Leave', 'Leave_General', 'Maternity_or_Paternity', 'Sabbatical_Leave', 'Extended_Sick_Leave'))
        Discipline = list(models.Discipline.objects.filter(Employee=user).values_list(
            'SCN_Disciplinary_Action', 'Warning_or_Caution', 'Other_action'))
        HR_Letter = list(models.HR_Letter.objects.filter(Employee=user).values_list(
            'Confirmation_Letter', 'PMS_Letter', 'Any_Other_Letter', 'Recognition'))
        Rating = list(models.Rating.objects.filter(Employee=user).values_list(
            'PMS_rating_FY_21', 'PMS_rating_FY_20', 'PMS_rating_FY_19'))
        Onboarding_documents = list(models.Onboarding_documents.objects.filter(
            Employee=user).values_list('Education_Certificate', 'Relieving_Letter', 'Joining_Form', 'Adhaar', 'PAN', 'Any_Other_document', 'CIBIL_rating'))

        row = []

        for i in employee[index]:
            row.append(i)

        for i in LD[0]:
            row.append(i)

        for i in Compensation_and_Benefit[0]:
            row.append(i)

        for i in Discipline[0]:
            row.append(i)

        for i in HR_Letter[0]:
            row.append(i)

        for i in Rating[0]:
            row.append(i)

        for i in Onboarding_documents[0]:
            row.append(i)

        writer.writerow(row)

    return response


admin.site.add_action(export_as_csv)
