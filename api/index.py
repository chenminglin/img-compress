from flask import Flask, request, jsonify
from PIL import Image
import os

app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#
# @app.route('/compress', methods=['POST'])
# def compress_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided'}), 400
#
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#
#     try:
#         # 打开上传的图片
#         img = Image.open(file)
#
#         # 将图像转换为8位索引颜色格式
#         img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
#
#         output_path = os.path.join(UPLOAD_FOLDER, 'compressed_' + file.filename)
#         img.save(output_path, format='PNG', optimize=True)
#
#         return jsonify({'message': 'Image compressed and converted to 8-bit successfully', 'path': output_path}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)