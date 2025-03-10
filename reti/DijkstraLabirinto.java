import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.*;

public class DijkstraLabirinto {
    private static final int SIZE = 10;
    private static final int WALL = -1;
    private static final int PATH = 0;
    private static final int START = 1;
    private static final int END = 2;
    private static final int VISITED = 3;
    private static final int SHORTEST = 4;
    
    private int[][] grid = new int[SIZE][SIZE];
    private JTable table;
    private Point start = null, end = null;
    
    public DijkstraLabirinto() {
        JFrame frame = new JFrame("Dijkstra - Labirinto");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        
        generateConnectedMaze();
        table = createTable();
        frame.add(new JScrollPane(table), BorderLayout.CENTER);
        
        JButton solveButton = new JButton("Trova percorso");
        solveButton.addActionListener(e -> findShortestPath());
        frame.add(solveButton, BorderLayout.SOUTH);
        
        frame.setVisible(true);
    }
    
    private void generateConnectedMaze() {
        for (int i = 0; i < SIZE; i++) {
            Arrays.fill(grid[i], WALL);
        }
        
        Stack<Point> stack = new Stack<>();
        Point startPoint = new Point(0, 0);
        grid[startPoint.x][startPoint.y] = PATH;
        stack.push(startPoint);
        
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Random rand = new Random();
        
        while (!stack.isEmpty()) {
            Point current = stack.pop();
            java.util.List<Point> neighbors = new ArrayList<>();
            for (int[] d : directions) {
                int nx = current.x + d[0] * 2, ny = current.y + d[1] * 2;
                if (nx >= 0 && ny >= 0 && nx < SIZE && ny < SIZE && grid[nx][ny] == WALL) {
                    neighbors.add(new Point(nx, ny));
                }
            }
            if (!neighbors.isEmpty()) {
                stack.push(current);
                Point next = neighbors.get(rand.nextInt(neighbors.size()));
                grid[next.x][next.y] = PATH;
                grid[(current.x + next.x) / 2][(current.y + next.y) / 2] = PATH;
                stack.push(next);
            }
        }
    }
    
    private JTable createTable() {
        DefaultTableModel model = new DefaultTableModel(SIZE, SIZE);
        JTable table = new JTable(model) {
            @Override
            public Component prepareRenderer(javax.swing.table.TableCellRenderer renderer, int row, int col) {
                Component c = super.prepareRenderer(renderer, row, col);
                switch (grid[row][col]) {
                    case WALL -> c.setBackground(Color.BLACK);
                    case PATH -> c.setBackground(Color.WHITE);
                    case START -> c.setBackground(Color.RED);
                    case END -> c.setBackground(Color.GREEN);
                    case VISITED -> c.setBackground(Color.YELLOW);
                    case SHORTEST -> c.setBackground(Color.BLUE);
                }
                return c;
            }
        };
        
        table.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int row = table.rowAtPoint(e.getPoint());
                int col = table.columnAtPoint(e.getPoint());
                if (start == null) {
                    start = new Point(row, col);
                    grid[row][col] = START;
                } else if (end == null) {
                    end = new Point(row, col);
                    grid[row][col] = END;
                }
                table.repaint();
            }
        });
        return table;
    }
    
    private void findShortestPath() {
        if (start == null || end == null) return;
        PriorityQueue<Point> queue = new PriorityQueue<>(Comparator.comparingInt(p -> p.x + p.y));
        Map<Point, Point> prev = new HashMap<>();
        queue.add(start);
        
        while (!queue.isEmpty()) {
            Point current = queue.poll();
            if (current.equals(end)) break;
            
            for (Point neighbor : getNeighbors(current)) {
                if (!prev.containsKey(neighbor) && grid[neighbor.x][neighbor.y] != WALL) {
                    prev.put(neighbor, current);
                    queue.add(neighbor);
                    grid[neighbor.x][neighbor.y] = VISITED;
                }
            }
            table.repaint();
            try { Thread.sleep(50); } catch (InterruptedException ignored) {}
        }
        
        reconstructPath(prev);
    }
    
    private List<Point> getNeighbors(Point p) {
        List<Point> neighbors = new ArrayList<>();
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : directions) {
            int nx = p.x + d[0], ny = p.y + d[1];
            if (nx >= 0 && ny >= 0 && nx < SIZE && ny < SIZE) {
                neighbors.add(new Point(nx, ny));
            }
        }
        return neighbors;
    }
    
    private void reconstructPath(Map<Point, Point> prev) {
        Point current = end;
        while (prev.containsKey(current)) {
            current = prev.get(current);
            if (!current.equals(start)) {
                grid[current.x][current.y] = SHORTEST;
            }
            table.repaint();
            try { Thread.sleep(50); } catch (InterruptedException ignored) {}
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(DijkstraLabirinto::new);
    }
}
