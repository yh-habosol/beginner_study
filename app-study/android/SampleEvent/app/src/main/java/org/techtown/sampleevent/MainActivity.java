package org.techtown.sampleevent;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.GestureDetector;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    GestureDetector detector;

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if(keyCode == KeyEvent.KEYCODE_BACK){
            Toast.makeText(this, "back button pressed", Toast.LENGTH_LONG).show();
            return true;
        }
        return false;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = findViewById(R.id.textView);
        View view = findViewById(R.id.view);
        view.setOnTouchListener(new View.OnTouchListener(){
            public boolean onTouch(View view, MotionEvent motionEvent){
                int action = motionEvent.getAction();
                float curX = motionEvent.getX();
                float curY = motionEvent.getY();

                if(action==MotionEvent.ACTION_DOWN){
                    println("손가락 눌림: " + curX + ", "+ curY);
                } else if(action==MotionEvent.ACTION_MOVE){
                    println("손가락 눌림: " + curX + ", "+ curY);
                } else if(action==MotionEvent.ACTION_UP){
                    println("손가락 눌림: " + curX + ", "+ curY);
                }
                return true;
            }
        });

        detector = new GestureDetector(this, new GestureDetector.OnGestureListener(){
            @Override
            public boolean onDown(MotionEvent e) {
                println("onDown() ");
                return true;
            }

            @Override
            public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
                println("onFling() ");
                return true;
            }

            @Override
            public boolean onScroll(MotionEvent e1, MotionEvent e2, float distanceX, float distanceY) {
                println("onScroll() ");
                return true;
            }

            @Override
            public void onLongPress(MotionEvent e) {
                println("onLongPress() ");
            }

            @Override
            public void onShowPress(MotionEvent e) {
                println("onShowPress() ");
            }

            @Override
            public boolean onSingleTapUp(MotionEvent e) {
                println("onSingleTabUp() ");
                return true;
            }
        });
        View view2 = findViewById(R.id.view2);
        view2.setOnTouchListener(new View.OnTouchListener(){
            public boolean onTouch(View view, MotionEvent motionEvent){
                detector.onTouchEvent(motionEvent);
                return true;
            }
        });

        }
    public void println(String data){
        textView.append(data + "\n");
    }
}