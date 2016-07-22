/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package missedfinder;

import javax.swing.event.TableModelListener;
import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;

/**
 *
 * @author ynl0zq
 */
public class MyTableModel extends AbstractTableModel{

    private String[] columnNames = {"ID", "Title", "URL"};
//    private Object[][] data = {
//        {"vv", "gg"},
//        {"hh", "ll"}
//    };
    private ArrayList<Item> data = Items.items;

    public int getColumnCount() {
        return columnNames.length;
    }

    public int getRowCount() {
//        return data.length;
        return data.size();
    }

    public String getColumnName(int col) {
        return columnNames[col];
    }

    public Object getValueAt(int row, int col) {
//        return data[row][col];
        switch(col) {
            case 0:
                return data.get(row).id;
//                break;
            case 1:
                return data.get(row).title;
            case 2:
                return data.get(row).url;
        }
        return null;
    }

    public Class getColumnClass(int c) {
        return getValueAt(0, c).getClass();
    }

}
