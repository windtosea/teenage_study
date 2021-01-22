from core import TeenageStudy

# param openid: 用户的id，可通过抓包获取
# param course: 每期课程的代号，可以通过规律来获取，也可以通过抓包来获取
openid = input('请输入用户id：')
course = input('请输入课程代号：')
TeenageStudy(openid, course).start_study()
