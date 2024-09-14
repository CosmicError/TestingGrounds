use std::collections::HashMap;
use std::time::Instant;

fn main() {

    let start = Instant::now();

    // Final Boss
    // let board = vec![
    //     1, 2, 0, 3, 0, 0, 0, 0, 0,
    //     4, 0, 0, 0, 0, 0, 3, 0, 0,
    //     0, 0, 3, 0, 5, 0, 0, 0, 0,
    //     0, 0, 4, 2, 0, 0, 5, 0, 0,
    //     0, 0, 0, 0, 8, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 5, 0, 7, 0,
    //     0, 0, 1, 5, 0, 2, 0, 0, 0,
    //     0, 0, 0, 0, 9, 0, 0, 6, 0,
    //     0, 0, 0, 0, 0, 7, 0, 0, 8
    // ];

    // Extreme Difficulty - Not Complete
    // solvable WITHOUT guessing
    let board = vec![
        0, 0, 0, 0, 0, 7, 0, 1, 0,
        0, 0, 0, 9, 1, 0, 6, 0, 7,
        0, 9, 0, 0, 8, 3, 0, 5, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 5, 0, 3, 0, 0, 0, 2, 0,
        9, 0, 0, 0, 7, 1, 0, 0, 5,
        0, 0, 5, 1, 0, 2, 0, 0, 0,
        0, 3, 0, 0, 0, 0, 0, 6, 0,
        0, 0, 0, 7, 0, 4, 0, 0, 8
    ];

    // Master Difficulty - Complete
    // let board = vec![
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 4, 1, 6, 2, 9, 0, 0,
    //     2, 0, 0, 0, 3, 0, 0, 7, 0,
    //     0, 9, 0, 0, 0, 0, 0, 6, 3,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 6, 0, 0, 1, 3, 0, 0, 7,
    //     9, 0, 6, 0, 0, 5, 0, 0, 0,
    //     8, 5, 0, 7, 0, 6, 4, 0, 0,
    //     0, 7, 0, 0, 0, 0, 0, 2, 0
    // ];

    // Expert Difficulty - Complete
    // let board = vec![
    //     4, 0, 0, 0, 5, 0, 8, 0, 2,
    //     0, 0, 0, 6, 0, 0, 0, 0, 0,
    //     0, 0, 3, 4, 0, 0, 1, 9, 6,
    //
    //     0, 0, 0, 0, 7, 6, 0, 8, 0,
    //     0, 0, 9, 0, 0, 0, 0, 0, 0,
    //     0, 0, 7, 0, 0, 5, 6, 0, 3,
    //
    //     0, 0, 0, 5, 1, 4, 0, 0, 0,
    //     0, 7, 4, 8, 0, 9, 0, 6, 0,
    //     1, 0, 0, 3, 0, 0, 0, 2, 9
    // ];

    // Hard Difficulty - Complete
    // let board = vec![
    //     6, 0, 0, 5, 3, 1, 9, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 7,
    //     5, 4, 9, 0, 0, 0, 0, 0, 0,
    //     2, 0, 0, 7, 0, 0, 0, 0, 0,
    //     0, 0, 7, 0, 9, 0, 0, 3, 2,
    //     0, 9, 0, 0, 1, 8, 0, 4, 5,
    //     0, 2, 0, 0, 7, 4, 5, 0, 1,
    //     4, 0, 0, 9, 0, 0, 3, 0, 0,
    //     0, 0, 3, 0, 0, 0, 0, 2, 0
    // ];

    // Medium Difficulty - Complete
    // let board = vec![
    //     9, 0, 3, 5, 6, 0, 0, 0, 7,
    //     2, 5, 0, 1, 0, 7, 0, 6, 0,
    //     6, 0, 7, 0, 0, 2, 0, 0, 0,
    //     0, 7, 0, 6, 0, 5, 3, 1, 0,
    //     1, 0, 0, 7, 3, 4, 0, 5, 8,
    //     0, 3, 0, 0, 1, 9, 0, 7, 4,
    //     0, 4, 5, 0, 2, 0, 0, 0, 1,
    //     0, 2, 6, 8, 0, 0, 0, 0, 0,
    //     0, 0, 1, 0, 0, 0, 5, 0, 0
    // ];

    // Easy Difficulty - Complete
    // let board = vec![
    //     0, 4, 5, 8, 7, 0, 9, 0, 0,
    //     0, 0, 0, 9, 0, 0, 0, 0, 0,
    //     2, 0, 8, 0, 6, 0, 0, 0, 4,
    //     0, 1, 0, 2, 0, 0, 4, 0, 0,
    //     9, 3, 0, 5, 4, 7, 2, 0, 0,
    //     0, 0, 4, 6, 9, 0, 7, 0, 3,
    //     0, 6, 0, 4, 8, 0, 0, 3, 1,
    //     3, 8, 0, 7, 0, 2, 6, 0, 9,
    //     0, 0, 0, 0, 0, 6, 0, 2, 7
    // ];

    // Blank Board
    // let board = vec![
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0,
    //     0, 0, 0, 0, 0, 0, 0, 0, 0
    // ];

    // for _ in 0..1000 {
        let mut game = Board::new(3, board);

        game.evaluate_board();
    // }

    let duration = start.elapsed();

    // actually show board
    // let mut game = Board::new(3, board.clone());
    // game.evaluate_board();
    game.print_board();
    //

    println!("1000 Run Average: {} microseconds", (duration.as_secs_f64() * 1000.0 * 1000.0) / 1000.0);
}

struct Cell {
    value: u8,
    global_index: usize,
    col_num: usize,
    row_num: usize,
    possibilities: u32, // Supports a max of 25x25 board
    house_index: usize
}

impl Cell {
    fn new(board_size: u8) -> Self {
        Cell {
            value: 0,
            global_index: 0,
            col_num: 0,
            row_num: 0,
            possibilities: (1 << board_size) - 1,
            house_index: 0,
        }
    }

    fn set_house_index(&mut self, num: usize) {
        self.house_index = num;
    }

    fn set_global_index(&mut self, board_size: usize, num: usize) {
        self.global_index = num;

        self.col_num = num % (board_size);
        self.row_num = num / (board_size);
    }

    fn set_value(&mut self, value: u8) {
        self.value = value
    }
}

struct Board {
    size: usize,
    board_size: usize,

    houses: Vec<Vec<Vec<usize>>>, // a vector that holds a 2d array of cell indices

    row_nums: Vec<u32>,
    col_nums: Vec<u32>,
    house_nums: Vec<u32>,

    unique_possibilities: Vec<HashMap<u8, usize>>,
    unset_cell_count: u16,
    // unset_cells: Vec<usize>, // cost more than to just iterate through all the cells and if check them

    cells: Vec<Cell>
}

impl Board {
    fn new(size: usize, values: Vec<u8>) -> Self {
        let total_cells: usize = size * size * size * size;
        let board_size = size * size;

        if values.len() != total_cells {
            panic!("Board information mismatch")
        }

        let mut cells: Vec<Cell> = Vec::with_capacity(total_cells);

        let mut houses = vec![vec![vec![0usize; size]; size]; board_size];

        let mut row_nums = vec![0u32; board_size];
        let mut col_nums = vec![0u32; board_size];
        let mut house_nums = vec![0u32; board_size];

        let mut unset_cell_count: u16 = 0;

        for i in 0..total_cells {
            let mut cell = Cell::new(board_size as u8);

            cell.set_global_index(board_size, i);
            cell.set_value(values[i]);

            let row: usize = cell.row_num;
            let col: usize = cell.col_num;

            houses[(row / size) * size + (col / size)][col % size][row % size] = cell.global_index;
            cell.set_house_index((row / size) * size + (col / size));

            if values[i] != 0 {
                row_nums[row] |= 1 << (values[i] - 1);
                col_nums[col] |= 1 << (values[i] - 1);
                house_nums[cell.house_index] |= 1 << (values[i] - 1);
            }
            else {
                unset_cell_count += 1;
            }

            cells.push(cell);
        }

        return Board {
            size,
            board_size,

            houses,

            row_nums,
            col_nums,
            house_nums,

            unique_possibilities: vec![HashMap::new(); board_size],
            unset_cell_count,

            cells,
        }
    }

    // fn row_start(self, global_index: usize) -> usize {
    //     // Pass in a random global index and get the global index of the cell the is first in the row
    //     return global_index - global_index % (self.board_size);
    // }
    //
    // fn col_start(self, global_index: usize) -> usize {
    //     // Pass in a random global index and get the global index of the cell the is first in the col
    //     return global_index % (self.board_size)
    // }
    //
    // fn house_start(self, global_index: usize) -> usize {
    //     // Pass in a random global index and get the top left cell global index of the same house
    //     return ((global_index / self.size) % (self.board_size)) * (self.board_size) + global_index % (self.board_size);
    // }

    fn update_cell_possibilities(&mut self) {
        for i in 0..(self.board_size * self.board_size) {
            let cell = &mut self.cells[i];

            if cell.value != 0 {
                continue;
            }

            let mut possibilities: u32 = (1 << (self.board_size)) - 1;

            possibilities &= !self.row_nums[cell.row_num];
            possibilities &= !self.col_nums[cell.col_num];
            possibilities &= !self.house_nums[cell.house_index];

            cell.possibilities = possibilities;
        }
    }

    fn update_unique_possibilities(&mut self) {
        let mut house_num: usize = 0;
        for house_index in 0..self.board_size {
            let mut unique_possibilities: u32 = 0;
            let mut common_possibilities: u32 = 0;

            for row_index in 0..self.size {
                for col_index in 0..self.size {
                    let cell = &self.cells[self.houses[house_index][row_index][col_index]];

                    if cell.value != 0 {
                        continue;
                    }

                    for possibility in 1..=(self.size*self.size) {
                        let pbit: u32 = 1 << (possibility - 1);

                        // possibility doesn't exist in the cell
                        if (cell.possibilities & pbit) == 0 {
                            continue;
                        }

                        // possibility is already assigned
                        if (self.house_nums[house_index] & pbit) != 0 {
                            continue;
                        }

                        // Not in common_possibilities and unique_possibilities
                        if (common_possibilities & pbit) == 0 && (unique_possibilities & pbit) == 0 {
                            unique_possibilities |= pbit;
                            self.unique_possibilities[house_num].insert(possibility as u8, cell.global_index);
                            continue;
                        }

                        if (unique_possibilities & pbit) != 0 {//self.unique_possibilities[house_num].contains_key(&(possibility as u8)) {
                            // remove the possibility, XOR returns a zero if both values are one
                            unique_possibilities ^= pbit;

                            // Add the possibility, OR returns a one if either value is a one
                            common_possibilities |= pbit;

                            self.unique_possibilities[house_num].remove(&(possibility as u8));
                        }
                    }
                }
            }

            house_num += 1;
        }
    }

    fn xwing_evaluate(&mut self) {
        let mut checked: Vec<usize> = Vec::with_capacity(self.board_size * self.board_size);
        for global_index in 0..(self.board_size*self.board_size) {

            if checked.contains(&global_index) {
                continue;
            }

            let mut cell = &self.cells[global_index];

            if cell.value != 0 {
                continue;
            }

            let mut row_indicies = global_index..(global_index - global_index % (self.board_size) + self.board_size);
            let mut col_indicies = (global_index % (self.board_size))..(global_index % (self.board_size) + self.board_size);

            for possibility in 0..self.board_size {
                // 1000 = top row
                // 0100 = bottom row
                // 0010 = left column
                // 0001 = right column
                let mut valid: u32 = 0b1111;
                let mut found: u32 = 0b0000;
                // let mut

                // top row
                for cell_index in &row_indicies {
                    if cell_index == global_index {
                        continue;
                    }

                    if self.cells[cell_index].value != 0 {
                        continue;
                    }

                    if self.cells[cell_index].possibilities & (1 << (possibility - 1)) == 0 {
                        continue;
                    }

                    found |= 1 << (4 - 1);
                }

                // didn't find a possibility in first row
                if found & 1 << (4 - 1) == 0 {
                    continue
                }

                // left column
                let mut lcol_index: usize = 0;
                for lcol_index in (global_index % (self.board_size))..(global_index % (self.board_size) + self.board_size) {
                    if lcol_index == global_index {
                        continue;
                    }

                    if self.cells[lcol_index].value != 0 {
                        continue;
                    }

                    if self.cells[lcol_index].possibilities & (1 << (possibility - 1)) == 0 {
                        continue;
                    }

                    found |= 1 << (2 - 1);

                    // right column
                    let mut rcol_index: usize = 0;
                    for rcol_index in (lcol_index % (self.board_size))..(lcol_index % (self.board_size) + self.board_size) {
                        if self.cells[rcol_index].value != 0 {
                            continue;
                        }

                        if self.cells[rcol_index].possibilities & (1 << (possibility - 1)) == 0 {
                            continue;
                        }

                        found |= 1 << (2 - 1);
                    }

                    // didn't find a possibility in left column
                    if found & 1 << (1 - 1) == 0 {
                        continue
                    }

                    // not same row
                    if self.cells[lcol_index].row_num != self.cells[rcol_index].row_num {
                        continue;
                    }
                }

                // didn't find a possibility in left column
                if found & 1 << (2 - 1) == 0 {
                    continue
                }
            }
        }
    }

    fn evaluate_board(&mut self) {
        let mut iters = 0;
        let mut change = true;
        while change {
            change = false;
            iters += 1;

            self.update_cell_possibilities();
            self.update_unique_possibilities();

            // Set all unique possibilities
            for i in 0..self.board_size {

                // If there are no unique possibilities in this house then go to the next house
                if self.unique_possibilities[i].len() == 0 {
                    continue;
                }

                // assign all found unique possibilities in that house to their respective cells
                for (&p, &cell_index) in self.unique_possibilities[i].iter() {
                    self.cells[cell_index].value = p;
                    self.cells[cell_index].possibilities = 0;

                    self.row_nums[self.cells[cell_index].row_num] |= 1 << (self.cells[cell_index].value - 1);
                    self.col_nums[self.cells[cell_index].col_num] |= 1 << (self.cells[cell_index].value - 1);
                    self.house_nums[self.cells[cell_index].house_index] |= 1 << (self.cells[cell_index].value - 1);

                    self.unset_cell_count -= 1;
                    change = true;
                }

                // clear this house's recorded unique possibilities
                let _ = &self.unique_possibilities[i].clear();
            }

            // Set all possibilities where in a cell it is the only possibility
            for cell_index in 0..(self.board_size * self.board_size) {

                // if the cell already has a value assigned, then continue
                if self.cells[cell_index].value != 0 {
                    continue;
                }

                if self.cells[cell_index].possibilities < 1 {
                    continue
                }

                // Check if the number already set in the house
                if self.house_nums[self.cells[cell_index].house_index] & self.cells[cell_index].possibilities != 0 {
                    continue;
                }

                // Checks if ONLY 1 bit is set in the mask, if more then 1 is set than the resulting number will be greater than 0
                // Example. 0b0000_1000 & 0b0000_1000 - 1  ->  0b0000_1000 & 0b1111_0111  ->  0
                if (self.cells[cell_index].possibilities & (self.cells[cell_index].possibilities - 1)) != 0 {
                    continue;
                }

                self.cells[cell_index].value = (self.cells[cell_index].possibilities.ilog2() + 1) as u8;
                self.cells[cell_index].possibilities = 0;

                self.row_nums[self.cells[cell_index].row_num] |= 1 << (self.cells[cell_index].value - 1);
                self.col_nums[self.cells[cell_index].col_num] |= 1 << (self.cells[cell_index].value - 1);
                self.house_nums[self.cells[cell_index].house_index] |= 1 << (self.cells[cell_index].value - 1);

                self.unset_cell_count -= 1;
                change = true;
            }
        }
    }

    fn print_board(&self) {
        let separator = "-".repeat(self.size * self.size * self.size - self.size * 2);
        for row in 0..self.board_size {
            for col in 0..self.board_size {
                let cell_index = row * self.board_size + col;
                let cell = &self.cells[cell_index];

                if col > 0 && col % self.size == 0 {
                    print!("| ");
                }

                if cell.value == 0 {
                    print!("  ");
                } else {
                    print!("{} ", cell.value);
                }
            }
            println!();
            if (row + 1) % self.size == 0 && row + 1 != self.board_size {
                println!("{}", separator);
            }
        }
    }
}