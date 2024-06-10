from ship_management import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ship_management.models import User


def usersSeeder():
    users01 = User( name = "太田 正紀" , email = "masanori.ota@nihon-eisen.com " ,  password = "password123", ms_id = "a47g071@molgroup.com")
    users02 = User( name = "坂倉 繁行" , email = "shigeyuki.sakakura@nihon-eisen.com " ,  password = "password123", ms_id = "a47g017@molgroup.com")
    users03 = User( name = "髙松 一憲" , email = "kazunori.takamatsu@nihon-eisen.com " ,  password = "password123", ms_id = "a47g070@molgroup.com")
    users04 = User( name = "二ツ石 聖示" , email = "seiji.futatsuishi@nihon-eisen.com " ,  password = "password123", ms_id = "a47m080@molgroup.com")
    users05 = User( name = "三宅 陸平" , email = "rikuhei.miyake@nihon-eisen.com " ,  password = "password123", ms_id = "a47m087@molgroup.com")
    users06 = User( name = "宮本 強" , email = "tsuyoshi.miyamoto@nihon-eisen.com" ,  password = "password123", ms_id = "a47g039@molgroup.com")
    users06 = User( name = "植田 廣幸" , email = "hiroyuki.ueda@nihon-eisen.com" ,  password = "password123", ms_id = "a47m027@molgroup.com")
    users07 = User( name = "黒田 秀明" , email = "hideaki.kuroda@nihon-eisen.com" ,  password = "password123", ms_id = "a47g079@molgroup.com")
    users08 = User( name = "吉田 美弥" , email = "miya.yoshida@nihon-eisen.com " ,  password = "password123", ms_id = "")
    users09 = User( name = "岩本 香利" , email = "kaori.iwamoto@nihon-eisen.com" ,  password = "password123", ms_id = "")
    users10 = User( name = "若狭 吉晴" , email = "yoshiharu.wakasa@nihon-eisen.com" ,  password = "password123", ms_id = "a47g077@molgroup.com")
    users11 = User( name = "荒川 純一" , email = "junichi.arakawa@nihon-eisen.com" ,  password = "password123", ms_id = "a47g082@molgroup.com")
    users12 = User( name = "青木 宏之" , email = "hiroyuki.aoki@nihon-eisen.com  " ,  password = "password123", ms_id = "a47g054@molgroup.com")
    users13 = User( name = "堀 容子" , email = "yoko.hori@nihon-eisen.com" ,  password = "password123", ms_id = "a47g044@molgroup.com")
    users14 = User( name = "村知 一世" , email = "kazuyo.murachi@nihon-eisen.com" ,  password = "password123", ms_id = "")
    users15 = User( name = "井上 佳代" , email = "kayo.inoue@nihon-eisen.com" ,  password = "password123", ms_id = "")
    users16 = User( name = "柄谷 仁美" , email = "hitomi.karatani@nihon-eisen.com" ,  password = "password123", ms_id = "")
    users17 = User( name = "小俣 真美" , email = "mami.omata@nihon-eisen.com" ,  password = "password123", ms_id = "")
    users18 = User( name = "西尾 哲郎" , email = "tetsuro.nishio@nihon-eisen.com" ,  password = "password123", ms_id = "")
    users19 = User( name = "田村 啓造" , email = "keizo.tamura@nihon-eisen.com" ,  password = "password123", ms_id = "a47g015@molgroup.com")
    users20 = User( name = "清水 斉" , email = "h-shimizu@eikichikaiun.co.jp" ,  password = "password123", ms_id = "")
    users21 = User( name = "増田 数一" , email = "k-masuda@eikichikaiun.co.jp" ,  password = "password123", ms_id = "")
    users22 = User( name = "大平 芳生" , email = "yoshio.ohira@nihon-eisen.com" ,  password = "password123", ms_id = "a47m088@molgroup.com")
    users23 = User( name = "Hideaki Kuroda" , email = "kurodah@gmail.com" ,  password = "password123", ms_id = "")
    db.session.add_all([users01,users02,users03,users04,users05,users06,users06,users07,users08,users09,users10,users11,users12,users13,users14,users15,users16,users17,users18,users19,users20,users21,users22,users23])
