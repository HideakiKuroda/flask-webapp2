from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import Department

def departmentsSeeder():
    dept01 = Department( name = '役員グループ')
    dept02 = Department( name = '企画管理部')
    dept03 = Department( name = '営業部')
    dept04 = Department( name = '船舶部')
    dept05 = Department( name = '名古屋支店')
    dept06 = Department( name = '坂出支店')
    dept07 = Department( name = '広島支店')
    dept08 = Department( name = '東京支店')
    dept09 = Department( name = '周南営業所')
    dept10 = Department( name = '石狩事務所')
    dept11 = Department( name = '本社内')
    dept12 = Department( name = '出向者')
    dept13 = Department( name = '生田＆マリン')
    dept14 = Department( name = '本船東海地区')
    dept15 = Department( name = '本船瀬戸内地区')
    dept16 = Department( name = '栄吉曳船')
    dept17 = Department( name = '北日本曳船')
    dept18 = Department( name = '船舶管理')
    db.session.add_all([dept01, dept02, dept03, dept04, dept05, dept06,dept07, dept08, dept09, dept10, dept11,dept12, dept13, dept14, dept15, dept16,dept12, dept17, dept18])