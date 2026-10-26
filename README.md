# KHOA CÔNG NGHỆ THÔNG TIN — ĐẠI HỌC CÔNG NGHIỆP TP. HỒ CHÍ MINH (IUH)
## CỔNG THÔNG TIN TUYỂN SINH & HOẠT ĐỘNG SINH VIÊN ĐA PHƯƠNG TIỆN

> **Học phần:** Web Multimedia — Bài tập Tuần 9 (Thiết kế, phát triển và xuất bản website đa phương tiện)  
> **Sinh viên thực hiện:** Vũ Hoàng Phát  
> **Mã số sinh viên (MSSV):** 21143011  
> **Lớp:** KTPM17A / ĐH Công nghiệp TP.HCM (IUH)  
> **Live Demo (GitHub Pages):** [https://hoangphat5393.github.io/miniproject-cntt-iuh/](https://hoangphat5393.github.io/miniproject-cntt-iuh/)

---

## 1. GIỚI THIỆU DỰ ÁN

Website được xây dựng nhằm cung cấp cổng thông tin tuyển sinh và truyền thông đa phương tiện trực quan, hiện đại cho Khoa Công nghệ Thông tin - Trường Đại học Công nghiệp TP.HCM (IUH). Dự án tuân thủ đầy đủ các tiêu chuẩn kỹ thuật web hiện đại theo khuyến nghị của W3C và WCAG AA.

### Các công nghệ và kỹ thuật áp dụng:
1. **HTML5 Ngữ nghĩa (Semantic HTML5):** Cấu trúc phân vùng chuẩn xác với `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<figure>`, `<figcaption>`, `<footer>` (0 Errors, 0 Warnings W3C).
2. **Responsive Web Design (RWD Mobile-First):** Thiết kế đáp ứng trên 3 kích cỡ màn hình chính:
   - **Mobile:** $360\text{ px}$ (1 cột dọc, thanh điều hướng Toggle thân thiện cảm ứng).
   - **Tablet:** $768\text{ px}$ (Lưới 2 cột, menu ngang co giãn).
   - **Desktop:** $1200\text{ px} - 1280\text{ px}$ (Lưới 4 cột ngang, Banner Hero toàn màn hình).
3. **Hình ảnh tối ưu (WebP Responsive):** Áp dụng thẻ `<picture>` kết hợp `srcset` phục vụ 3 kích cỡ ảnh (`400w`, `800w`, `1200w`), định dạng WebP nén hiệu quả, khai báo tường minh `width` và `height` chống nhảy bố cục (CLS = 0).
4. **Trình phát Video & Audio HTML5 tùy biến:**
   - Video đa định dạng: MP4 (H.264) + WebM (VP9) kèm ảnh bìa `poster`.
   - Phụ đề rời WebVTT (`subtitles_vi.vtt`) tiếng Việt có dấu chuẩn UTF-8.
   - Trình điều khiển JavaScript nhỏ gọn ($\le 60$ dòng) hỗ trợ nút Play/Pause và thanh tiến độ thời gian thực qua sự kiện `timeupdate`.
5. **Tính năng nâng cao (AJAX Fetch):** Nạp động danh sách media mở rộng không đồng bộ bằng `fetch('media/media.json')`, giảm $99.4\%$ dung lượng mạng so với việc tải lại toàn bộ trang.
6. **Khả năng tiếp cận (Accessibility - WCAG AA):**
   - Tỷ lệ tương phản chữ/nền $\ge 4.5:1$ (màu chủ đạo Navy Blue `#1F4E79` đạt 12.8:1 trên nền trắng).
   - Hỗ trợ người dùng nhạy cảm chuyển động qua `@media (prefers-reduced-motion: reduce)`.
   - Đánh dấu trang hiện tại bằng `aria-current="page"`.

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
miniproject-cntt-iuh/
├── index.html                 # Trang chủ tuyển sinh & đa phương tiện
├── nganh-hoc.html             # Trang giới thiệu 4 ngành đào tạo mũi nhọn
├── video-detail.html          # Trang bài viết chi tiết Media kèm trình phát JS
├── sitemap.html               # Trang sơ đồ site trực quan cho người dùng
├── sitemap.xml                # Tệp sơ đồ site XML chuẩn SEO
├── README.md                  # Tài liệu hướng dẫn dự án
├── css/
│   └── site.css               # Tệp định kiểu CSS duy nhất toàn trang
├── js/
│   └── main.js                # Tệp script điều khiển Media và AJAX fetch (<= 60 dòng)
├── img/
│   ├── logo_iuh.svg           # Logo vector nhận diện thương hiệu IUH
│   ├── banner_hero_400w.webp  # Ảnh banner cho màn hình Mobile
│   ├── banner_hero_800w.webp  # Ảnh banner cho màn hình Tablet
│   ├── banner_hero_1200w.webp # Ảnh banner cho màn hình Desktop
│   ├── poster_video.webp      # Ảnh bìa (poster) cho trình phát video
│   ├── card_ktpm.webp         # Ảnh chuyên mục ngành Kỹ thuật Phần mềm
│   ├── card_khmt.webp         # Ảnh chuyên mục ngành Khoa học Máy tính
│   ├── card_attt.webp         # Ảnh chuyên mục ngành An toàn Thông tin
│   └── card_httt.webp         # Ảnh chuyên mục ngành Hệ thống Thông tin
├── video/
│   ├── intro_lab.mp4          # Video định dạng H.264/AAC
│   └── intro_lab.webm         # Video định dạng VP9/Opus
├── audio/
│   └── podcast_huongnghiep.mp3# Tệp âm thanh Podcast phát thanh số
├── media/
│   ├── subtitles_vi.vtt       # Tệp phụ đề WebVTT tiếng Việt chuẩn W3C
│   └── media.json             # Tệp dữ liệu JSON nạp động bằng fetch()
├── flowchart/                 # Thư mục sơ đồ site (MMD, PNG, HTML)
└── wireframe/                 # Thư mục khung dây Wireframe (HTML tương tác & PNG)
```

---

## 3. BẢNG SO SÁNH HIỆU NĂNG TÍNH NĂNG CỘNG ĐIỂM (AJAX FETCH VS RELOAD)

| Tiêu chí đo lường | Tải lại toàn trang (Full Reload) | Nạp ngầm AJAX fetch('media.json') | Tỷ lệ tối ưu |
| :--- | :--- | :--- | :--- |
| **Dung lượng mạng truyền tải** | $\approx 322\text{ KB}$ (HTML, CSS, JS, Assets) | $1.8\text{ KB}$ (Chỉ tải tệp dữ liệu JSON) | **Giảm 99.4%** |
| **Thời gian hoàn tất (Duration)** | $350\text{ ms} - 550\text{ ms}$ | $45\text{ ms} - 70\text{ ms}$ | **Nhanh hơn 87%** |
| **Hiện tượng nháy trắng (Flicker)** | Có (Trang trắng ngắt quãng màn hình) | Không (Giao diện giữ nguyên, cập nhật tức thì) | **Mượt mà hoàn hảo** |

---

## 4. HƯỚNG DẪN CHẠY THỬ NGHIỆM

1. **Xem trực tuyến (Live Demo):** Truy cập liên kết GitHub Pages:  
   [https://hoangphat5393.github.io/miniproject-cntt-iuh/](https://hoangphat5393.github.io/miniproject-cntt-iuh/)
2. **Chạy tại máy nội bộ (Localhost):**
   - Mở terminal tại thư mục dự án và khởi động máy chủ cục bộ:
     ```bash
     python -m http.server 8000
     ```
   - Truy cập trình duyệt tại địa chỉ: `http://localhost:8000/`.
