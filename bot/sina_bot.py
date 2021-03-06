#encoding:utf-8
#Created by Liang Sun in 2012
import re
from bot import Robot

class RobotSina(Robot):
    def __init__(self, root, charset):
        Robot.__init__(self, root, charset)
        self.url_pattern = re.compile(ur'^(http://\w+\.zufang\.sina\.com\.cn(|/|/detail/\d+/?|/house/(n\d+)?/?)|http://\w+\.esf\.sina\.com\.cn/?)$', re.U | re.I)

    def is_valid_url(self, url):
        return Robot.is_valid_url(self, url) and self.url_pattern.match(url) != None

a = RobotSina('http://bj.zufang.sina.com.cn/house/v0/', 'gbk')
a.start()
