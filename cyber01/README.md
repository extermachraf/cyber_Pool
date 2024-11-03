# TOTP: A Comprehensive Guide to Time-Based One-Time Password Algorithms

## Introduction
In the digital age, securing online transactions and user authentication is critical. Two widely adopted methods for enhancing security are the HMAC-based One-Time Password (HOTP) and the Time-Based One-Time Password (TOTP). Both algorithms offer robust security solutions, yet they differ in implementation and application. HOTP, defined in [RFC 4226](https://www.rfc-editor.org/rfc/rfc4226), is based on an event counter, while TOTP, defined in [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238), uses a time-based moving factor.

## Step-by-Step Breakdown of HOTP Algorithm
1. **Initialize Variables**
   - **Shared Secret (K)**: A secret key known to both the client and the server.
     - Example: `K = "12345678901234567890"`
   - **Counter (C)**: Starts at 0 and increments with each use.
     - Example: `C = 1`

2. **HMAC-SHA-1 Calculation**
   - Combine K and C using HMAC-SHA-1:
     - Convert C to an 8-byte array in binary format.
     - The counter value 1 in 8-byte binary format is: `00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000001`
     - Calculate HMAC-SHA-1:
       - `HMAC-SHA-1(K, C)` generates a 20-byte (160-bit) hash.
       - Suppose we get: `1f8698690e02ca16618550ef7f19da8e945b555a`

3. **Dynamic Truncation**
   - Extract Offset:
     - Last byte of the HMAC-SHA-1 hash: `5a` in hex.
     - Binary of `5a`: `01011010`
     - Offset is determined by the lower 4 bits: `1010` (binary) = 10 (decimal)
     - **Offset**: `10`
   - Extract 4-Byte Code:
     - Starting at Offset, extract 4 bytes:
     - Bytes at Offset 10: `50ef7f19`
     - Converting the hex bytes to binary:
       - `50`: `01010000`
       - `ef`: `11101111`
       - `7f`: `01111111`
       - `19`: `00011001`
     - Combine 4 bytes:
       - Concatenate these binary strings:
         - `01010000 11101111 01111111 00011001`

4. **Convert to 31-bit Number**
   - Ignore Most Significant Bit:
     - Binary: `01010000 11101111 01111111 00011001` (32 bits)
     - 31-bit: `00101111 01111101 01110011 01110111`
   - Convert to Decimal:
     - Binary: `00101111 01111101 01110011 01110111`
     - Decimal: `789016471`

5. **Generate Final OTP**
   - Modulo Operation:
     - If 6-digit OTP: `Snum mod 10^6`
     - `789016471 mod 10^6 = 16471`
   - **Final OTP**:
     - The OTP generated is `16471`. Note: It should have been zero-padded to six digits, making it `016471`.

### Summary:
- **HS (HMAC-SHA-1)**: `1f8698690e02ca16618550ef7f19da8e945b555a`
- **Offset**: `10`
- **Extracted 4 Bytes**: `50ef7f19`
- **31-bit Binary**: `00101111 01111101 01110011 01110111`
- **Decimal Number**: `789016471`
- **Final OTP**: `016471`

Every step ensures the OTP is secure and unique, making it a robust method for authentication.

## TOTP Implementation:

### Overview:
TOTP (Time-Based One-Time Password) is defined as TOTP = HOTP(K, T), where T is an integer representing the number of time steps between the initial counter time (T0) and the current Unix time. Specifically, T is calculated as:


\[ T = \frac{\text{Current Unix time} - T0}{X} \]


using the default floor function.

### Example:
With T0 = 0 and Time Step X = 30:
- If the current Unix time is 59 seconds, T = 1.
- If the current Unix time is 60 seconds, T = 2.

The algorithm must support time values larger than a 32-bit integer beyond the year 2038. System parameters X and T0 are set during provisioning and shared between the prover and verifier as part of this step.

Does this look good, or would you like to tweak anything?

