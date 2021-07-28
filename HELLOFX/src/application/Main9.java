package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

public class Main9 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			Button btn1 = (Button) scene.lookup("#btn1");
			Button btn2 = (Button) scene.lookup("#btn2");
			Button btn3 = (Button) scene.lookup("#btn3");
			Button btn4 = (Button) scene.lookup("#btn4");
			Button btn5 = (Button) scene.lookup("#btn5");
			Button btn6 = (Button) scene.lookup("#btn6");
			Button btn7 = (Button) scene.lookup("#btn7");
			Button btn8 = (Button) scene.lookup("#btn8");
			Button btn9 = (Button) scene.lookup("#btn9");
			Button btn0 = (Button) scene.lookup("#btn0");
			Button btnCall = (Button) scene.lookup("#btnCall");
			Button btnDel = (Button) scene.lookup("#btnDel");
			TextField tf = (TextField) scene.lookup("#tf");
			
			Button[] btns = {btn0, btn1, btn2, btn3, btn4, btn5
							, btn6, btn7, btn8, btn9};
			
			for(int i = 0; i < btns.length; i++) {
				int num = i;
				btns[i].setOnMouseClicked(new EventHandler<Event>() {
					@Override
					public void handle(Event event) {
						// Button temp = (Button) event.getTarget();
						// System.out.println(temp.getText());  => 0, 1, 2, 3, 4 ...
						String number = tf.getText();
						number += num;
						if(number.length() == 3 || number.length() == 8) {
							number += "-";
						}
						if(number.length() == 14) {
							return;
						}
						tf.setText(number);
					}
				});
			}
			
			btnDel.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String number = tf.getText();
					number = number.substring(0, number.length() - 1);
					tf.setText(number);
				}
			});
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					Alert alert = new Alert(AlertType.CONFIRMATION);
					alert.setTitle("Call");
					alert.setHeaderText("Calling...");
					alert.setContentText(tf.getText());
					
					alert.showAndWait();
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
