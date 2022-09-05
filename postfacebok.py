from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import win32com.client as comclt
from time import sleep
import sys,pyautogui, time 
from webdriver_manager.chrome import ChromeDriverManager 
def main():
    # Set up Facebook login account name and password
    account = "shayona163@gmail.com"
    passwordCredential = "ajay123*"
    descripcionPost = "description sample"\
        "description sample"\
        " description sample"\
        " description sample"    
    titlePost ="title sample"
    pricePost ="250"
    groupPostList = [
        "https://www.facebook.com/Wordpress-beginner-102735147894097",
    ]    
    imageFolderPath = 'C:/Users/MS/Downloads/pinterest-downloader-master/pinterest-downloader-master/images/vvmahesh/Couple Photography Poses'
    nameImagesToPost = '"2.jpg"'
    
    
    #Log of post correct
    file = open("gruposLogs.txt", "w") 
    contador = 0;
    for group in groupPostList:
        # Login Facebook
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.facebook.com')
        driver.execute_script("document.getElementById('email').setAttribute('type','password')")
        email=driver.find_element_by_id('email') #find email input
        password=driver.find_element_by_id('pass') #find password input
        email.send_keys(account)
        password.send_keys(passwordCredential)
        login=driver.find_element_by_name('login') #find button login
        login.click()
        time.sleep(1)         
        try:
            driver.get(group)
            file.write('\n'+group)                      
            time.sleep(2)
            contador +=1            
            searchBar = driver.find_element(By.XPATH,'//*[@class="qi72231t nu7423ey tav9wjvu flwp5yud tghlliq5 gkg15gwv s9ok87oh s9ljgwtm lxqftegz bf1zulr9 frfouenu bonavkto djs4p424 r7bn319e bdao358l fsf7x5fv s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk dnr7xe2t om3e55n1 cr00lzj9 rn8ck1ys s3jn8y49 g4tp4svg jl2a5g8c f14ij5to l3ldwz01 icdlwmnq i85zmo3j h8391g91 m0cukt09 kpwa50dg ta68dy8c alzwoclg jg3vgc78 cgu29s5g i15ihif8 jcxyg2ei g10o6gae q46jt4gp b0eko5f3 r5g9zsuq fwlpnqze"]')     #find button of group
            searchBar.click()               
            time.sleep(2)
            '''button_list = driver.find_elements_by_class_name("bp9cbjyn.rq0escxv.j83agx80.cbu4d94t.datstx6m.taijpn5t.tvx22r68.hv4rvrfc.cifkjjtc.dati1w0a.oppkgyvt.k1338c9a.ntikgwu3.c34aag8n")                  
            button_list[0].click()
            itemsForm=driver.find_elements_by_class_name("a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5")
            driver.execute_script("document.getElementsByClassName('oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 j83agx80 mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l')[0].setAttribute('id','inputToFile')")
            driver.execute_script("document.getElementsByClassName('oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 j83agx80 mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l')[0].setAttribute('type','file')")
            btn=driver.find_element_by_id('inputToFile')            
            btn.click()'''
            sleep = 1            
            windowsShell = comclt.Dispatch("WScript.Shell")
            time.sleep(sleep)
            windowsShell.SendKeys("{TAB}{TAB}{TAB}{TAB}{TAB}")
            windowsShell.SendKeys("{ENTER}")
            time.sleep(sleep)
            windowsShell.SendKeys(imageFolderPath)
            windowsShell.SendKeys("{ENTER}")
            time.sleep(sleep)
            windowsShell.SendKeys("{TAB}")
            time.sleep(sleep)
            windowsShell.SendKeys("{TAB}")
            time.sleep(sleep)
            windowsShell.SendKeys("{TAB}")
            time.sleep(sleep)
            windowsShell.SendKeys("{TAB}")
            time.sleep(sleep)
            windowsShell.SendKeys("{TAB}")
            time.sleep(sleep)
            windowsShell.SendKeys(nameImagesToPost)
            time.sleep(sleep)
            windowsShell.SendKeys("{ENTER}")
            time.sleep(2)                
            time.sleep(1)
            time.sleep(5)
            '''title_input = driver.find_element(By.XPATH,'//*[@aria-label="Título"]')
            time.sleep(1)
            title_input.send_keys(titlePost)
            time.sleep(1)
            price_input =  driver.find_elements_by_class_name("oajrlxb2.rq0escxv.f1sip0of.hidtqoto.e70eycc3.lzcic4wl.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.oo9gr5id.qc3s4z1d.knj5qynh.fo6rh5oj.osnr6wyh.hv4rvrfc.dati1w0a.p0x8y401.k4urcfbm.iu8raji3")
            time.sleep(1)
            price_input[1].send_keys(pricePost) 
            time.sleep(1)
            desc = driver.find_elements_by_class_name('oajrlxb2.rq0escxv.f1sip0of.hidtqoto.lzcic4wl.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.oo9gr5id.j83agx80.jagab5yi.knj5qynh.fo6rh5oj.oud54xpy.l9qdfxac.ni8dbmo4.stjgntxs.hv4rvrfc.dati1w0a.ieid39z1.k4urcfbm')
            time.sleep(1)
            desc[0].send_keys(descripcionPost) 
            time.sleep(1)            
            post_button = driver.find_element(By.XPATH,'//*[@aria-label="Siguiente"]')            
            post_button.click()
            time.sleep(2)'''
            btn_savePost = driver.find_element(By.XPATH,'//*[@class="bdao358l sl27f92c r227ecj6 gt60zsk1 mfclru0v"]')     #find button of group
            btn_savePost.click()   
            time.sleep(5)
            '''btn_savePost =  driver.find_elements_by_class_name("bdao358l sl27f92c r227ecj6 gt60zsk1 mfclru0v")
            btn_savePost[2].click()'''
             
        except Exception:
           file.close()           
           print('########   ERROR #### in the group ' +group)
           
    file.close()

if __name__ == '__main__':
  main()