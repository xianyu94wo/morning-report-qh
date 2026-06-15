import base64, os

tiny_dir = "/home/ubuntu/.hermes/wechat_article_tiny"

# Read all images as base64
b64 = {}
for fname in ["gfs_500hpa_f000.jpg", "gfs_500hpa_f006.jpg", "gfs_500hpa_f012.jpg",
              "gfs_500hpa_f018.jpg", "gfs_500hpa_f024.jpg", "qinghai_precip_24h.jpg"]:
    with open(os.path.join(tiny_dir, fname), "rb") as f:
        b64[fname.replace(".jpg", "")] = base64.b64encode(f.read()).decode()

# CSS
css = """* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Helvetica Neue", "Microsoft YaHei", sans-serif; background: #f2f2f2; color: #333; -webkit-font-smoothing: antialiased; }
.article-wrapper { max-width: 680px; margin: 0 auto; background: #fff; min-height: 100vh; }
.account-header { display: flex; align-items: center; padding: 20px 20px 0; font-size: 14px; color: #576b95; }
.account-avatar { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #07c160, #06ad56); display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold; font-size: 16px; margin-right: 10px; flex-shrink: 0; }
.account-name { font-weight: 500; }
.account-name small { font-weight: normal; color: #999; font-size: 12px; margin-left: 6px; }
.article-header { padding: 25px 20px 10px; }
.article-title { font-size: 22px; font-weight: 600; line-height: 1.5; color: #1a1a1a; letter-spacing: 0.5px; }
.article-meta { padding: 10px 20px 0; font-size: 13px; color: #999; display: flex; gap: 12px; flex-wrap: wrap; }
.article-meta .author { color: #576b95; }
.divider { margin: 15px 20px; border: 0; height: 1px; background: #e5e5e5; }
.article-body { padding: 0 20px 30px; font-size: 16px; line-height: 1.75; color: #333; }
.article-body h2 { font-size: 18px; font-weight: 600; margin: 30px 0 12px; color: #1a1a1a; padding-left: 12px; border-left: 4px solid #07c160; }
.article-body h3 { font-size: 16px; font-weight: 600; margin: 20px 0 10px; color: #1a1a1a; }
.article-body p { margin: 8px 0; text-align: justify; }
.article-body ul { margin: 8px 0; padding-left: 18px; list-style: none; }
.article-body ul li { position: relative; margin: 6px 0; padding-left: 4px; }
.article-body blockquote { margin: 20px 0; padding: 15px 18px; background: #f7f7f7; border-left: 3px solid #07c160; border-radius: 0 6px 6px 0; color: #666; font-size: 14px; font-style: italic; }
.weather-card { background: linear-gradient(135deg, #e8f5e9, #f1f8e9); border-radius: 10px; padding: 16px 18px; margin: 12px 0; }
.weather-card .temp { font-size: 28px; font-weight: 700; color: #e53935; }
.weather-card .temp small { font-size: 14px; font-weight: normal; color: #666; }
.chart-item { border-radius: 8px; overflow: hidden; background: #fafafa; border: 1px solid #eee; margin: 15px 0; }
.chart-item img { width: 100%; height: auto; display: block; }
.chart-item .chart-label { font-size: 13px; color: #666; text-align: center; padding: 8px; background: #f5f5f5; border-top: 1px solid #eee; }
.balance-box { display: flex; gap: 12px; flex-wrap: wrap; margin: 12px 0; }
.balance-card { flex: 1; min-width: 120px; padding: 12px 15px; border-radius: 8px; text-align: center; }
.balance-card.deepseek { background: #e3f2fd; }
.balance-card.zhipu { background: #e8f5e9; }
.balance-card .label { font-size: 12px; color: #666; margin-bottom: 4px; }
.balance-card .value { font-size: 18px; font-weight: 700; color: #1a1a1a; }
.balance-card .sub { font-size: 11px; color: #999; margin-top: 2px; }
.status-green { display: inline-block; background: #e8f5e9; color: #2e7d32; padding: 2px 10px; border-radius: 4px; font-size: 13px; }
.tag { display: inline-block; font-size: 12px; padding: 1px 8px; border-radius: 3px; margin-right: 4px; }
.tag-red { background: #ffebee; color: #c62828; }
.article-footer { padding: 20px; text-align: center; border-top: 1px solid #eee; }
.footer-text { font-size: 12px; color: #999; line-height: 1.6; }
@media (prefers-color-scheme: dark) {
  body { background: #1a1a1a; } .article-wrapper { background: #1e1e1e; }
  .article-title { color: #e0e0e0; } .article-body { color: #ccc; }
  .article-body h2 { color: #e0e0e0; border-left-color: #07c160; }
  .chart-item { background: #2a2a2a; border-color: #333; }
  .chart-item .chart-label { background: #2a2a2a; color: #999; border-color: #333; }
  .weather-card { background: linear-gradient(135deg, #1b3a1b, #2a3a1b); }
  .weather-card .temp { color: #ff6f60; }
  .article-footer { border-color: #333; }
  .balance-card.deepseek { background: #1a2a3a; }
  .balance-card.zhipu { background: #1a2a1a; }
  .article-body blockquote { background: #2a2a2a; color: #999; }
}"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Hermes 晨报 · GFS 日报 | 2026年5月27日</title>
<style>{css}</style>
</head>
<body>
<div class="article-wrapper">
<div class="account-header"><div class="account-avatar">H</div><div class="account-name">Hermes 气象日报 <small>· 青海站</small></div></div>
<div class="article-header"><h1 class="article-title">Hermes 晨报 · GFS 日报<br>2026年5月27日 星期三</h1></div>
<div class="article-meta"><span class="author">Hermes Agent</span><span>·</span><span>2026年5月27日 06:46</span></div>
<hr class="divider">
<div class="article-body">

<h2>📅 天气简报</h2>
<div class="weather-card">
<strong>📍 青海 · 西宁</strong>
<div style="margin-top:6px;"><span class="temp">5<span style="font-size:16px;font-weight:normal;color:#999;"> ~ </span>11</span><small>°C</small> <span style="margin-left:8px;font-size:14px;color:#666;">🌧️ 小雨转阴</span></div>
<div style="margin-top:8px;font-size:14px;color:#555;"><span class="tag tag-red">⚠️ 大风黄色预警</span> 西宁各区7级以上大风，阵风8级以上</div>
<div style="margin-top:6px;font-size:13px;color:#888;">🟢 空气质量良（PM2.5 25）· 体感温度2°C</div>
</div>
<p><strong>📍 青海省整体趋势</strong></p>
<ul>
<li>🌦️ 全省大部有降雨，海东、海北、海南、黄南等地均有降水</li>
<li>🏔️ 海拔较高地区气温偏低，昼夜温差大</li>
<li>☀️ 未来几天逐步转晴，周末高温有望升至22~23°C</li>
</ul>

<h2>📰 今日要闻</h2>
<ul>
<li>🔥 <strong>美伊冲突持续</strong> — 美军对伊朗南部发动新一轮打击；特朗普称协议"基本谈成"</li>
<li>⚽ <strong>U17国少憾失亚洲杯冠军</strong> — 2-3惜败日本获亚军</li>
<li>🌧️ <strong>中东部强降雨</strong> — 湖北安徽暴雨致灾风险高，局地雨量或破纪录</li>
<li>🤝 <strong>中德足球青训合作</strong> — 中国足协与多特蒙德签署备忘录</li>
</ul>

<h2>🤖 AI 动态</h2>
<ul>
<li>🔥 <strong>GPT-5.6意外曝光</strong> — 上下文150万tokens，六月大模型混战在即</li>
<li>🏆 <strong>阿里Qwen3.7-Max编程全球第二</strong> — Code Arena 1541分</li>
<li>💰 <strong>支付宝披露</strong> — 累计3亿笔AI付</li>
<li>🍎 <strong>苹果Siri升级</strong> — 搭载1.2万亿参数谷歌定制模型"掌脑"</li>
</ul>

<h2>📊 气象前沿</h2>
<ul>
<li>🌐 <strong>NVIDIA发布开源气象模型新架构</strong></li>
<li>🇨🇳 <strong>中国AI模型体系</strong> — "风雷""风清""风顺"覆盖0-60天预报</li>
<li>🚀 <strong>"十五五"气象规划</strong> — 2030年灾害监测率85%</li>
</ul>

<h2>💰 API 状态</h2>
<div class="balance-box">
<div class="balance-card deepseek"><div class="label">🔵 DeepSeek</div><div class="value">42.11 元</div><div class="sub">充值 42.11 · 赠送 0.00</div><div style="margin-top:6px;"><span class="status-green">✅ 正常可用</span></div></div>
<div class="balance-card zhipu"><div class="label">🟢 智谱 AI</div><div class="value">正常</div><div class="sub">CogView-3-Flash 免费</div><div style="margin-top:6px;"><span class="status-green">✅ 正常</span></div></div>
</div>

<hr class="divider" style="margin:25px 0;">

<h2 style="border-left-color:#576b95;">🌤️ GFS 日报</h2>
<p style="font-size:14px;color:#888;">GFS 0.25° | 起报18Z（北京时02:00）| 2026年5月27日</p>

<h3>📈 500hPa 高空形势（全国）</h3>
<div class="chart-item"><img src="data:image/jpeg;base64,{b64["gfs_500hpa_f000"]}" alt="500hPa f000"><div class="chart-label">初始分析场（f000）</div></div>
<div class="chart-item"><img src="data:image/jpeg;base64,{b64["gfs_500hpa_f006"]}" alt="500hPa f006"><div class="chart-label">06小时预报（f006）</div></div>
<div class="chart-item"><img src="data:image/jpeg;base64,{b64["gfs_500hpa_f012"]}" alt="500hPa f012"><div class="chart-label">12小时预报（f012）</div></div>
<div class="chart-item"><img src="data:image/jpeg;base64,{b64["gfs_500hpa_f018"]}" alt="500hPa f018"><div class="chart-label">18小时预报（f018）</div></div>
<div class="chart-item"><img src="data:image/jpeg;base64,{b64["gfs_500hpa_f024"]}" alt="500hPa f024"><div class="chart-label">24小时预报（f024）</div></div>

<h3>🌧️ 青海省24h降水预报</h3>
<div class="chart-item"><img src="data:image/jpeg;base64,{b64["qinghai_precip_24h"]}" alt="青海降水"><div class="chart-label">色标 GB/T 35968-2018 · 最大降水中心已标注</div></div>

<blockquote>🌅 新的一天已经开始，无论风雨还是晴空，保持前行的节奏——每一个努力的清晨，都在为更好的自己铺路。加油！☕✨</blockquote>
</div>
<div class="article-footer"><div class="footer-text"><strong>Hermes Agent · 自动气象日报</strong><br>每日06:00自动生成 · 数据：GFS 0.25°<br><span style="font-size:11px;color:#bbb;">由 Hermes AI Agent 自动推送 · 仅供参考</span></div></div>
</div>
</body>
</html>"""

out_path = "/home/ubuntu/.hermes/wechat_article/self_contained.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

mb = os.path.getsize(out_path) / 1024 / 1024
print(f"Self-contained HTML created: {mb:.1f}MB")
