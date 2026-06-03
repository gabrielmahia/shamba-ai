import streamlit as st
import urllib.request
import json
import datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Shamba AI — Mshauri wa Kilimo",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""<style>
.main { background: #0a1a0a; color: #e8f5e9; }
.stApp { background: #0a1a0a; }
.crop-card {
    background: #0d2b0d; border: 1px solid #1b5e20;
    border-radius: 10px; padding: 14px 18px; margin: 8px 0;
}
.stButton > button {
    background: #2e7d32; color: white; border: none;
    border-radius: 8px; padding: 10px 24px; font-weight: 700;
    width: 100%;
}
</style>""", unsafe_allow_html=True)

# ── API Key ───────────────────────────────────────────────────────────────────
API_KEY = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")

# ── Gemini helper ─────────────────────────────────────────────────────────────
def ask_gemini(prompt: str, system: str = "") -> str:
    if not API_KEY:
        return "❌ API key not configured. Add GOOGLE_API_KEY to .streamlit/secrets.toml"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "systemInstruction": {"parts": [{"text": system}]} if system else {},
        "generationConfig": {"temperature": 0.4, "maxOutputTokens": 800}
    }
    try:
        req = urllib.request.Request(
            url, data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read())
            return d["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"❌ Error: {e}"

SYSTEM = """Wewe ni mshauri wa kilimo kwa wakulima wa Kenya.
Jibu kwa Kiswahili wazi na rahisi kuelewa.
Toa ushauri wa vitendo unaotegemea hali halisi ya Kenya.
Kama hujui jibu sahihi, sema hivyo na umpeleke mkulima kwa mtaalamu wa ugani.
Usijibu mambo yasiyohusiana na kilimo."""

# ── UI ─────────────────────────────────────────────────────────────────────────
st.markdown("# 🌾 Shamba AI")
st.markdown("**Mshauri wa Kilimo — Kiswahili**")
st.caption("Uliza swali lolote kuhusu kilimo, magonjwa ya mazao, bei za soko, au hali ya hewa.")

tab1, tab2, tab3 = st.tabs(["🔍 Magonjwa ya Mazao", "💰 Bei za Soko", "🌱 Ushauri wa Kilimo"])

with tab1:
    st.markdown("### Gundua Ugonjwa wa Zao")
    crop = st.selectbox("Zao", ["Mahindi", "Maharagwe", "Nyanya", "Viazi", "Chai", "Kahawa", "Ngano", "Mchele"])
    symptoms = st.text_area("Elezea dalili unazoziona:", 
                             placeholder="Mfano: Majani yanageuka njano na kuwa na madoa mekundu...",
                             height=120)
    if st.button("🔍 Gundua Ugonjwa", key="disease_btn"):
        if symptoms:
            with st.spinner("Nachanganua..."):
                prompt = f"Zao: {crop}\nDalili: {symptoms}\n\nNini kinaweza kuwa ugonjwa huu? Toa: 1) Jina la ugonjwa 2) Sababu 3) Jinsi ya kutibu 4) Jinsi ya kuzuia"
                result = ask_gemini(prompt, SYSTEM)
            st.markdown(f"""<div class="crop-card">{result.replace(chr(10), '<br>')}</div>""", unsafe_allow_html=True)
        else:
            st.warning("Tafadhali elezea dalili kwanza.")

with tab2:
    st.markdown("### Bei za Soko Leo")
    county = st.selectbox("Kaunti", ["Nairobi", "Kiambu", "Meru", "Nakuru", "Kisumu", "Mombasa", "Eldoret", "Thika"])
    market_crop = st.selectbox("Zao", ["Mahindi", "Maharagwe", "Nyanya", "Viazi vitamu", "Ndizi", "Sukari", "Unga wa mahindi"])
    if st.button("📊 Angalia Bei", key="price_btn"):
        with st.spinner("Ninatafuta..."):
            today = datetime.date.today().strftime("%B %Y")
            prompt = f"Bei za {market_crop} katika soko la {county} Kenya, {today}. Toa bei ya jumla (kwa debe/kg) na bei ya rejareja. Kama hujui bei halisi, toa makadirio ya kawaida na ushauri wa ambapo mkulima anaweza kupata bei sahihi."
            result = ask_gemini(prompt, SYSTEM)
        st.markdown(f"""<div class="crop-card">{result.replace(chr(10), '<br>')}</div>""", unsafe_allow_html=True)

with tab3:
    st.markdown("### Uliza Swali lolote la Kilimo")
    question = st.text_area("Swali lako:", placeholder="Mfano: Ni wakati gani mzuri wa kupanda mahindi Rift Valley?", height=120)
    if st.button("💡 Pata Ushauri", key="advice_btn"):
        if question:
            with st.spinner("Ninafikiri..."):
                result = ask_gemini(question, SYSTEM)
            st.markdown(f"""<div class="crop-card">{result.replace(chr(10), '<br>')}</div>""", unsafe_allow_html=True)
        else:
            st.warning("Tafadhali andika swali lako.")

st.markdown("---")
st.caption("⚠️ Ushauri huu ni kwa madhumuni ya elimu tu. Thibitisha kwa mtaalamu wa ugani kabla ya kutenda. | Shamba AI v1.0")
