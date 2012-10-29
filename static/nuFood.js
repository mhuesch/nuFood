/* from: location.js

 * Name:    ...
 * Purpose: ...
 * Params:  ...
 * Returns: ...
 */
var lat;
var lon;

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(Start);
}

function Start(location) {
  lat = location.coords.latitude;
  lon = location.coords.longitude;
}

function ProximityRedirect(opinion) {
  window.location = "/?lat=" + lat + "&lon=" + lon;
}


/* Name:    displayDayName
 * Purpose: display friendly name of a day, rather than a number
 * Params:  the current day, an int 0-6 (from database)
 * Returns: the day name in string form
 */
function displayDayName(day) {
    switch (day) 
    {
        case 0: return "Monday";
        case 1: return "Tuesday"; 
        case 2: return "Wednesday"; 
        case 3: return "Thursday"; 
        case 4: return "Friday"; 
        case 5: return "Saturday"; 
        case 6: return "Sunday"; 
        default: return "Unknown weekday"; 
    }
    return "Unknown weekday";
}

/* Name:    displayDayName
 * Purpose: display abbreviated day name (for url)
 * Params:  the current day, an int 0-6 (from database)
 * Returns: the day name in string form
 */
function getShortDayName(day) {
    switch (day) 
    {
        case 0: return "mon";
        case 1: return "tue"; 
        case 2: return "wed"; 
        case 3: return "thu"; 
        case 4: return "fri"; 
        case 5: return "sat"; 
        case 6: return "sun"; 
        default: return "unk"; 
    }
    return "unk";
}


/* Name:    displayMealName
 * Purpose: display friendly name of a meal
 * Params:  a mealType, a 3-letter identifier (from database)
 * Returns: the meal type name in string form
 */
function displayMealName(mealType) { 
    switch (mealType) 
    {
        case 'BRK': return "Breakfast";
        case 'BRU': return "Brunch";
        case 'LUN': return "Lunch";
        case 'DIN': return "Dinner";
        case 'LAT': return "Late Night";
        case 'RET': return "Retail";
        default: return "Other";
    }
    return "Other";
}

/* Name:    displayMenuTitle
 * Purpose: display a descriptive heading for the menu page
 * Params:  dining location hall name, mealType, day, date
 * Returns: the menu title in string format
 */
function displayMenuTitle(hallName, mealType, weekday, month, date) {
    var returnStr = "Menu for ";
    
    returnStr += displayMealName(mealType);
    
    returnStr += " in ";
    returnStr += hallName; //"{{hallName}}";
    returnStr += " for ";
    
    returnStr += displayDayName(weekday);
    
    // TODO: display only the month and date of hte date
    // currently shows month day year + time
    // ex: Oct. 24, 2012, 3:40 p.m
    //returnStr += ", "+ month + " " + date; //"{{date}}";
    
    return returnStr;
}

/* Name:    displayTime
 * Purpose: display a time in 12hr format
 * Params:  an int hour and min
 * Returns: the time in string format
 */
function displayTime(hour, min) {
    
    // Javascript allows you to change variable type, int to string here
    // properly display single-digit minutes with leading 0
    if (min < 10) min = "0"+min;

    // Modulo operator in case hour is 24 or above.
    // (i.e. late-night retail stores hours)
    hour = hour % 24;

    // Subtract 12 for 12 hour display, instead of 24hr
    // could also do mod, but whatever
    if (hour > 12) {
        return (hour-12) + ":" + min + "pm";
    }
    
    // Display noon correctly (12pm)
    if (hour == 12) { 
        return hour + ":" + min + "pm"; 
    }
    
    // Display midnight correctly
    if (hour == 0) { 
        hour = 12;
        //return (hour+12) + ":" + min + "am";
    }

    return hour + ":" + min + "am";
}

/* Name:    displayOpenCloseTime
 * Purpose: display opening/closing time of a dining location in 12hr format
            if dining location is opening/closing soon, displays minutes left
 * Params:  an int hour and min for an open or close time,
            a boolean whether the dining location is open now
 * Returns: the time in string format
 */
function displayOpenCloseTime(hour, min, isOpen) {
    
    // If time left open/close is less than this many minutes,
    // the hall is deemed to be changing state "soon"
    var soonLimit = 30;
    
    var now = new Date();
    var hourNow = now.getHours();
    var minNow = now.getMinutes();
    
    /* 
    // use this block if the script is internal in the html,
    // (to access python values)
    
    // getting this from .py file for testing for now
    // var now = new Date(); 
    
    var hourNow = {{nowHr}}; // now.getHours();
    var minNow ={{nowMin}};  // now.getMinutes();
    
    */
    
    timeLabelStr = "<font class='timeLabel'>closes at </font>";
    if (!isOpen) timeLabelStr = "<font class='timeLabel'>opens at </font>";
    
    // calculate difference between current time and given time
    // diff = given-current  to calculate time left open
    // diff = current-given  to calculate time until open (or x -1)
    var timeDiff = (hour*60+min)-(hourNow*60+minNow);
    
    // -- dining location is closing soon --
    if( isOpen & timeDiff>0 & timeDiff<soonLimit )
        return "<font class='timeLabel'><font color='mediumvioletred'>closes in </font>" + timeDiff + " min</font>";

    // -- dining location is opening soon --
    if ( !isOpen & timeDiff>0 & timeDiff<soonLimit)
        return "<font class='timeLabel'><font color='green'>opens in </font>" + timeDiff + " min</font>";
   
    // dining location is not opening or closing soon
    // so just display the time normally
    return timeLabelStr + displayTime(hour, min);

}

/* Name:    displayCurrentDayTime
 * Purpose: 
 * Params:  
 * Returns: 
 */
function displayCurrentDayTime(day, hour, min) {
    var string = "Current Time: ";
    string +="<br/>"; // add line break to display location sort button inline nicely on iphone
    //<!--{{nowHr}}:{{nowMin|stringformat:"02d"}}-->
    
    string += displayDayName(day);
    string += " ";
    string += displayTime(hour, min);
    
    return string;
}


  /*     // can we import this here or anything…?

    <!-- Javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/bootstrap/js/jquery.js"></script>
    <script src="/static/bootstrap/js/bootstrap-transition.js"></script>
    <script src="/static/bootstrap/js/bootstrap-alert.js"></script>
    <script src="/static/bootstrap/js/bootstrap-modal.js"></script>
    <script src="/static/bootstrap/js/bootstrap-dropdown.js"></script>
    <script src="/static/bootstrap/js/bootstrap-scrollspy.js"></script>
    <script src="/static/bootstrap/js/bootstrap-tab.js"></script>
    <script src="/static/bootstrap/js/bootstrap-tooltip.js"></script>
    <script src="/static/bootstrap/js/bootstrap-popover.js"></script>
    <script src="/static/bootstrap/js/bootstrap-button.js"></script>
    <script src="/static/bootstrap/js/bootstrap-collapse.js"></script>
    <script src="/static/bootstrap/js/bootstrap-carousel.js"></script>
    <script src="/static/bootstrap/js/bootstrap-typeahead.js"></script>

*/