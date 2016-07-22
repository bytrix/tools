/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package missedfinder;

import java.util.ArrayList;
import java.util.HashMap;

/**
 *
 * @author ynl0zq
 */
public class Item {
//    public static ArrayList<Integer> index = new ArrayList<>();
//    public static ArrayList<String> URLs;
//    public static ArrayList<String> LeftURLs;
    
    public int id;
    public String title;
    public String url;
    
    public Item(int id, String title) {
        this.id = id;
        this.title = title;
    }
    
    public void setUrl(String url) {
        this.url = url;
    }
}
