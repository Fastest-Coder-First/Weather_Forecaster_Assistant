import speech_recognition as sr
import pyttsx3
import time
import requests

print('Loading your AI personal Weather Forecaster Weather One')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 190) 

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        time.sleep(3)

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}\n")
    except Exception as e:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    return command.lower()

speak("Loading your AI personal Weather Forecaster")

if __name__=='__main__':
    

    while True:
        print("\n Speak weather to search for weather report of any city or speak exit to quit the assistant")
        speak("Speak weather to search for weather report of any city or speak exit to quit the assistant")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            print("What is the city name")
            speak("What is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                max_temperature = y["temp_max"]
                min_temperature = y["temp_min"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print("City name = " + city_name +
                      "\n Temperature in kelvin unit = " +
                      str(current_temperature) + "K" +
                      "\n Humidity (in percentage) = " +
                      str(current_humidiy) + "%" +
                      "\n Maximum temperature in kelvin unit is = " +
                      str(max_temperature) + "K" +
                      "\n Minimum temperature in kelvin unit is = " +
                      str(min_temperature) + "K" +
                      "\n Description = " +
                      str(weather_description))
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) + 
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n maximum temperature in kelvin unit is " +
                      str(max_temperature) +
                      "\n minimum temperature in kelvin unit is " +
                      str(min_temperature) +
                      "\n description  " +
                      str(weather_description))
                
            else:
                speak(" City Not Found ")
                
        elif "exit" in statement or "quit" in statement:
                speak("Thanks for using me Goodbye!!")
                print("Thanks for using me, Goodbye!!")
                break   