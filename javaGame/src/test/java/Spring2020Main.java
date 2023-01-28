import java.util.ArrayList;
import java.util.Properties;
import java.util.Random;

import com.codingame.gameengine.runner.MultiplayerGameRunner;
import com.codingame.gameengine.runner.dto.GameResult;

public class Spring2020Main {
    public static void main(String[] args) {
        Random random = new Random();

        MultiplayerGameRunner gameRunner = new MultiplayerGameRunner();

        gameRunner.addAgent("py config/Boss.py", "Blinky", "https://static.codingame.com/servlet/fileservlet?id=43829808065962");
        gameRunner.addAgent("py C:/Users/noata/Documents/pacNNproject/PacManNNTrainer/testGame.py", "pacNet", null);

        gameRunner.setSeed(random.nextLong());

        Properties params = new Properties();

        gameRunner.setGameParameters(params);
        gameRunner.setLeagueLevel(3);

        gameRunner.start(8888);

        // ArrayList<GameResult> results = new ArrayList<GameResult>();
        // for(int i = 0; i < 100; i++) {
        //     MultiplayerGameRunner gameRunner = new MultiplayerGameRunner();
        //     gameRunner.setSeed(random.nextLong());
        //     gameRunner.addAgent("py config/Boss.py", "Blinky", "https://static.codingame.com/servlet/fileservlet?id=43829808065962");
        //     gameRunner.addAgent("py config/Boss.py", "Inky", "https://static.codingame.com/servlet/fileservlet?id=43829821541064");
        //     Properties params = new Properties();
        //     gameRunner.setGameParameters(params);
        //     gameRunner.setLeagueLevel(3);
        //     results.add(gameRunner.simulate());
        // }
        // System.out.println("done.");
    }
}
