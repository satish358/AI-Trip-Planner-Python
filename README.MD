# AI Trip Planner Backend [Python]

The AI Trip Planner is a smart travel assistant designed to create personalized itineraries based on the number of days, travel style, and city of your choice. Whether you're planning a short weekend getaway or an extended vacation, this AI tool takes into account your preferences for relaxation, adventure, or cultural experiences, offering tailored recommendations for sightseeing, activities, dining, and accommodations. Simply input your travel dates, preferred style (e.g., relaxation, adventure), and destination, and let the AI curate the perfect trip for you.

- ReactJS front-end repository - [ai-trip-planner-ui-react](https://github.com/satish358/ai-trip-planner-ui-react)

#### ⚠️IMPORTANT - Add your OpenAI API key in app.py file

```python
KEY = "YOUR_OPEN_AI_API_KEY"
client = OpenAI(
    api_key=KEY,
)
```

## Required libraries installation

Below libraries are required to run the applicaiton

### Using manual installation

- Flask - `pip insatll flask`
- Flask_Cors - `pip install flask_cors`
- OpenAI - `pip install openai`

### Using conda env installation

- You have to install anaconda in you system.
- Fist step to create conda `env` using `conda env create --name NAME --file FILE` command, For example `conda env create --name open_ai --file anaconda_open_ai_env.yaml`
- Now activate created `env` using `conda activate open_ai`, here `open_ai` is your `env` name

## How to run application

- First you need to clone the backend repository and run it.
- Navagate to project folder using command prompt (`Skip` this step if your using `IDE`)
- Activate your conda `env` where you install all libraries or added conda `env` file.
- Now run `app.py` file, you will see output like below click on http address or open it using chrome.

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 682-010-683
```

## How to add latest frontend build

Do below in frontend repository after your changes.

- Fist stop the `dev` server if running.
- Then use `npm run build` to build the project.
- Replace the `dist` folder to backend folder.
- Your latest build is available. Now you can run `app.py` and see the results.
