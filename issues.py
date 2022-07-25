# optimize Visualizer label text:
v = Visualizer(frame[:, :, ::-1], 
               metadata=metadata,
               scale=0.8,
               instance_mode=ColorMode.IMAGE_BW)
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
            
