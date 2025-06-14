import requests

# ▼ エンドポイント
#   https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
#   （e-Stat API 3.0 の JSON形式 統計データ取得用エンドポイント）
#
# ▼ 使用する統計表
#   statsDataId: 0000020201
#   → 国勢調査（産業等基本集計） 市区町村別の就業者統計データ
#
# ▼ 主なパラメータの意味
#   - appId         : e-Statの利用登録で取得したアプリケーションID
#   - statsDataId   : 使用する統計表のID（各表ごとにユニーク）
#   - cdArea        : 地域コード（市区町村単位）※5桁のコード
#   - cdCat01       : 統計分類コード（E1303: 第3次産業従業者数）
#   - metaGetFlg    : メタ情報（分類名など）も取得（Y推奨）
#   - cntGetFlg     : 件数のみ取得（N＝データ本体取得）
#   - explanationGetFlg : 説明文を含める
#   - annotationGetFlg  : 注釈を含める
#   - lang          : 言語設定（J＝日本語）

APP_ID = "a3fbc62cc56fa6cefeb1e1009a88089394cef676"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0000020201", # 労働力調査(基本集計)
    "cdArea":"08000", # 茨城県コード
    "cdCat01": "F110201, F110202, F110701, F110702", # 就業者数(15歳以上・男女計)、完全失業者数(15歳以上・男女計)
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



# APIリクエスト送信
response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# レスポンスをJSONとして取得
data = response.json()
# 取得したデータの中身を確認
print(data)