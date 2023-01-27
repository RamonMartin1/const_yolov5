import React, { useEffect, useState } from "react";
import "./styles.css";
import Boundingbox from "react-bounding-box";

export default function App() {
  const [boxes, setBoxes] = useState([]);
  var base_url = 'https://www.ishn.com/ext/resources/hi-vis-supply-construction-site.jpg'
  var url = 'http://localhost:8000/?url=' + base_url
  // response is xmin,ymin,xmax,ymax,confidence,class,name,

  const fetchData = async () => {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error('Data coud not be fetched!')
    } else {
      return response.json()
    }
  }

  useEffect(() => {
    fetchData()
      .then((res) => {
        // JSON.parse(res) is used in place of `res` since the returned val from the api is a str
        const mappedBoxes = JSON.parse(res).map(box => ({
            coord: [box.xmin, box.ymin, box.xmax - box.xmin, box.ymax - box.ymin],
            label: box.name
        }));
        setBoxes(mappedBoxes)
      })
      .catch((e) => {
        console.log(e.message)
      })
  }, [])

  const params = {
    image: base_url,
    // boxes: [
    //   // coord(0,0) = top left corner of image
    //   //[x, y, width, height]
    //   // [0, 0, 250, 250],
    //   // [300, 0, 250, 250],
    //   // [700, 0, 300, 25],
    //   // [1100, 0, 25, 300]
    //   { coord: [300, 300, 350, 350], label: "test" },
    //   { coord: [300, 0, 250, 250], label: "A" },
    //   { coord: [700, 0, 300, 25], label: "B" },
    //   { coord: [1100, 0, 25, 300], label: "C" }
    // ],
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
      <h1>Image labeller</h1>
      <h2>Currently viewing: {base_url}</h2>
      <Boundingbox
        image={params.image}
        boxes={boxes}
        options={params.options}
      />
    </div>
  );
}
