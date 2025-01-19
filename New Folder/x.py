from seleniumbase import SB

with SB(uc=True) as sb:
    url = "https://chatgpt.com"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(30)
