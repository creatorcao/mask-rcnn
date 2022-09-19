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

###################
  (transform): GeneralizedRCNNTransform(
      Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
      Resize(min_size=(800,), max_size=1333, mode='bilinear')
  )
###################
  (rpn): RegionProposalNetwork(
    (anchor_generator): AnchorGenerator()
    (head): RPNHead(
      (conv): Sequential(
        (0): Conv2dNormActivation(
          (0): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (1): ReLU(inplace=True)
        )
      )
      (cls_logits): Conv2d(256, 3, kernel_size=(1, 1), stride=(1, 1))
      (bbox_pred): Conv2d(256, 12, kernel_size=(1, 1), stride=(1, 1))
    )
  )
  (roi_heads): RoIHeads(
    (box_roi_pool): MultiScaleRoIAlign(featmap_names=['0', '1', '2', '3'], output_size=(7, 7), sampling_ratio=2)
    (box_head): TwoMLPHead(
      (fc6): Linear(in_features=12544, out_features=1024, bias=True)
      (fc7): Linear(in_features=1024, out_features=1024, bias=True)
    )
    (box_predictor): FastRCNNPredictor(
      (cls_score): Linear(in_features=1024, out_features=91, bias=True)
      (bbox_pred): Linear(in_features=1024, out_features=364, bias=True)
    )
  )
)
