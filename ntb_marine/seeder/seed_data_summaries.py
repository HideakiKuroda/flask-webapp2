from ntb_marine import db
# from ship_management.models import User,UserDescription,Department,DeptAssignment,Ship,ShipAssignment,ShipAttachment,OperatSection,NavigationArea,Summary,Summary2,ShipOwner,Concerned,ProCategory,TaskCategory,Project,Task,ProAttachment,ProAssignment,TaskAttachment,ProDescription,TakDescription,Role,UserHasRoles,Schedule
from ntb_marine.models import Summary

def SummarySeeder():
    summary01 = Summary(ship_id = 1, official_number = '140272', signal_code = 'JD2202', engine_kw = '3600', pera_spec = 'ZP-21-3A', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '23892/23893', pera_sno = 'P0835/0836', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　上部', exhaust = 'ZP後方', aux_engine = '', dk_machine_pp = '主機右舷付', fire_pump = '主機左舷付', harbor_gen = '機関室後部', fire_extinguish = '粉末消火設備')
    summary02 = Summary(ship_id = 2, official_number = '141151', signal_code = 'JD2999', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '25341/25342', pera_sno = 'P1802/1803', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　上部', exhaust = 'ZP後方', aux_engine = 'ﾔﾝﾏｰ4HAL2-TN1', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = '甲板：ﾏｽﾄ後部', fire_extinguish = '粉末消火設備')
    summary03 = Summary(ship_id = 3, official_number = '142670', signal_code = 'JD4020', engine_kw = '4500', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '27435/27436', pera_sno = 'P3313/3314', fire_equipt = '', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = 'ﾔﾝﾏｰ4HAL2-TN1', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = '', fire_extinguish = '粉末消火設備')
    summary04 = Summary(ship_id = 4, official_number = '143768', signal_code = 'JD4749', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '28334/28335', pera_sno = 'P3906/3907', fire_equipt = '', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = 'ﾔﾝﾏｰ4HAL2-TN1', dk_machine_pp = '機関室：独立', fire_pump = '機関室：独立', harbor_gen = '', fire_extinguish = '粉末消火設備')
    summary05 = Summary(ship_id = 5, official_number = '132373', signal_code = 'JJ3847', engine_kw = '3600', pera_spec = 'KST-180ZF/A', me_model = 'ﾔﾝﾏｰZ280-EN', me_sno = '', pera_sno = '', fire_equipt = '', full_length = '34', lpp = '29', breadth = '9.2', beam_depth = '4.2', mold_draft = '3.2', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2層', winch_tension = '船首 1船尾 1', stern_towboat = '門型ﾋﾞｯﾄﾑｱﾘﾝｸﾞﾎｰﾙ', intake = 'ﾌｧﾝﾈﾙ横菌型通風筒　２', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = 'ｼｮｳﾜｾｲｷｺｳｷﾞｮｳ6HAL-N', dk_machine_pp = '機関室：独立', fire_pump = '', harbor_gen = '', fire_extinguish = '')
    summary06 = Summary(ship_id = 6, official_number = '136164', signal_code = 'JK5611', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '23143/23144', pera_sno = 'P0471/0472', fire_equipt = '3・4', full_length = '37', lpp = '33.2', breadth = '8.8', beam_depth = '3.9', mold_draft = '3', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = '', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '主機左舷付', fire_pump = '主機右舷付', harbor_gen = '', fire_extinguish = '粉末消火設備' )
    summary07 = Summary(ship_id = 7, official_number = '141351', signal_code = 'JD3131', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '25625/25626', pera_sno = 'P1996/1997', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備' )
    summary08 = Summary(ship_id = 8, official_number = '144125', signal_code = 'JD4992', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '28621/28622', pera_sno = 'P4086/4087', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.4', draft_m = '＋30', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = '', intake = 'ﾏｽﾄ　上部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = 'ﾔﾝﾏｰ4HAL2-TN1', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = '機関室上後方', fire_extinguish = '粉末消火設備' )
    summary09 = Summary(ship_id = 9, official_number = '143218', signal_code = 'JD4355', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX-CR', me_sno = '27841/27842', pera_sno = 'P3653/3654', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.3', draft_m = '＋20', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary10 = Summary(ship_id = 10, official_number = '142773', signal_code = 'JD4080', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '27511/27512', pera_sno = 'P3395/3396', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.3', draft_m = '＋20', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary11 = Summary(ship_id = 11, official_number = '142112', signal_code = 'JD3644', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '26591/26592', pera_sno = 'P2689/2690', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.3', draft_m = '＋20', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary12 = Summary(ship_id = 12, official_number = '144505', signal_code = 'JD5245', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX-CR', me_sno = '28846/28847', pera_sno = 'P4254/4255', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.4', draft_m = '＋30', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = '', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary13 = Summary(ship_id = 13, official_number = '143839', signal_code = 'JD4804', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '28376/28377', pera_sno = 'P3926/3927', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.4', draft_m = '＋30', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary14 = Summary(ship_id = 14, official_number = '140804', signal_code = 'JD2765', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '24852/24853', pera_sno = 'P1405/1406', fire_equipt = '3・4', full_length = '42', lpp = '36.5', breadth = '9', beam_depth = '3.8', mold_draft = '3.1', draft_mark_F = '1.4～3.4', draft_mark_A = '3.2～4.0', fm_bl = '3.3', draft_m = '＋20', layer_2or3 = '3層', winch_tension = '船首 1', stern_towboat = '', intake = 'ﾏｽﾄ　上部', exhaust = 'ZP後方', aux_engine = '', dk_machine_pp = '主機右舷付', fire_pump = '主機左舷付', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary15 = Summary(ship_id = 15, official_number = '143400', signal_code = 'JD4484', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾔﾝﾏｰ6EY26DF', me_sno = '1373/1374', pera_sno = 'P3741/3742', fire_equipt = '3・4', full_length = '43.6', lpp = '38.6', breadth = '9.2', beam_depth = '4', mold_draft = '3.15', draft_mark_F = '1.4～3.6', draft_mark_A = '3.4～4.2', fm_bl = '3.35', draft_m = '＋20', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = '', intake = 'ﾏｽﾄ　上部', exhaust = 'ﾌｧﾝﾈﾙ×２', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = '機関室後部', fire_extinguish = '粉末消火設備')
    summary16 = Summary(ship_id = 16, official_number = '141755', signal_code = 'JD3406', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '26016/26017', pera_sno = 'P2293/2294', fire_equipt = '3・4', full_length = '37.5', lpp = '33', breadth = '9.8', beam_depth = '4.2', mold_draft = '3.2', draft_mark_F = '1.4～3.2', draft_mark_A = '3.2～4.2', fm_bl = '3.4', draft_m = '＋20', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary17 = Summary(ship_id = 17, official_number = '141745', signal_code = 'JD3399', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾔﾝﾏｰ6EY-26W', me_sno = '0814/0815', pera_sno = 'P2335/2336', fire_equipt = '3・4', full_length = '34', lpp = '29', breadth = '9.8', beam_depth = '4.1', mold_draft = '3.2', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1船尾 1', stern_towboat = 'ZP室上部ﾑｱﾘﾝｸﾞﾎｰﾙ', intake = '２ﾌｧﾝﾈﾙ間菌型通風筒　２', exhaust = 'ﾌｧﾝﾈﾙ×２', aux_engine = '', dk_machine_pp = '機関室：独立', fire_pump = '機関室：独立', harbor_gen = '', fire_extinguish = '粉末消火設備')
    summary18 = Summary(ship_id = 18, official_number = '142593', signal_code = 'JD3967', engine_kw = '3600', pera_spec = 'ZP-21', me_model = 'ﾔﾝﾏｰ6EY26W', me_sno = '1100/1101', pera_sno = 'P3259/3260', fire_equipt = '3・4', full_length = '32.8', lpp = '28', breadth = '9.6', beam_depth = '4.1', mold_draft = '3.2', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = '', intake = '２ﾌｧﾝﾈﾙ間菌型通風筒　２', exhaust = 'ﾌｧﾝﾈﾙ×２', aux_engine = '', dk_machine_pp = '機関室：独立', fire_pump = '機関室：独立', harbor_gen = '', fire_extinguish = '粉末消火設備')
    summary19 = Summary(ship_id = 19, official_number = '140641', signal_code = 'JD2507', engine_kw = '3752', pera_spec = '2 翼', me_model = 'ﾐﾂﾋﾞｼS16K-MTK', me_sno = '13758/13759', pera_sno = '', fire_equipt = '3・4', full_length = '38', lpp = '34.8', breadth = '6.2', beam_depth = '3.3', mold_draft = '1.45', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2層', winch_tension = '', stern_towboat = '', intake = '甲板上', exhaust = '船尾', aux_engine = 'ﾔﾝﾏｰ6CHL-TN', dk_machine_pp = '', fire_pump = '機関室：独立', harbor_gen = '機関室：独立', fire_extinguish = '粉末消火設備')
    summary20 = Summary(ship_id = 20, official_number = '136004', signal_code = 'JJ4054', engine_kw = '2000', pera_spec = '2 翼', me_model = 'ﾆｲｶﾞﾀ6MG17HX', me_sno = '23307/23308', pera_sno = '', fire_equipt = '3・4', full_length = '28', lpp = '27.46', breadth = '6', beam_depth = '3', mold_draft = None, draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '1.5層', winch_tension = '', stern_towboat = '', intake = '甲板上', exhaust = '船尾', aux_engine = 'ﾔﾝﾏｰ6CHL-N', dk_machine_pp = '', fire_pump = '主機右舷付', harbor_gen = '機関室：独立', fire_extinguish = '粉末消火設備')
    summary21 = Summary(ship_id = 21, official_number = '142190', signal_code = 'JD3701', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '26593/26594', pera_sno = 'P2691/2692', fire_equipt = '3・4', full_length = '37.5', lpp = '33', breadth = '9.8', beam_depth = '4.2', mold_draft = '3.2', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ　下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = '', fire_extinguish = '粉末消火設備')
    summary22 = Summary(ship_id = 22, official_number = '143103', signal_code = 'JD4287', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX-CR', me_sno = '27743/27744', pera_sno = 'P3602/3603', fire_equipt = '3・4', full_length = '40', lpp = '35.25', breadth = '9.2', beam_depth = '3.8', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = '', intake = 'ﾏｽﾄ　後部', exhaust = 'ZP後部', aux_engine = '', dk_machine_pp = '再船首区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary23 = Summary(ship_id = 23, official_number = '142353', signal_code = 'JD3811', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '26954/26955', pera_sno = 'P2960/2961', fire_equipt = '3・4', full_length = '37.5', lpp = '33.2', breadth = '9', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '3層', winch_tension = '船首 1', stern_towboat = '', intake = '２層後部', exhaust = 'ZP後部', aux_engine = '', dk_machine_pp = '再船首区画', fire_pump = '機関室：独立', harbor_gen = '機関室上後方', fire_extinguish = '粉末消火設備')
    summary24 = Summary(ship_id = 24, official_number = '136195', signal_code = 'JK5631', engine_kw = '4000', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '23433/23434', pera_sno = 'P0592/0593', fire_equipt = '3・4', full_length = '37.5', lpp = '33.2', breadth = '9', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.4～3.6', draft_mark_A = '2.8～4.0', fm_bl = '3.4', draft_m = '＋30', layer_2or3 = '3層', winch_tension = '船首 2', stern_towboat = '', intake = '２層後部', exhaust = 'ZP後部', aux_engine = '主機左舷付×1独立×１', dk_machine_pp = '主機右舷付', fire_pump = '機関室：独立', harbor_gen = '機関室上後方', fire_extinguish = '粉末消火設備')
    summary25 = Summary(ship_id = 25, official_number = '141477', signal_code = 'JD3218', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '25719/25720', pera_sno = 'P2062/2063', fire_equipt = '3・4', full_length = '37.5', lpp = '33.2', breadth = '9', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.4～3.6', draft_mark_A = '3.0～4.0', fm_bl = '3.4', draft_m = '＋30', layer_2or3 = '3層', winch_tension = '船首 1', stern_towboat = '', intake = '2層後部', exhaust = 'ZP後部', aux_engine = '', dk_machine_pp = '再船首区画', fire_pump = '機関室：独立', harbor_gen = '機関室上後方', fire_extinguish = '粉末消火設備')
    summary26 = Summary(ship_id = 26, official_number = '143281', signal_code = 'JD4397', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '27899/27900', pera_sno = 'P3687/3688', fire_equipt = '3・4', full_length = '37.5', lpp = '33.2', breadth = '9', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.4～3.6', draft_mark_A = '3.0～4.0', fm_bl = '3.4', draft_m = '＋30', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = '', intake = 'ﾏｽﾄ　後部', exhaust = 'ZP後部', aux_engine = '', dk_machine_pp = '再船首区画', fire_pump = '機関室：独立', harbor_gen = '機関室上後方', fire_extinguish = '粉末消火設備')
    summary27 = Summary(ship_id = 27, official_number = '142452', signal_code = 'JD3878', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '', pera_sno = '', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '1.2～3.4', draft_mark_A = '3.2～4.2', fm_bl = '3.3', draft_m = '＋20', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ﾄｰｲﾝｸﾞﾋﾞｯﾄH:ﾛｰﾌﾟｶﾞｰﾄﾞ', intake = 'ﾏｽﾄ下部', exhaust = 'ﾌｧﾝﾈﾙ×１', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary28 = Summary(ship_id = 28, official_number = '141507', signal_code = 'JD3238', engine_kw = '4400', pera_spec = 'ZP-31', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '25807/25808', pera_sno = 'P2129/2130', fire_equipt = '3・4', full_length = '33.3', lpp = '29', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = '', intake = 'ﾏｽﾄ上部', exhaust = '主機ZP後部ﾌｧﾝﾈﾙ×２', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '機関室：独立', harbor_gen = '機関室上後方', fire_extinguish = '粉末消火設備')
    summary29 = Summary(ship_id = 29, official_number = '135964', signal_code = 'JJ4021', engine_kw = '3600', pera_spec = 'ZP-21-3A', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '', pera_sno = '', fire_equipt = '3・4', full_length = '33.9', lpp = '29.5', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2', stern_towboat = 'ｸﾛｽﾋﾞｯﾄﾄｰｲﾝｸﾞｱｰﾁ', intake = 'ﾏｽﾄ　上部', exhaust = 'ZP後方', aux_engine = '', dk_machine_pp = '主機右舷付', fire_pump = '主機左舷付', harbor_gen = '機関室後部', fire_extinguish = '粉末消火設備')
    summary30 = Summary(ship_id = 30, official_number = '131610', signal_code = 'JH3199', engine_kw = '3600', pera_spec = 'ZP-21-3A', me_model = 'ﾆｲｶﾞﾀ6L28HX', me_sno = '', pera_sno = '', fire_equipt = '3・4', full_length = '33.9', lpp = '29.5', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 2船尾 1', stern_towboat = 'ﾛｰﾌﾟﾄﾞﾗﾑ小ﾄｰｲﾝｸﾞｱｰﾁ', intake = 'ﾏｽﾄ　上部', exhaust = 'ZP後部', aux_engine = '', dk_machine_pp = '機関室：独立', fire_pump = '機関室：独立', harbor_gen = 'ZP室', fire_extinguish = '粉末消火設備')
    summary31 = Summary(ship_id = 31, official_number = '142813', signal_code = 'JD4104', engine_kw = '3600', pera_spec = 'ZP-21', me_model = 'ﾆｲｶﾞﾀ 6L26HLX', me_sno = '27613/27614', pera_sno = 'P3490/3491', fire_equipt = '3', full_length = '33.9', lpp = '29.5', breadth = '9.4', beam_depth = '4', mold_draft = '3.1', draft_mark_F = '', draft_mark_A = '', fm_bl = '', draft_m = '', layer_2or3 = '2.5層', winch_tension = '船首 1', stern_towboat = '', intake = 'ﾏｽﾄ　下部', exhaust = 'ZP後部', aux_engine = '', dk_machine_pp = '居室区画', fire_pump = '主機左舷付', harbor_gen = '', fire_extinguish = '')
    db.session.add_all([summary01,summary02,summary03,summary04,summary05,summary06,summary07,summary08,summary09,summary10,summary11,summary12,summary13,summary14,summary15,summary16,summary17,summary18,summary19,summary20,summary21,summary22,summary23,summary24,summary25,summary26,summary27,summary28,summary29,summary30,summary31])
            