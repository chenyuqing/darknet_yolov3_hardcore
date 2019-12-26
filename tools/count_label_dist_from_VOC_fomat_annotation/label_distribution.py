# 解析标注的xml文件，并且统计label的分布情况
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os

class labelDistribution(object):
    def __init__(self, xml_path, label_file):
        self.xml_path = xml_path
        self.label_file = label_file

    # 获取label的名称列表
    def get_labels(self):
        lf = open(self.label_file)
        return [n.strip('\n') for n in lf]
        # for i, n in enumerate(lf):
        #     print('class {} : {}'.format(i, n))

    # 解析xml的文件地址
    def xml_path_parse(self):
        in_files = [os.path.join(self.xml_path, n) for n in os.listdir(self.xml_path)]
        # for i, infile in enumerate(in_files):
        #     print('xml path {}: {}'.format(i, infile))
        return in_files

    # 统计xml文件中的label的数量
    def convert_annotation(self):
        labels = self.get_labels()
        in_files = self.xml_path_parse()

        count_labels_res = {}
        for l in labels:
            count_labels_res[l] = 0

        for i, infile in enumerate(in_files):
            in_file = open(infile)
            tree = ET.parse(in_file)
            root = tree.getroot()

            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in labels:
                    continue
                count_labels_res[cls] += 1

        return count_labels_res

    # 画柱状图
    def plot_bar(self):
        res = self.convert_annotation()
        name = []
        num = []
        for k, v in res.items():
            name.append(k)
            num.append(v)

        plt.bar(name, num, color='rgby')
        plt.xlabel('label distribution')
        plt.ylabel('count of labels')
        plt.title('Test')

        for a, b in zip(name, num):
            plt.text(a, b,  '%.0f' % b, ha='center', va='bottom', fontsize=11)

        plt.savefig("./label_dist.png")
        plt.show()


if __name__ == '__main__':
    xml_path = './xml'
    label_file = './classes.names'

    print('start ....')
    ld = labelDistribution(xml_path, label_file)
    # ld.xml_path_parse()
    res = ld.convert_annotation()
    # print('type : {}'.format(type(res)))
    for k, v in res.items():
        print('labels : {}, count : {}'.format(k, v))

    ld.plot_bar()
