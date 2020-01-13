def generate(label):
    (
        bbox_xmin,
        bbox_ymin,
        bbox_xmax,
        bbox_ymax,
        img_width,
        img_height
    ) = (
        label.get('xmin'),
        label.get('ymin'),
        label.get('xmax'),
        label.get('ymax'),
        label.get('img_width'),
        label.get('img_height')
    )
    dw = 1. / img_width
    dh = 1. / img_height
    x = (bbox_xmin + bbox_xmax) / 2.0
    y = (bbox_ymin + bbox_ymax) / 2.0
    w = bbox_xmax - bbox_xmin
    h = bbox_ymax - bbox_ymin
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
