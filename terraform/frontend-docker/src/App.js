import React from "react";
import "./styles.css";
import Boundingbox from "react-bounding-box";

export default function App() {
  const params = {
    image: "http://i.imgur.com/gF7QYwa.jpg",
    boxes: [
      // coord(0,0) = top left corner of image
      //[x, y, width, height]
      // [0, 0, 250, 250],
      // [300, 0, 250, 250],
      // [700, 0, 300, 25],
      // [1100, 0, 25, 300]
      { coord: [300, 300, 350, 350], label: "test" },
      { coord: [300, 0, 250, 250], label: "A" },
      { coord: [700, 0, 300, 25], label: "B" },
      { coord: [1100, 0, 25, 300], label: "C" }
    ],
    options: {
      colors: {
        normal: "rgba(255,225,255,1)",
        selected: "rgba(0,225,204,1)",
        unselected: "rgba(100,100,100,1)"
      },
      style: {
        maxWidth: "100%",
        maxHeight: "90vh"
      }
      // showLabels: false
    }
  };
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      <Boundingbox
        image={params.image}
        boxes={params.boxes}
        options={params.options}
      />
    </div>
  );
}
