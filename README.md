# automatedAlarm()
 your alarm clock can be programmed by Python provided you can write a function to automate it.

**requirements:**
----------
You want to make sure your alarm is set for...
* ***If it's a standard school day***...
  * set it for 7:00 on Mondays, Tuesdays, Thursdays, and Fridays
  * set it for 7:30 on Wednesdays
* ***If there is no school on a weekday*** (it's summer, a holiday, or some other break),
  * then it's 9:30 on Mondays (no school)
  * or 8:30 on all other weekdays (again, no school)
* Always set the alarm for 9:00am on the weekends (regardless of the day)

**Inputs:**
----------
* **automatedAlarm()** receives two inputs (string and boolean): *day* and *noSchool*
  * **day** is a string ("Monday", "Tuesday", "Wednesday"...)
  * **noSchool** is a boolean
    * True = if it's a vacation, holiday, or summer
    * False = if it's a standard school day

**Output:**
------------
automatedAlarm() returns one output (a string): time (e.g. "8:00")

**Examples:**
inputs => output/s
--------------------------------
* Wednesday True => 8:30
* Monday True => 9:30
* Monday False => 7:00
* Wednesday False => 7:30
* Saturday True => 9:00
* Saturday False => 9:00
* Friday False => 7:00
* Friday True => 8:30
