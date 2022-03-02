/**
 * Author: Suvarna Lakshmi P
 * Last Modified: 09/02/2022
 * Requirement: Course Booking by students 
 */

import java.util.*;

class Institute {
    private String streamName;
    private String semester;
    private int minCreds;
    private Course[] course; // Composition from Course class
    public  Institute(int minCreds) {
        this.minCreds=16;
    }

    public Institute(String streamName, String semester,Course[] course){
        this.streamName = streamName;
        this.semester=semester;
        this.course = course;
    }
    
    
     /**
     * @return int return the minCreds
     */
    public int getMinCreds() {
        return minCreds;
    }
    /**
     * @return String return the streamName
     */
    public String getStreamName() {
        return streamName;
    }

    /**
     * @param streamName the streamName to set
     */
    public void setStreamName(String streamName) {
        this.streamName = streamName;
    }

    /**
     * @return String return the semester
     */
    public String getSemester() {
        return semester;
    }

    /**
     * @param semester the semester to set
     */
    public void setSemester(String semester) {
        this.semester = semester;
    }
    
}

 class BTech extends Institute{ // for BTech students-Inheritence from Institute
    private int maxCreds;

    

     public BTech(String streamName, String semester,Course[] course){
         super(streamName,semester,course);
         
         this.maxCreds = 160;
     }
    /**
     * @return int return the maxCreds
     */
    public int getMaxCreds() {
        return maxCreds;
    }
}

class MTech extends Institute{ // for Mtech Students-Inheritence from Institute
    
    private int maxCreds;
     
     public MTech(String streamName, String semester,Course[] course){ 
        super(streamName,semester,course);
        this.maxCreds = 72; 
         
     }
    /**
     * @return int return the maxCreds
     */
    public int getMaxCreds() {
        return maxCreds;
    }
}

class Course{ // For different Courses
          public String courseName[];  
          public String courseCode[]; 
          public int creds[];
          public String courseType[];
          public String facName[];
         
    

          public Course(){
              this.courseName = new String[]{"Java","Python","C++"};
              this.courseCode =new String[]{"CSE1007","CSE1009","CSE1004"};
              this.creds = new int[]{4,3,2};
              this.courseType = new String[]{"ETL","LO","ETL"};
              this.facName = new String[]{"Uma","Badri","Prem"};
          }

    /**
     * @return String return the courseName
     */
    public String getCourseName(int index1) {
            String cn;
            cn = courseName[index1];
            return cn;
    
    }

    
    /**
     * @return String return the courseCode
     */
    public String getCourseCode(int index2) {
        String cc;
        cc= courseCode[index2];
        return cc;
    }
    /**
     * @return int return the creds
     */
    public int getCreds(int index3) {
        int cred = creds[index3];
        return cred;
    }
    /**
     * @return String return the courseType
     */
    public String getCourseType(int index4) {
        String ct = courseType[index4];
        return ct;
    }   
    /**
     * @return String return the courseType
     */
    public String getFacName(int index5) {
        String fn = facName[index5];
        return fn;
    }   

}



class CourseBooking extends Course{ // Booking of the courses-Inheritance from Course
          int seats;
          int seatsC;
          String minStat;
          int CredsT;

          CourseBooking(int seats ){
            
            this.seats = 65;       
          }
         /**
     * @return String return the courseType
     */
    public int getSeats() {
        return seats;
    }

    /**
     * @param courseType the courseType to set
     */
    public void setSeats(int seats) {
        this.seats= seats;
    }
    public int CredsTot(int index7){
           CredsT=CredsT + creds[index7];
           return CredsT;
    }
    public boolean minCredsCheck(){
           if (CredsT <= 16){ 
            return true;
           }
           else{
               return false;
           }
    }
    public boolean thLabCheck(int index6){//Checking if the course is ETL
              String ct = courseType[index6];
              if(ct.compareTo("ETL")==0){
                  return true;
              }
              else{
                  return false;
              }
    }

    public int seatsCount(){//counting available seats
        this.seats--;
        return seats;
    }

    public int compulsoryCourse(int cs){// registering compulsory course
        this.seats=cs;
        seats--;
        return seats; 
    }
}

public class Booking{//main class
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Course course[] = new Course[3];//creating array of objects
        CourseBooking coursebook= new CourseBooking(65);
         
        String sn,sem,ch,stName,regNo;
        int seatsAvailable,ci,i=0;
        System.out.println("Enter name and reg no");
        stName=sc.nextLine();
        regNo = sc.next();
        System.out.println("Enter Stream Name and semester");
        sn=sc.next();
        sem=sc.next();
        Institute stud = new Institute(sn, sem, course);
        seatsAvailable = coursebook.seats;
        coursebook.compulsoryCourse(seatsAvailable);
        while(true){
        course[i]= new Course();
        stud.getMinCreds();
        
        if(sn.compareTo("BTech")==0){
            BTech stb = new BTech(sn, sem, course);
            stb.getMaxCreds();
            System.out.println("Enter the index for getting course name [0,1,2]");
            ci = sc.nextInt();
            System.out.println("Course Code: "+ course[i].getCourseCode(ci)); 
            System.out.println("Course Name: " + course[i].getCourseName(ci));
            System.out.println("Credits: "+ course[i].getCreds(ci));
            System.out.println("Faculty Name: "+course[i].getFacName(ci));
            System.out.println("Seats available:" + coursebook.seatsCount()); 
            System.out.println("Total Creds: "+ coursebook.CredsTot(ci));
            if(coursebook.minCredsCheck()== true){
              System.out.println("Less than Minimum Credits");
              continue;
            }

        }
        if(sn.compareTo("MTech")==0){

            MTech stm = new MTech(sn, sem, course);
            stm.getMaxCreds();
            System.out.println("Enter the index for getting course name [0,1,2]");
            ci = sc.nextInt();
            System.out.println("Course Code: "+ course[i].getCourseCode(ci)); 
            System.out.println("Course Name: " + course[i].getCourseName(ci));
            System.out.println("Credits: "+ course[i].getCreds(ci));
            System.out.println("Faculty Name: "+course[i].getFacName(ci));
            System.out.println("Seats available:" + coursebook.seatsCount());  
            System.out.println("Total Creds: "+ coursebook.CredsTot(ci));
            if(coursebook.minCredsCheck()== true){
                System.out.println("Less than Minimum Credits");
                continue;
              }
        }
        System.out.println("Do you want to continue( press y/n)"); 
        ch=sc.next();
        if(ch.compareTo("y")==0)
        continue;
        else if(ch.compareTo("n")==0)
        break;
    }
    System.out.println("Name: "+ stName);
    System.out.println("Register Number: "+ regNo);
}
}


