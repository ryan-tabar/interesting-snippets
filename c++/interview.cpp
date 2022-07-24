#include <iostream>
#include <array>
constexpr unsigned int ROWS = 7;
constexpr unsigned int COLS = 7;
constexpr unsigned int MAX_ROW = ROWS - 1;
constexpr unsigned int MAX_COL = COLS - 1;
constexpr unsigned int ROW_WIN = 3;
constexpr unsigned int COL_WIN = 3;
constexpr unsigned int DIRECTIONS = 4;

typedef std::array<std::array<char, COLS>, ROWS> BoardArray;
typedef std::array<std::pair<int, int>, DIRECTIONS> Directions;

void printBoard(const BoardArray& board) {
	for (const auto& row : board) {
		for (const auto& col : row) {
			std::cout << col;
		}
		std::cout << std::endl;
	}
	std::cout << "------------" << std::endl;
}

Directions getDirections(const unsigned int row, const unsigned int col, const unsigned int delta) {
	return { {{row - delta, col},
			  {row + delta, col},
			  {row, col - delta},
			  {row, col + delta}} };
}

bool doMoves(const BoardArray& board, const int jumpsToComplete) {
	// winning condition
	if (jumpsToComplete == 0 && board[ROW_WIN][COL_WIN] == 'o') {
		return true;
	}

	// for every piece on the board
	for (int row = 0; row < ROWS; ++row) {
		for (int col = 0; col < COLS; ++col) {
			// skip if no ball
			if (board[row][col] != 'o') {
				continue;
			}

			// define jumps
			unsigned int delta = 1;
			const Directions jumpOvers = getDirections(row, col, delta);

			delta = 2;
			const Directions jumpTos = getDirections(row, col, delta);

			// for every direction
			for (int i = 0; i < DIRECTIONS; ++i) {
				// skip if out of index range
				if (jumpTos[i].first < 0 || 
					jumpTos[i].first > MAX_ROW || 
					jumpTos[i].second < 0 || 
					jumpTos[i].second > MAX_COL) {
					continue;
				}
				
				// copy board
				BoardArray copiedBoard = board;

				// define cells
				char& current = copiedBoard[row][col];
				char& jumpOver = copiedBoard[jumpOvers[i].first][jumpOvers[i].second];
				char& jumpTo = copiedBoard[jumpTos[i].first][jumpTos[i].second];

				// if there's a ball to jump over and an empty spot after it
				if (jumpOver == 'o' && jumpTo == ' ') {
					// make the jump
					current = ' ';
					jumpOver = ' ';
					jumpTo = 'o';
					if (doMoves(copiedBoard, jumpsToComplete - 1)) {
						printBoard(copiedBoard);
						return true;
					}
				}
			}

		}
	}
	return false;
}

int main() {
	BoardArray board =
    {{{ 'x', 'x', 'o', 'o', 'o', 'x', 'x' },
      { 'x', 'x', 'o', 'o', 'o', 'x', 'x' },
	  { 'o', 'o', 'o', 'o', 'o', 'o', 'o' },
	  { 'o', 'o', 'o', ' ', 'o', 'o', 'o' },
	  { 'o', 'o', 'o', 'o', 'o', 'o', 'o' },
	  { 'x', 'x', 'o', 'o', 'o', 'x', 'x' },
	  { 'x', 'x', 'o', 'o', 'o', 'x', 'x' }}};

	const unsigned int jumpsToComplete = 31;
	doMoves(board, jumpsToComplete);
	printBoard(board);

	return 0;
}