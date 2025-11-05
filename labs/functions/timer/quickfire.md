# Azure Functions Timer Trigger - Quickfire Questions

## Question 1
What is a timer-triggered Azure Function used for?


- A) Running scheduled tasks at specific intervals
- B) Responding to database changes
- C) Processing HTTP requests
- D) Handling blob uploads

**Answer: A**
Timer triggers execute functions on a schedule, similar to cron jobs or scheduled tasks.
---
## Question 2
What expression format is used to define timer schedules?


- A) NCRONTAB expressions (similar to cron)
- B) JSON format
- C) ISO 8601
- D) Plain English

**Answer: A**
Timer triggers use NCRONTAB expressions: `{second} {minute} {hour} {day} {month} {day-of-week}` with 6 fields.
---
## Question 3
What does the NCRONTAB expression `0 */5 * * * *` mean?


- A) Every 5 minutes
- B) Every 5 seconds
- C) Every 5 days
- D) Every 5 hours

**Answer: A**
The expression runs at second 0 of every 5th minute (* */5 * * * *).
---
## Question 4
What does the NCRONTAB expression `0 0 9 * * 1-5` mean?


- A) Every Monday at 9 PM
- B) Every 9 hours on weekdays
- C) Every weekday (Monday-Friday) at 9 AM
- D) Every day at 9 AM

**Answer: C**
Runs at 9:00 AM (0 0 9) every day (*) of every month (*) on weekdays (1-5, Monday-Friday).
---
## Question 5
How can you prevent multiple instances of a timer function from running concurrently?


- A) Use the Singleton attribute or host.json configuration
- B) Use singleton mode (RunOnStartup = false)
- C) Not possible
- D) Only run in Consumption plan

**Answer: A**
The [Singleton] attribute in C# or singleton configuration in host.json ensures only one instance executes at a time.
---
## Question 6
What is the TimerInfo parameter in timer functions?


- A) Function cost information
- B) Object containing schedule info, past due status, and last/next execution times
- C) Timer configuration
- D) Monitoring data

**Answer: B**
TimerInfo provides schedule status, whether execution is past due, and schedule occurrences.
---
## Question 7
What happens if a timer function execution is missed (e.g., during app restart)?


- A) The schedule resets
- B) It's skipped permanently
- C) The function is triggered immediately upon startup (catch-up execution)
- D) An error is thrown

**Answer: C**
By default, missed executions trigger immediately when the app starts, unless UseMonitor is false.
---
## Question 8
How can you temporarily disable a timer trigger?


- A) Stop the Function App
- B) Remove the schedule
- C) Set the AzureWebJobs.{FunctionName}.Disabled app setting to true
- D) Delete the function

**Answer: C**
Setting AzureWebJobs.{FunctionName}.Disabled to "true" or "1" disables the timer trigger without code changes.
---
## Question 9
What time zone is used for timer schedules by default?


- A) Local server time
- B) GMT
- C) UTC
- D) Eastern Time

**Answer: C**
Timer schedules use UTC by default. You can specify a different timezone using the WEBSITE_TIME_ZONE app setting.
---
## Question 10
Can timer-triggered functions scale out to multiple instances?


- A) Only for long-running tasks
- B) No, only one instance executes per schedule (with singleton locking)
- C) Yes, multiple instances run in parallel
- D) Only in Premium plan

**Answer: B**
Timer triggers use singleton locking to ensure only one instance executes per scheduled time, preventing duplicate work.