# Description
This is a simple application that mimicks the game [Simon](https://en.wikipedia.org/wiki/Simon_(game)). I built this to primarily help children and teens learn about the fundamentals of programming.

# Usage
You may use this project however you see fit.

# How to start
1. **Install Python**  
   Ensure you have the correct version of [Python](https://www.python.org/downloads/) installed. If needed, upgrade/downgrade your Python version to match the project’s requirements.  

2. **Clone the Repository**  
   ```bash
   git clone <repository_url>
   ```

3. **Navigate to the Project Directory**  
   ```bash
   cd <project_directory>
   ```

4. **Set Up a Virtual Environment**  
   - Create a virtual environment to isolate dependencies:  
     ```bash
     python3 -m venv venv  # Use "python" instead of "python3" if needed
     ```
   - Activate the virtual environment:  
     - **Windows (Command Prompt/PowerShell):**  
       ```bash
       .\venv\Scripts\activate
       ```
     - **macOS/Linux:**  
       ```bash
       source venv/bin/activate
       ```  
     *(Your terminal prompt will now show `(venv)` to indicate the active environment.)*

5. **Install Dependencies**  
   Run this command **inside the activated virtual environment**:  
   ```bash
   pip install .  # Or "pip install -r requirements.txt" if the project uses a requirements file
   ```

6. **Run the Game**  
   Ensure the virtual environment is still active, then execute:  
   ```bash
   python3 main.py
   ```

7. **Deactivate the Virtual Environment (When Finished)**  
   ```bash
   deactivate
   ```

# How to play
Use `QWAS` keys, corresponding to 4 corners of a square. Memorize the order that the squares light up and try repeating it.

# How it works
It uses emojis to represent 4 segments of the board. The program will activate the square corresponding to the `QWAS` keys. The game uses a queue to keep track of the order of buttons, and a buffer to convert user input so it would be easier to interpret.
