import java.util.*;

class Team implements Comparable<Team> {

    int autoRamps = 0;
    int autoKickstands = 0;
    int autoCenterGoals = 0;
    int autoRollingGoals = 0;
    int numOfMatches = 0;
    int teamNumber;
    int teamScore;

    public Team (int number) {
        teamNumber = number;
    }

    public int compareTo (Team otherTeam) {
        if (this.teamScore == otherTeam.teamScore) {
            return 0;
        } else if (this.teamScore > otherTeam.teamScore) {
            return 1;
        } else {
            return -1;
        }
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
        int teamScore = autoScore + teleScore;
        return teamScore;
    }

}

public class scoutReport {

    public static void main (String[] args) {

        System.out.println("Program Started");
        String queue = "*";
        String nextState = "INIT";
        // Scanner in = new Scanner(System.in);

        while (nextState != "quit") {
            switch (nextState) {

                case "INIT":
                    System.out.println("--> The INIT case ran");
                    /*Add teams to a list*/
                    int[] teamNums = {4150,4324};
                    ArrayList<Team> teamList = new ArrayList<Team>();
                    teamList.add(new Team(teamNums[0]));
                    for (int i = 1; i <= teamNums.length; i++) {
                        teamList.add(new Team(teamNums[i]));
                    }
                    // String teamNumbers = "4150,4324" ;
                    // String[] teamList = teamNumbers.split(",");
                    // System.out.println("Teams Present");
                    // for (int i = 0; i < teamList.length; i++) {
                    //     System.out.println(teamList[i]);
                    // }
                    queue += "EXIT*";
                    break;

                case "IDLE":
                    System.out.println("--> Idle case ran");
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
                    System.out.println("--> The rankings case ran");
                    getRankings(2,teamList);
                    queue += "EXIT*";
                    break;

                case "EXIT":
                    System.out.println("--> The program will exit");
                    break;

                default:
                    System.out.println("--> Default case reached");
                    queue += "EXIT*";
                    break;
            }

            if (queue.indexOf("*") != -1) {
                /*
                Takes the next string from the queue (from the begining of
                the string to the asterisk)
                */
                nextState = queue.substring(0, queue.indexOf("*"));
                /*Removes the next state from the queue*/
                queue = queue.substring((nextState.length() + 1), queue.length());
            } else {
                nextState = "quit";
            }

        }

    }

    public static void getRankings (int numOfRanks, ArrayList<Team> teamList) {
        Collections.sort(teamList);
        for (int i = 0; i < numOfRanks; i++) {
            System.out.println(i + ") " + teamList.get(i));
        }
    }

}
