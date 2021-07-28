package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main8 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main8.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			Button btn = (Button) scene.lookup("#btn");
			TextField tfDan = (TextField) scene.lookup("#tfDan");
			TextArea ta = (TextArea) scene.lookup("#ta");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String dan = tfDan.getText();
					String result = "";
					for(int i = 1; i < 10; i++) {
						result += dan + " X " + i + " = " + Integer.parseInt(dan) * i + "\n";
 					}
					ta.setText(result);
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
