# Python Imaging Library
import sys

from PIL import Image


# python3 image_format_converter.py ~/Downloads/image.webp png
def convert_image(input_path, output_format):
    # 입력 파일의 확장자를 확인
    if not input_path.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif', 'webp')):
        print(f"Unsupported file format: {input_path}")
        return

    # 이미지 파일 열기
    try:
        with Image.open(input_path) as img:
            # 파일명과 확장자 분리
            output_path = '.'.join(input_path.split('.')[:-1]) + f'.{output_format}'

            # 지정된 포맷으로 이미지 저장
            img.save(output_path, output_format.upper())
            print(f"Image saved as {output_path}")
            print(f"format:{img.format}, size:{img.size}, mode{img.mode}")
    except IOError:
        print(f"Error opening or saving the file: {input_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_format>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_format = sys.argv[2]

    convert_image(input_file_path, output_format)
