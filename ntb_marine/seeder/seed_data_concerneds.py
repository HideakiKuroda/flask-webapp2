from ship_management import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ship_management.models import Concerned

# def __init__(self, ship_id, operator, borrower, manager, crew_arrange ):
#         self.ship_id = ship_id
#         self.operator = operator
#         self.borrower = borrower
#         self.manager = manager
#         self.crew_arrange = crew_arrange

def concernedsSeeder():       
    concerneds01 = Concerned( ship_id= 1, operator = "石狩新港サービス", borrower = "石狩湾新港サービス", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds02 = Concerned( ship_id= 2, operator = "石狩新港サービス", borrower = "石狩湾新港サービス", manager = "日本栄船", crew_arrange = "石狩湾新港サービス" )
    concerneds03 = Concerned( ship_id= 3, operator = "北日本曵船", borrower = "北日本曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船" )
    concerneds04 = Concerned( ship_id= 4, operator = "北日本曵船", borrower = "北日本曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船" )
    concerneds05 = Concerned( ship_id= 5, operator = "金沢港運", borrower = "金沢港運", manager = "金沢港運", crew_arrange = "金沢港運")
    concerneds06 = Concerned( ship_id= 6, operator = "富山新港管理局", borrower = "", manager = "", crew_arrange = "" )
    concerneds07 = Concerned( ship_id= 7, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds08 = Concerned( ship_id= 8, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds09 = Concerned( ship_id= 9, operator = "日本栄船", borrower = "日本栄船", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds10 = Concerned( ship_id= 10, operator = "日本栄船", borrower = "日本栄船", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds11 = Concerned( ship_id= 11, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds12 = Concerned( ship_id= 12, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds13 = Concerned( ship_id= 13, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds14 = Concerned( ship_id= 14, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds15 = Concerned( ship_id= 15, operator = "日本栄船", borrower = "日本栄船", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds16 = Concerned( ship_id= 16, operator = "日本栄船", borrower = "", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds17 = Concerned( ship_id= 17, operator = "神戸曳船", borrower = "神戸曳船", manager = "日本栄船", crew_arrange = "神戸曳船" )
    concerneds18 = Concerned( ship_id= 18, operator = "神戸曳船", borrower = "神戸曳船", manager = "日本栄船", crew_arrange = "神戸曳船" )
    concerneds19 = Concerned( ship_id= 19, operator = "日本栄船", borrower = "栄吉曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船" )
    concerneds20 = Concerned( ship_id= 20, operator = "日本栄船", borrower = "栄吉曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船" )
    concerneds21 = Concerned( ship_id= 21, operator = "栄吉曳船", borrower = "栄吉曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船")
    concerneds22 = Concerned( ship_id= 22, operator = "栄吉曳船", borrower = "栄吉曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船" )
    concerneds23 = Concerned( ship_id= 23, operator = "栄吉曳船", borrower = "栄吉曳船", manager = "栄吉曳船", crew_arrange = "栄吉曳船")
    concerneds24 = Concerned( ship_id= 24, operator = "日本栄船", borrower = "日本栄船", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds25 = Concerned( ship_id= 25, operator = "日本栄船", borrower = "日本栄船", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds26 = Concerned( ship_id= 26, operator = "日本栄船", borrower = "日本栄船", manager = "日本栄船", crew_arrange = "日本栄船" )
    concerneds27 = Concerned( ship_id= 27, operator = "日本栄船", borrower = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ", manager = "日本栄船", crew_arrange = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ" )
    concerneds28 = Concerned( ship_id= 28, operator = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ", borrower = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ", manager = "日本栄船", crew_arrange = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ")
    concerneds29 = Concerned( ship_id= 29, operator = "東海曳船", borrower = "", manager = "", crew_arrange = "" )
    concerneds30 = Concerned( ship_id= 30, operator = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ", borrower = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ", manager = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ", crew_arrange = "宇部ﾎﾟｰﾄｻｰﾋﾞｽ" )
    concerneds31 = Concerned( ship_id= 31, operator = "中電環境ﾃｸﾉｽ", borrower = "栄吉曳船", manager = "日本栄船", crew_arrange = "栄吉曳船" )
    db.session.add_all([concerneds01,concerneds02,concerneds03,concerneds04,concerneds05,concerneds06,concerneds07,concerneds08,concerneds09,concerneds10,concerneds11,concerneds12,concerneds13,concerneds14,concerneds15,concerneds16,concerneds17,concerneds18,concerneds19,concerneds20,concerneds21,concerneds22,concerneds23,concerneds24,concerneds25,concerneds26,concerneds27,concerneds28,concerneds29,concerneds30,concerneds31])