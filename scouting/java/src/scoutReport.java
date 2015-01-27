import java.util.*;
import java.io.Console;

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
        otherTeam.getScore();
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
        this.getScore();
    }

    public int getScore () {
        int autoScore = ((autoKickstands * 800) + (autoRamps * 200) + (autoCenterGoals * 1000) + (autoRollingGoals * 350)) / (4 * numOfMatches);
        int teleScore = 0;
        teamScore = autoScore + teleScore;
        return teamScore;
    }

}

public class scoutReport {

    public static void main (String[] args) {
        String queue = "*";
        String nextState = "INIT";
        ArrayList<Team> teamList = new ArrayList<Team>();
        Console console = System.console();

        while (nextState != "quit") {
            switch (nextState) {

                case "INIT":
                    System.out.println("* The INIT case ran");
                    /*Add teams to a list*/
                    int[] teamNums = {4150,4324};
                    int[][] matchData = getMatchData("testData.csv");
                    for (int i = 0; i < teamNums.length; i++) {
                        Team team = new Team(teamNums[i]);
                        for (int j = 0; j < matchData.length; j++) {
                            if (matchData[j][0] == team.teamNumber) {
                                int[] teamMatch = Arrays.copyOfRange(matchData[j], 1, matchData[j].length);
                                team.addMatch(teamMatch);
                            }
                        }
                        team.getScore();
                        teamList.add(team);
                    }
                    queue += "IDLE*";
                    break;

                case "IDLE":
                    System.out.println("* Idle case ran");
                    // System.out.println("--> Please enter command:");
                    String command = console.readLine("--> Please enter command:"); /*Needs work*/
                    // String command = "report";
                    if (command == "rankings") {
                        queue += "RANKS*";
                    } else if (command == "report") {
                        queue += "REPORT*";
                    } else if (command == "exit") {
                        queue += "EXIT*";
                    } else {
                        System.out.println("--> Command not recognized.");
                        System.out.println("--> Command input: " + command);
                        queue += "IDLE*";
                    }
                    break;

                case "RANKS":
                    System.out.println("* The rankings case ran");
                    Collections.sort(teamList);
                    int numOfRanks = Integer.parseInt(console.readLine("Please enter the number of teams to rank: "));
                    // int numOfRanks = Integer.parseInt(in.nextLine()); /*Needs work*/
                    // int numOfRanks = 2;
                    for (int i = 0; i < numOfRanks; i++) {
                        System.out.println(i+1 + ") " + teamList.get(i).teamNumber);
                    }
                    queue += "IDLE*";
                    break;

                case "REPORT":
                    int teamNum = Integer.parseInt(console.readLine("Please enter a team number you wish to recieve a report about: "));
                    // int teamNum = in.nextLine();
                    // int teamNum = 4150;
                    for (int i = 0; i < teamList.size(); i++) {
                        Team team = teamList.get(i);
                        if (team.teamNumber == teamNum) {
                            team.getStats();
                            break;
                        } else {
                            System.out.println("Team " + teamNum + " not found.");
                        }
                    }
                    queue += "IDLE*";
                    break;

                case "EXIT":
                    System.out.println("* The program will exit");
                    queue = "";
                    break;

                default:
                    // System.out.println("* Default case reached; Error occured in the QSM");
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

    public static int[][] getMatchData (String filename) {
        int[][] matchData = {{4150,0,0,0,1},{4324,1,0,0,1},{4150,1,0,0,1}};
        return matchData;
    }

}
