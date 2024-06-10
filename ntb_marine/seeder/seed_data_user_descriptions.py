from ship_management import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ship_management.models import UserDescription

def UserDescriptionSeeder():
    user_descriptions01 = UserDescription(user_id= "1", emp_id="", name_2 = "太田",  name_1 = "正紀" , memo="", phone="080-2505-3769")
    user_descriptions02 = UserDescription(user_id= "2",  emp_id="", name_2 = "坂倉",  name_1 = "繁行" , memo="", phone="090-2703-0778")
    user_descriptions03 = UserDescription(user_id= "3",  emp_id="", name_2 = "髙松",  name_1 = "一憲" , memo="", phone="090-3651-3058")
    user_descriptions04 = UserDescription(user_id= "4", emp_id="", name_2 = "二ツ石",  name_1 = "聖示", memo="", phone="080-2412-2817")
    user_descriptions05 = UserDescription(user_id= "5", emp_id="", name_2 = "三宅",  name_1 = "陸平", memo="", phone="090-5365-7747" )
    user_descriptions06 = UserDescription(user_id= "6", emp_id="", name_2 = "宮本",  name_1 = "強", memo="", phone="080-8946-9550" )
    user_descriptions07 = UserDescription(user_id= "7", emp_id="", name_2 = "植田",  name_1 = "廣幸", memo="", phone="080-1522-6740" )
    user_descriptions08 = UserDescription(user_id= "8", emp_id="", name_2 = "黒田",  name_1 = "秀明", memo="", phone="070-4462-3467" )
    user_descriptions09 = UserDescription(user_id= "9", emp_id="", name_2 = "吉田",  name_1 = "美弥", memo="", phone=None )
    user_descriptions10 = UserDescription(user_id= "10", emp_id="", name_2 = "岩本",  name_1 = "香利", memo="", phone=None )
    user_descriptions11 = UserDescription(user_id= "11", emp_id="", name_2 = "若狭",  name_1 = "吉晴", memo="", phone="090-6999-9728" )
    user_descriptions12 = UserDescription(user_id= "12", emp_id="", name_2 = "荒川",  name_1 = "純一", memo="", phone="090-3897-4524" )
    user_descriptions13 = UserDescription(user_id= "13",  emp_id="", name_2 = "青木",  name_1 = "宏之", memo="", phone="080-8515-4114" )
    user_descriptions14 = UserDescription(user_id= "14",  emp_id="", name_2 = "堀",  name_1 = "容子", memo="", phone="080-2542-4872" )
    user_descriptions15 = UserDescription(user_id= "15",  emp_id="", name_2 = "村知",  name_1 = "一世", memo="", phone=None )
    user_descriptions16 = UserDescription(user_id= "16",  emp_id="", name_2 = "井上",  name_1 = "佳代", memo="", phone="090-1712-2229" )
    user_descriptions17 = UserDescription(user_id= "17",  emp_id="", name_2 = "柄谷",  name_1 = "仁美", memo="", phone=None )
    user_descriptions18 = UserDescription(user_id= "18",  emp_id="", name_2 = "小俣",  name_1 = "真美", memo="", phone=None )
    user_descriptions19 = UserDescription(user_id= "19",  emp_id="", name_2 = "西尾",  name_1 = "哲郎", memo="", phone=None )
    user_descriptions20 = UserDescription(user_id= "20",  emp_id="", name_2 = "田村",  name_1 = "啓造", memo="", phone="090-1682-9414" )
    user_descriptions21 = UserDescription(user_id= "21",  emp_id="", name_2 = "清水",  name_1 = "斉", memo="", phone="090-2021-0330" )
    user_descriptions22 = UserDescription(user_id= "22",  emp_id="", name_2 = "増田",  name_1 = "数一", memo="", phone="090-4972-6989" )
    user_descriptions23 = UserDescription(user_id= "23",  emp_id="", name_2 = "大平",  name_1 = "芳生", memo="", phone="080-2544-9399" )
    db.session.add_all([user_descriptions01,user_descriptions02,user_descriptions03,user_descriptions04,user_descriptions05,user_descriptions06,user_descriptions07,user_descriptions08,user_descriptions09,user_descriptions10,user_descriptions11,user_descriptions12,user_descriptions13,user_descriptions14,user_descriptions15,user_descriptions16,user_descriptions17,user_descriptions18,user_descriptions19,user_descriptions20,user_descriptions21,user_descriptions22,user_descriptions23])