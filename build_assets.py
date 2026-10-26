import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont

def generate_assets(proj_dir):
    img_dir = os.path.join(proj_dir, "img")
    video_dir = os.path.join(proj_dir, "video")
    audio_dir = os.path.join(proj_dir, "audio")
    media_dir = os.path.join(proj_dir, "media")
    css_dir = os.path.join(proj_dir, "css")
    js_dir = os.path.join(proj_dir, "js")

    for d in [img_dir, video_dir, audio_dir, media_dir, css_dir, js_dir]:
        os.makedirs(d, exist_ok=True)

    print("[1] Đang sinh ảnh WebP đáp ứng (Responsive Images)...")
    
    # 1. Banner Hero 3 kích cỡ (400w, 800w, 1200w)
    sizes = [
        (400, 225, "banner_hero_400w.webp", "KHOA CNTT - IUH (Mobile 400w)"),
        (800, 350, "banner_hero_800w.webp", "KHOA CÔNG NGHỆ THÔNG TIN - IUH (Tablet 800w)"),
        (1200, 450, "banner_hero_1200w.webp", "KHOA CÔNG NGHỆ THÔNG TIN — ĐẠI HỌC CÔNG NGHIỆP TP.HCM (Desktop 1200w)")
    ]
    for w, h, fname, label in sizes:
        img = Image.new("RGB", (w, h), color=(31, 78, 121))
        draw = ImageDraw.Draw(img)
        # Gradient effect
        for y in range(h):
            r = int(31 + (y / h) * 15)
            g = int(78 + (y / h) * 35)
            b = int(121 + (y / h) * 50)
            draw.line([(0, y), (w, y)], fill=(r, g, b))
        
        # Grid lines pattern
        for x in range(0, w, 40):
            draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 20), width=1)
        
        draw.rectangle([(20, 20), (w - 20, h - 20)], outline=(186, 230, 253), width=2)
        draw.text((w // 2, h // 2 - 15), label, fill=(255, 255, 255), anchor="mm")
        draw.text((w // 2, h // 2 + 15), "Kiến tạo Tương lai Số | Tuyển sinh & Nghiên cứu Khoa học", fill=(224, 242, 254), anchor="mm")
        img.save(os.path.join(img_dir, fname), "WEBP", quality=85)
        print(f"  -> Đã tạo: {fname} ({w}x{h})")

    # 2. Poster Video WebP
    p_img = Image.new("RGB", (960, 540), color=(15, 23, 42))
    p_draw = ImageDraw.Draw(p_img)
    p_draw.rectangle([(10, 10), (950, 530)], outline=(56, 189, 248), width=3)
    p_draw.text((480, 250), "▶ TRẢI NGHIỆM PHÒNG LAB IOT & AI", fill=(255, 255, 255), anchor="mm")
    p_draw.text((480, 290), "Khoa Công nghệ Thông tin — IUH | 1080p Full HD", fill=(148, 163, 184), anchor="mm")
    p_img.save(os.path.join(img_dir, "poster_video.webp"), "WEBP", quality=85)

    # 3. 4 Cards ngành học (WebP)
    majors = [
        ("card_ktpm.webp", "KỸ THUẬT PHẦN MỀM", "Chuyên sâu DevOps, Web, Mobile App"),
        ("card_khmt.webp", "KHOA HỌC MÁY TÍNH", "Trí tuệ Nhân tạo & Xử lý Dữ liệu lớn"),
        ("card_attt.webp", "AN TOÀN THÔNG TIN", "Bảo mật Hệ thống & An ninh mạng"),
        ("card_httt.webp", "HỆ THỐNG THÔNG TIN", "Phân tích Nghiệp vụ & Chuyển đổi số")
    ]
    for fname, title, desc in majors:
        c_img = Image.new("RGB", (400, 260), color=(248, 250, 252))
        c_draw = ImageDraw.Draw(c_img)
        c_draw.rectangle([(0, 0), (400, 150)], fill=(30, 41, 59))
        c_draw.text((200, 75), title, fill=(255, 255, 255), anchor="mm")
        c_draw.text((200, 190), title, fill=(31, 78, 121), anchor="mm")
        c_draw.text((200, 220), desc, fill=(100, 116, 139), anchor="mm")
        c_draw.rectangle([(0, 0), (399, 259)], outline=(203, 213, 225), width=2)
        c_img.save(os.path.join(img_dir, fname), "WEBP", quality=85)

    # 4. Logo IUH SVG
    logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 60" width="280" height="60">
  <rect width="280" height="60" rx="8" fill="#1F4E79"/>
  <text x="25" y="40" font-family="Arial, sans-serif" font-size="28" font-weight="bold" fill="#FFFFFF">IUH</text>
  <line x1="85" y1="12" x2="85" y2="48" stroke="#BAE6FD" stroke-width="2"/>
  <text x="95" y="28" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#BAE6FD">KHOA CÔNG NGHỆ THÔNG TIN</text>
  <text x="95" y="44" font-family="Arial, sans-serif" font-size="10" fill="#E0F2FE">ĐẠI HỌC CÔNG NGHIỆP TP.HCM</text>
</svg>"""
    with open(os.path.join(img_dir, "logo_iuh.svg"), "w", encoding="utf-8") as f:
        f.write(logo_svg)

    print("[2] Đang tải mẫu video MP4 & WebM và âm thanh MP3...")
    # Tải video mẫu chuẩn W3C CC0 (nhẹ ~1MB)
    video_mp4 = os.path.join(video_dir, "intro_lab.mp4")
    video_webm = os.path.join(video_dir, "intro_lab.webm")
    audio_mp3 = os.path.join(audio_dir, "podcast_huongnghiep.mp3")

    if not os.path.exists(video_mp4):
        urllib.request.urlretrieve("https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4", video_mp4)
        print("  -> Đã tải: intro_lab.mp4")
    
    if not os.path.exists(video_webm):
        urllib.request.urlretrieve("https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm", video_webm)
        print("  -> Đã tải: intro_lab.webm")

    if not os.path.exists(audio_mp3):
        urllib.request.urlretrieve("https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3", audio_mp3)
        print("  -> Đã tải: podcast_huongnghiep.mp3")

    # 5. Phụ đề WebVTT UTF-8 chuẩn xác
    vtt_content = """WEBVTT - Phụ đề Giới thiệu Phòng Lab IoT & AI - Khoa CNTT IUH

00:00:00.000 --> 00:00:03.000
Chào mừng các bạn đến với Khoa Công nghệ Thông tin - Trường Đại học Công nghiệp TP.HCM.

00:00:03.000 --> 00:00:07.000
Hệ thống phòng Lab thực hành hiện đại, trang bị đầy đủ máy trạm AI và thiết bị IoT tân tiến.

00:00:07.000 --> 00:00:12.000
Sinh viên được trực tiếp nghiên cứu, phát triển ứng dụng di động, điện toán đám mây và an ninh mạng.

00:00:12.000 --> 00:00:15.000
Đạt chuẩn kiểm định quốc tế AUN-QA, mở rộng cơ hội nghề nghiệp toàn cầu.

00:00:15.000 --> 00:00:18.000
Khoa CNTT - IUH: Nơi khởi đầu ước mơ công nghệ vững chắc của bạn!
"""
    with open(os.path.join(media_dir, "subtitles_vi.vtt"), "w", encoding="utf-8") as f:
        f.write(vtt_content)
    print("  -> Đã tạo: subtitles_vi.vtt")

    # 6. Tệp media.json cho tính năng AJAX fetch
    json_content = """[
  {
    "id": "med-01",
    "title": "Hội thảo Công nghệ Trí tuệ Nhân tạo & Generative AI 2026",
    "duration": "04:35",
    "type": "Video Full HD",
    "thumb": "img/card_khmt.webp",
    "desc": "Chia sẻ từ các chuyên gia đầu ngành về xu hướng mô hình ngôn ngữ lớn và ứng dụng thực tiễn."
  },
  {
    "id": "med-02",
    "title": "Chung kết Cuộc thi Lập trình Phần mềm Sáng tạo IUH Hackathon",
    "duration": "06:12",
    "type": "Video Full HD",
    "thumb": "img/card_ktpm.webp",
    "desc": "Các dự án công nghệ xuất sắc của sinh viên giải quyết bài toán giao thông và y tế thông minh."
  },
  {
    "id": "med-03",
    "title": "Podcast số 02: Kỹ năng sinh viên CNTT cần trang bị trước khi thực tập",
    "duration": "12:40",
    "type": "Audio MP3",
    "thumb": "img/card_attt.webp",
    "desc": "Đối thoại cùng cựu sinh viên đang làm việc tại các tập đoàn công nghệ đa quốc gia."
  },
  {
    "id": "med-04",
    "title": "Lễ Ký kết Hợp tác Doanh nghiệp và Ngày hội Việc làm IT Day",
    "duration": "03:50",
    "type": "Video 720p",
    "thumb": "img/card_httt.webp",
    "desc": "Hơn 50 doanh nghiệp hàng đầu phỏng vấn tuyển dụng trực tiếp sinh viên năm cuối."
  }
]"""
    with open(os.path.join(media_dir, "media.json"), "w", encoding="utf-8") as f:
        f.write(json_content)
    print("  -> Đã tạo: media.json")

    # 7. Sitemap.xml chuẩn SEO
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-cntt-iuh/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-cntt-iuh/nganh-hoc.html</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-cntt-iuh/video-detail.html</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://hoangphat5393.github.io/miniproject-cntt-iuh/sitemap.html</loc>
    <priority>0.5</priority>
  </url>
</urlset>"""
    with open(os.path.join(proj_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("  -> Đã tạo: sitemap.xml")

if __name__ == '__main__':
    p1 = r"e:\he_thong_da_phuong_tien\Tuan9\DuAn1_KhoaCNTT_IUH"
    generate_assets(p1)
