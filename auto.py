import pyautogui as pg
import keyboard
import time

time.sleep(3)

pg.hotkey('win', '2')
pg.click(650,425,button='right')
pg.write("CMMI models")
pg.press('enter')
pg.click(450,400,button='right')
