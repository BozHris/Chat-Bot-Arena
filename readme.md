A bot arena between ChaGPT 3.5 turbo and Claude 2.1

This is how the App looks.
![Streamlit App](https://github.com/BozHris/Chat-Bot-Arena/assets/113389241/43014adb-d75e-45dc-9e56-5736f7e90c86)

The idea is not to be biased when choosing the model so when we input something like "What is the coldest city on earth?" We get this: 
![image](https://github.com/BozHris/Chat-Bot-Arena/assets/113389241/d6751d20-6729-4748-bd4d-564611be06cd)

After we select an answer we get this: 
![image](https://github.com/BozHris/Chat-Bot-Arena/assets/113389241/433d3b3f-64ab-44ec-83b5-f576b9d4dc39)

The result is saved in a mysql table and after the vote is done the connection is closed so the user can't change the vote in one session and needs to refresh the page(thus refreshing the result) to vote again

This app compares ChatGPT 3.5 turbo with Claude 2.1, each response is limited to 100 tokens. 
