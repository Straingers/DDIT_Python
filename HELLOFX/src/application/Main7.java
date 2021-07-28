package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main7 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main7.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			Button btn = (Button) scene.lookup("#btn");
			TextField tfMine = (TextField) scene.lookup("#tfMine");
			TextField tfCom = (TextField) scene.lookup("#tfCom");
			TextField tfResult = (TextField) scene.lookup("#tfResult");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String mine = tfMine.getText();
					double a = Math.random();
					String com = "";
					if(a > 0.66) {
						com = "가위";
					} else if(a > 0.33){
						com = "바위";
					} else {
						com = "보";
					}
					tfCom.setText(com);
					String result = "";
					
					if(mine.equals("가위") && com.equals("보")) {
						result = "승리!";
					} else if(mine.equals("바위") && com.equals("가위")) {
						result = "승리!";
					} else if(mine.equals("보") && com.equals("바위")) {
						result = "승리!";
					} else if(mine.equals("가위") && com.equals("바위")) {
						result = "패배!";
					} else if(mine.equals("바위") && com.equals("보")) {
						result = "패배!";
					} else if(mine.equals("보") && com.equals("가위")) {
						result = "패배!";
					} else {
						result = "무승부!";
					}
					tfResult.setText(result);
				}
			});
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
