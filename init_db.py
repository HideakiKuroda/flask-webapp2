from ntb_marine import db , app
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import Concerned
from ntb_marine.seeder.seed_data_concerneds import concernedsSeeder
from ntb_marine.seeder.seed_data_ships import shipsSeeder
from ntb_marine.seeder.seed_data_operat_sections import operatSectionSeeder
from ntb_marine.seeder.seed_data_navigation_areas import  navigationsAreaSeeder
from ntb_marine.seeder.seed_data_users import usersSeeder
from ntb_marine.seeder.seed_data_summary2s import Summary2seeder
from ntb_marine.seeder.seed_data_summaries import SummarySeeder
from ntb_marine.seeder.seed_data_file_categories import file_categorySeeder
from ntb_marine.seeder.seed_data_doc_templates import doc_templatesSeeder
from ntb_marine.seeder.seed_data_departments import departmentsSeeder
from ntb_marine.seeder.seed_data_dept_assignments import deptAssignmentsSeeder
from ntb_marine.seeder.seed_data_ship_owners import ship_ownersSeeder

with app.app_context():
    # db.drop_table('dec_templates')
    # db.drop_table('users')
    # db.drop_all()
    # db.create_all()

    # usersSeeder()
    # navigationsAreaSeeder()
    # operatSectionSeeder()
    # shipsSeeder()
    # concernedsSeeder()
    # Summary2seeder()
    # SummarySeeder()
    # file_categorySeeder()
    # doc_templatesSeeder()
    # departmentsSeeder()
    # deptAssignmentsSeeder()
    ship_ownersSeeder()

    db.session.commit()