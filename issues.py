# optimize Visualizer label text:
v = Visualizer(frame[:, :, ::-1], 
               metadata=metadata,
               scale=0.8,
               instance_mode=ColorMode.IMAGE_BW)

## show instance prediction
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))

## show bbox and add text
for box in outputs["instances"].pred_boxes.to('cpu'):
    v.draw_box(box)
    v.draw_text(str(box[:2].numpy()), tuple(box[:2].numpy()))
    
## show mask
for mask in outputs["instances"].pred_masks.to('cpu'):
  v.draw_soft_mask(mask, alpha = 0.3, color = 'r')
  
v = v.get_output()
img =  v.get_image()[:, :, ::-1]
cv2_imshow(img)

