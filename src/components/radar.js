import React, { useEffect, useRef } from 'react';

function Radar({ planeInfo, max_radius }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');

    canvas.width = 550;
    canvas.height = 550;

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // Set the stroke color to white
    context.strokeStyle = "white";
    context.font = "20px Arial";
    context.fillStyle = "white";


    context.fillText(`*in km`, canvas.width - 70, canvas.height - 10);
    context.fillText(`N`, centerX - 20, 20);
    context.fillText(`S`, centerX + 5, canvas.height);

    // Draw circles with different radii
    context.beginPath();
    context.arc(centerX, centerY, 250 * 0.25, 0, 2 * Math.PI);
    context.fillText(`${Math.round(max_radius * 0.25)}`, 250 + 250 * 0.25 + 30, centerX - 5);
    context.stroke();
    context.beginPath();
    context.arc(centerX, centerY, 250 * 0.5, 0, 2 * Math.PI);
    context.fillText(`${Math.round(max_radius * 0.5)}`, 250 + 250 * 0.5 + 30, centerX - 5);
    context.stroke();
    context.beginPath();
    context.arc(centerX, centerY, 250 * 0.75, 0, 2 * Math.PI);
    context.fillText(`${Math.round(max_radius * 0.75)}`, 250 + 250 * 0.75 + 30, centerX - 5);
    context.stroke();
    context.beginPath();
    context.arc(centerX, centerY, 250, 0, 2 * Math.PI);
    context.fillText(`${Math.round(max_radius)}`, 250 + 250 + 30, centerX - 5);
    context.stroke();

    //Draw NS EW
    context.beginPath();
    context.moveTo(0, centerY);
    context.lineTo(canvas.width, centerY);
    context.stroke();
    context.beginPath();
    context.moveTo(centerX, 0);
    context.lineTo(centerX, canvas.height);
    context.stroke();

    // 1 KM circle
    context.strokeStyle = "lime";
    context.fillStyle = "lime";
    context.beginPath();
    context.arc(centerX, centerY, Math.floor(250 / max_radius), 0, 2 * Math.PI);
    context.fillText(`1`, 250 + Math.floor(250 / max_radius) + 30, centerX - 5);
    context.stroke();

    // let planeInfo = [[0.2, -0.3, 260,"1"],[-0.2, -0.6, 105,"2"]]

    let arrowImg = new Image();
    arrowImg.src = "flights/arrow.svg";

    arrowImg.onload = function () {
      for (let i = 0; i < planeInfo.length; i++) {
        planeArrow(arrowImg, centerX, context, planeInfo[i]);
      }
    }

  }, [max_radius, planeInfo]);

  return (
    <canvas id="radar" ref={canvasRef}></canvas>
  );
}

function planeArrow(arrowImg, centerX, context, planeInfo, arrowSize = 20) {

  // Save the current context state
  context.save();

  // Translate the context to the center of the arrow image
  const x = planeInfo[0] * centerX;
  const y = -planeInfo[1] * centerX;
  context.translate(centerX + x, centerX + y);

  // Rotate the context by the plane's heading
  context.rotate((planeInfo[2] * Math.PI) / 180);

  // Draw the arrow image on the canvas
  context.drawImage(arrowImg, -arrowSize / 2, -arrowSize / 2, arrowSize, arrowSize);

  // Restore the context state
  context.restore();

  // Draw the call sign text at the plane's position
  context.fillStyle = "red";
  context.font = "10px Arial";
  let textX = centerX + planeInfo[0] * centerX + arrowSize / 2;
  let textY = centerX + - planeInfo[1] * centerX + arrowSize / 2;
  context.fillText(planeInfo[3], textX, textY);
}

export default Radar;