class Node{
   int x;
   int y;
   Node parent = this;
   double fCost = 0;
   double gCost = Double.POSITIVE_INFINITY; 
   double cost = 1.0;
   boolean wall = false;
   ArrayList<Node> neighbors = new ArrayList<Node>();
  
    Node(int x, int y){
      this.x = x;
      this.y = y;
      
      if (Math.random()*10 > 7){
        wall = true;
      }
    }
    
    void getNeighbors(Node[][] grid){
        if (this.x > 0){
           this.neighbors.add(grid[this.x - 1][this.y]);
        }
        if (this.y > 0){
           this.neighbors.add(grid[this.x][this.y - 1]);
        }
        if (this.x + 1 < grid.length){
           this.neighbors.add(grid[this.x + 1][this.y]);
        }
        if (this.y + 1 < grid[x].length){
           this.neighbors.add(grid[this.x][this.y + 1]);
        }
    }
  
   void reset(){
     gCost = Double.POSITIVE_INFINITY;
     fCost = 0;
     neighbors.clear();
     parent = this;
     
   }
}
    