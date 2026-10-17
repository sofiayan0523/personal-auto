# -*- coding: utf-8 -*-
import re

html_path = '.omni/demo_template_extracted.html'
html = open(html_path, encoding='utf-8').read()

print("Applying Phase 3 changes to demo_template_extracted.html...")

# 1. State Addition
old_state = """  state = {
    tab: 'today',
    commuteDone: false,"""

new_state = """  state = {
    tab: 'today',
    role: (typeof window !== 'undefined' ? (new URLSearchParams(window.location.search).get('role') || (window.location.hash === '#b2b' ? 'b2b' : 'passenger')) : 'passenger'),
    isOffPeak: false,
    commuteDone: false,"""

if old_state in html:
    html = html.replace(old_state, new_state, 1)
    print("✓ State replacement succeeded.")
else:
    print("✗ State replacement FAILED: target not found.")

# 2. Methods Addition (completeCommute, toggleOffPeak, toggleRolePassenger, toggleRoleB2B)
old_commute = """  completeCommute() {
    if (this.state.commuteDone) return;
    const oldM = this.multiplier(this.monthCarbon());
    const newMc = this.base + this.tripCarbon + this.state.extraTrips * this.tripCarbon;
    const newM = this.multiplier(newMc);
    this.setState({ commuteDone: true, exitPushOpen: true, seeds: this.state.seeds + 1 });
    this.award(Math.round(15 * newM), this.tripCarbon, '完成今日通勤');
    if (newM > oldM) this._levelUp(newM);
  }"""

new_commute = """  completeCommute() {
    if (this.state.commuteDone) return;
    const oldM = this.multiplier(this.monthCarbon());
    const newMc = this.base + this.tripCarbon + this.state.extraTrips * this.tripCarbon;
    const newM = this.multiplier(newMc);
    const bonusSeed = this.state.isOffPeak ? 1 : 0;
    this.setState({ commuteDone: true, exitPushOpen: true, seeds: this.state.seeds + 1 + bonusSeed });
    let eventName = '完成今日通勤';
    if (this.state.isOffPeak) {
      eventName = '完成今日離峰通勤（獎勵 +1 種子 🌱）';
    }
    this.award(Math.round(15 * newM), this.tripCarbon, eventName);
    if (newM > oldM) this._levelUp(newM);
  }
  toggleOffPeak(val) {
    if (this.state.commuteDone) return;
    this.setState({ isOffPeak: val });
  }
  toggleRolePassenger() {
    this.setState({ role: 'passenger' });
    if (typeof window !== 'undefined') window.location.hash = '';
  }
  toggleRoleB2B() {
    this.setState({ role: 'b2b' });
    if (typeof window !== 'undefined') window.location.hash = 'b2b';
  }"""

if old_commute in html:
    html = html.replace(old_commute, new_commute, 1)
    print("✓ Methods replacement succeeded.")
else:
    print("✗ Methods replacement FAILED: target not found.")

# 3. Tab Shows & Return Block Updates
old_show = """      todayShow: tab === 'today' ? 'flex' : 'none',
      routeShow: tab === 'route' ? 'flex' : 'none',
      carbonShow: tab === 'carbon' ? 'flex' : 'none',
      meShow: tab === 'me' ? 'flex' : 'none',"""

new_show = """      todayShow: tab === 'today' && S.role !== 'b2b' ? 'flex' : 'none',
      routeShow: tab === 'route' && S.role !== 'b2b' ? 'flex' : 'none',
      carbonShow: tab === 'carbon' && S.role !== 'b2b' ? 'flex' : 'none',
      meShow: tab === 'me' && S.role !== 'b2b' ? 'flex' : 'none',
      b2bShow: S.role === 'b2b' ? 'flex' : 'none',
      passengerNavShow: S.role === 'b2b' ? 'none' : 'flex',
      b2bLedgerHash: '0x' + (1045239 + S.redeemedVouchers.length * 8122).toString(16) + '·b8e2·' + (498807 + S.liveEvents.length * 23).toString(16) + '·provenance',
      toggleRolePassenger: () => this.toggleRolePassenger(),
      toggleRoleB2B: () => this.toggleRoleB2B(),
      peakBg: !S.isOffPeak ? '#FFEAD2' : 'transparent',
      peakCol: !S.isOffPeak ? '#17231C' : '#fff',
      offPeakBg: S.isOffPeak ? '#FFEAD2' : 'transparent',
      offPeakCol: S.isOffPeak ? '#17231C' : '#fff',
      selectPeak: () => this.toggleOffPeak(false),
      selectOffPeak: () => this.toggleOffPeak(true),
      challenge1Bg: S.isOffPeak && S.commuteDone ? '#F2FBEE' : '#FFFDF2',
      challenge1TagBg: S.isOffPeak && S.commuteDone ? '#C8F3DF' : '#fff',
      challenge1TagCol: S.isOffPeak && S.commuteDone ? '#0B7A75' : '#6E776F',
      challenge1Status: S.isOffPeak && S.commuteDone ? '已完成' : '挑戰中',"""

if old_show in html:
    html = html.replace(old_show, new_show, 1)
    print("✓ Tab show rendering replacement succeeded.")
else:
    print("✗ Tab show rendering replacement FAILED: target not found.")

# 4. Commute switcher addition in Today Card
old_switcher = """              <div style="font-size:11.5px; opacity:.78; margin-top:7px;">每公里少排 {{ diffCoef }} g · 你今天通勤 {{ commuteKmStr }} 公里 · 以官方參考係數計算</div>
              <!-- Tooltip Box (QW-2) -->"""

new_switcher = """              <div style="font-size:11.5px; opacity:.78; margin-top:7px;">每公里少排 {{ diffCoef }} g · 你今天通勤 {{ commuteKmStr }} 公里 · 以官方參考係數計算</div>
              <!-- Peak/Off-peak selection switcher (B2B-2) -->
              <div style="margin-top:14px; display:flex; gap:6px; background:rgba(255,255,255,.08); border-radius:12px; padding:3px; border:1.5px solid rgba(255,255,255,.15); position:relative;">
                <button onclick="{{ selectPeak }}" style="all:unset; cursor:pointer; flex:1; text-align:center; padding:6px; border-radius:10px; font-size:11.5px; font-weight:800; background:{{ peakBg }}; color:{{ peakCol }}; transition:.15s;">☀️ 尖峰通勤</button>
                <button onclick="{{ selectOffPeak }}" style="all:unset; cursor:pointer; flex:1; text-align:center; padding:6px; border-radius:10px; font-size:11.5px; font-weight:800; background:{{ offPeakBg }}; color:{{ offPeakCol }}; transition:.15s;">☕ 離峰通勤 (+1種子)</button>
              </div>
              <!-- Tooltip Box (QW-2) -->"""

if old_switcher in html:
    html = html.replace(old_switcher, new_switcher, 1)
    print("✓ Commute switcher addition succeeded.")
else:
    print("✗ Commute switcher addition FAILED: target not found.")

# 5. Spacing for completeCommute button
old_btn_spacing = """            <button onclick="{{ completeCommute }}" style="all:unset; cursor:pointer; box-sizing:border-box; margin-top:18px; width:100%; text-align:center; padding:14px; border-radius:15px; font-weight:800; font-size:15px; background:{{ ctaBg }}; color:{{ ctaCol }}; border:2.5px solid #17231C; box-shadow:4px 4px 0 rgba(23,35,28,.9); transition:.15s;">{{ ctaLabel }}</button>"""

new_btn_spacing = """            <button onclick="{{ completeCommute }}" style="all:unset; cursor:pointer; box-sizing:border-box; margin-top:14px; width:100%; text-align:center; padding:14px; border-radius:15px; font-weight:800; font-size:15px; background:{{ ctaBg }}; color:{{ ctaCol }}; border:2.5px solid #17231C; box-shadow:4px 4px 0 rgba(23,35,28,.9); transition:.15s;">{{ ctaLabel }}</button>"""

if old_btn_spacing in html:
    html = html.replace(old_btn_spacing, new_btn_spacing, 1)
    print("✓ Spacing adjustment succeeded.")
else:
    print("✗ Spacing adjustment FAILED: target not found.")

# 6. Cut Operation Dashboard & Insert Challenges
old_dashboard = """          <!-- OPERATION DASHBOARD -->
          <div style="background:#fff; border-radius:20px; padding:18px; border:2px solid rgba(23,35,28,.8); margin-top:16px;">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
              <div>
                <div style="font-size:13px; font-weight:900;">北捷／合作方 dashboard</div>
                <div style="font-size:11.5px; color:#6E776F; margin-top:3px; line-height:1.45;">營運夥伴即時總覽：觸及、導客、換券、核銷、點數消耗與健康減碳成果。</div>
              </div>
              <span style="font-size:10.5px; color:#2776C9; background:#EAF3FB; padding:4px 8px; border-radius:999px; font-weight:800; flex:none;">營運總覽</span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px; margin-top:13px;">
              <sc-for list="{{ dashboardMetrics }}" as="d" hint-placeholder-count="6">
                <div style="background:{{ d.bg }}; border-radius:14px; padding:11px 12px; border:1px solid {{ d.border }};">
                  <div style="font-size:10.5px; color:#6E776F; font-weight:800;">{{ d.label }}</div>
                  <div style="font-family:'Space Grotesk'; font-size:20px; font-weight:800; color:{{ d.col }}; margin-top:2px;">{{ d.value }}</div>
                  <div style="font-size:10.5px; color:#6E776F; margin-top:2px; line-height:1.35;">{{ d.note }}</div>
                </div>
              </sc-for>
            </div>
            <div style="margin-top:10px; display:flex; align-items:center; justify-content:space-between; gap:8px; background:#17231C; border-radius:12px; padding:10px 12px; color:#fff;">
              <span style="font-size:11px; font-weight:900;">稽核就緒：核銷 / 減碳紀錄 100% 附資料指紋</span>
              <span style="font-size:9.5px; font-weight:800; color:#FFD34D; flex:none;">Numbers Protocol</span>
            </div>
            <div style="margin-top:10px; border:2px solid #17231C; border-radius:14px; overflow:hidden; box-shadow:3px 3px 0 rgba(23,35,28,.85);">
              <div style="display:flex; align-items:center; gap:7px; padding:9px 12px; background:#083C37; color:#fff;">
                <span style="width:8px; height:8px; border-radius:50%; background:#FF6A3D; display:inline-block; animation:ctmGlow 1.6s infinite;"></span>
                <span style="font-size:11px; font-weight:900; letter-spacing:.08em;">LIVE 即時事件流</span>
                <span style="font-size:9.5px; opacity:.72; margin-left:auto;">乘客端互動即時同步</span>
              </div>
              <sc-for list="{{ liveEvents }}" as="e" hint-placeholder-count="3">
                <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; padding:9px 12px; border-top:1px solid rgba(23,35,28,.08); background:#FFFDF2; animation:ctmRise .4s ease both;">
                  <span style="font-size:11.5px; font-weight:700; flex:1; min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{{ e.label }}</span>
                  <span style="display:flex; gap:7px; align-items:center; flex:none;">
                    <span style="font-family:'Space Grotesk'; font-size:11.5px; font-weight:800; color:{{ e.accent }};">{{ e.delta }}</span>
                    <span style="font-size:10px; font-weight:800; color:#0B7A75; background:#C8F3DF; border-radius:999px; padding:2px 7px;">{{ e.cgTxt }}</span>
                  </span>
                </div>
              </sc-for>
            </div>
          </div>"""

new_dashboard = """          <!-- PEAK-SHAVING CHALLENGES (B2B-2) -->
          <div style="background:#fff; border-radius:20px; padding:18px; border:2.5px solid #17231C; box-shadow:4px 4px 0 #17231C; margin-top:16px;">
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="font-size:14px; font-weight:900;">🎯 捷運分流與減碳挑戰</span>
              <span style="font-size:10px; font-weight:900; border:1.5px solid #17231C; border-radius:8px; padding:2px 6px; box-shadow:1.5px 1.5px 0 #17231C; margin-left:auto; background:#FFF0DC; color:#C47500;">分流活動 (B2B-2)</span>
            </div>
            <p style="font-size:12.5px; color:#6E776F; margin-top:6px; line-height:1.45;">參與台北捷運分流與特選站點挑戰，共同守護城市減碳森林，還能賺取額外捷運點與稀有種子！</p>
            
            <div style="display:flex; flex-direction:column; gap:10px; margin-top:12px;">
              <!-- Challenge 1 -->
              <div style="background:{{ challenge1Bg }}; border:1.5px solid #17231C; border-radius:12px; padding:10px 12px; display:flex; justify-content:space-between; align-items:center;">
                <div style="flex:1; min-width:0; padding-right:8px;">
                  <div style="font-size:12px; font-weight:800; color:#17231C;">☕ 離峰通勤大作戰</div>
                  <div style="font-size:10.5px; color:#6E776F; margin-top:2px; line-height:1.4;">早上 10:00 後搭乘捷運，每趟加碼送 1 顆種子 🌱</div>
                </div>
                <span style="font-size:10.5px; font-weight:800; padding:4px 8px; border-radius:8px; background:{{ challenge1TagBg }}; color:{{ challenge1TagCol }}; border:1.5px solid #17231C;">{{ challenge1Status }}</span>
              </div>
              
              <!-- Challenge 2 -->
              <div style="background:#FFFDF2; border:1.5px solid #17231C; border-radius:12px; padding:10px 12px; display:flex; justify-content:space-between; align-items:center;">
                <div style="flex:1; min-width:0; padding-right:8px;">
                  <div style="font-size:12px; font-weight:800; color:#17231C;">💎 冷門站探索任務</div>
                  <div style="font-size:10.5px; color:#6E776F; margin-top:2px; line-height:1.4;">在板南線冷門站（如永春站）出站可得稀有種子</div>
                </div>
                <span style="font-size:10.5px; font-weight:800; padding:4px 8px; border-radius:8px; background:#fff; color:#6E776F; border:1.5px solid #17231C;">挑戰中</span>
              </div>
            </div>
          </div>"""

# Remove CR LF and standardize newlines before comparison to avoid string matching issues
html_norm = html.replace('\r\n', '\n')
old_dashboard_norm = old_dashboard.replace('\r\n', '\n')

if old_dashboard_norm in html_norm:
    html_norm = html_norm.replace(old_dashboard_norm, new_dashboard, 1)
    html = html_norm
    print("✓ Dashboard removed and Challenges inserted successfully.")
else:
    print("✗ Dashboard replacement FAILED: target not found.")

# 7. Add B2B console entrance to Me page and the dedicated B2B tab content
old_me_end = """          <!-- live slot -->
          <div style="margin-top:16px; border:1.5px dashed rgba(23,35,28,.18); border-radius:18px; padding:15px; display:flex; align-items:center; gap:11px;">
            <div style="width:8px; height:8px; border-radius:50%; background:#C47500;"></div>
            <div style="flex:1;">
              <div style="font-size:13px; font-weight:700;">減碳證明技術</div>
              <div style="font-size:11.5px; color:#6E776F; margin-top:2px;">你的減碳證明以 Numbers Protocol 技術封存，隨時可以驗證。</div>
            </div>
          </div>
        </div>

      </div>

      <!-- ═══════════ BOTTOM NAV ═══════════ -->
      <div style="height:78px; flex:none; background:rgba(255,253,242,.96); backdrop-filter:blur(12px); border-top:2.5px solid #17231C; display:flex; align-items:flex-start; padding:9px 12px 0; z-index:20;">"""

new_me_end = """          <!-- live slot -->
          <div style="margin-top:16px; border:1.5px dashed rgba(23,35,28,.18); border-radius:18px; padding:15px; display:flex; align-items:center; gap:11px;">
            <div style="width:8px; height:8px; border-radius:50%; background:#C47500;"></div>
            <div style="flex:1;">
              <div style="font-size:13px; font-weight:700;">減碳證明技術</div>
              <div style="font-size:11.5px; color:#6E776F; margin-top:2px; line-height:1.45;">你的減碳與核銷紀錄像發票存進載具一樣，自動安全封存為可攜式數位資產，隨時可被第三方稽核，更換手機也絕不遺失。</div>
            </div>
          </div>

          <!-- B2B Entrance (B2B-1) -->
          <div style="margin-top:16px; border:1.5px solid rgba(39,118,201,.3); background:#EAF3FB; border-radius:18px; padding:15px; display:flex; align-items:center; gap:11px;">
            <div style="width:8px; height:8px; border-radius:50%; background:#2776C9;"></div>
            <div style="flex:1;">
              <div style="font-size:13px; font-weight:800; color:#2776C9; display:flex; align-items:center; justify-content:space-between; width:100%;">
                <span>B2B 營運合作夥伴主控台</span>
                <button onclick="{{ toggleRoleB2B }}" style="all:unset; cursor:pointer; font-size:11px; font-weight:800; background:#2776C9; color:#fff; border-radius:6px; padding:3px 8px; border:1.5px solid #17231C; box-shadow:1.5px 1.5px 0 #17231C;">進入主控台</button>
              </div>
              <div style="font-size:11.5px; color:#5B6A75; margin-top:3px; line-height:1.45;">提供臺北捷運及各站內租賃合作商家專屬的主控看板，監控導客量、核銷實績、分流與減碳成效，稽核準備就緒。</div>
            </div>
          </div>
        </div>

        <!-- ───── B2B OPERATION CONSOLE (B2B-1 ~ B2B-4) ───── -->
        <div style="display:{{ b2bShow }}; flex-direction:column; padding:4px 18px 96px;">
          <!-- B2B Header -->
          <div style="display:flex; justify-content:space-between; align-items:center; margin:8px 0 14px;">
            <div>
              <div style="font-size:11px; color:#2776C9; font-weight:800; background:#EAF3FB; padding:3px 8px; border-radius:6px; display:inline-block; border:1px solid rgba(39,118,201,.2);">🎛️ B2B 合作夥伴營運總覽</div>
              <div style="font-size:20px; font-weight:900; margin-top:5px; color:#17231C;">台北捷運 GO · 營運主控台</div>
            </div>
            <button onclick="{{ toggleRolePassenger }}" style="all:unset; cursor:pointer; font-size:11px; font-weight:800; border:2px solid #17231C; background:#fff; padding:6px 12px; border-radius:10px; box-shadow:2px 2px 0 #17231C;">👤 返回 C 端</button>
          </div>

          <!-- B2B-1: OPERATION DASHBOARD -->
          <div style="background:#fff; border-radius:20px; padding:18px; border:2.5px solid #17231C; box-shadow:4px 4px 0 #17231C; margin-top:10px;">
            <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
              <div>
                <div style="font-size:13.5px; font-weight:900;">北捷／合作商家 營運 Dashboard</div>
                <div style="font-size:11.5px; color:#6E776F; margin-top:3px; line-height:1.45;">即時稽核指標：精準會員觸及、實名引導導客、核銷與健康共享活動實績。</div>
              </div>
            </div>
            
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:9px; margin-top:13px;">
              <sc-for list="{{ dashboardMetrics }}" as="d" hint-placeholder-count="6">
                <div style="background:{{ d.bg }}; border-radius:14px; padding:11px 12px; border:1.5px solid {{ d.border }};">
                  <div style="font-size:10.5px; color:#6E776F; font-weight:800;">{{ d.label }}</div>
                  <div style="font-family:'Space Grotesk'; font-size:20px; font-weight:800; color:{{ d.col }}; margin-top:2px;">{{ d.value }}</div>
                  <div style="font-size:10.5px; color:#6E776F; margin-top:2px; line-height:1.35;">{{ d.note }}</div>
                </div>
              </sc-for>
            </div>
            
            <div style="margin-top:10px; display:flex; align-items:center; justify-content:space-between; gap:8px; background:#17231C; border-radius:12px; padding:10px 12px; color:#fff; border:1.5px solid #17231C;">
              <span style="font-size:11px; font-weight:900; color:#fff;">✓ 稽核就緒：減碳與核銷紀錄 100% 附數據指紋</span>
              <span style="font-size:9.5px; font-weight:800; color:#FFD34D; flex:none;">Numbers Protocol</span>
            </div>

            <!-- B2B-2: Peak-Shaving Events mappings to TRTC Operations KPIs -->
            <div style="margin-top:14px; border-top:1px dashed rgba(23,35,28,.15); padding-top:12px;">
              <div style="font-size:12.5px; font-weight:900; color:#17231C; margin-bottom:8px;">🎯 分流與營運事件 (對映北捷 KPI)</div>
              <div style="display:flex; flex-direction:column; gap:8px;">
                <div style="background:#FFFDF2; border-radius:10px; padding:8px 10px; border:1px solid rgba(23,35,28,.08); font-size:11.5px;">
                  <div style="font-weight:800; color:#0B7A75;">🌧️ 雨天借用共享傘 (raingo)</div>
                  <div style="color:#6E776F; margin-top:2px; line-height:1.45;">營運對映：<strong>提升雨傘週轉率與站內防汛防滑安全</strong></div>
                </div>
                <div style="background:#F2FBEE; border-radius:10px; padding:8px 10px; border:1px solid rgba(23,35,28,.08); font-size:11.5px;">
                  <div style="font-weight:800; color:#C47500;">☕ 離峰通勤引導 (10:00 後搭乘)</div>
                  <div style="color:#6E776F; margin-top:2px; line-height:1.45;">營運對映：<strong>舒緩尖峰運能舒緩 + 離峰乘座率提升 15%</strong></div>
                </div>
                <div style="background:#EAF3FB; border-radius:10px; padding:8px 10px; border:1px solid rgba(23,35,28,.08); font-size:11.5px;">
                  <div style="font-weight:800; color:#2776C9;">💎 冷門站點探索挑戰 (稀有種子)</div>
                  <div style="color:#6E776F; margin-top:2px; line-height:1.45;">營運對映：<strong>引導熱點人流均衡 + 提升站內場站租賃觸及率</strong></div>
                </div>
              </div>
            </div>

            <!-- B2B-3: Real-name lead success attribution ledger -->
            <div style="margin-top:14px; border-top:1px dashed rgba(23,35,28,.15); padding-top:12px;">
              <div style="font-size:12.5px; font-weight:900; color:#17231C; margin-bottom:8px;">🛡️ B2B-3: 實名導客實數歸因與可稽核存證</div>
              <p style="font-size:11.5px; color:#6E776F; line-height:1.45; margin:0 0 8px;">每一次 C 端的優惠券兌換及導引，系統會即時寫入去識別化的 provenance Ledger。這將做為北捷與合作商家之間「CPS 導客效果計費」及「減碳回饋清算」的真實、不可篡改憑證。</p>
              <div style="background:#FFFDF2; border:1.5px solid #17231C; border-radius:10px; padding:8px 10px; font-size:11px;">
                <div style="font-weight:800; color:#17231C; display:flex; align-items:center; gap:5px;"><span style="width:6px;height:6px;border-radius:50%;background:#38B86F;"></span>CPS Attribution Fingerprint Ledger</div>
                <div style="font-family:'Space Grotesk'; color:#6E776F; margin-top:3px;">Ledger Hash: {{ b2bLedgerHash }}</div>
                <div style="font-size:9.5px; color:#9AA39B; margin-top:2px;">Verified by Numbers Protocol Web3 Anchor</div>
              </div>
            </div>

            <!-- B2B-4: Station Line Forest Screen Concept -->
            <div style="margin-top:14px; border-top:1px dashed rgba(23,35,28,.15); padding-top:12px;">
              <div style="font-size:12.5px; font-weight:900; color:#17231C; margin-bottom:8px;">🌲 B2B-4: 站點共同森林（城市大螢幕連動）</div>
              <p style="font-size:11.5px; color:#6E776F; line-height:1.45; margin:0 0 8px;">板南線全體用戶共同累積的減碳量將種植出一座巨大的「板南線共同神木森林」，該形象在各實體捷運站電子螢幕上即時輪播，以極具視覺衝擊力的方式展現綠色低碳城市的形象，吸引更多市民轉乘捷運。</p>
              <div style="background:linear-gradient(135deg,#0B7A75 0%,#083C37 100%); border-radius:12px; padding:12px; color:#fff; border:1.5px solid #17231C; display:flex; align-items:center; justify-content:space-between; box-shadow:2px 2px 0 #17231C;">
                <div>
                  <div style="font-size:10.5px; opacity:.85; font-weight:700;">板南線全線共同減碳進度</div>
                  <div style="font-size:16px; font-weight:900; margin-top:2px; color:#FFD34D;">🌱 24,980 棵神木已成功解鎖</div>
                </div>
                <div style="display:flex; gap:3px;">
                  <span style="font-size:16px; animation:ctmBob 2s infinite;">🌲</span>
                  <span style="font-size:16px; animation:ctmBob 2.2s infinite;">🌳</span>
                  <span style="font-size:16px; animation:ctmBob 1.8s infinite;">🌲</span>
                </div>
              </div>
            </div>

            <!-- Live Events Log (CORE-6 success attribution) -->
            <div style="margin-top:14px; border-top:1px dashed rgba(23,35,28,.15); padding-top:12px;">
              <div style="font-size:12.5px; font-weight:900; color:#17231C; margin-bottom:8px; display:flex; align-items:center; gap:6px;"><span style="width:8px; height:8px; border-radius:50%; background:#FF6A3D; display:inline-block; animation:ctmGlow 1.6s infinite;"></span>CPS LIVE 乘客端互動流</div>
              <div style="border:2px solid #17231C; border-radius:12px; overflow:hidden; box-shadow:2px 2px 0 rgba(23,35,28,.85);">
                <sc-for list="{{ liveEvents }}" as="e" hint-placeholder-count="3">
                  <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; padding:8px 10px; border-top:1px solid rgba(23,35,28,.08); background:#FFFDF2; font-size:11px;">
                    <span style="font-weight:700; flex:1; min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{{ e.label }}</span>
                    <span style="display:flex; gap:6px; align-items:center; flex:none;">
                      <span style="font-family:'Space Grotesk'; font-weight:800; color:{{ e.accent }};">{{ e.delta }}</span>
                      <span style="font-weight:800; color:#0B7A75; background:#C8F3DF; border-radius:999px; padding:1px 6px;">{{ e.cgTxt }}</span>
                    </span>
                  </div>
                </sc-for>
              </div>
            </div>

          </div>
        </div>

      </div>

      <!-- ═══════════ BOTTOM NAV ═══════════ -->
      <div style="height:78px; flex:none; background:rgba(255,253,242,.96); backdrop-filter:blur(12px); border-top:2.5px solid #17231C; display:{{ passengerNavShow }}; align-items:flex-start; padding:9px 12px 0; z-index:20;">"""

html_norm = html.replace('\r\n', '\n')
old_me_end_norm = old_me_end.replace('\r\n', '\n')

if old_me_end_norm in html_norm:
    html_norm = html_norm.replace(old_me_end_norm, new_me_end, 1)
    html = html_norm
    print("✓ B2B console view and Me entrance replacement succeeded.")
else:
    print("✗ B2B console view replacement FAILED: target not found.")

# Write back
open(html_path, 'w', encoding='utf-8').write(html)
print("Phase 3 changes successfully written.")
