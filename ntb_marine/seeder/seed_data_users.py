from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import User


def usersSeeder():
    users01 = User( name = "太田 正紀" , email = "masanori.ota@nihon-eisen.com " , ms_email = "A47g071@molgroup.com", ms_id="")
    users02 = User( name = "坂倉 繁行" , email = "shigeyuki.sakakura@nihon-eisen.com " , ms_email = "A47g017@molgroup.com", ms_id="")
    users03 = User( name = "髙松 一憲" , email = "kazunori.takamatsu@nihon-eisen.com " , ms_email = "A47g070@molgroup.com", ms_id="")
    users04 = User( name = "二ツ石 聖示" , email = "seiji.futatsuishi@nihon-eisen.com " , ms_email = "A47m080@molgroup.com", ms_id="")
    users05 = User( name = "三宅 陸平" , email = "rikuhei.miyake@nihon-eisen.com " , ms_email = "A47m087@molgroup.com", ms_id="")
    users06 = User( name = "宮本 強" , email = "tsuyoshi.miyamoto@nihon-eisen.com" , ms_email = "A47g039@molgroup.com", ms_id="")
    users07 = User( name = "植田 廣幸" , email = "hiroyuki.ueda@nihon-eisen.com" , ms_email = "A47m027@molgroup.com", ms_id="")
    users08 = User( name = "黒田 秀明" , email = "hideaki.kuroda@nihon-eisen.com" , ms_email = "A47g079@molgroup.com", ms_id="")
    users09 = User( name = "若狭 吉晴" , email = "yoshiharu.wakasa@nihon-eisen.com" , ms_email = "A47g077@molgroup.com", ms_id="")
    users10 = User( name = "荒川 純一" , email = "junichi.arakawa@nihon-eisen.com" , ms_email = "A47g082@molgroup.com", ms_id="")
    users11 = User( name = "青木 宏之" , email = "hiroyuki.aoki@nihon-eisen.com  " , ms_email = "A47g054@molgroup.com", ms_id="")
    users12 = User( name = "堀 容子" , email = "yoko.hori@nihon-eisen.com" , ms_email = "A47g044@molgroup.com", ms_id="")
    users13 = User( name = "清水 斉" , email = "h-shimizu@eikichikaiun.co.jp" , ms_email = "", ms_id="")
    users14 = User( name = "増田 数一" , email = "k-masuda@eikichikaiun.co.jp" , ms_email = "", ms_id="")
    users15 = User( name = "大平 芳生" , email = "yoshio.ohira@nihon-eisen.com" , ms_email = "A47m088@molgroup.com", ms_id="")
    users16 = User( name = "Hideaki Kuroda" , email = "kurodah@gmail.com" , ms_email = "kurodah@gmail.com", ms_id="")
    db.session.add_all([users01,users02,users03,users04,users05,users06,users07,users08,users09,users10,users11,users12,users13,users14,users15,users16])
