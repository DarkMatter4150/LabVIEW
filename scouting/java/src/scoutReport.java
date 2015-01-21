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
        team _4150 = new team("4150");
        team _4324 = new team("4324");
        int[][] scoutData = {{4150,1,0,0,1},{4150,1,0,0,1},{4324,0,0,0,1},{4324,1,0,0,1}};
        for (int i = 0; i < scoutData.length; i++) {
            int[] matchStats = Arrays.copyOfRange(scoutData[i], 1, scoutData[i].length);
            if (scoutData[i][0] == 4150) {
                _4150.addMatch(matchStats);
            }
        }
        _4150.getStats();
        _4324.getStats();
        System.out.println("\n4150's score: " + _4150.getScore());
    }
}
