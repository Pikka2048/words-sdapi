# words-sdapi

## 説明
このスクリプトは、ランダムなプロンプトを基にしたアニメ風キャラクターの画像を自動生成するツールです。プロンプトはテキストファイルからランダムに組み合わせて作成され、stable Diffusion webuiのAPIを通して画像が生成されます。指定枚数分の画像を生成し、クールタイムを挿入してGPU負荷を軽減します。

```py
PROMPT = f"{SYSYTEM_PROMPT}, {choice(colors)}, {choice(hairstyles)} hair, {choice(colors)} eyes, {choice(emotions)}, {choice(eye_motion)}, {choice(places)}, {choice(daytime)}, Glasses , {choice(pose)}, {choice(action)},{choice(cloth)} {choice(shot)}"
```

## 必要ライブラリ
このスクリプトを実行するには、以下のPythonライブラリが必要です：

- `requests` - APIリクエストの送信に使用
- `Pillow` - 画像処理用ライブラリ
- `tqdm` - 進行状況バー表示に使用
