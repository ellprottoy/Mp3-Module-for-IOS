import AVFoundation

// Get the URL for the MP3 file
let fileURL = URL(fileURLWithPath: "/path/to/file.mp3")

// Create an AVAudioPlayer instance
do {
  let player = try AVAudioPlayer(contentsOf: fileURL)
  player.play()
} catch {
  print("Error playing MP3 file: \(error)")
}

import AVFoundation

let fileURL = URL(fileURLWithPath: "/path/to/file.mp3")

do {
  player = try AVAudioPlayer(contentsOf: fileURL)
} catch {
  print("Error loading MP3 file: \(error)")
}
@IBAction func playButtonTapped(_ sender: Any) {
  player.play()
}
