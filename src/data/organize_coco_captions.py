import json

if __name__ == '__main__':
    ann_path = '/Users/gillevi/Projects/unsup_clip/data/mscoco/annotations/captions_train2014.json'
    im_path = '/Users/gillevi/Projects/unsup_clip/data/mscoco/train2014'

    with open(ann_path) as f:
        ann = json.load(f)

    sorted_ann = sorted(ann['annotations'], key=lambda a: a['image_id'])
    im_predix = '/Users/gillevi/Projects/unsup_clip/data/mscoco/train2014/COCO_train2014_{:012d}.jpg'
    with open('/Users/gillevi/Projects/unsup_clip/data/mscoco/annotations/captions_train2014_sorted.txt', 'w+') as f:
        for a in sorted_ann[::5]:
            f.write(f'{im_predix.format(a["image_id"])}\t{a["caption"]}\n')

    gil = 1

