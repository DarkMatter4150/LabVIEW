import java.util.Scanner;
import java.util.Arrays;

class team {

    int autoRamps = 0;
    int autoKickstands = 0;
    int autoCenterGoals = 0;
    int autoRollingGoals = 0;
    int numOfMatches = 0;
    String teamNumber;

    public team (String number) {
        teamNumber = number;
    }

    public void addMatch (int[] matchArray) {

        numOfMatches++;
        int autoRamp = matchArray[0];
        int autoKickstand = matchArray[1];
        int autoCenterGoal = matchArray[2];
        int autoRollingGoal = matchArray[3];

        if (autoRamp == 1) {
            autoRamps++;
        }
        if (autoKickstand == 1) {
            autoKickstands++;
        }
        if (autoCenterGoal == 1) {
            autoCenterGoal++;
        }
        if (autoRollingGoal == 1) {
            autoRollingGoals++;
        }

    }

    public void getStats () {
        System.out.println("==# Team: " + teamNumber + " #==");
        System.out.println("~ Auto Stats ~");
        System.out.println("Drove off ramps: " + autoRamps + "/" + numOfMatches);
        System.out.println("Kickstands: " + autoKickstands + "/" + numOfMatches);
        System.out.println("Center goals: " + autoCenterGoals + "/" + numOfMatches);
        System.out.println("Rolling goals: " + autoRollingGoals + "/" + numOfMatches);
        System.out.println("~ Team Score ~");
        System.out.println(this.getScore());
    }

    public int getScore () {
        int autoScore = ((autoKickstands * 800) + (autoRamps * 200) + (autoCenterGoals * 1000) + (autoRollingGoals * 350)) / (4 * numOfMatches);
        int teleScore = 0;
        int totalScore = autoScore + teleScore;
        return totalScore;
    }

}

public class scoutReport {

    public static void main (String[] args) {
        System.out.println("Program Started");
        // team _4150 = new team("4150");
        // team _4324 = new team("4324");
        // int[][] scoutData = {{4150,1,0,0,1},{4150,1,0,0,1},{4324,0,0,0,1},{4324,1,0,0,1}};
        // for (int i = 0; i < scoutData.length; i++) {
        //     int[] matchStats = Arrays.copyOfRange(scoutData[i], 1, scoutData[i].length);
        //     if (scoutData[i][0] == 4150) {
        //         _4150.addMatch(matchStats);
        //     } else if (scoutData[i][0] == 4324) {
        //         _4324.addMatch(matchStats);
        //     }
        // }

        /*Start CLI state machine*/
        /*ERROR HERE*/
        String queue = "";
        String nextState = "INIT";
        // Scanner in = new Scanner(System.in);

        while (nextState != "quit") {
            switch (nextState) {

                case "INIT":
                    System.out.println("The INIT case ran");
                    /*Add teams to a list*/
                    String teamNumbers = "4150,4324" ;
                    String[] teamList = teamNumbers.split(",");
                    System.out.println("Teams Present");
                    for (int i = 0; i < teamList.length; i++) {
                        System.out.println(teamList[i]);
                    }
                    queue += "IDLE*";
                    break;

                case "IDLE":
                    System.out.println("Please enter command:");
                    // String command = in.nextLine(); /*Needs work*/
                    String command = "rankings";
                    if (command == "rankings") {
                        System.out.println("Printing a list of rankings");
                        queue += "RANKS*";
                    } else if (command == "exit") {
                        queue += "EXIT*";
                    } else {
                        System.out.println("Command not recognized.");
                        System.out.println("Command input: " + command);
                        queue += "IDLE*";
                    }
                    break;

                case "RANKS":
                    System.out.println("The rankings case ran");
                    queue += "IDLE*";
                    break;

                case "FUNCTION2":
                    System.out.println("The funciton2 case has ran");
                    break;

                case "EXIT":
                    System.out.println("The program will exit");
                    break;

                default:
                    System.out.println("Default case reached");
                    queue += "EXIT*";
                    break;
            }
            System.out.println("Index of `*`: " + queue.indexOf("*"));
            if (queue.indexOf("*") != -1) {
                /*
                Takes the next string from the queue (from the begining of
                the string to the asterisk)
                */
                nextState = queue.substring(0, queue.indexOf("*"));
                System.out.println("nextState: " + nextState);
                /*Removes the next state from the queue*/
                queue = queue.substring((nextState.length() + 1), queue.length());
                System.out.println("Remaining queue:" + queue);
            } else {
                nextState = "quit";
            }

        }

    }

    // public static void getRankings (int numOfRanks) {
    //     String[] fakeScores = {"474", "415"};
    //     String[] teamRanks = sortTeams(fakeScores);
    //
    //     for (int i = 1; i <= numOfRanks; i++) {
    //         System.out.println(i + ") " + teamRanks[i-1]);
    //     }
    //
    // }
    //
    // public static String[] sortTeams (String[] teamScores) {
    //     String[] sorted = {"4150", "4324"};
    //     return sorted;
    // }
}
