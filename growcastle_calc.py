def calculate_outputs(wave):
    # Calculate the outputs based on the given wave number
    castle = wave * 0.05
    giant = wave * 0.05
    dbm = wave * 0.045
    sniper = wave * 0.035
    edward_min = wave * 0.02
    edward_max = wave * 0.03
    elf = wave * 0.02
    slinger_angels = wave * 0.01

    # Print the results
    print(f"Wave: {wave}")
    print(f"Castle: {castle:.2f}")
    print(f"Giant: {giant:.2f}")
    print(f"DBM: {dbm:.2f}")
    print(f"Sniper: {sniper:.2f}")
    print(f"Edward: {edward_min:.2f} to {edward_max:.2f}")
    print(f"Elf: {elf:.2f}")
    print(f"Slinger and Angels: {slinger_angels:.2f}")

# Example usage
if __name__ == "__main__":
    wave_input = int(input("Enter the wave number: "))
    calculate_outputs(wave_input)
