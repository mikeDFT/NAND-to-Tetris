// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Code1 (not too cool, but normal fill)
// pseudo-code
//int i
//
//if(RAM[KBD]!=0)
//	{ (1)
//		for(i=SCREEN; i<KBD; i++)
//			RAM[i] = -1;
//			
//		(1.1)
//		while(RAM[KBD] != 0)
//			(1.1)
//		
//		(2)
//	}
//else
//	{ (2)
//		for(i=SCREEN; i<KBD; i++)
//			RAM[i] = 0;
//			
//		(1.2)
//		while(RAM[KBD] != 0)
//			(1.2)
//		
//		(1)
//	}

@i 			// init variables
@address

@KBD		// key pressed ?
D=M
@TURN_BLACK
D;JNE
@TURN_WHITE
0;JMP


(TURN_BLACK)
@SCREEN		// address = SCREEN
D=A
@address
M=D

(BLACK_LOOP)
@KBD		// address<KBD ?
D=A
@address
D=M-D
@BLACK_END
D;JGE

@address	// RAM[address] = -1
A=M
M=-1

@address	// address++
M=M+1

@BLACK_LOOP
0;JMP

(BLACK_END)
@KBD
D=M
@TURN_WHITE	// turn white if key released
D;JEQ
@BLACK_END	// wait until key released
0;JMP


(TURN_WHITE)
@SCREEN		// address = SCREEN
D=A
@address
M=D

(WHITE_LOOP)
@KBD		// address<KBD ?
D=A
@address
D=M-D
@WHITE_END
D;JGE

@address	// RAM[address] = 0
A=M
M=0

@address	// address++
M=M+1

@WHITE_LOOP
0;JMP

(WHITE_END)
@KBD
D=M
@TURN_BLACK	// turn black if key pressed
D;JNE
@WHITE_END	// wait until key pressed
0;JMP
