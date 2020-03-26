import string
import requests

all_char=string.ascii_letters[26:]+string.digits

def create_string(now_string):
    if len(now_string)<32:#说明需要继续添加字符串
        for i in range(0,len(all_char)):
            now_string+=all_char[i]
            create_string(now_string)
    if len(now_string)==32:
        get_pass(now_string)

def get_pass(md5):
    print("正在尝试获取"+md5+"的密码")
    url="https://api.vscodev.tk/zip?md5="+"B6B86428AB6626506DCF889C7F8E4459"
    res=requests.get(url)
    if (password:=res.content.decode("utf-8")) != "此文件的解压密码尚未收录＞﹏＜":
        print("md5:"+md5+password[5:])
        

def main():
    md5=""
    create_string(md5)
    

if __name__ == '__main__':
    main()
    