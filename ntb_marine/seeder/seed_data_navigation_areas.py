from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import NavigationArea

def navigationsAreaSeeder():
    navigations01 =  NavigationArea(name ="平水", description = "")
    navigations02 =  NavigationArea(name ="沿海", description = "" )
    navigations03 =  NavigationArea(name ="限定沿海", description = "" )
    navigations04 =  NavigationArea(name ="近海", description = "" )
    db.session.add_all([navigations01,navigations02,navigations03,navigations04])        
