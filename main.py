import requests
import base64
from PIL import Image
from io import BytesIO
from tqdm import tqdm
import os
import random
import time

# APIのURL
url = "http://localhost:7860/sdapi/v1/txt2img"
headers = {"Content-Type": "application/json"}
OUTPUT_DIR = "output/"

def generate_image(prompt, steps=20, width=896, height=1152):

    payload = {
        "prompt": prompt,
        "negative_prompt": "flat color, simple background, wrong lighting, bad quality",
        "steps": steps,
        "width": width,
        "height": height,
        "scheduler": "Simple",
        "cfg_scale": 1,
        "sampler_name": "[Forge] Flux Realistic",
    }

    # APIリクエストを送信
    response = requests.post(url, headers=headers, json=payload)

    # レスポンスが成功したか確認
    if response.status_code == 200:
        # Base64でエンコードされた画像データをデコード
        image_data = response.json()["images"][0]
        image_bytes = base64.b64decode(image_data)

        image = Image.open(BytesIO(image_bytes))

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        outdir_count = len(os.listdir(OUTPUT_DIR))


        save_name = f"{OUTPUT_DIR}/{outdir_count}_{prompt[:60]}.png"
        image.save(save_name)
        print(f"prompt: {prompt} Saved.")
    else:
        print("Error:", response.status_code, response.text)


def choice(word_list):
    return random.choice(word_list)


def load_list(file_path):
    with open(file_path, "r") as f:
        prompts = f.readlines()
    prompts = [prompt.replace("\n", "") for prompt in prompts]
    return prompts


if __name__ == "__main__":
    colors = load_list("prompts/color.txt")
    hairstyles = load_list("prompts/hairstyle.txt")
    places = load_list("prompts/place.txt")
    pose = load_list("prompts/pose.txt")
    shot = load_list("prompts/shot.txt")
    cloth = load_list("prompts/cloth.txt")
    emotions = load_list("prompts/emotion.txt")
    action = load_list("prompts/action.txt")
    daytime = load_list("prompts/daytime.txt")
    eye_motion = load_list("prompts/eye_motion.txt")

    N = 1000
    COOL_TIME = 25
    SYSYTEM_PROMPT = "A anime girl, detailed, portrait"
    for i in tqdm(range(N)):
        if i % COOL_TIME == 0 and i != 0:
            print("GPU cooling time")
            time.sleep(30)

        PROMPT = f"{SYSYTEM_PROMPT}, {choice(colors)}, {choice(hairstyles)} hair, {choice(colors)} eyes, {choice(emotions)}, {choice(eye_motion)}, {choice(places)}, {choice(daytime)}, Glasses , {choice(pose)}, {choice(action)},{choice(cloth)} {choice(shot)} "
        generate_image(PROMPT)
