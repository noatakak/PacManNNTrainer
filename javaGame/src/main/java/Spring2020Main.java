import java.util.ArrayList;
import java.util.Properties;
import java.util.Random;

import com.codingame.gameengine.runner.MultiplayerGameRunner;
//import com.codingame.gameengine.runner.simulate.GameResult;
import com.codingame.gameengine.runner.dto.GameResult;

public class Spring2020Main {
    public static void main(String[] args) {
        Random random = new Random();

        //  MultiplayerGameRunner gameRunner = new MultiplayerGameRunner();

        //  gameRunner.addAgent("py C:/Users/noata/PycharmProjects/PacManNNTrainer/javaGame/config/Boss.py", "Blinky", "https://static.codingame.com/servlet/fileservlet?id=43829808065962");
        //  gameRunner.addAgent("py C:/Users/noata/PycharmProjects/PacManNNTrainer/testGame.py", "pacNet", null);

        //  gameRunner.setSeed(random.nextLong());

        //  Properties params = new Properties();

        //  gameRunner.setGameParameters(params);
        //  gameRunner.setLeagueLevel(3);

        //  gameRunner.start(8888);

       ArrayList results = new ArrayList<>();
       for (int i = 0; i < 10; i++) {
           MultiplayerGameRunner gameRunner = new MultiplayerGameRunner();
           gameRunner.setSeed(random.nextLong());
           gameRunner.addAgent("py C:/Users/noata/PycharmProjects/PacManNNTrainer/javaGame/config/Boss.py", "Blinky", "https://static.codingame.com/servlet/fileservlet?id=43829808065962");
           gameRunner.addAgent("py C:/Users/noata/PycharmProjects/PacManNNTrainer/testGame.py", "pacNet", null);
           Properties params = new Properties();
           gameRunner.setGameParameters(params);
           gameRunner.setLeagueLevel(3);
           GameResult result = gameRunner.simulate();
           results.add(result);
           System.out.println("Finished game: " + (i+1));
       }
       System.out.println("done.");
    }
}