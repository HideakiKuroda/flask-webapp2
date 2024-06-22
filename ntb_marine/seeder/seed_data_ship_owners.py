from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import ShipOwner

def ship_ownersSeeder():
	ship_owners_data = [
		{ 'ship_id' : 1, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 2, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 3, 'name' : '日本栄船', 'ratio' : 40 },
		{ 'ship_id' : 4, 'name' : '日本栄船', 'ratio' : 22.5 },
		{ 'ship_id' : 5, 'name' : '神戸曳船', 'ratio' : 100 },
		{ 'ship_id' : 6, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 7, 'name' : '日本栄船', 'ratio' : 60 },
		{ 'ship_id' : 8, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 9, 'name' : '協伸商会', 'ratio' : 100 },
		{ 'ship_id' : 10, 'name' : '日本栄船', 'ratio' : 70 },
		{ 'ship_id' : 11, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 12, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 13, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 14, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 15, 'name' : '商船三井', 'ratio' : 100 },
		{ 'ship_id' : 16, 'name' : '日本栄船', 'ratio' : 100 },
		{ 'ship_id' : 17, 'name' : '神戸曳船', 'ratio' : 100 },
		{ 'ship_id' : 18, 'name' : '日本栄船', 'ratio' : 50 },
		{ 'ship_id' : 19, 'name' : '日本栄船', 'ratio' : 50 },
		{ 'ship_id' : 20, 'name' : '日本栄船', 'ratio' : 37.5 },
		{ 'ship_id' : 21, 'name' : '日本栄船', 'ratio' : 50 },
		{ 'ship_id' : 22, 'name' : '日本栄船', 'ratio' : 50 },
		{ 'ship_id' : 23, 'name' : '日本栄船', 'ratio' : 75 },
		{ 'ship_id' : 24, 'name' : '日本栄船', 'ratio' : 75 },
		{ 'ship_id' : 25, 'name' : '日本栄船', 'ratio' : 90 },
		{ 'ship_id' : 26, 'name' : '日本栄船', 'ratio' : 65 },
		{ 'ship_id' : 27, 'name' : '日本栄船', 'ratio' : 80 },
		{ 'ship_id' : 28, 'name' : '日本栄船', 'ratio' : 50 },
		{ 'ship_id' : 29, 'name' : '宇部ﾎﾞｰﾄｻｰﾋﾞｽ', 'ratio' : 85 },
		{ 'ship_id' : 30, 'name' : '宇部ﾎﾟｰﾄｻｰﾋﾞｽ:', 'ratio' : 85 },
		{ 'ship_id' : 31, 'name' : '日本栄船', 'ratio' : 25 },
		{ 'ship_id' : 3, 'name' : '栄吉海運', 'ratio' : 30 },
		{ 'ship_id' : 4, 'name' : '北日本曵船', 'ratio' : 30 },
		{ 'ship_id' : 7, 'name' : '駿河湾曳船', 'ratio' : 40 },
		{ 'ship_id' : 10, 'name' : '生田ｱﾝﾄﾞﾏﾘﾝ:', 'ratio' : 30 },
		{ 'ship_id' : 18, 'name' : '神戸曳船', 'ratio' : 50 },
		{ 'ship_id' : 19, 'name' : '内海曳船', 'ratio' : 50 },
		{ 'ship_id' : 20, 'name' : '内海曳船', 'ratio' : 37.5 },
		{ 'ship_id' : 21, 'name' : '栄吉海運', 'ratio' : 50 },
		{ 'ship_id' : 22, 'name' : '栄吉海運', 'ratio' : 50 },
		{ 'ship_id' : 23, 'name' : '栄吉海運', 'ratio' : 25 },
		{ 'ship_id' : 24, 'name' : '中電環境ﾃｸﾉｽ', 'ratio' : 25 },
		{ 'ship_id' : 25, 'name' : '生田ｱﾝﾄﾞﾏﾘﾝ', 'ratio' : 10 },
		{ 'ship_id' : 26, 'name' : '中電環境ﾃｸﾉｽ', 'ratio' : 35 },
		{ 'ship_id' : 27, 'name' : '宇部ﾎﾟｰﾄｻｰﾋﾞｽ', 'ratio' : 20 },
		{ 'ship_id' : 28, 'name' : '宇部ﾎﾟｰﾄｻｰﾋﾞｽ', 'ratio' : 50 },
		{ 'ship_id' : 29, 'name' : '宇部興産海運㈱', 'ratio' : 15 },
		{ 'ship_id' : 30, 'name' : '宇部興産海運', 'ratio' : 15 },
		{ 'ship_id' : 31, 'name' : '中電環境ﾃｸﾉｽ', 'ratio' : 75 },
		{ 'ship_id' : 3, 'name' : '北日本曳船', 'ratio' : 30 },
		{ 'ship_id' : 4, 'name' : '栄吉海運', 'ratio' : 30 },
		{ 'ship_id' : 20, 'name' : '早駒運輸', 'ratio' : 25 },
		{ 'ship_id' : 4, 'name' : '東栄汽船', 'ratio' : 17.5 }	
	]
	ship_owners = [ShipOwner(ship_id=data['ship_id'], name=data['name'], ratio=data['ratio']) for data in ship_owners_data]
	db.session.add_all(ship_owners)