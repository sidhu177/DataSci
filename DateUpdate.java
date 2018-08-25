import java.time.LocalDate;
import java.time.temporal.TemporalAdjusters;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.Date;

public class DateUpdate                                       // Beginning the Class
{
      public static void main(String[] args)                  // Main Class
      {
    	  
    	  System.out.print("Dates Before Conversion : ");     //print statement to beginning the program
    	  List<String> reportingPeriodEnding = getDummyInput(); //input data
    	  for(String reportingPeriod : reportingPeriodEnding)  //looping through the input data to get the month and year
    	  {  
    		  String converted = convertReportingPeriods(reportingPeriod); //passing the formatted date
    		  System.out.println(converted);                     //printing the stored value
    	  }
    	 
      }

	private static String convertReportingPeriods(String reportingPeriodEnding)   
	{
			String month = reportingPeriodEnding.split("-")[0];
			String year = reportingPeriodEnding.split("-")[1];
			LocalDate lastDayofMonthGivenDate = LocalDate.of(Integer.parseInt(year), Integer.parseInt(month), 1).with(TemporalAdjusters.lastDayOfMonth());
			return lastDayofMonthGivenDate.getDayOfMonth() + "-" + month + "-" + year;
	}

	private static List<String> getDummyInput() 
	{
		  List<String> reportingPeriodEnding = new ArrayList<>();
		  reportingPeriodEnding.add("10-2016");
		  reportingPeriodEnding.add("11-2016");
		  reportingPeriodEnding.add("02-2016");
		  return reportingPeriodEnding;
	}
}                                                                            