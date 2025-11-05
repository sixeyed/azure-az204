# Azure Functions Timer Trigger - Quickfire Questions

## Question 1
What is a timer-triggered Azure Function used for?

- A) Processing HTTP requests
- B) Running scheduled tasks at specific intervals
- C) Responding to database changes
- D) Handling blob uploads

**Answer: B**
Timer triggers execute functions on a schedule, similar to cron jobs or scheduled tasks.

---

## Question 2
What expression format is used to define timer schedules?

- A) ISO 8601
- B) NCRONTAB expressions (similar to cron)
- C) Plain English
- D) JSON format

**Answer: B**
Timer triggers use NCRONTAB expressions: `{second} {minute} {hour} {day} {month} {day-of-week}` with 6 fields.

---

## Question 3
What does the NCRONTAB expression `0 */5 * * * *` mean?

- A) Every 5 seconds
- B) Every 5 minutes
- C) Every 5 hours
- D) Every 5 days

**Answer: B**
The expression runs at second 0 of every 5th minute (* */5 * * * *).

---

## Question 4
What does the NCRONTAB expression `0 0 9 * * 1-5` mean?

- A) Every day at 9 AM
- B) Every weekday (Monday-Friday) at 9 AM
- C) Every Monday at 9 PM
- D) Every 9 hours on weekdays

**Answer: B**
Runs at 9:00 AM (0 0 9) every day (*) of every month (*) on weekdays (1-5, Monday-Friday).

---

## Question 5
How can you prevent multiple instances of a timer function from running concurrently?

- A) Use singleton mode (RunOnStartup = false)
- B) Use the Singleton attribute or host.json configuration
- C) Not possible
- D) Only run in Consumption plan

**Answer: B**
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

- A) It's skipped permanently
- B) The function is triggered immediately upon startup (catch-up execution)
- C) An error is thrown
- D) The schedule resets

**Answer: B**
By default, missed executions trigger immediately when the app starts, unless UseMonitor is false.

---

## Question 8
How can you temporarily disable a timer trigger?

- A) Delete the function
- B) Set the AzureWebJobs.{FunctionName}.Disabled app setting to true
- C) Remove the schedule
- D) Stop the Function App

**Answer: B**
Setting AzureWebJobs.{FunctionName}.Disabled to "true" or "1" disables the timer trigger without code changes.

---

## Question 9
What time zone is used for timer schedules by default?

- A) Local server time
- B) UTC
- C) Eastern Time
- D) GMT

**Answer: B**
Timer schedules use UTC by default. You can specify a different timezone using the WEBSITE_TIME_ZONE app setting.

---

## Question 10
Can timer-triggered functions scale out to multiple instances?

- A) Yes, multiple instances run in parallel
- B) No, only one instance executes per schedule (with singleton locking)
- C) Only in Premium plan
- D) Only for long-running tasks

**Answer: B**
Timer triggers use singleton locking to ensure only one instance executes per scheduled time, preventing duplicate work.
