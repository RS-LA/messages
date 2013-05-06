package com.messages.android;

import android.os.Bundle;
import android.util.Log;

import com.actionbarsherlock.view.Menu;
import com.messages.util.BaseFragmentActivity;

public class MainFragmentActivity extends BaseFragmentActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Log.e("MainActivity onCreate", "WHAT");
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getSupportMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
}