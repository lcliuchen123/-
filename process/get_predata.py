

# 133种操作,5174个预定义文本。
# 人工标注，第一阶段，每个类别标注30条，再标注部分为其它，一共标注5000条。

# ['垃圾清理', '手机瘦身', 'QQ专清', '微信专清',
#  '网络助手', '电量管理', '安全扫描', '应用管理',
#  '优化加速', '安全中心首页', '关机', '重启',
# '锁屏', 'MIUI版本', '字体大小', '壁纸', '个性主题',
#  '铃声设置', '日期和时间设置', '耳机和音效', '应用双开',
#  '应用锁', '查手机情况', '主题排行榜', '话费充值', '运动步数',
#  '清理后台', '音乐热歌榜', '铃声首页', '字体首页', '主题首页',
#  '小爱同学任务', '游戏加速', '回到桌面', '拨号界面',
# '打开语音助手', '锁屏画报', '输入法', '我的设备', '关于手机',
#  '云服务', '用户反馈', '打开录音机', '停止录音', 'IMEI信息',
# '打开公交卡、门禁卡、银行卡', '截屏', '开始录屏', '设置',
#  'VPN页面', '电量使用记录', '更多连接方式', 'WLAN',
# '打开扫描页面', 'WIFI高级设置', 'APN设置', '蓝牙设置',
# '修改语言', '添加键盘', '实体键盘', '显示设置',
# '开源代码许可', '系统安全', '位置设置', '更多应用',
# '无障碍界面', '色彩校正', '字幕', '文字转语音设置',
#  '指纹管理', '存储空间', '开发者选项', '打印', '无线显示',
#  '同步', '添加', '用户设置', '声音和振动', '防打扰',
#  '备份和重置', '默认应用设置', '护眼模式', '生活缴费',
#  '信用卡账单', '办信用卡', '整理全部图标', '整理当前屏幕图标',
# '图标自动分类', '恢复图标', '银行卡', '交易记录',
# '余额', '付款码', '小米钱包-中信银行信用卡申请',
# 'MIUI10升级公告', '米币中心', '论坛签到',
#  '小米金融--我要买保险', '小爱同学微博主页',
# '语音唤醒设置', '邀好友赚赏金', '多看签到', '打卡签到赚现金活动',
# '我要红包导流微博', '手机急救箱', '语音播报', '小爱实验室',
# '定时开关机', '设置锁屏密码和指纹', '设置电量和性能',
#  '清除所有数据', '全面屏设置', '门卡', '公交卡',
# '小爱升级', '5种使用小爱同学的方法', '小米账号', '一键换机',
#  '用户个人训练页面', '公共训练计划', '创建训练计划',
#  '音乐源设置', '应用升级', '米家授权', '电话设置', '打开捷径',
# '通知和状态栏', '微博小爱捷径挑战', '语音便签', '小爱同学定制礼物',
#  '设置锁屏时间', '早起挑战', '小爱老师商城购买页']

def  get_pre_sentence(file_name):
    with open(file_name+'.txt','r',encoding='utf-8') as f:
        pre_sentence = {}
        line = f.readline()
        line = line.strip()
        count = 0
        while line:
            count += 1
            sentence = line.split()
            # print(sentence)
            if not pre_sentence.get(sentence[0]):
                pre_sentence[sentence[0]] = [sentence[1]]

            else:
                pre_sentence[sentence[0]].append(sentence[1])

            line = f.readline()
            line = line.strip()
        print(count)

        return pre_sentence



if __name__ == "__main__":
    file_name = 'F:\毕业论文\sentence-embedding\数据\query_pair2019-09-24'
    pre_sentence = get_pre_sentence(file_name)
    label_list = list(pre_sentence.keys())
    pre_text = list(pre_sentence.values())
    print(len(pre_sentence))
    print(sum([len(pre_text[i]) for i in range(len(pre_text))]))
    print(label_list)
    # with open('F:\毕业论文\sentence-embedding\数据\label.txt','w',encoding='utf8') as f:
    #     for item in label_list:
    #         f.write(item)
    #         f.write('\n')

    count = 0
    with open('F:\毕业论文\sentence-embedding\数据\data.txt','w',encoding='utf8') as f:
        for item in label_list:
            count += 1
            if count > 28:
                for i in range(30):
                    f.write(item)
                    f.write('\n')

