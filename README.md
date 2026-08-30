# media_deck_gui
This repository contains the layout of my visual interface for logging my media consumpion. The various media I track consists of books, movies, and TV shows. The GUI will be displayed on a raspberry pi 4 with 4GB. For more information about this project, here it is!


## Background Inspiration: 
Since 2022, I have thorouhgly enjoyed logging the main forms of media I consume, including movies, books, TV shows, and musicals, I decided to create a Notion page for tracking this. Within the Notion page there are 4 databases, one for each media type. While this system works well, there is always room for improvement!
<br><br>

## Media Deck Product User Interview: 
* What is the purpose of this media deck? 
    * To track my media in the forms of books, movies, TV shows, and musicals. It would be cool to add concerts too. This device should function as a portable handheld device that can access the internet. 
* Who's going to use this?
    * Just me, but could serve as a build guide for others. 
* How often is this going to be used?
    * At least every week. Approxiamately 3 or 4 times a week.
* Where will this platform be used? 
    * in a bed
    * while sitting on the floor 
    * at a desk
* What should the platform look like?
    * Clock
    * Display my most recent media consumed
    * Buttons for immediately adding new entries for each media type
    * Ability to view and access all logs for each media type
<br><br>

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">
  <h2> Media Deck User Stories: </h2>
    <ol>
        <li> I have finished watching a movie, while in bed and I want to get my immediate thoughts down about it. I want to have a dedicated device for tracking my media consumption anywhere.  </li>
        <li> I have finished watching a TV show at my desk and I want to log my media comfortably at my desk. </li>
        <li> I have finished a movie at a new friend's house, in which I do not have the Wi-Fi password and I want to log my submission. </li>
        <li> I want to log my entries through this media deck device and other online devices. </li>
        <li> I want to be able to tell the time from immediately using my device. </li>
        <li> I want to see my most recent media consumed immediately when turning on my device. The device should display the most recent media. </li>
    </ol>

</div>

<div style="flex: 1;">

<h2> Media Deck Objectives </h2>

<input type="checkbox" id="obj1" name="obj1" value="Power">
<label for="obj1"> 1. The device should have a portable power source. </label><br>
<input type="checkbox" id="obj2" name="obj2" value="Table">
<label for="obj2"> 2. The device should be usable from stable flat surface. </label><br>
<input type="checkbox" id="obj3" name="obj3" value="Locations">
<label for="obj3"> 3. The device should be accessible offline from multiple locations. </label><br>  
<input type="checkbox" id="obj4" name="obj4" value="Devices">
<label for="obj4"> 4. The entry system should be accessible through multiple devices. </label><br>  
<input type="checkbox" id="obj5" name="obj5" value="Clock">
<label for="obj5"> 5. The device should device should display a clock interface. </label><br> 
<input type="checkbox" id="obj6" name="obj6" value="Recent Media">
<label for="obj6"> 6. The device should display the most recent media. </label><br>  

</div>

</div>


<!-- ## Media Deck User Stories: 
1. I have finished watching a movie, while in bed and I want to get my immediate thoughts down about it. I want to have a dedicated device for tracking my media consumption. The device should have a portable power source. 
2. I have finished watching a TV show at my desk and I want to log my media comfortably at my desk. The device should be usable from stable flat surface. 
3. I have finished a movie at a new friend's house and I want to log my submission. The device should be accessible offline from multiple locations.
4. I want to log my entries through this media deck device and other online devices. The entry system should be accessible through multiple devices.
5. I want to be able to tell the time from immediately using my device. The device should device should display a clock interface.
6. I want to see my most recent media consumed immediately when turning on my device. The device should display the most recent media.


## Media Deck Objectives: 
[] The device has a portable power source and does not rely on another device to operate. -->


## Update Log: 

*Week of Aug 24, 2026*
<br>
For this week, I started reworking the GUI of my platform. For this, I used some user research data I collected and the wireframes I made to implement my GUI using GUIZero. Throughout the week I implemented the base layout of the platform (without the functionality), the clock interface using datetime, the display of the gif image. There is moe to be done with implementing the functionality of the Notion API within the platform and finalizing the design of the buttons that lead to adding a new media entry.  

*Week of Aug 17, 2026* 
<br>
For this week, I started ideating the layout of the platform, at least for the startup page. I did some user research with myself to figure out how I wanted the platform to truly look. I also designed low fidelity, medium fidelity, and high fidelity wireframes on paper and in Figma to outline the layout of the startup page. I enjoyed this process of designing it to ensure that the intial loading page was aesthetically appealing and also functional.

*Week of Aug 10, 2026* 
<br>
After getting buying the RPi, I started exploring the GUI design and implementation process for an RPi. I started using GUIZero and followed the documentation for implementing the UI. The first iteration I had was wiped as the memory card of the Rpi4 stopped working, so it was necessary to start over with the design of the GUI.


*Aug 02, 2026*
<br>
On this day, I officialy moved on from the ideation process by buying the Raspberry Pi 4 that this device would be based on. I bought my device from MicroCenter and immediately began setting up the RPi4. I had little issue in setting up the RPi OS as there was a lot of documentation online. I have linked some of the resources I used for setting up the RPi4.
**Sources** : [Setting up RPi4 OS (in Gadget Mode)](https://www.youtube.com/watch?v=U45RJ4iUpw8) and [RPi Official Setting up Documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html).