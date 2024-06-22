from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import DocTemplate

# def __init__(self, ship_id, operator, borrower, manager, crew_arrange ):
#         self.ship_id = ship_id
#         self.operator = operator
#         self.borrower = borrower
#         self.manager = manager
#         self.crew_arrange = crew_arrange

def doc_templatesSeeder():
    doct01 = DocTemplate(doc_code= "10010", name = "不具合事項改善要望書", file_name = "10010：不具合事項改善要望書：10-000-01改訂.docx", file_id="01PADKQGWPBZ6IENNX5RBZAY4TZT22YLQ5", file_category_id =9 )
    doct02 = DocTemplate(doc_code= "10020", name = "是正措置通知書・報告書", file_name = "10020：是正措置通知書・報告書：10-000-02.docx", file_id="01PADKQGSWD3HR6CYBPFBJQFGUXBZGXFOB", file_category_id =9 )
    doct03 = DocTemplate(doc_code= "11130", name = "改善依頼書・報告書", file_name = "11130：改善依頼書・報告書：11-010-03.docx", file_id="01PADKQGXOJ4R6ZFFYPBDIUHRDAR7U2VRX", file_category_id =9 )
    doct04 = DocTemplate(doc_code= "6110", name = "船長引継記録簿", file_name = "6110：船長引継記録簿：06-010-01改訂.xlsx", file_id="01PADKQGQBD3SNPI3HFFC2GIZYGO27EJLZ", file_category_id =1 )
    doct05 = DocTemplate(doc_code= "6120", name = "機関長引継記録簿", file_name = "6120：機関長引継記録簿：06-010-02改訂.xlsx", file_id="01PADKQGTU2RPHNP55FNG2TJ6XHIVMUABZ", file_category_id =1 )
    doct06 = DocTemplate(doc_code= "6210", name = "発航前検査等記録簿", file_name = "6210：発航前検査等記録簿：06-020-01改訂.xlsx", file_id="01PADKQGQNITL6ZP4SRRH36WXHS7CF3IRG", file_category_id =10 )
    doct07 = DocTemplate(doc_code= "6510", name = "証書等船内備付書類点検表", file_name = "6510：証書等船内備付書類点検表：06-050-01改訂.xlsx", file_id="01PADKQGQNT6YSWDRJINCZT35HQ3HMHBF7", file_category_id =10 )
    doct08 = DocTemplate(doc_code= "6710", name = "安全衛生チェックリスト", file_name = "6710：安全衛生チェックリスト：06-070-01改訂.xlsx", file_id="01PADKQGXAIBAG7S5ZZBBIFOOUUVWREDS4", file_category_id =2 )
    doct09 = DocTemplate(doc_code= "6720", name = "船内安全衛生委員会議事録", file_name = "6720：船内安全衛生委員会議事録：06-070-02改訂.xlsx", file_id="01PADKQGUXBXJGC7UVANCZBUOQBWX4ZMRG", file_category_id =2 )
    doct10 = DocTemplate(doc_code= "7110", name = "補油作業安全確認表", file_name = "7110：補油作業安全確認表：07-010-01改訂.xlsx", file_id="01PADKQGT5EBDYBGPI5JEY7O5Y2NVX4VVY", file_category_id =8 )
    doct11 = DocTemplate(doc_code= "8111", name = "船体 損傷報告書", file_name = "8111：船体 損傷報告書：08-010-01改訂.docx", file_id="01PADKQGXW6FMKNWSHGFFLB24XBJV5VR5G", file_category_id =3 )
    doct12 = DocTemplate(doc_code= "8112", name = "機関 損傷報告書", file_name = "8112：機関 損傷報告書：08-010-01改訂.docx", file_id="01PADKQGSMX3LPNMDL4JHJXSTTDR5YXIFQ", file_category_id =3 )
    doct13 = DocTemplate(doc_code= "8121", name = "甲板 修繕施工申請書", file_name = "8121：甲板 修繕施工申請書：08-010-02改定.xlsx", file_id="01PADKQGTUVH5X2Z526JGZFDTUHTRH4YBE", file_category_id =3 )
    doct14 = DocTemplate(doc_code= "8122", name = "機関 修繕施工申請書", file_name = "8122：機関 修繕施工申請書：08-010-02改訂.xlsx", file_id="01PADKQGXSFV6KLB4GJVEL7AHOO5VL6XCF", file_category_id =3 )
    doct15 = DocTemplate(doc_code= "8131", name = "補償工事報告書 甲板", file_name = "8131：補償工事報告書 甲板：08-010-03改訂.xlsx", file_id="01PADKQGS2C26EABKF7NBKUI2U7FE76D7R", file_category_id =4 )
    doct16 = DocTemplate(doc_code= "8132", name = "補償工事報告書 機関", file_name = "8132：補償工事報告書 機関：08-010-03改訂.xlsx", file_id="01PADKQGVWWBLVQHG725CJ5LA7YX2J6M3O", file_category_id =4 )
    doct17 = DocTemplate(doc_code= "8211", name = "甲板 入渠工事申請書", file_name = "8211：甲板 入渠工事申請書：08-020-01改訂.xlsx", file_id="01PADKQGWVQZR2G5XVUFG24BEC7Q4Z3GTW", file_category_id =4 )
    doct18 = DocTemplate(doc_code= "8212", name = "機関 入渠工事申請書", file_name = "8212：機関 入渠工事申請書：08-020-01改訂.xlsx", file_id="01PADKQGX4AYQHHWCNJJFI7VPADKNZHXXZ", file_category_id =4 )
    doct19 = DocTemplate(doc_code= "8221", name = "甲板 入渠工事仕様書", file_name = "8221：甲板 入渠工事仕様書：08-020-02改訂.xlsx", file_id="01PADKQGW7WUWUCWZEXRF2Q27EOCBUFYF5", file_category_id =4 )
    doct20 = DocTemplate(doc_code= "8222", name = "機関 入渠工事仕様書", file_name = "8222：機関 入渠工事仕様書：08-020-02改訂.xlsx", file_id="01PADKQGQNPRBQWFU5T5ELHJPA7CQP2TR3", file_category_id =4 )
    doct21 = DocTemplate(doc_code= "8330", name = "重要機器作動確認ﾁｪｯｸﾘｽﾄ", file_name = "8330：重要機器作動確認ﾁｪｯｸﾘｽﾄ：08-030-03改訂.xlsx", file_id="01PADKQGUMYD4KAUWQVZE275DUELPKSEEY", file_category_id =5 )
    doct22 = DocTemplate(doc_code= "8331", name = "甲板 重要機器作動確認ﾁｪｯｸﾘｽﾄ", file_name = "8331：甲板 重要機器作動確認ﾁｪｯｸﾘｽﾄ：08-030-03改訂.xlsx", file_id="01PADKQGSWAT74DAWYJVG3FACDTICFPHJ4", file_category_id =5 )
    doct23 = DocTemplate(doc_code= "8332", name = "機関 重要機器作動確認ﾁｪｯｸﾘｽﾄ", file_name = "8332：機関 重要機器作動確認ﾁｪｯｸﾘｽﾄ：08-030-03改訂.xlsx", file_id="01PADKQGTOW6ENJDMV4JDIW24IAUI26DEX", file_category_id =5 )
    doct24 = DocTemplate(doc_code= "8410", name = "備品管理台帳（甲板）", file_name = "8410：備品管理台帳（甲板）：08-040-01改訂.xlsx", file_id="01PADKQGU3M6MUM7A7YFHLEQ5KYQZOIPND", file_category_id =6 )
    doct25 = DocTemplate(doc_code= "8420", name = "備品管理台帳（機関）", file_name = "8420：備品管理台帳（機関）：08-040-02改訂.xlsx", file_id="01PADKQGR5EAPSTHXELJCKBVFQ4ZBCJ3ID", file_category_id =6 )
    doct26 = DocTemplate(doc_code= "8431", name = "甲板 船用品注文書", file_name = "8431：甲板 船用品注文書：08-040-03改訂.xlsx", file_id="01PADKQGQVUOCKEVM2MNALADJFJSA7QIXP", file_category_id =7 )
    doct27 = DocTemplate(doc_code= "8432", name = "機関 船用品注文書", file_name = "8432：機関 船用品注文書：08-040-03改訂.xlsx", file_id="01PADKQGUK7UBFNWVEUNBK3TGF7FL67UUH", file_category_id =7 )
    doct28 = DocTemplate(doc_code= "8441", name = "甲板 機器補修部品注文書", file_name = "8441：甲板 機器補修部品注文書：08-040-04改訂.xlsx", file_id="01PADKQGTZT6SLA7D7NVHJRAG643CTRKN3", file_category_id =7 )
    doct29 = DocTemplate(doc_code= "8442", name = "機関 機器補修部品注文書", file_name = "8442：機関 機器補修部品注文書：08-040-04改訂.xlsx", file_id="01PADKQGR3JS2MXKJQRBAIQFV5G7BKOTSM", file_category_id =7 )
    doct30 = DocTemplate(doc_code= "8450", name = "曳船索・報告書／注文書", file_name = "8450：曳船索・報告書／注文書：08-040-05（改定）.xlsx", file_id="01PADKQGWRPVDMD7ZER5CIOOD32F4WPJAA", file_category_id =7 )
    doct31 = DocTemplate(doc_code= "8460", name = "Ａ重油依頼書", file_name = "8460：Ａ重油依頼書：08-040-06改訂.xlsx", file_id="01PADKQGWSLXZITWEBI5B3P2H6J6UEXGKU", file_category_id =8 )
    doct32 = DocTemplate(doc_code= "8470", name = "潤滑油依頼書", file_name = "8470：潤滑油依頼書：08-040-07改訂.xlsx", file_id="01PADKQGRZDVV4B6RSZJC36XQCHDGBEXC4", file_category_id =8 )
    doct33 = DocTemplate(doc_code= "9110", name = "事故報告書", file_name = "9110：事故報告書：09-010-01改訂.docx", file_id="01PADKQGUOVV2TBOG3JNC3F344X7LRZVD4", file_category_id =9 )
    db.session.add_all([doct01,doct02,doct03,doct04,doct05,doct06,doct07,doct08,doct09,doct10,doct11,doct12,doct13,doct14,doct15,doct16,doct17,doct18,doct19,doct20, doct21, doct22, doct23, doct24, doct25, doct26, doct27, doct28,doct29, doct30, doct31, doct32, doct33])

