document.addEventListener('DOMContentLoaded', () => {
  // 1. Menu Toggle Responsive (Mobile)
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => navMenu.classList.toggle('is-active'));
  }

  // 2. Trình điều khiển Video tùy biến (Play/Pause & timeupdate)
  const video = document.getElementById('mainVideo');
  const btnPlay = document.getElementById('btnPlayPause');
  const pBar = document.getElementById('pBarFill');
  const tDisplay = document.getElementById('timeText');

  if (video && btnPlay && pBar && tDisplay) {
    btnPlay.addEventListener('click', () => {
      if (video.paused || video.ended) {
        video.play().then(() => {
          btnPlay.textContent = '⏸ Tạm dừng';
        }).catch(err => console.warn('Autoplay/Playback policy error:', err));
      } else {
        video.pause();
        btnPlay.textContent = '▶ Phát';
      }
    });

    video.addEventListener('timeupdate', () => {
      const cur = video.currentTime, dur = video.duration || 1;
      pBar.style.width = `${(cur / dur) * 100}%`;
      const format = (s) => `${Math.floor(s / 60).toString().padStart(2, '0')}:${Math.floor(s % 60).toString().padStart(2, '0')}`;
      tDisplay.textContent = `${format(cur)} / ${format(dur)}`;
    });
  }

  // 3. Tính năng cộng điểm: Nạp động AJAX / fetch('media/media.json')
  const btnLoad = document.getElementById('btnLoadMore');
  const ajaxContainer = document.getElementById('ajaxList');
  if (btnLoad && ajaxContainer) {
    btnLoad.addEventListener('click', () => {
      btnLoad.textContent = 'Đang tải dữ liệu...';
      fetch('media/media.json')
        .then(res => res.json())
        .then(data => {
          ajaxContainer.innerHTML = data.map(item => `
            <div class="ajax-item">
              <img src="${item.thumb}" alt="${item.title}" class="ajax-thumb" width="90" height="60" loading="lazy">
              <div>
                <h4 style="font-size:0.95rem; color:#1F4E79; margin-bottom:0.25rem;">${item.title}</h4>
                <p style="font-size:0.8rem; color:#64748B;">Thời lượng: ${item.duration} | ${item.type}</p>
                <p style="font-size:0.8rem; color:#334155; margin-top:0.2rem;">${item.desc}</p>
              </div>
            </div>`).join('');
          btnLoad.style.display = 'none';
        })
        .catch(err => {
          btnLoad.textContent = 'Lỗi nạp dữ liệu';
          console.error('Fetch error:', err);
        });
    });
  }
});
