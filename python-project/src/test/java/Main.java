import com.codingame.gameengine.runner.SoloGameRunner;

public class Main {
    public static void main(String[] args) {
        
        SoloGameRunner gameRunner = new SoloGameRunner();
        gameRunner.setTestCase("test9.json");
        gameRunner.setAgent(Solution.class);
        gameRunner.start();
    }
}
