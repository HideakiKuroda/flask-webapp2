from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import Concerned
from ntb_marine.seeder.seed_data_concerneds import concernedsSeeder
from ntb_marine.seeder.seed_data_ships import shipsSeeder
from ntb_marine.seeder.seed_data_operat_sections import operatSectionSeeder
from ntb_marine.seeder.seed_data_navigation_areas import  navigationsAreaSeeder
from ntb_marine.seeder.seed_data_users import usersSeeder
from ntb_marine.seeder.seed_data_user_descriptions import UserDescriptionSeeder
from ntb_marine.seeder.seed_data_summary2s import Summary2seeder
from ntb_marine.seeder.seed_data_summaries import SummarySeeder

db.drop_all()
db.create_all()

usersSeeder()
navigationsAreaSeeder()
operatSectionSeeder()
shipsSeeder()
concernedsSeeder()
UserDescriptionSeeder()
Summary2seeder()
SummarySeeder()

db.session.commit()