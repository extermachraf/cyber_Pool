# Reverse Engineering a Binary: A Step-by-Step Guide

## Step 2: Analyze the Binary

### Disassemble the Binary

Use `objdump` to disassemble the binary:

```sh
objdump -d your_binary > disassembled.txt
```

### Use `strings` to Find Useful Information

Extract readable strings from the binary:

```sh
strings your_binary > strings.txt
```

## Step 3: Debug with GDB

### Start GDB

Launch GDB with your binary:

```sh
gdb your_binary
```

### Set a Breakpoint at `main`

In GDB, set a breakpoint at the `main` function:

```gdb
(gdb) break main
```

### Run the Program

Run the program within GDB:

```gdb
(gdb) run
```

### Step Through the Code

Step through the code line by line:

```gdb
(gdb) step
```

### Inspect Variables and Memory

Inspect variables and memory to understand the program's behavior:

```gdb
(gdb) print variable_name
(gdb) x/10x memory_address
```

## Step 4: Analyze the Disassembled Code

### Example Disassembled Code

```assembly
080484a0 <main>:
 80484a0: 55                    push   %ebp
 80484a1: 89 e5                 mov    %esp,%ebp
 80484a3: 83 ec 18              sub    $0x18,%esp
 80484a6: 83 e4 f0              and    $0xfffffff0,%esp
 80484a9: b8 00 00 00 00        mov    $0x0,%eax
 80484ae: e8 fc ff ff ff        call   80484af <__x86.get_pc_thunk.ax>
 80484b3: 05 00 00 00 00        add    $0x0,%eax
 80484b8: 89 45 fc              mov    %eax,-0x4(%ebp)
 80484bb: 83 ec 0c              sub    $0xc,%esp
 80484be: 68 00 00 00 00        push   $0x0
 80484c3: e8 fc ff ff ff        call   80484c4 <puts@plt>
```

### Explanation of Disassembled Code

#### Function Prologue

Sets up the stack frame and saves registers:

```assembly
 80484a0: 55                    push   %ebp
 80484a1: 89 e5                 mov    %esp,%ebp
```

#### Initialization

Adjusts `ebx` to point to some data and initializes variables:

```assembly
 80484a3: 83 ec 18              sub    $0x18,%esp
 80484a6: 83 e4 f0              and    $0xfffffff0,%esp
```

#### Print Prompt

Prints a prompt asking for a password:

```assembly
 80484be: 68 00 00 00 00        push   $0x0
 80484c3: e8 fc ff ff ff        call   80484c4 <puts@plt>
```

#### Read Input

Reads user input using `scanf`:

```assembly
 80484c8: 68 00 00 00 00        push   $0x0
 80484cd: e8 fc ff ff ff        call   80484ce <scanf@plt>
```

#### Compare Input

Compares the input with a stored password using `strcmp`:

```assembly
 80484d2: 68 00 00 00 00        push   $0x0
 80484d7: e8 fc ff ff ff        call   80484d8 <strcmp@plt>
```

#### Print Result

Prints a success or failure message based on the comparison result:

```assembly
 80484dc: 68 00 00 00 00        push   $0x0
 80484e1: e8 fc ff ff ff        call   80484e2 <puts@plt>
```

#### Function Epilogue

Cleans up the stack frame and returns:

```assembly
 80484e6: c9                    leave
 80484e7: c3                    ret
```

This guide provides a basic overview of reversing a binary. For more complex binaries, additional tools and techniques may be required.