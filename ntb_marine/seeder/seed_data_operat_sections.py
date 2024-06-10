from ship_management import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ship_management.models import OperatSection

    # def __init__(self, section, memo):
    #     self.section = section
    #     self.memo = memo

def operatSectionSeeder():
    operat_sections01 = OperatSection(section = "瀬戸内地区" , memo = "泉北・神戸・坂出・広島" )
    operat_sections02 = OperatSection(section = "東海地区" , memo = "伊勢湾・三河湾" )
    operat_sections03 = OperatSection(section = "神戸" , memo = "神戸曳船" )
    operat_sections04 = OperatSection(section = "石狩新港" , memo = "石狩新港サービス" )
    operat_sections05 = OperatSection(section = "苫小牧" , memo = "北日本曳船" )
    operat_sections06 = OperatSection(section = "金沢港" , memo = "金沢港運" )
    operat_sections07 = OperatSection(section = "富山新港" , memo = "富山新港管理局" )
    operat_sections08 = OperatSection(section = "清水" , memo = "東海曳船" )
    operat_sections09 = OperatSection(section = "宇部ポート" , memo = "宇部ポートサービス" )
    operat_sections10 = OperatSection(section = "三隅発電所" , memo = "中電環境テクノス株式会社" )
    db.session.add_all([operat_sections01,operat_sections02,operat_sections03,operat_sections04,operat_sections05,operat_sections06,operat_sections07,operat_sections08,operat_sections09,operat_sections10])
            