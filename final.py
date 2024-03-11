from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui


def success(data, count, video_count,email_id,f_name,l_name,passw,video_name,video_bio,channelDescription,index,tick):
    try:
        service = Service(executable_path="Final-Year-Project\\AutomatingUserCreation\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.get("http://localhost:5001/")
# ---------------------------------------------------------------------------------------------------
        # Automating Sign Up page 

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div//button[2]"))
        )
        sign_up = driver.find_element(By.XPATH, "//div//button[2]")
        sign_up.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form//div[1]//input[1]"))
        )
        email = driver.find_element(By.XPATH, "//form//div[1]//input[1]")
        email.send_keys(email_id)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form//div[2]//input[1]"))
        )
        fname = driver.find_element(By.XPATH, "//form//div[2]//input[1]")
        fname.send_keys(f_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form//div[3]//input[1]"))
        )
        lname = driver.find_element(By.XPATH, "//form//div[3]//input[1]")
        lname.send_keys(l_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form//div[4]//input[1]"))
        )
        password = driver.find_element(By.XPATH, "//form//div[4]//input[1]")
        password.send_keys(passw)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//form//div[5]//input[1]"))
        )
        password_conf = driver.find_element(By.XPATH, "//form//div[5]//input[1]")
        password_conf.send_keys(passw)

        # time.sleep(10)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Sign In'][1]"))
        )
        sign_in = driver.find_element(By.XPATH, "//button[text()='Sign In'][1]")
        sign_in.click()     
        
# ---------------------------------------------------------------------------------------------------------
        # Login In page

        time.sleep(5)
    
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[1]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        username = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[1]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        username.send_keys(email_id)    

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[2]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        password_login = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[2]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        password_login.send_keys(passw)       
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[@class='flex items-center gap-4']/button[@class='bg-theme text-white px-5 py-1.5  h-max w-max rounded-md uppercase hover:bg-themeHover']"))
        )
        login = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[@class='flex items-center gap-4']/button[@class='bg-theme text-white px-5 py-1.5  h-max w-max rounded-md uppercase hover:bg-themeHover']")
        login.click()
# # ---------------------------------------------------------------------------------------------------------
# # Create Channel
        
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[1]"))
        )
        create_video = driver.find_element(By.XPATH, "//button[1]")
        create_video.click()        
        
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/button[@class='group/item flex items-center text-white gap-4 px-4 py-6 rounded bg-gradient-to-r from-[#FF0000] to-[#590000]']"))
        )
        create_channel = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/button[@class='group/item flex items-center text-white gap-4 px-4 py-6 rounded bg-gradient-to-r from-[#FF0000] to-[#590000]']")
        create_channel.click()

        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/section[@class=' overflow-auto  w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1 border-l-2']/div[1]/input[@class=' w-full bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        channel_name = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/section[@class=' overflow-auto  w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1 border-l-2']/div[1]/input[@class=' w-full bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        channel_name.clear()
        channel_name.send_keys(f_name)

        time.sleep(2)


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/section[@class=' overflow-auto  w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1 border-l-2']/div[2]/textarea[@class=' w-full min-h-[30vh] bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        channel_descr = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/section[@class=' overflow-auto  w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1 border-l-2']/div[2]/textarea[@class=' w-full min-h-[30vh] bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        channel_descr.send_keys(channelDescription)


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/section[@class=' overflow-auto  w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1 border-l-2']/div[@class='flex gap-2 items-center']/button[@class='w-max flex-end bg-theme border border-transparent text-white px-5 py-1.5 h-max rounded-md uppercase']"))
        )
        create = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/section[@class=' overflow-auto  w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1 border-l-2']/div[@class='flex gap-2 items-center']/button[@class='w-max flex-end bg-theme border border-transparent text-white px-5 py-1.5 h-max rounded-md uppercase']")
        create.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/button[@class='border mb-2 pl-3 pr-5 py-1.5 h-max rounded-md uppercase flex items-center gap-2']"))
        )
        my_profile = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/button[@class='border mb-2 pl-3 pr-5 py-1.5 h-max rounded-md uppercase flex items-center gap-2']")
        my_profile.click()

# # ---------------------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------------------
#         # Video Upload 

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/ul[@class='flex-column space-y space-y-4 text-sm font-medium text-gray-500  md:me-4 mb-4 md:mb-0']/li[2]/a[@class=' inline-flex items-center px-4 py-3 rounded-lg w-full  group/item  hover:text-gray-800 bg-white']"))
        )
        my_studio = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/ul[@class='flex-column space-y space-y-4 text-sm font-medium text-gray-500  md:me-4 mb-4 md:mb-0']/li[2]/a[@class=' inline-flex items-center px-4 py-3 rounded-lg w-full  group/item  hover:text-gray-800 bg-white']")
        my_studio.click()       
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/button[@class='border-2 rounded-md p-12 min-w-80 disabled:opacity-70']"))
        )
        ad_video = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/button[@class='border-2 rounded-md p-12 min-w-80 disabled:opacity-70']")
        ad_video.click()  

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto p-8 w-full  flex flex-col justify-center']/div[@class='border-dashed border-2 border-opacity-70 border-gray-400 py-12 flex flex-col justify-center items-center']/label[@id='button']"))
        )
        upload_video = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto p-8 w-full  flex flex-col justify-center']/div[@class='border-dashed border-2 border-opacity-70 border-gray-400 py-12 flex flex-col justify-center items-center']/label[@id='button']")
        upload_video.click()

        time.sleep(2)

        pyautogui.typewrite(f"\\C:\\Dhanush\\Final-Year-Project\\4_3\\{index}", interval=0.1)

        pyautogui.press("enter")

        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[1]/input[@class=' w-full bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        video_title = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[1]/input[@class=' w-full bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        video_title.send_keys(video_name)

        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[2]/textarea[@class=' w-full min-h-[30vh] bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        video_descr = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[2]/textarea[@class=' w-full min-h-[30vh] bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        video_descr.send_keys(video_bio)       
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[@class='flex gap-2 items-center']/button[@class='w-max flex-end bg-theme border border-transparent text-white px-5 py-1.5 h-max rounded-md uppercase']"))
        )
        video_save = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[@class='flex gap-2 items-center']/button[@class='w-max flex-end bg-theme border border-transparent text-white px-5 py-1.5 h-max rounded-md uppercase']")
        video_save.send_keys(video_bio)

# # ---------------------------------------------------------------------------------------------------------
        
        time.sleep(5)
        # If successful, move to the next user
        count += 1
        # video_count += 1
        driver.quit()

    except Exception as e:
        print(f"Error for user {data['username']}: {e}")
        # video_count += 1
        tick += 1
        count = 0
        driver.quit()
        # count -= 1
        # error(data, count, video_count,email_id,f_name,l_name,passw,video_name,video_bio,channelDescription,index,tick,)
    return count

def error(data, count, video_count,email_id,f_name,l_name,passw,video_name,video_bio,channelDescription,index,tick):
    try:
        # if tick == 3:
            # read(data, count, video_count,email_id,f_name,l_name,passw,video_name,video_bio,channelDescription,index,tick,)
        # Your existing code for the success scenario
        service = Service(executable_path="Final-Year-Project\\AutomatingUserCreation\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.quit()
        time.sleep(1)
        service = Service(executable_path="Final-Year-Project\\AutomatingUserCreation\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)


        driver.get("http://localhost:5001/login-account")
# --------------------------------------------------------------------------------------------------------------------------
        # Login In page

        time.sleep(5)
    
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[1]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        username = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[1]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        username.send_keys(email_id)    

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[2]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        password_login = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[2]/input[@class='w-80 bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        password_login.send_keys(passw)       
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[@class='flex items-center gap-4']/button[@class='bg-theme text-white px-5 py-1.5  h-max w-max rounded-md uppercase hover:bg-themeHover']"))
        )
        login = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div[@class='grid grid-cols-5 w-full h-screen overflow-hidden']/div[@class='flex flex-col mx-16 mt-16 col-span-2 gap-8']/form[@class='flex flex-col gap-3']/div[@class='flex items-center gap-4']/button[@class='bg-theme text-white px-5 py-1.5  h-max w-max rounded-md uppercase hover:bg-themeHover']")
        login.click()
# # ---------------------------------------------------------------------------------------------------------
# # Create Channel
        
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[1]"))
        )
        create_video = driver.find_element(By.XPATH, "//button[1]")
        create_video.click()        
        
        time.sleep(2)

# # ---------------------------------------------------------------------------------------------------------

# # ---------------------------------------------------------------------------------------------------------
#         # Video Upload     
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/button[@class='border-2 rounded-md p-12 min-w-80 disabled:opacity-70']"))
        )
        ad_video = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div[@class='flex gap-8 ']/button[@class='border-2 rounded-md p-12 min-w-80 disabled:opacity-70']")
        ad_video.click()  

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto p-8 w-full  flex flex-col justify-center']/div[@class='border-dashed border-2 border-opacity-70 border-gray-400 py-12 flex flex-col justify-center items-center']/label[@id='button']"))
        )
        upload_video = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto p-8 w-full  flex flex-col justify-center']/div[@class='border-dashed border-2 border-opacity-70 border-gray-400 py-12 flex flex-col justify-center items-center']/label[@id='button']")
        upload_video.click()

        time.sleep(2)

        pyautogui.typewrite(f"\\C:\\Dhanush\\Final-Year-Project\\4_3\\{index}", interval=0.1)

        pyautogui.press("enter")

        time.sleep(20)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[1]/input[@class=' w-full bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        video_title = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[1]/input[@class=' w-full bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        video_title.send_keys(video_name)

        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[2]/textarea[@class=' w-full min-h-[30vh] bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']"))
        )
        video_descr = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[2]/textarea[@class=' w-full min-h-[30vh] bg-white px-4 py-2 rounded-md border-2 border-gray-500 shadow focus:outline-none']")
        video_descr.send_keys(video_bio)       
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[@class='flex gap-2 items-center']/button[@class='w-max flex-end bg-theme border border-transparent text-white px-5 py-1.5 h-max rounded-md uppercase']"))
        )
        video_save = driver.find_element(By.XPATH, "/html/body/div[@id='root']/div/div[@class='pt-12 grid-cols-7 grid']/div[@class='col-span-6']/div[@class='md:flex p-4 bg-gray-100 min-h-screen']/div[@class='p-6 bg-white   rounded-lg w-full']/div/section[@class='h-full overflow-auto my-4 w-full  flex flex-col justify-center']/div[@class='flex gap-4 border-2 rounded-xl  p-2']/form[@class='flex flex-col gap-3 px-4 w-full flex-1']/div[@class='flex gap-2 items-center']/button[@class='w-max flex-end bg-theme border border-transparent text-white px-5 py-1.5 h-max rounded-md uppercase']")
        video_save.send_keys(video_bio)

        time.sleep(5)
        count += 1
        driver.quit()

    except Exception as e:
        print(f"Error for user {data['username']}: {e}")
        driver.quit()
        count = 1
    return count

user_data = {
  "user1": {"email": "user1@gmail.com", "password": "pass@123", "first_name": "Ram", "last_name": "Patel", "video_name": "ExcitingAdventure", "video_bio": "Join the thrilling adventure in this action-packed video!"},
  "user2": {"email": "user2@gmail.com", "password": "superPwd2#", "first_name": "Lakhan", "last_name": "Manohar", "video_name": "FunnyCatMoments", "video_bio": "Laugh out loud with these hilarious cat moments!"},
  "user3": {"email": "user3@gmail.com", "password": "coolPwd3^", "first_name": "Olivia", "last_name": "Davis", "video_name": "LearnCodingBasics", "video_bio": "Master the basics of coding in this informative tutorial"},
  "user4": {"email": "user4@gmail.com", "password": "excellentPwd4%", "first_name": "Noah", "last_name": "Wilson", "video_name": "BeautifulSunsets", "video_bio": "Enjoy the breathtaking views of mesmerizing sunsets"},
  "user5": {"email": "user5@gmail.com", "password": "awesomePwd5!", "first_name": "Ava", "last_name": "Brown", "video_name": "CookingMasterclass", "video_bio": "Unlock your culinary skills with this cooking masterclass"},
  "user6": {"email": "user6@gmail.com", "password": "amazingPwd6#", "first_name": "Sophia", "last_name": "Miller", "video_name": "DIYHomeDecor", "video_bio": "Get creative and enhance your living space with these DIY decor ideas"},
  "user7": {"email": "user7@gmail.com", "password": "greatPwd7^", "first_name": "Jackson", "last_name": "Davis", "video_name": "TravelVlogEurope", "video_bio": "Embark on a virtual journey through the charm of European destinations"},
  "user8": {"email": "user8@gmail.com", "password": "superbPwd8%", "first_name": "Isabella", "last_name": "Smith", "video_name": "HealthandWellnessTips", "video_bio": "Discover useful tips for maintaining a healthy and balanced lifestyle"},
  "user9": {"email": "user9@gmail.com", "password": "fantasticPwd9!", "first_name": "Lucas", "last_name": "Brown", "video_name": "ScienceExperimentsatHome", "video_bio": "Turn your home into a science lab with these fun experiments"},
  "user10": {"email": "user10@gmail.com", "password": "coolPwd10#", "first_name": "Mia", "last_name": "Wilson", "video_name": "MusicMixParty", "video_bio": "Set the mood right with this energetic music mix for your next party"},
  "user11": {"email": "user11@gmail.com", "password": "excellentPwd11^", "first_name": "Ethan", "last_name": "Johnson", "video_name": "ExtremeSportsHighlights", "video_bio": "Experience the adrenaline rush with highlights from extreme sports"},
  "user12": {"email": "user12@gmail.com", "password": "superPwd12#", "first_name": "Madison", "last_name": "Taylor", "video_name": "ArtisticPaintingTutorial", "video_bio": "Unleash your creativity with step-by-step painting instructions"},
  "user13": {"email": "user13@gmail.com", "password": "coolPwd13^", "first_name": "Aiden", "last_name": "Brown", "video_name": "TechnologyNewsUpdate", "video_bio": "Stay informed with the latest updates in the world of technology"},
  "user14": {"email": "user14@gmail.com", "password": "excellentPwd14%", "first_name": "Scarlett", "last_name": "Miller", "video_name": "YogaforBeginners", "video_bio": "Start your journey to wellness with beginner-friendly yoga sessions"},
  "user15": {"email": "user15@gmail.com", "password": "awesomePwd15!", "first_name": "Carter", "last_name": "Davis", "video_name": "TravelDestinationGuide", "video_bio": "Explore must-visit destinations with this comprehensive travel guide"},
  "user16": {"email": "user16@gmail.com", "password": "fantasticPwd16#", "first_name": "Grace", "last_name": "Wilson", "video_name": "ProductReviewSmartphones", "video_bio": "Get insights into the latest smartphones with this detailed review"},
  "user17": {"email": "user17@gmail.com", "password": "amazingPwd17^", "first_name": "Benjamin", "last_name": "Smith", "video_name": "FashionTrendsShowcase", "video_bio": "Stay stylish with a showcase of the latest fashion trends and tips"},
  "user18": {"email": "user18@gmail.com", "password": "greatPwd18%", "first_name": "Chloe", "last_name": "Taylor", "video_name": "MotivationalSpeechInspiration", "video_bio": "Find inspiration and motivation with this powerful speech"},
  "user19": {"email": "user19@gmail.com", "password": "superbPwd19!", "first_name": "Henry", "last_name": "Johnson", "video_name": "PhotographyTipsBeginners", "video_bio": "Capture stunning moments with essential photography tips for beginners"},
  "user20": {"email": "user20@gmail.com", "password": "coolPwd20#", "first_name": "Ella", "last_name": "Brown", "video_name": "MovieReviewNewReleases", "video_bio": "Stay updated on the latest movie releases with this insightful review"},
  "user21": {"email": "user21@gmail.com", "password": "excellentPwd21^", "first_name": "Wyatt", "last_name": "Miller", "video_name": "DeliciousSmoothieRecipes", "video_bio": "Blend up delicious and nutritious smoothies with these recipes"},
  "user22": {"email": "user22@gmail.com", "password": "fantasticPwd22%", "first_name": "Lily", "last_name": "Wilson", "video_name": "OnlineLearningPlatformsReview", "video_bio": "Explore the best online learning platforms with this comprehensive review"},
  "user23": {"email": "user23@gmail.com", "password": "awesomePwd23!", "first_name": "Sebastian", "last_name": "Davis", "video_name": "HomeWorkoutRoutine", "video_bio": "Stay fit at home with this effective and easy-to-follow workout routine"},
  "user24": {"email": "user24@gmail.com", "password": "amazingPwd24#", "first_name": "Addison", "last_name": "Smith", "video_name": "BookRecommendations2024", "video_bio": "Discover must-read books with these recommendations for 2024"},
  "user25": {"email": "user25@gmail.com", "password": "greatPwd25^", "first_name": "Owen", "last_name": "Johnson", "video_name": "CutePuppyCompanion", "video_bio": "Experience joy with adorable moments featuring cute puppies"},
  "user26": {"email": "user26@gmail.com", "password": "superbPwd26%", "first_name": "Avery", "last_name": "Taylor", "video_name": "GardeningTipsandTricks", "video_bio": "Transform your garden with these expert gardening tips and tricks"},
  "user27": {"email": "user27@gmail.com", "password": "fantasticPwd27!", "first_name": "Elijah", "last_name": "Brown", "video_name": "DIYHairStylingTutorials", "video_bio": "Create stunning hairstyles at home with these easy-to-follow tutorials"},
  "user28": {"email": "user28@gmail.com", "password": "coolPwd28#", "first_name": "Natalie", "last_name": "Miller", "video_name": "TravelDocumentaryAfrica", "video_bio": "Embark on a captivating journey through the diverse landscapes of Africa"},
  "user29": {"email": "user29@gmail.com", "password": "excellentPwd29^", "first_name": "Evan", "last_name": "Wilson", "video_name": "ScienceFictionBookReviews", "video_bio": "Explore the imaginative world of science fiction with these book reviews"},
  "user30": {"email": "user30@gmail.com", "password": "awesomePwd30!", "first_name": "Leah", "last_name": "Davis", "video_name": "CreativeCraftsforKids", "video_bio": "Engage your kids with fun and creative craft ideas for hours of entertainment"},
  "user31": {"email": "user31@gmail.com", "password": "amazingPwd31#", "first_name": "Zoe", "last_name": "Smith", "video_name": "HealthyVegetarianRecipes", "video_bio": "Discover delicious and nutritious vegetarian recipes for a healthy lifestyle"},
  "user32": {"email": "user32@gmail.com", "password": "greatPwd32^", "first_name": "Nathan", "last_name": "Johnson", "video_name": "CarRestorationProject", "video_bio": "Witness the transformation of classic cars in this exciting restoration project"},
  "user33": {"email": "user33@gmail.com", "password": "superbPwd33%", "first_name": "Gabriel", "last_name": "Taylor", "video_name": "LanguageLearningTips", "video_bio": "Enhance your language learning journey with these effective tips and strategies"},
  "user34": {"email": "user34@gmail.com", "password": "fantasticPwd34!", "first_name": "Hannah", "last_name": "Brown", "video_name": "InterviewwithIndustryExperts", "video_bio": "Gain insights into various industries with exclusive interviews from experts"},
  "user35": {"email": "user35@gmail.com", "password": "coolPwd35#", "first_name": "Christopher", "last_name": "Miller", "video_name": "HomeDecorOnaBudget", "video_bio": "Revamp your living space without breaking the bank with these budget-friendly decor ideas"},
  "user36": {"email": "user36@gmail.com", "password": "excellentPwd36^", "first_name": "Isaac", "last_name": "Wilson", "video_name": "OutdoorCookingAdventures", "video_bio": "Explore the joy of cooking outdoors with these adventurous recipes"},
  "user37": {"email": "user37@gmail.com", "password": "awesomePwd37!", "first_name": "Savannah", "last_name": "Davis", "video_name": "FinancialPlanningWorkshop", "video_bio": "Empower yourself with valuable financial planning insights in this workshop"},
  "user38": {"email": "user38@gmail.com", "password": "amazingPwd38#", "first_name": "Alexa", "last_name": "Smith", "video_name": "VirtualRealityExploration", "video_bio": "Immerse yourself in virtual worlds with this exploration of virtual reality experiences"},
  "user39": {"email": "user39@gmail.com", "password": "greatPwd39^", "first_name": "Aiden", "last_name": "Johnson", "video_name": "HealthyLivingHabits", "video_bio": "Establish and maintain healthy living habits with these practical tips"},
  "user40": {"email": "user40@gmail.com", "password": "superbPwd40%", "first_name": "Penelope", "last_name": "Taylor", "video_name": "ClassicMovieNight", "video_bio": "Rediscover timeless classics with a cozy movie night featuring iconic films"},
  "user41": {"email": "user41@gmail.com", "password": "fantasticPwd41!", "first_name": "Mason", "last_name": "Brown", "video_name": "SustainableLivingGuide", "video_bio": "Transition to a more sustainable lifestyle with this comprehensive living guide"},
  "user42": {"email": "user42@gmail.com", "password": "coolPwd42#", "first_name": "Scarlett", "last_name": "Miller", "video_name": "FunnyStandUpComedy", "video_bio": "Laugh your heart out with a collection of side-splitting stand-up comedy performances"},
  "user43": {"email": "user43@gmail.com", "password": "excellentPwd43^", "first_name": "Avery", "last_name": "Wilson", "video_name": "SpaceExplorationDocumentary", "video_bio": "Embark on a cosmic journey with this documentary exploring the wonders of space"},
  "user44": {"email": "user44@gmail.com", "password": "awesomePwd44!", "first_name": "Lily", "last_name": "Davis", "video_name": "MindfulnessMeditationSession", "video_bio": "Experience tranquility and peace with a guided mindfulness meditation session"},
  "user45": {"email": "user45@gmail.com", "password": "amazingPwd45#", "first_name": "Daniel", "last_name": "Smith", "video_name": "DIYGiftIdeas", "video_bio": "Show your creativity with handmade gifts using these thoughtful DIY ideas"},
  "user46": {"email": "user46@gmail.com", "password": "greatPwd46^", "first_name": "Madison", "last_name": "Johnson", "video_name": "LocalFoodieGuide", "video_bio": "Indulge in the culinary delights of your local area with this foodie's guide"},
  "user47": {"email": "user47@gmail.com", "password": "superbPwd47%", "first_name": "Jackson", "last_name": "Taylor", "video_name": "LearntoDrawCartoons", "video_bio": "Unleash your artistic side with step-by-step tutorials on drawing charming cartoons"},
  "user48": {"email": "user48@gmail.com", "password": "fantasticPwd48!", "first_name": "Zoe", "last_name": "Brown", "video_name": "TechnologyGadgetsShowcase", "video_bio": "Stay updated on the latest and coolest gadgets with this showcase"},
  "user49": {"email": "user49@gmail.com", "password": "coolPwd49#", "first_name": "Ethan", "last_name": "Miller", "video_name": "HomeWorkoutChallenge", "video_bio": "Take on a fitness challenge with these intense yet rewarding home workout routines"},
  "user50": {"email": "user50@gmail.com", "password": "excellentPwd50^", "first_name": "Aria", "last_name": "Wilson", "video_name": "PhotographyLessonsAdvanced", "video_bio": "Elevate your photography skills with advanced lessons and pro tips"}
}

count = 1  # Initial count
video_count = 0
tick = 1
channelDescription = "Welcome to a world of endless possibilities at our channel! Dive into a diverse range of content that caters to your interests, from informative tutorials and entertaining vlogs to captivating documentaries and insightful discussions. Join our community and embark on a journey filled with knowledge, laughter, and inspiration. Subscribe now for a one-of-a-kind experience that transcends boundaries and celebrates the beauty of diverse perspectives!"
video_to_upload = ["video1.mp4","video2.mp4","video3.mp4","video4.mp4","video5.mp4"]

for username, data in user_data.items():
    email_id = data['email']
    f_name = data['first_name']
    l_name = data['last_name']
    passw = data['password']
    video_name = data['video_name']
    video_bio = data['video_bio']
    data['username'] = username
    if video_count == 0:
        index = video_to_upload[video_count]
        video_count += 1
    elif video_count == 1:
        index = video_to_upload[video_count]
        video_count += 1
    elif video_count == 2:
        index = video_to_upload[video_count]
        video_count += 1
    elif video_count == 3:
        index = video_to_upload[video_count]
        video_count += 1
    else :
        index = video_to_upload[video_count]
        video_count = 0
    
    count = success(data, count, video_count,email_id,f_name,l_name,passw,video_name,video_bio,channelDescription,index,tick)

# Check the count, if 0 then re-try the current user, if 1 then move to the next user
    while count == 0:
        if video_count == 0:
            index = video_to_upload[video_count]
            video_count += 1
        elif video_count == 1:
            index = video_to_upload[video_count]
            video_count += 1
        elif video_count == 2:
            index = video_to_upload[video_count]
            video_count += 1
        elif video_count == 3:
            index = video_to_upload[video_count]
            video_count += 1
        else :
            index = video_to_upload[video_count]
            video_count = 0
        count = error(data, count, video_count,email_id,f_name,l_name,passw,video_name,video_bio,channelDescription,index,tick)
        