package org.techtown.sampleorientation;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    String name;
    EditText editText;
    @Override
    protected void onStart() {
        super.onStart();
        showToast("onStart()");
    }

    @Override
    protected void onStop() {
        super.onStop();
        showToast("OnStop()");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        showToast("onDestory()");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        showToast("onCreate()");

        editText = findViewById(R.id.editText);
        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener(){
            public void onClick(View view){
                name = editText.getText().toString();
                showToast("saved name");
            }
        });
        if(savedInstanceState!=null){
            name = savedInstanceState.getString("name");
            showToast("restore name");
        }
    }


    @Override
    protected void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putString("name", name);
    }

    public void showToast(String data){
        Toast.makeText(this, data, Toast.LENGTH_LONG).show();
    }
}