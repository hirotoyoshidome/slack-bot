# coding: utf-8
import configparser
# Git非管理の設定ファイルを読み込む
inifile = configparser.ConfigParser()
inifile.read("./config.ini", "UTF-8")

# botアカウントのトークンを指定
API_TOKEN = inifile.get('settings', "token")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "こんにちはEdBotくんです。要件は何ですか？\n・時間を教えて\n・曜日を教えて"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
