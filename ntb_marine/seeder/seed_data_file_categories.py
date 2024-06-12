from ntb_marine import db
from ntb_marine.models import FileCategory

def file_categorySeeder():
    file_category01 = FileCategory(name = "船長・機関長引継書")
    file_category02 = FileCategory(name = "船内安全委員会")
    file_category03 = FileCategory(name = "損傷報告・修繕申請")
    file_category04 = FileCategory(name = "入渠・補償工事関連")
    file_category05 = FileCategory(name = "確認チェックリスト")
    file_category06 = FileCategory(name = "備品管理台帳")
    file_category07 = FileCategory(name = "注文書(船用品・部品・曳船索)")
    file_category08 = FileCategory(name = "補油(A油・潤滑油)")
    file_category09 = FileCategory(name = "事故・不具合")
    file_category10 = FileCategory(name = "その他")
    db.session.add_all([file_category01,file_category02,file_category03,file_category04,file_category05,file_category06,file_category07,file_category08,file_category09,file_category10])
