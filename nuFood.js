/* Name:    displayTime
 * Purpose: display the opening/closing time of a dining location in 12hr format
            if dining location is opening/closing soon, displays minutes left
 * Params:  an int hour and min, whether the dining location is open now
 * Returns: the time in string format
 */
function displayTime(hour, min, isOpen) {
    
    // If time left open/close is less than this many minutes,
    // the hall is deemed to be changing state "soon"
    var soonLimit = 30;
    
    // getting this from .py file for testing for now
    // var now = new Date(); 
    
    var hourNow = {{nowHr}}; // now.getHours();
    var minNow ={{nowMin}};  // now.getMinutes();
    
    timeLabelStr = "closes at ";
    if (!isOpen) timeLabelStr = "opens at ";
    
    // calculate difference between current time and given time
    // diff = given-current  to calculate time left open
    // diff = current-given  to calculate time until open (or x -1)
    var timeDiff = (hour*60+min)-(hourNow*60+minNow);
    
    // dining location is closing soon
    if( isOpen & timeDiff>0 & timeDiff<soonLimit )
        return "closes in "+timeDiff+" min";
        
    timeDiff = timeDiff*-1;

    // dining location is opening soon
    if ( !isOpen & timeDiff>0 & timeDiff<soonLimit)
        return "opens in "+timeDiff+" min";
   
    // Javascript allows you to change variable type, int to string here
    if (min < 10) min = "0"+min;

    // Modulo operator in case hour is 24 or above.
    hour = hour % 24;

    // Subtract 12 for 12 hour display, instead of 24hr 
    if (hour > 12) {
        hour = hour-12;
        return  timeLabelStr+hour+":"+min+"pm";
    }
    
    // Display midnight correctly
    if (hour==0) { hour = 12; }
    
    return timeLabelStr+hour+":"+min+"am";
}

function displayCurrentDayTime() {
    var string="Current Time: ";
    var currMin = {{nowMin|stringformat:"02d"}};
    switch ({{day}}) 
    {
        case 0: string += "Monday"; break;
        case 1: string += "Tuesday"; break;
        case 2: string += "Wednesday"; break;
        case 3: string += "Thursday"; break;
        case 4: string += "Friday"; break;
        case 5: string += "Saturday"; break;
        case 6: string += "Sunday"; break;
        default: string += "Unknown day"; break;
    }

    string += " ";

    if({{nowHr}}>12) {
        string += ({{nowHr}}-12)+":"+currMin+"pm";
    }

    else if ({{nowHr}}==12) {
        string += ({{nowHr}})+":"+currMin+"pm";
    }

    else if ({{nowHr}} == 0) {
        string += ({{nowHr}}+12)+":"+currMin+"am";
    }

        /*<!--{{nowHr}}:{{nowMin|stringformat:"02d"}}-->
        {% if nowHr > 12 %}
        {{nowHr|add:"-12"}}:{{nowMin|stringformat:"02d"}} pm
        {% elif nowHr == 12 %}
        {{nowHr}}:{{nowMin|stringformat:"02d"}} pm
        {% elif nowHr == 0 %}
        {{nowHr}}:{{nowMin|stringformat:"02d"}} am
        {% else %}
        {{ nowHr|stringformat:"02d" }}:{{ nowMin|stringformat:"02d"}} am
        {% endif %}
        */
    
    /*  {% if day == 6 %}
            return "Sunday";
        {% elif day == 0 %}
            return "Monday";
        {% elif day == 1 %}
            return "Tuesday";
        {% elif day == 2 %}
            return "Wednesday";
        {% elif day == 3 %}
            return "Thursday";
        {% elif day == 4 %}
            return "Friday"
        {% elif day == 5 %}
            return "Saturday"
        {% endif %}
    */
    return string;
}




    
  /*      

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