# Sounds and Sights of a Flight

The assignment: Write a Jython program that sonifies some real-world data to generate an interesting musical output that maps important attributes of the data to sound so that they can be better understood. I chose a flight log of the first leg I took leaving a family reunion in December 2023.

The project consists of two complementary programs: one for sonifying flight data into music and the other for visualizing the flight path graphically.

## Sonification Program

The **Flight Sonification** program transforms flight data (longitude, latitude, altitude) into a musical composition.

### Features

- Maps longitude, latitude, and altitude to bass, tenor, soprano, and other musical parts.
- Outputs a MIDI file (`flightSonification.mid`) for playback.
- Visualizes the musical score and piano roll.

### Output

- **Longitude:** Bass and Baritone parts (low register).
- **Latitude:** Tenor and Alto parts (mid-range harmony).
- **Altitude:** Mezzo-Soprano and Soprano parts (melodic high register).

## Visualization Program

The **Flight Visualization** program graphically represents the flight path, displaying altitude and geographical data in a dynamic interface.

### Features

- Uses `flightData.txt` for the flight's longitude, latitude, and altitude.
- Plots the path over a graphical background (`back.png`).
- Adds airport labels for start (`Saigon`) and end (`Narita`).
- Altitude visualized via circle size and color (altitude mapped to green intensity).

### Output Example

- **Longitude & Latitude:** Mapped to x-y coordinates for visual positioning.
- **Altitude:** Circle size and green intensity reflect altitude changes.

## Prerequisites

- Python environment set up, preferably in Jython Music.
- Libraries for music (`jMusic`) and graphics display.
- A valid `flightData.txt` file containing tab-separated values in the format:
  
  ```
  time    longitude    latitude    altitude
  ```

## Future Enhancements

- **Sonification:** Experiment with different scales or instruments.
- **Visualization:** Add animations or interactivity to the flight path.
- **Integration:** Combine sonification and visualization for a synchronized experience.

## Contact Information
- **Author:** Chi Nguyen
- **Email:** c.n91702@gmail.com
