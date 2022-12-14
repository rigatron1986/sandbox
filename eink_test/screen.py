import os
import re
import subprocess
import socket
import logging
import datetime
import psutil
import speedtest
import netifaces as ni
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET
from PIL import Image, ImageDraw, ImageFont

try:
    from waveshare_epd import epd2in13b_V3
except ImportError:
    pass

SCREEN_HEIGHT = 104
SCREEN_WIDTH = 212

# print(os.path.join(os.path.dirname(__file__), 'Roses.ttf'))

FONT_SMALL = ImageFont.truetype(
    os.path.join(os.path.dirname(__file__), 'Roses.ttf'), 6)
FONT_MEDIUM = ImageFont.truetype(
    os.path.join(os.path.dirname(__file__), 'Roses.ttf'), 14)
FONT_LARGE = ImageFont.truetype(
    os.path.join(os.path.dirname(__file__), 'PixelSplitter-Bold.ttf'), 22)
logging.basicConfig(level=logging.INFO)


class Epd2in13bv3(object):

    def __init__(self, mode=None):
        super().__init__()
        self.epd = epd2in13b_V3.EPD()

        logging.info("init and Clear")
        self.epd.init()
        self.epd.Clear()
        self.data = {}
        self.image_black = Image.new('1', (SCREEN_WIDTH, SCREEN_HEIGHT), 255)
        self.image_ry = Image.new('1', (SCREEN_WIDTH, SCREEN_HEIGHT), 255)
        self.draw_black = ImageDraw.Draw(self.image_black)
        self.draw_ry = ImageDraw.Draw(self.image_ry)
        self.mode = mode

    @staticmethod
    def get_font(size=6):
        return ImageFont.truetype(
            os.path.join(os.path.dirname(__file__), 'PixelSplitter-Bold.ttf'), size)

    @staticmethod
    def getHostname():
        hostname = socket.gethostname()
        return hostname

    @staticmethod
    def GetBootTime():
        return datetime.datetime.fromtimestamp(psutil.boot_time())

    @staticmethod
    def get_wifi_ip_address():
        try:
            ni.interfaces()
            return ni.ifaddresses('wlan0')[AF_INET][0]['addr']
        except:
            return 'inactive'

    @staticmethod
    def GetMemUsed():
        mem_used = psutil.virtual_memory()[2]
        return mem_used

    @staticmethod
    def check_CPU_temp():
        temp = None
        err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
        if not err:
            m = re.search(r'-?\d\.?\d*', msg)  # a solution with a  regex
            try:
                temp = float(m.group())
            except ValueError:  # catch only error needed
                pass
        return temp, msg

    @staticmethod
    def GetDiskUsed():
        diskUsed = psutil.disk_usage('/')[3]
        return diskUsed

    def form_image(self):
        self.draw_black.rectangle((0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), fill="white")
        black_draw = self.draw_black
        # red_draw = self.draw_ry
        red_draw = self.draw_black

        # flatten_prices = [item for sublist in prices for item in sublist]
        black_draw.text((0, 0), "Ip Addr:", font=self.get_font(12))
        red_draw.text((70, 0), "{}".format(self.data['ip_addr']), font=self.get_font(10))
        black_draw.line([(0, 15), (212, 15)])
        black_draw.text((0, 18), "Boot Time:", font=self.get_font(12))
        red_draw.text((85, 20), "{}".format(self.data['boot_time']), font=self.get_font(9))
        black_draw.line([(0, 33), (212, 33)])
        black_draw.text((0, 35), "Space used:", font=self.get_font(12))
        red_draw.text((105, 38), "{}%".format(self.data['space_used']), font=self.get_font(10))
        black_draw.line([(0, 50), (212, 50)])

        black_draw.text((0, 55), "CPU temp:", font=self.get_font(12))
        red_draw.text((85, 58), "{}°".format(self.data['cpu_temp']), font=self.get_font(10))  # Alt + 0176
        black_draw.line([(0, 70), (212, 70)])

        red_draw.text((0, 75), "Download:", font=self.get_font(10))
        red_draw.text((80, 75), "Upload:", font=self.get_font(10))
        red_draw.text((150, 75), "Ping:", font=self.get_font(10))

        black_draw.text((0, 90), "{}Mbps".format('{:5.2f}'.format(self.data['speed']['download'] / 1E6, 2)),
                        font=self.get_font(9))
        black_draw.text((80, 90), "{}Mbps".format('{:5.2f}'.format(self.data['speed']['upload'] / 1E6, 2)),
                        font=self.get_font(9))
        black_draw.text((150, 90), "{}ms".format('{:5.2f}'.format(self.data['speed']['ping'])),
                        font=self.get_font(9))

        # black_draw.text((0, 75), "down_speed:", font=self.get_font(12))
        # red_draw.text((120, 75), "{}".format('{:5.2f}'.format(self.data['speed']['download'] / 1E6, 2)),
        #               font=self.get_font(10))
        # black_draw.line([(0, 90), (212, 90)])

        # screen_draw.line([(33, 3), (33, 80)])
        # screen_draw.line([(51, 87), (51, 101)])

        # red_draw.line([(0, 20), (204, 20)])
        # black_draw.rectangle((60, 60, 150, 80), fill=0, outline=0, width=2)
        # red_draw.rectangle((60, 85, 150, 90), fill=1, outline=0, width=2)
        # red_draw.rectangle((59, 59, 151, 81), fill=1, outline=0, width=2)
        # red_draw.text((60, 60), "CPU temp:", font=self.get_font(12))
        # red_draw.chord((90, 130, 150, 190), 0, 360, fill=0)

    @staticmethod
    def get_speed():
        bw_down = 0
        bw_up = 0
        ping = 0
        try:
            # TEST
            s = speedtest.Speedtest()
            s.get_best_server()
            bw_down = s.download()
            bw_up = s.upload()
            results_dict = s.results.dict()
            ping = (results_dict['ping'])
            return bw_down, bw_up, ping
        except Exception as e:
            return bw_down, bw_up, ping

    def get_data(self):
        speed = self.get_speed()
        self.data = {'ip_addr': self.get_wifi_ip_address(),
                     'boot_time': self.GetBootTime(),
                     'space_used': self.GetDiskUsed(),
                     'cpu_temp': self.check_CPU_temp()[0],
                     'speed': {'upload': speed[1],
                               'download': speed[0],
                               'ping': speed[2]}
                     }

    def update(self):
        logging.info('getting all data')
        self.get_data()
        logging.info('Updating the screen')
        self.form_image()
        image_black_rotated = self.image_black.rotate(180)
        image_ry_rotated = self.image_ry.rotate(180)
        self.epd.display(
            self.epd.getbuffer(image_black_rotated),
            self.epd.getbuffer(image_ry_rotated)
        )
        logging.info('Screen going to sleep')
        self.epd.sleep()

    def close(self):
        self.epd.Dev_exit()


d = Epd2in13bv3()
d.update()
