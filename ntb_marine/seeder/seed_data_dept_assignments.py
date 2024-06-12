from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import DeptAssignment

def deptAssignmentsSeeder():
    dpass01 = DeptAssignment( user_id = 1, department_id = 4 )
    dpass02 = DeptAssignment( user_id = 2, department_id = 4 )
    dpass03 = DeptAssignment( user_id = 3, department_id = 4 )
    dpass04 = DeptAssignment( user_id = 4, department_id = 4 )
    dpass05 = DeptAssignment( user_id = 5, department_id = 4 )
    dpass06 = DeptAssignment( user_id = 6, department_id = 4 )
    dpass07 = DeptAssignment( user_id = 7, department_id = 4 )
    dpass08 = DeptAssignment( user_id = 8, department_id = 4 )
    dpass09 = DeptAssignment( user_id = 9, department_id = 4 )
    dpass10 = DeptAssignment( user_id = 10, department_id = 4 )
    dpass11 = DeptAssignment( user_id = 11, department_id = 2 )
    dpass12 = DeptAssignment( user_id = 12, department_id = 2 )
    dpass13 = DeptAssignment( user_id = 13, department_id = 16 )
    dpass14 = DeptAssignment( user_id = 14, department_id = 16)
    dpass15 = DeptAssignment( user_id = 15, department_id = 4 )
    dpass16 = DeptAssignment( user_id = 16, department_id = 4 )
    dpass17 = DeptAssignment( user_id = 9, department_id = 10 )
    dpass18 = DeptAssignment( user_id = 10, department_id = 10 )
    dpass19 = DeptAssignment( user_id = 13, department_id = 1 )
    dpass20 = DeptAssignment( user_id = 11, department_id = 10 )
    dpass21 = DeptAssignment( user_id = 12, department_id = 10 )
    dpass22 = DeptAssignment( user_id = 1, department_id = 1 )
    dpass23 = DeptAssignment( user_id = 3, department_id = 1 )
    dpass24 = DeptAssignment( user_id = 11, department_id = 1 )
    db.session.add_all([dpass01, dpass02, dpass03, dpass04, dpass05, dpass06, dpass07, dpass08, dpass09, dpass10, dpass11, dpass12, dpass13, dpass14, dpass15, dpass16, dpass17, dpass18, dpass19, dpass20, dpass21, dpass22, dpass23, dpass24])
        