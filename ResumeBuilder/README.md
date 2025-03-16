# Resume Builder

### Instructions
1. Change the contents of `job-description.txt` and `resume.txt`.
2. Run following commands:
    ```
    pip install groq
    export GROQ_API_KEY=<replace with your own API key>
    python resumebuilder.py
    ```
3. See output as `resume_YYYYMMDDhhmmss.md`

### Troubleshooting
1. If you encounter following error:
   ```
   TypeError: Client.__init__() got an unexpected keyword argument 'proxies'
   ```
   Make sure you are using latest `groq` library installed by running following command:
   ```
   pip install --upgrade groq 
   ```
