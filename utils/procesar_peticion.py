import requests
from lxml import html
import json

def eafit(pagina,post_id,model_id,category):
    url = "http://bitacora.eafit.edu.co/wp-admin/admin-ajax.php"
    data = {
        "action": "raven_get_render_posts",
        "post_id": post_id,
        "model_id": model_id,
        "paged": pagina,
        "category": category,
    }
    salida = []
    datos = requests.post(url, data=data)
    post = json.loads(datos.text)
    post = post["data"]["posts"]
    for html_data in post:
        raw_data = html.fromstring(html_data)
        link = raw_data.xpath("//a[@href]/@href")[0]
        salida.append(link)
    return salida

def uniminuto(pagina):
    url = "https://www.uniminutoradio.com.co/wp-admin/admin-ajax.php?td_theme_name=Newspaper&v=10.3.9.1"
    data = {
        "td_atts":'{"modules_on_row":"eyJwaG9uZSI6IjEwMCUifQ==","modules_gap":"eyJsYW5kc2NhcGUiOiI0MCIsInBvcnRyYWl0IjoiMjgifQ==","modules_category":"above","show_excerpt":"eyJwb3J0cmFpdCI6Im5vbmUiLCJwaG9uZSI6Im5vbmUifQ==","show_btn":"none","ajax_pagination":"infinite","image_height":"eyJhbGwiOiI2NiIsInBob25lIjoiMTAwIn0=","limit":"10","image_floated":"float_left","image_width":"eyJhbGwiOiI0OSIsImxhbmRzY2FwZSI6IjQ2IiwicG9ydHJhaXQiOiI0MCIsInBob25lIjoiMjYifQ==","meta_padding":"eyJhbGwiOiIwIDAgMCAyMHB4IiwicGhvbmUiOiIwIDAgMCAxNnB4In0=","modules_category_padding":"0 0 6px","show_com":"none","f_title_font_family":"712","f_title_font_size":"eyJhbGwiOiIyNiIsImxhbmRzY2FwZSI6IjE4IiwicG9ydHJhaXQiOiIxOCIsInBob25lIjoiMTYifQ==","f_title_font_line_height":"1.2","f_title_font_weight":"500","f_cat_font_family":"712","f_cat_font_size":"11","f_cat_font_weight":"400","f_cat_font_line_height":"1","f_meta_font_family":"712","f_meta_font_size":"11","f_meta_font_weight":"400","title_txt_hover":"#004b8e","all_underline_color":"","cat_bg":"rgba(0,0,0,0)","cat_txt":"#666666","cat_txt_hover":"#000000","author_txt":"#666666","author_txt_hover":"#000000","mc1_el":"40","all_modules_space":"eyJhbGwiOiI1MCIsImxhbmRzY2FwZSI6IjMwIiwicG9ydHJhaXQiOiIzMCIsInBob25lIjoiMzAifQ==","pag_a_bg":"#004b8e","pag_a_border":"#004b8e","pag_h_border":"#004b8e","pag_h_bg":"rgba(0,0,0,0)","pag_h_text":"#000000","f_pag_font_family":"712","f_pag_font_size":"eyJhbGwiOiIxMyIsInBvcnRyYWl0IjoiMTEifQ==","f_ex_font_size":"eyJsYW5kc2NhcGUiOiIxMiIsImFsbCI6IjE4In0=","pag_space":"eyJsYW5kc2NhcGUiOiIyMCIsImFsbCI6IjQwIiwicG9ydHJhaXQiOiIyMCIsInBob25lIjoiMjUifQ==","tdc_css":"eyJwb3J0cmFpdCI6eyJtYXJnaW4tYm90dG9tIjoiNDAiLCJkaXNwbGF5IjoiIn0sInBvcnRyYWl0X21heF93aWR0aCI6MTAxOCwicG9ydHJhaXRfbWluX3dpZHRoIjo3NjgsImxhbmRzY2FwZSI6eyJtYXJnaW4tYm90dG9tIjoiNTAiLCJkaXNwbGF5IjoiIn0sImxhbmRzY2FwZV9tYXhfd2lkdGgiOjExNDAsImxhbmRzY2FwZV9taW5fd2lkdGgiOjEwMTksInBob25lIjp7Im1hcmdpbi1ib3R0b20iOiI0MCIsImRpc3BsYXkiOiIifSwicGhvbmVfbWF4X3dpZHRoIjo3Njd9","pag_padding":"eyJwb3J0cmFpdCI6IjVweCAxMHB4In0=","f_ex_font_family":"453","f_ex_font_line_height":"1.1","ex_txt":"#000000","search_query":"conflicto armado","block_type":"tdb_loop","separator":"","custom_title":"","custom_url":"","block_template_id":"","mc1_tl":"","offset":"","post_ids":"","sort":"","ajax_pagination_infinite_stop":"","container_width":"","m_padding":"","m_radius":"","modules_border_size":"","modules_border_style":"","modules_border_color":"#eaeaea","modules_divider":"","modules_divider_color":"#eaeaea","h_effect":"","image_size":"","image_radius":"","hide_image":"","video_icon":"","video_popup":"yes","video_rec":"","spot_header":"","video_rec_title":"- Advertisement -","video_rec_color":"","show_vid_t":"block","vid_t_margin":"","vid_t_padding":"","video_title_color":"","video_title_color_h":"","video_bg":"","video_overlay":"","vid_t_color":"","vid_t_bg_color":"","f_vid_title_font_header":"","f_vid_title_font_title":"Video pop-up article title","f_vid_title_font_settings":"","f_vid_title_font_family":"","f_vid_title_font_size":"","f_vid_title_font_line_height":"","f_vid_title_font_style":"","f_vid_title_font_weight":"","f_vid_title_font_transform":"","f_vid_title_font_spacing":"","f_vid_title_":"","f_vid_time_font_title":"Video duration text","f_vid_time_font_settings":"","f_vid_time_font_family":"","f_vid_time_font_size":"","f_vid_time_font_line_height":"","f_vid_time_font_style":"","f_vid_time_font_weight":"","f_vid_time_font_transform":"","f_vid_time_font_spacing":"","f_vid_time_":"","meta_info_align":"","meta_info_horiz":"content-horiz-left","meta_width":"","meta_margin":"","art_title":"","art_excerpt":"","excerpt_col":"1","excerpt_gap":"","art_audio":"","art_audio_size":"1.5","art_btn":"","meta_info_border_size":"","meta_info_border_style":"","meta_info_border_color":"#eaeaea","modules_category_margin":"","modules_cat_border":"","modules_category_radius":"0","show_cat":"inline-block","show_author":"inline-block","author_photo":"","author_photo_size":"","author_photo_space":"","author_photo_radius":"","show_date":"inline-block","show_modified_date":"","show_review":"inline-block","review_size":"2.5","excerpt_middle":"","excerpt_inline":"","show_audio":"block","hide_audio":"","meta_space":"","btn_title":"","btn_margin":"","btn_padding":"","btn_border_width":"","btn_radius":"","pag_border_width":"","pag_border_radius":"","prev_tdicon":"","next_tdicon":"","pag_icons_size":"","f_header_font_header":"","f_header_font_title":"Block header","f_header_font_settings":"","f_header_font_family":"","f_header_font_size":"","f_header_font_line_height":"","f_header_font_style":"","f_header_font_weight":"","f_header_font_transform":"","f_header_font_spacing":"","f_header_":"","f_pag_font_title":"Pagination text","f_pag_font_settings":"","f_pag_font_line_height":"","f_pag_font_style":"","f_pag_font_weight":"","f_pag_font_transform":"","f_pag_font_spacing":"","f_pag_":"","f_title_font_header":"","f_title_font_title":"Article title","f_title_font_settings":"","f_title_font_style":"","f_title_font_transform":"","f_title_font_spacing":"","f_title_":"","f_cat_font_title":"Article category tag","f_cat_font_settings":"","f_cat_font_style":"","f_cat_font_transform":"","f_cat_font_spacing":"","f_cat_":"","f_meta_font_title":"Article meta info","f_meta_font_settings":"","f_meta_font_line_height":"","f_meta_font_style":"","f_meta_font_transform":"","f_meta_font_spacing":"","f_meta_":"","f_ex_font_title":"Article excerpt","f_ex_font_settings":"","f_ex_font_style":"","f_ex_font_weight":"","f_ex_font_transform":"","f_ex_font_spacing":"","f_ex_":"","f_btn_font_title":"Article read more button","f_btn_font_settings":"","f_btn_font_family":"","f_btn_font_size":"","f_btn_font_line_height":"","f_btn_font_style":"","f_btn_font_weight":"","f_btn_font_transform":"","f_btn_font_spacing":"","f_btn_":"","mix_color":"","mix_type":"","fe_brightness":"1","fe_contrast":"1","fe_saturate":"1","mix_color_h":"","mix_type_h":"","fe_brightness_h":"1","fe_contrast_h":"1","fe_saturate_h":"1","m_bg":"","shadow_shadow_header":"","shadow_shadow_title":"Module Shadow","shadow_shadow_size":"","shadow_shadow_offset_horizontal":"","shadow_shadow_offset_vertical":"","shadow_shadow_spread":"","shadow_shadow_color":"","title_txt":"","all_underline_height":"","cat_bg_hover":"","cat_border":"","cat_border_hover":"","meta_bg":"","date_txt":"","com_bg":"","com_txt":"","shadow_m_shadow_header":"","shadow_m_shadow_title":"Meta info shadow","shadow_m_shadow_size":"","shadow_m_shadow_offset_horizontal":"","shadow_m_shadow_offset_vertical":"","shadow_m_shadow_spread":"","shadow_m_shadow_color":"","audio_btn_color":"","audio_time_color":"","audio_bar_color":"","audio_bar_curr_color":"","btn_bg":"","btn_bg_hover":"","btn_txt":"","btn_txt_hover":"","btn_border":"","btn_border_hover":"","nextprev_border_h":"","pag_text":"","pag_a_text":"","pag_bg":"","pag_border":"","el_class":"","td_column_number":2,"header_color":"","td_ajax_preloading":"","td_ajax_filter_type":"","td_filter_default_txt":"","td_ajax_filter_ids":"","color_preset":"","border_top":"","css":"","class":"tdi_84_33c","tdc_css_class":"tdi_84_33c","tdc_css_class_style":"tdi_84_33c_rand_style"}',
        "td_block_id":"tdi_84_f66",
        "td_column_number":2,
        "td_current_page":pagina,
        "block_type":"tdb_loop",
        "action" :"td_ajax_block",
        "td_magic_token" : "09a546b4a9"
    }
    datos = requests.post(url, data=data)
    raw_data = json.loads(datos.text)
    raw_data = raw_data["td_data"]
    links = html.fromstring(raw_data)
    links = links.xpath("//div/a[@href]/@href")
    for link in links:
        if link.find("/seccion/") != -1:
            links.remove(link)
    return links

print(uniminuto(6))