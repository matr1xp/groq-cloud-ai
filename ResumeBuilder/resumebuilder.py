import datetime

from groq import Groq

client = Groq()

with open('resume.txt', 'r') as resume_file:
    resume = resume_file.read()

with open('job-description.txt', 'r') as job_description_file:
    jobDescription = job_description_file.read()

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": "Build a custom resume for this job posting. Here is the resume:\n" +
                       resume + "\n and here is the job description:\n" + jobDescription
        },
        {
            "role": "assistant",
            "content": "Please provide the job posting, and I'll create a custom resume tailored to the requirements "
                       "and qualifications listed."
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
with open(f"resume_{timestamp}.md", 'w') as file:
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
        content = chunk.choices[0].delta.content or ""
        file.write(content)
