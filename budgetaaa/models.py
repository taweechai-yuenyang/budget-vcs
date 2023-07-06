from django.db import models

# Create your models here.
class BudgetTypeAAA(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    Code=models.CharField(max_length=50, verbose_name="รหัส", db_column='bt_code')# bt_code nvarchar(50) COLLATE Thai_CI_AS NULL,
    Description=models.CharField(max_length=50, verbose_name="รายละเอียด", db_column='bt_name')# bt_name nvarchar(50) COLLATE Thai_CI_AS NULL,
    Status=models.IntegerField(verbose_name="สถานะ", db_column="bt_status")# bt_status int NULL,
    BgID=models.CharField(max_length=50, verbose_name="BG ID", db_column="bg_id")# bg_id int NULL,
    BnID=models.CharField(max_length=50, verbose_name="BN ID", db_column="bn_id")# bn_id int NULL,
    CreatedAt=models.DateField(verbose_name="Add Date", db_column="ADDDATE", auto_now_add=True)# ADDDATE datetime NULL,
    def __str__(self) -> str:
        return f"{self.Description}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Budget_type"
        app_label = "budgetaaa"
        verbose_name = "ข้อมูล Budget Type"
        verbose_name_plural = "Budget Type"

# class StatusAAA(models.Model):
#     ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int NOT NULL,
#     Title=models.CharField(max_length=50, verbose_name="หัวข้อ", db_column='Name_statusPR')# Name_statusPR nvarchar(50) COLLATE Thai_CI_AS NULL

#     def __str__(self) -> str:
#         return f"{self.Title}"

#     class Meta:
#         # db_table_comment = "formula_vcst"
#         db_table = "status_pr"
#         app_label = "budgetaaa"
#         verbose_name = "ข้อมูล Status PR"
#         verbose_name_plural = "Status PR"

class BudgetAAA(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    BudgetNo=models.CharField(max_length=50, verbose_name="เลขที่เอกสาร", db_column='bu_no')# bu_no nvarchar(50) COLLATE Thai_CI_AS NULL,
    BudgetDescription=models.CharField(max_length=50, verbose_name="รายละเอียด", db_column='bu_desc')# bu_desc nvarchar(50) COLLATE Thai_CI_AS NULL,
    Price=models.FloatField(verbose_name="ราคา", db_column='bu_price')# bu_price numeric(18,2) NULL,
    DueDate=models.DateField(verbose_name="วันที่จ่าย", db_column="ddate")# ddate date NULL,
    Status=models.IntegerField(verbose_name="สถานะ", db_column="status")# status int NULL,
    DepartmentID=models.CharField(max_length=50, verbose_name="แผนก", db_column="dept_id")# dept_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    BtID=models.ForeignKey(BudgetTypeAAA, verbose_name="ประเภท", db_column='bt_id', on_delete=models.CASCADE)# bt_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    TypeIncome=models.IntegerField(verbose_name="ประเภทการรับ", db_column="type_income")# type_income int NULL,
    CreatedAt=models.DateTimeField(verbose_name="Add Date", db_column="ADDDATE", auto_now_add=True)# ADDDATE datetime NULL,
    def __str__(self) -> str:
        return str(self.ID)

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Budget"
        app_label = "budgetaaa"
        verbose_name = "ข้อมูล Budget"
        verbose_name_plural = "Budget"

class EmployeeAAA(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    EmpID=models.CharField(max_length=50, verbose_name="รหัสพนักงาน", db_column='emp_id')# emp_id varchar(50) COLLATE Thai_CI_AS NULL,
    FirstName=models.CharField(max_length=50, verbose_name="ชื่อ", db_column='emp_name')# emp_name varchar(150) COLLATE Thai_CI_AS NULL,
    LastName=models.CharField(max_length=50, verbose_name="นาสกุล", db_column='emp_surname')# emp_surname varchar(150) COLLATE Thai_CI_AS NULL,
    DepartmentID=models.CharField(max_length=50, verbose_name="แผนก/ฝ่าย", db_column='emp_dept')# emp_dept varchar(50) COLLATE Thai_CI_AS NULL,
    UserName=models.CharField(max_length=50, verbose_name="ชื่อผู้ใช้งาน", db_column='emp_user')# emp_user varchar(50) COLLATE Thai_CI_AS NULL,
    Password=models.CharField(max_length=50, verbose_name="รหัสผ่าน", db_column='emp_pass')# emp_pass varchar(50) COLLATE Thai_CI_AS NULL,
    Status=models.IntegerField(verbose_name="สถานะ", db_column="emp_status")# emp_status int DEFAULT 0 NULL,
    CreatedByID=models.CharField(max_length=50, verbose_name="รหัสพนักงานที่ทำการบันทึก", db_column='emp_createby')# emp_createby varchar(50) COLLATE Thai_CI_AS NULL,
    CreatedAt=models.DateTimeField(verbose_name="บันทึกเมื่อ", db_column="emp_createdate", auto_now_add=True)# emp_createdate datetime NULL,
    UpdatedByID=models.CharField(max_length=50, verbose_name="รหัสพนักงานที่อัพเดท", db_column='emp_updateby')# emp_updateby varchar(50) COLLATE Thai_CI_AS NULL,
    UpdatedAt=models.DateTimeField(verbose_name="แก้ไข", db_column="emp_updatedate", auto_now=True)# emp_updatedate datetime NULL,
    EmailAddress=models.CharField(max_length=50, verbose_name="ที่อยู่ E-Mail", db_column='emp_email')# emp_email varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    EmpFormulaID=models.CharField(max_length=50, verbose_name="Formula Emp ID", db_column='FCSKID_EMP_FM', blank=True, null=True)# FCSKID_EMP_FM nvarchar(50) COLLATE Thai_CI_AS NULL,
    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Employee"
        app_label = "budgetaaa"
        verbose_name = "ข้อมูล Employee"
        verbose_name_plural = "Employee"


class RTApproveAAA(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    DepartmentID=models.CharField(max_length=50, verbose_name="แผนก/ฝ่าย", db_column='dept_id')# dept_id varchar(50) COLLATE Thai_CI_AS NULL,
    Step=models.IntegerField(verbose_name="ลำดับที่", db_column="step")# step int NULL,
    Email=models.CharField(max_length=50, verbose_name="ที่อยู่ E-Mail", db_column='email')# email nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    ApproveName=models.CharField(max_length=250, verbose_name="ชื่อผู้อนุมัติ", db_column='appr_name')# appr_name nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    ImageSignal=models.CharField(max_length=250, verbose_name="ลายเซ็นต์", db_column='image_sig')# image_sig nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    FType=models.IntegerField(verbose_name="FType", db_column="ftype", null=True, default=0)# ftype int DEFAULT 0 NOT NULL,
    BgAmount=models.DecimalField(decimal_places=4, max_digits=4, verbose_name="จำนวน", db_column='bg_amount', null=True,default=0)# bg_amount numeric(18,4) NULL,
    Position=models.CharField(max_length=250, verbose_name="ตำแหน่ง", db_column='position', null=True, blank=True)# position nvarchar(MAX) COLLATE Thai_CI_AS NULL
        
    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "RT_APPROVE"
        app_label = "budgetaaa"
        verbose_name = "ข้อมูล RT Approve"
        verbose_name_plural = "RT Approve"