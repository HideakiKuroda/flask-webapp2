# models.py
#UserMixin ログインユーザーをチェしたり表示したする
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from ntb_marine import db  # SQLAlchemyインスタンスをインポート
from datetime import datetime
from pytz import timezone
from sqlalchemy.orm import backref
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr

class TimestampMixin(object):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=lambda: datetime.now(timezone('Asia/Tokyo')), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime, 
            default=lambda: datetime.now(timezone('Asia/Tokyo')), 
            onupdate=lambda: datetime.now(timezone('Asia/Tokyo')), 
            nullable=False
        )
    
class User(db.Model,TimestampMixin,UserMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True)
    name = db.Column(db.String(64))
    ms_email = db.Column(db.String(128))
    ms_id = db.Column(db.String(128))
    #relationship
    departments = db.relationship('Department', secondary='dept_assignments', backref=db.backref('user', lazy='dynamic')) #多対多
    ships = db.relationship('Ship', secondary='ship_assignments', back_populates='users')
    roles = db.relationship('Role', secondary='user_has_roles', backref=db.backref('user', lazy='dynamic')) #多対多
    def __init__(self, email, name, ms_email,ms_id):
        self.email = email  #インスタンスの属性として設定
        self.name = name
        self.ms_email = ms_email
        self.ms_id = ms_id

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False    


class Department(db.Model,TimestampMixin):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    def __init__(self, name):
        self.name = name

class DeptAssignment(db.Model,TimestampMixin):
    __tablename__ = 'dept_assignments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    def __init__(self, user_id, department_id):
        self.user_id = user_id
        self.department_id = department_id
    
class Ship(db.Model,TimestampMixin):
    __tablename__ = 'ships'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    ex_name = db.Column(db.String(128))
    former_name = db.Column(db.String(128))
    yard = db.Column(db.String(128))
    ship_no = db.Column(db.String(128))
    delivered = db.Column(db.DateTime)
    issued_Inscert = db.Column(db.DateTime)
    expiry_date = db.Column(db.DateTime)
    gross_tonn = db.Column(db.Numeric(8,2))
    operat_section_id = db.Column(db.Integer, db.ForeignKey('operat_sections.id'))
    navigation_area_id = db.Column(db.Integer, db.ForeignKey('navigation_areas.id'))
    #relationship
    summaries = db.relationship('Summary', backref = 'ship', uselist = False)
    summaries2 = db.relationship('Summary2', backref = 'ship', uselist = False)
    projects = db.relationship('Project', backref = 'ship', lazy ='dynamic')
    ship_owners = db.relationship('ShipOwner', backref = 'ship', lazy ='dynamic')
    # users = db.relationship('User', secondary='ship_assignments', backref=db.backref('ship', lazy='dynamic'))
    users = db.relationship('User', secondary='ship_assignments', back_populates='ships')
    ship_attachments = db.relationship('ShipAttachment', backref = 'ship', lazy ='dynamic')
    concerneds = db.relationship('Concerned', backref = 'ship', uselist = False) 
    schedules = db.relationship('Schedule', backref = 'ship', uselist = False)  
    documents = db.relationship('Document', backref='ship')
    def __init__(self, name, ex_name, former_name, yard, ship_no, delivered, issued_Inscert, expiry_date, gross_tonn, operat_section_id, navigation_area_id):
        self.name = name
        self.ex_name = ex_name
        self.former_name = former_name 
        self.yard = yard 
        self.ship_no = ship_no 
        self.delivered = delivered 
        self.issued_Inscert = issued_Inscert 
        self.expiry_date = expiry_date 
        self.gross_tonn = gross_tonn 
        self.operat_section_id = operat_section_id 
        self.navigation_area_id = navigation_area_id


class ShipAssignment(db.Model,TimestampMixin):
    __tablename__ = 'ship_assignments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    def __init__(self,user_id, ship_id):
        self.user_id = user_id
        self.ship_id = ship_id

class ShipAttachment(db.Model,TimestampMixin):
    __tablename__ = 'ship_attachments'
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    filename  = db.Column(db.String(255))
    originname  = db.Column(db.String(255))
    title  = db.Column(db.String(128))
    icon = db.Column(db.String(255))
    def __init__(self, ship_id, user_id, filename, orginname, title, icon):
        self.ship_id = ship_id
        self.user_id = user_id
        self.filename = filename
        self.originname = orginname
        self.title = title
        self.icon = icon

class OperatSection(db.Model,TimestampMixin):
    __tablename__ = 'operat_sections'
    id = db.Column(db.Integer, primary_key = True)
    section  = db.Column(db.String(128))
    memo = db.Column(db.Text)
    #relationship
    ships = db.relationship('Ship', backref = 'operat_sections', lazy ='dynamic')
    def __init__(self, section, memo):
        self.section = section
        self.memo = memo

class NavigationArea(db.Model,TimestampMixin):
    __tablename__ = 'navigation_areas'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)
    #relationship
    ships = db.relationship('Ship', backref = 'navigation_areas', lazy ='dynamic')
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Summary(db.Model,TimestampMixin):
    __tablename__ = 'summaries'
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    official_number  = db.Column(db.String(128))
    signal_code  = db.Column(db.String(128))
    engine_kw  = db.Column(db.String(128))
    pera_spec  = db.Column(db.String(128))
    me_model  = db.Column(db.String(128))
    me_sno  = db.Column(db.String(128))
    pera_sno  = db.Column(db.String(128))
    fire_equipt  = db.Column(db.String(128))
    full_length = db.Column(db.Numeric(8,2))
    lpp = db.Column(db.Numeric(8,2))
    breadth = db.Column(db.Numeric(8,2))
    beam_depth = db.Column(db.Numeric(8,2))
    mold_draft = db.Column(db.Numeric(8,2))
    draft_mark_F  = db.Column(db.String(128))
    draft_mark_A  = db.Column(db.String(128))
    fm_bl  = db.Column(db.String(128))
    draft_m  = db.Column(db.String(128))
    layer_2or3  = db.Column(db.String(128))
    winch_tension  = db.Column(db.String(255))
    stern_towboat  = db.Column(db.String(255))
    intake  = db.Column(db.String(128))
    exhaust  = db.Column(db.String(128))
    aux_engine  = db.Column(db.String(128))
    dk_machine_pp  = db.Column(db.String(128))
    fire_pump  = db.Column(db.String(128))
    harbor_gen  = db.Column(db.String(128))
    fire_extinguish  = db.Column(db.String(128))
    def __init__(self, ship_id, signal_code, official_number, engine_kw, pera_spec, me_model, me_sno, pera_sno, fire_equipt, full_length, lpp, breadth, beam_depth, mold_draft, draft_mark_F, draft_mark_A, fm_bl, draft_m, layer_2or3, winch_tension, stern_towboat, intake, exhaust, aux_engine, dk_machine_pp, fire_pump, harbor_gen, fire_extinguish):
        self.ship_id = ship_id
        self.signal_code = signal_code
        self.official_number = official_number
        self.engine_kw = engine_kw
        self.pera_spec = pera_spec
        self.me_model = me_model
        self.me_sno = me_sno
        self.pera_sno = pera_sno
        self.fire_equipt = fire_equipt
        self.full_length = full_length
        self.lpp = lpp
        self.breadth = breadth 
        self.beam_depth = beam_depth
        self.mold_draft = mold_draft
        self.draft_mark_F = draft_mark_F
        self.draft_mark_A = draft_mark_A
        self.fm_bl = fm_bl
        self.draft_m = draft_m
        self.layer_2or3 = layer_2or3
        self.winch_tension = winch_tension
        self.stern_towboat = stern_towboat
        self.intake = intake
        self.exhaust = exhaust
        self.aux_engine = aux_engine
        self.dk_machine_pp = dk_machine_pp
        self.fire_pump = fire_pump
        self.harbor_gen = harbor_gen
        self.fire_extinguish = fire_extinguish

class Summary2(db.Model,TimestampMixin):
    __tablename__ = 'summaries2'
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    insurance_type  = db.Column(db.String(128))
    international_ton  = db.Column(db.String(128))
    passenger_capacity  = db.Column(db.String(128))
    speed50 = db.Column(db.Numeric(8,2))
    speed100 = db.Column(db.Numeric(8,2))
    rpm_peller50 = db.Column(db.Numeric(8,2))
    rpm_peller100 = db.Column(db.Numeric(8,2))
    slip_rate50 = db.Column(db.Numeric(8,2))
    slip_rate100 = db.Column(db.Numeric(8,2))
    tug_force50 = db.Column(db.Numeric(8,2))
    tug_force100 = db.Column(db.Numeric(8,2))
    #relationship
    def __init__(self, ship_id, insurance_type, international_ton, passenger_capacity, speed50, speed100, rpm_peller50, rpm_peller100, slip_rate50, slip_rate100, tug_force50, tug_force100 ):
        self.ship_id = ship_id
        self.insurance_type = insurance_type
        self.international_ton = international_ton
        self.passenger_capacity = passenger_capacity
        self.speed50 = speed50
        self.speed100 = speed100
        self.rpm_peller50 = rpm_peller50
        self.rpm_peller100 = rpm_peller100
        self.slip_rate50 = slip_rate50
        self.slip_rate100 = slip_rate100
        self.tug_force50 = tug_force50
        self.tug_force100 = tug_force100
        

class ShipOwner(db.Model,TimestampMixin):
    __tablename__ = 'ship_owners'
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    name = db.Column(db.String(128))
    ratio = db.Column(db.Numeric(8,2))
    def __init__(self, ship_id, name, ratio ):
        self.ship_id = ship_id
        self.name = name
        self.ratio = ratio

class Concerned(db.Model,TimestampMixin):
    __tablename__ ='concerneds'  
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    operator = db.Column(db.String(128))
    borrower = db.Column(db.String(128))
    manager = db.Column(db.String(128))
    crew_arrange = db.Column(db.String(128))
    def __init__(self, ship_id, operator, borrower, manager, crew_arrange ):
        self.ship_id = ship_id
        self.operator = operator
        self.borrower = borrower
        self.manager = manager
        self.crew_arrange = crew_arrange

class ProCategory(db.Model,TimestampMixin):
    __tablename__ = 'pro_categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    memo = db.Column(db.Text)
    dock =db.Column(db.Boolean)
    projects = db.relationship('Project', backref = 'pro_category', lazy ='dynamic')
    def __init__(self, name, memo, dock ):
        self.name = name
        self.memo = memo
        self.dock = dock

class TaskCategory(db.Model, TimestampMixin):
    __tablename__ = 'task_categories'
    id = db.Column(db.Integer, primary_key = True)
    category_no = db.Column(db.String(128))
    name = db.Column(db.String(128))
    memo = db.Column(db.Text)
    tasks = db.relationship('Task', backref = 'task_category', lazy ='dynamic')
    def __init__(self, category_no, name, memo ):
        self.category_no = category_no
        self.name = name
        self.memo = memo

class Project(db.Model, TimestampMixin):
    __tablename__ ='projects'
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    name = db.Column(db.String(128))
    pro_category_id = db.Column(db.Integer, db.ForeignKey('pro_categories.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    completion = db.Column(db.DateTime)
    date_of_issue = db.Column(db.DateTime)
    users = db.relationship('User', secondary='pro_assignments', backref=db.backref('project', lazy='dynamic'))
    pro_attachments = db.relationship('ProAttachment', backref = 'project', lazy ='dynamic')
    pro_descriptions = db.relationship('ProDescription', backref = 'project', lazy ='dynamic') 
    tasks = db.relationship('Task', backref = 'project', lazy ='dynamic') 
    def __init__(self, ship_id, name, pro_category_id, start_date, end_date, completion, date_of_issue ):
        self.ship_id = ship_id
        self.name = name
        self.pro_category_id = pro_category_id
        self.start_date = start_date
        self.end_date = end_date
        self.completion = completion
        self.date_of_issue = date_of_issue

# class Task(db.Model, TimestampMixin):
    # __tablename__ = 'tasks'
    # id = db.Column(db.Integer, primary_key = True)
    # project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    # parent_id  = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    # name = db.Column(db.String(128))
    # task_categories = db.Column(db.Integer, db.ForeignKey('task_categories.id'))
    # task_attachments = db.relationship('TaskAttachment', backref = 'task', lazy ='dynamic')
    # task_descriptions = db.relationship('TaskDescription', backref = 'task', lazy ='dynamic') 
    # subtasks = db.relationship('Task', backref = 'task', lazy ='dynamic') 
    # ganttchart = db.Column(db.Integer)
    # start_date = db.Column(db.DateTime)
    # deadline = db.Column(db.DateTime)
    # completion = db.Column(db.DateTime)
    # priority = db.Column(db.Integer)
class Task(db.Model, TimestampMixin):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    name = db.Column(db.String(128))
    task_categories = db.Column(db.Integer, db.ForeignKey('task_categories.id'))
    task_attachments = db.relationship('TaskAttachment', backref='task', lazy='dynamic')
    task_descriptions = db.relationship('TaskDescription', backref='task', lazy='dynamic')
    subtasks = db.relationship('Task', backref=backref('parent', remote_side=[id]), lazy='dynamic', cascade="all, delete-orphan")
    ganttchart = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    completion = db.Column(db.DateTime)
    priority = db.Column(db.Integer)

    def __init__(self, project_id, parent_id, name, task_categories, ganttchart, start_date, deadline, completion, priority ):
        self.project_id = project_id
        self.parent_id = parent_id 
        self.name = name
        self.task_categories =task_categories
        self.ganttchart = ganttchart
        self.start_date = start_date
        self.deadline = deadline
        self.completion = completion
        self.priority = priority

class ProAttachment(db.Model, TimestampMixin):
    __tablename__ = 'pro_attachments'
    id = db.Column(db.Integer, primary_key = True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    filename  = db.Column(db.String(255))
    originname  = db.Column(db.String(255))
    title  = db.Column(db.String(128))
    icon = db.Column(db.String(255))
    def __init__(self, project_id, user_id, filename, originname, title, icon ):
        self.project_id = project_id
        self.user_id = user_id
        self.filename = filename
        self.originname = originname
        self.title = title
        self.icon = icon

class ProAssignment(db.Model, TimestampMixin):
    __tablename__ = 'pro_assignments'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    def __init__(self, user_id, project_id ):
        self.user_id = user_id
        self.project_id = project_id

class TaskAttachment(db.Model, TimestampMixin):
    __tablename__ = 'task_attachments'
    id = db.Column(db.Integer, primary_key = True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    filename  = db.Column(db.String(255))
    originname  = db.Column(db.String(255))
    title  = db.Column(db.String(128))
    icon = db.Column(db.String(255))
    def __init__(self, task_id, user_id, filename, originname, title, icon ):
        self.task_id = task_id
        self.user_id = user_id
        self.filename = filename
        self.originname =originname
        self.title = title
        self.icon = icon

class ProDescription(db.Model, TimestampMixin):
    __tablename__ = 'pro_descriptions'
    id = db.Column(db.Integer, primary_key = True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    memo = db.Column(db.Text)
    def __init__(self, project_id, user_id, memo):
        self.project_id = project_id
        self.user_id = user_id
        self.memo = memo

class TaskDescription(db.Model, TimestampMixin):
    __tablename__ = 'task_descriptions'
    id = db.Column(db.Integer, primary_key = True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    memo = db.Column(db.Text)
    def __init__(self, task_id, user_id, memo):
        self.task_id = task_id
        self.user_id = user_id
        self.memo = memo

class Role(db.Model, TimestampMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    def __init__(self, name):
        self.name = name

class UserHasRoles(db.Model, TimestampMixin):
    __tablename__ = 'user_has_roles'
    id = db.Column(db.Integer, primary_key = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __init__(self, role_id, user_id ):
        self.role_id = role_id
        self.user_id = user_id

class Schedule(db.Model, TimestampMixin):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key = True)
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    interim_start1 = db.Column(db.Date)
    interim_dline1 = db.Column(db.Date)
    periodic_start1 = db.Column(db.Date)
    periodic_dline1 = db.Column(db.Date)
    interim_start2 = db.Column(db.Date)
    interim_dline2 = db.Column(db.Date)
    periodic_start2 = db.Column(db.Date)
    periodic_dline2 = db.Column(db.Date)
    def __init__(self, ship_id, interim_start1, interim_dline1, periodic_start1, periodic_dline1, interim_start2, interim_dline2, periodic_start2, periodic_dline2):
        self.ship_id = ship_id
        self.interim_start1 = interim_start1
        self.interim_dline1 = interim_dline1
        self.periodic_start1 = periodic_start1
        self.periodic_dline1 = periodic_dline1
        self.interim_start2 = interim_start2
        self.interim_dline2 = interim_dline2
        self.periodic_start2 = periodic_start2
        self.periodic_dline2 = periodic_dline2

class DocTemplate(db.Model, TimestampMixin):
    __tablename__ = 'doc_templates'
    id = db.Column(db.Integer, primary_key = True)
    doc_code = db.Column(db.String(12))
    name = db.Column(db.String(128))
    file_name = db.Column(db.String(128))
    file_id = db.Column(db.String(255))
    file_category_id = db.Column(db.Integer, db.ForeignKey('file_categories.id'))
    def __init__(self, doc_code, name, file_name, file_id, file_category_id ):
        self.doc_code = doc_code
        self.name = name
        self.file_name = file_name
        self.file_id = file_id
        self.file_category_id = file_category_id


class FileCategory(db.Model, TimestampMixin):
    __tablename__ = 'file_categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    doc_templates = db.relationship('DocTemplate', backref='file_category', lazy='dynamic')
    documents = db.relationship('Document', backref='file_category', lazy='dynamic')
    def __init__(self, name):
        self.name = name

class Document(db.Model, TimestampMixin):
    __textname__ = 'documents'
    id = db.Column(db.Integer, primary_key = True)
    doc_code = db.Column(db.String(12))
    name = db.Column(db.String(128))
    file_name = db.Column(db.String(128))
    file_id = db.Column(db.String(255))
    file_category_id = db.Column(db.Integer, db.ForeignKey('file_categories.id'))
    signature = db.Column(db.String(128))
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'))
    def __init__(self, doc_code, name, file_name, file_id,file_category_id, signature, ship_id ):
        self.doc_code = doc_code
        self.name = name
        self.file_name = file_name
        self.file_id = file_id
        self.file_category_id = file_category_id
        self.signature = signature
        self.ship_id = ship_id















   


        
        
        
   
    

