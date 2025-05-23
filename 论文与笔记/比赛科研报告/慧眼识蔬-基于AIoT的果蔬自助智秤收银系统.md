# **第1章**      作品概述

传统的果蔬称重方式存在排队等候和人工操作繁重的问题。竞品如自动称重设备虽已存在，但多数依赖人工输入或缺乏自动识别功能。此项目通过果蔬自动识别和实时称重，提高了结算效率并减少人工干预，适用于超市、菜市场等零售场景，面向的用户为超市运营商和消费者。

为了解决这些问题，本研究设计了基于AIoT的果蔬拍照识别物联网电子秤系统，旨在提高超市和菜市场中果蔬称重和结账的效率。系统由拍照识别模块、传感器称重模块、数据存储模块和显示模块组成，通过实时拍照识别果蔬类型并计算总价，实现便捷的结账功能。技术上，系统使用了卷积神经网络（CNN）和Python编程语言，结合PyQt6界面设计和MySQL数据库存储数据，为超市提供了高效、智能的称重结算方案。

硬件方面，系统结合树莓派4、HX711 AD转换模块和USB摄像头，构成了称重和拍照识别模块，确保了系统的实时性和高效性。软件层面，通过PyTorch框架实现基于ResNet-18模型的果蔬识别，并使用OpenCV进行图像处理，结合UI设计用户交互界面，使得系统不仅高效、准确，而且用户友好。



# **第2章**      需求分析

## 2.1 用户体验

随着零售行业的快速发展，消费者对购物体验的要求越来越高，尤其是在超市和菜市场等高人流量的零售场所，传统的果蔬称重和结算方式已经无法满足现代消费者的需求。传统的称重方式通常需要消费者排队等候，称重员手动输入商品信息，这不仅效率低下，还容易出现人为错误，导致消费者体验不佳。此外，超市运营商也面临着人工成本高、操作繁琐等问题，亟需一种更加智能、高效的解决方案。

本项目的核心目标是通过自动化和智能化技术，提升果蔬称重和结算的效率，减少人工干预，优化用户体验。对于超市运营商而言，系统提供了一种自动化、高效的果蔬称重和结算解决方案，能够显著提升工作效率。称重员不再需要手动输入商品编码，系统通过摄像头自动识别果蔬种类，并结合称重模块实时计算价格，减少了人工操作的繁琐性和错误率。这不仅降低了人工成本，还提高了称重和结算的准确性，减少了因人为错误导致的损耗。

对于消费者而言，系统的自动化和智能化设计提供了更加便捷和快速的购物体验。消费者只需将果蔬放置在称重台上，系统会自动识别果蔬种类并计算价格，整个过程仅需几秒钟，大大减少了排队等候的时间。此外，系统还提供了直观的用户界面，消费者可以实时查看果蔬的种类、重量和价格信息，确保信息的透明性和准确性。这种高效、便捷的购物体验能够显著提升消费者的满意度，增强其对超市的忠诚度。

## 2.2 市场需求分析

随着零售行业的自动化和智能化趋势，越来越多的超市和菜市场开始引入智能称重和结算系统。传统的称重方式已经无法满足现代零售行业的需求，尤其是在高人流量的零售场所，人工操作的效率和准确性都面临巨大挑战。市场上虽然已经出现了一些自动称重设备，但大多数设备仍然依赖人工输入商品信息，缺乏自动识别功能，无法真正实现智能化。

本项目的果蔬自动识别与实时称重系统，通过结合物联网技术和深度学习技术，提供了一种全新的智能化解决方案。系统不仅能够自动识别果蔬种类，还能实时计算价格，减少人工干预，提高结算效率。这种智能化的称重和结算方式，能够显著提升超市和菜市场的运营效率，降低人工成本，同时为消费者提供更加便捷、快速的购物体验。

此外，随着无人零售和智能超市的兴起，自动化和智能化的称重系统将成为未来零售行业的重要发展方向。本系统的设计理念和技术架构，完全符合未来零售行业的发展趋势，具有广阔的市场前景。通过不断优化和扩展，系统还可以应用于更多的零售场景，如生鲜、日用品等，进一步推动零售行业的智能化升级。

## 2.3 主要功能

**果蔬信息识别**：使用摄像头从外部获取视频，结合 OpenCV 图像处理和机器视觉（基于ResNet-18的神经网络），能实现对蔬果实时自动识别出标签，并准确区分不同种类的蔬果。同时，通过模电转换和负载传感器结合的称重模块，可以实时读取当前物品的重量信息，并与果蔬种类匹配单价表并计算价格，实现对当前信息标签的补充。

**购物车管理与软件界面**：实现对物品的管理，操作者可以将当前识别出来的物品信息保存到购物车中，最后统一结算。程序可以根据当前购物车信息打印出来条形码和二维码，这两个可以作为本次交易的标识。同时，如果确定本次交易，本次记录也会上报给服务器数据库。

**数据存储与管理**：系统除了能够记录每笔交易的果蔬信息、价格和结算金额，为超市提供数据报告，帮助管理者进行库存管理，价格调整和市场分析，还能够自动化跟新货物单价。

在性能方面，果蔬识别率在测试集的识别准确率高达 95%，在实际操作中也有很高正确率，能够正确区分常见的三十多种果蔬。同时果蔬信息采集具有实时性，可以实时判断果蔬种类和重量到标签信息中。

# **第3章**      技术方案

## 3.1 硬件平台设计

### 3.1.1 硬件连接布局

<img src=C:\Users\Holme\Desktop\Raspberry-Pi-4-Model-B-interface2.jpg width=70%>

<center>图 1 树莓派接口</center>

以树莓派4B座位整个系统的核心控制单元，运行了 Python 程序来进行控制和反馈给用户。整个系统由树莓派4B、HX711 AD转换模块与形变称重传感器、USB摄像头以及显示器组成，以下是各个模块的硬件连接布局及其功能说明。

### 3.1.2 树莓派的环境配置与硬件操作

在本系统中，树莓派与HX711AD转换模块和摄像头配合使用，组成了高效的称重和拍照识别模块，能够实时监控并处理传感器数据及图像。系统通过连接USB摄像头实现了果蔬的实时图像捕捉，同时通过GPIO接口连接HX711模块，接收和处理来自称重传感器的数据。这种高度集成的硬件布局确保了系统能够迅速响应和实时处理数据，从而提高了果蔬识别的效率和精度。

树莓派4 Model B运行的是Raspberry Pi OS，这是基于Debian的操作系统，专为树莓派硬件优化。该操作系统为开发者提供了丰富的工具和库，支持Python、C++等多种编程语言，便于实现各种硬件交互和软件功能，可以轻松实现图像处理、深度学习模型训练与推理等功能。结合PyTorch框架和OpenCV库，树莓派4为该项目的图像识别和实时数据处理提供了强大的计算支持。

## 3.2 软件平台设计

### 3.2.1 基于 PyTorch 的识别模型与包装

基于PyTorch的识别模型采用卷积神经网络（CNN）实现了果蔬的自动识别。为提高识别精度，系统使用了ResNet-18这一预训练模型，并通过迁移学习对其进行微调，适应特定的果蔬识别任务。训练过程中，采用了数据增强和图像预处理技术，如调整图像尺寸和归一化，以提升模型的泛化能力。模型通过训练数据集学习不同果蔬的特征，并最终在测试集上进行验证，以确保其准确性。

在应用中，训练好的模型被部署到树莓派上，通过连接的USB摄像头实时捕捉图像，输入到模型中进行预测。预测结果会用于实时计算果蔬的价格，并进行结算。整个过程结合了深度学习与硬件平台的优势，实现了高效的果蔬识别与自动结算。

### 3.2.2 用户交互界面

1.主窗口

UI界面的主窗口负责展示视频流、管理购物车、显示物品信息和进行支付。它使用从摄像头捕获视频流，并实时显示在主窗口中。捕获的每一帧图像会传递给一个物体分类模型，该模型进行分类然后返回物体类别，也就是在视频和信息框内实时显示当前检测到的物品种类。信息框会显示当前的物品信息，包括物品种类，单价，质量和总价，用户可以选择添加当前物品到购物车，此物品信息会被打包添加到购物车表格中。用户可以在购物车中查看物品、删除物品，或者清空整个购物车。购物车总价格也会随时更新。

3.选择窗口

这个窗口是用来选择识别可能出错的商品，用户可以从下拉列表中选择物品标签，并输入物品的重量。系统会根据选择的标签和重量计算总价格，并显示在界面上。当用户确认时，选择的物品会被添加到购物车。选择标签和输入重量的功能通过信号与主窗口连接，主窗口会根据添加的物品更新购物车。

2.付款窗口

这是一个支付窗口，在收银界面点击支付按钮后，程序会根据购物车和状态生成条形码标签和付款二维码。信息供用户核对，可以选择取消返回购物车进行更改，也可以点击确定完成支付。



# **第4章**      方案实现

## 4.1 树莓派的环境配置与硬件操作

### 4.1.1 称重模块与 usb 摄像头模块

本系统采用树莓派4作为核心处理器，集成了称重模块和USB摄像头模块，旨在实现果蔬的自动化称重、识别与计价。

**称重模块部分：**该模块利用高精度的HX711 AD转换器与负载传感器，构建了一个实时称重系统。HX711模块负责将传感器采集的模拟信号转换为数字信号，并通过GPIO接口传输至树莓派。软件层面，我们采用Python编程，结合HX711库，实现了传感器数据的读取、解析与校准。为确保称重精度，系统在硬件连接和软件算法上进行了优化，并通过校准程序减少了环境因素对测量结果的影响。

**USB摄像头模块部分：**该模块通过USB接口连接高清摄像头，利用OpenCV库进行图像采集与处理。结合预训练的ResNet-18深度学习模型，系统能够实时识别摄像头捕捉的果蔬图像，并准确判断其品种。识别结果与预先建立的果蔬数据库进行比对，获取相应的价格信息。此外，系统还提供了实时视频流功能，为用户提供可视化的操作反馈。

**系统协同与性能：**为实现称重与识别的同步，系统设计了精细的数据交互机制。当称重模块检测到重量变化时，摄像头模块会同步捕捉图像，两个模块的数据在树莓派上进行实时处理，确保称重与识别结果的对应性。树莓派强大的计算能力保证了系统运行的实时性和稳定性，提高了整体的效率和用户体验。该系统通过称重模块和USB摄像头模块的有机结合，实现了果蔬的自动化称重、识别与计价功能。两个模块在硬件和软件层面都经过了精心设计和优化，确保了系统的精度、稳定性和实时性。

### 4.1.2 树莓派环境与运行模式

介于 Python 的运行环境，方便实现交叉开发的模式，所以采用其作为开发语言。而树莓派运行了 Raspberry Pi OS，这是一个 arm 系的 Linux 系统，方便进行 Python 开发。

项目的运行环境比较复杂，包含了大量第三方库，因此需要创建虚拟环境来运行本项目。我们采用了 Miniconda 作为 Anaconda 和 venv 环境的替代，来适应树莓派开发板系统资源较小的情况。首先在 Windows 中将第三方库全部显示并保存到 `requirements.txt` 中，再在树莓派系统中创建 Miniconda 环境并使用 `conda` 命令下载 `requirements.txt` 中的第三方库。

```bash
conda create --name <env_name>
pip install -r requirements.txt
```

## 4.2 用户交互操作

### 4.2.1 基于 PyTorch 框架的果蔬识别模型

为了实现果蔬的自动识别，本系统采用了基于卷积神经网络（CNN）的深度学习模型，具体使用了 PyTorch 框架来构建和训练模型。以下是实现该模型的详细过程。

1. 模型选择

在果蔬识别任务中，由于图像分类的需求，我们选择了**ResNet-18**作为基础模型。ResNet（Residual Network）是一种在深度学习中广泛应用的卷积神经网络，它通过残差学习（Residual Learning）有效解决了深度神经网络训练中的梯度消失问题，使得网络可以更加深层次且高效地学习。

ResNet-18是ResNet系列中参数较少的一个变种，它包含18层的神经网络结构，适用于对计算资源要求不高且数据量较小的任务。通过微调（fine-tuning）ResNet-18模型，我们可以快速适应果蔬识别任务。

2. 数据准备

为了训练模型，我们首先准备了果蔬图像数据集。数据集被分为训练集和测试集，并存储在本地文件夹中。每个果蔬品类的图片都被组织在不同的文件夹中，且每个文件夹命名为对应的果蔬类别名称。图片作为模型的输入，都通过预先定义的 transform 进行变化然后输入到模型中

```python
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(0, 1)
])
```

3. 模型设计与训练

使用PyTorch的`torchvision.models`模块，我们可以直接加载一个预训练的ResNet-18模型，并对其进行微调以适应我们的数据集。我们仅保留网络的前几层（特征提取部分），然后替换掉全连接层，使其输出类别数等于果蔬种类的数量。

模型的微调步骤如下：

- 使用预训练的ResNet-18模型作为初始化。
- 修改最后的全连接层，使其输出类别数等于果蔬数据集的类别数（在本项目中，假设为30种）。
- 设置合适的优化器和学习率，进行训练。

```python
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, num_classes)
model.to(device)
```

在训练过程中，采用交叉熵损失函数（`CrossEntropyLoss`）和Adam优化器（`torch.optim.Adam`）进行模型的训练和优化。

4. 模型评估与测试

训练完成后，模型会在测试集上进行评估。评估时，我们计算分类准确率（Accuracy）和损失函数值（Loss），以便评估模型在未知数据上的表现。

```
......

epoch20
100%| 98/98 [04:15<00:00,  2.61s/it]
training Accuracy: 98.6
100%| 12/12 [00:32<00:00,  2.68s/it]
Test Accuracy: 96.10%, Test Avg loss: 0.128465
```

5. 部署与应用

训练完成的模型可以导出为 `.pth` 格式，保存在树莓派上。当用户将果蔬放置在称重平台上时，系统通过连接的USB摄像头捕捉图像，并将图像输入到训练好的果蔬识别模型中。模型对输入图像进行预测，识别出物品的类别，并根据数据库中的价格信息进行实时结算。

```python
torch.save(model, 'fruit_vegetable_model.pth')
```

6. 总结

通过使用基于ResNet-18的深度学习模型，本系统能够较为准确地识别不同种类的果蔬，并实现自动结算。通过对PyTorch框架的高效使用，以及结合硬件平台的实时识别需求，系统能够实现较为流畅且精确的果蔬识别。

### 4.2.2 视频与图像边缘处理

在捕捉图像时进行边缘处理，它不仅增强了图像的可视化效果，还有效地提升了物体识别的精确度与鲁棒性。通过结合计算机视觉技术与深度学习模型，您能够实时捕捉摄像头视频流，并对每一帧图像进行处理，以便在视觉层面上突出物体的边缘特征。这一过程涉及到多个层次的图像处理技术，主要包括图像的预处理、边缘检测、目标分类和信息标注。

```python
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
class_idx = detection.classify_by_image(frame_rgb)
predicted_label = class_dict.class_names[class_idx]
```

通过边缘处理后的图像，深度学习模型能够更加精确地识别图像中的物体类别。物体的类别标签会被渲染到图像上，实时在视频帧上进行标注和显示，帮助用户直观了解识别结果。边缘信息的处理和物体分类的结合，提升了图像识别的精度与响应速度，使得系统不仅能够准确识别目标，还能快速反应于变化的环境。

```python
frame_tensor = transform(Image.fromarray(frame_rgb)).unsqueeze(0)
with torch.no_grad():
    output = model(frame_tensor)
    _, predicted = torch.max(output, 1)
class_idx = predicted.item()
```



### 4.2.3 用户交互界面

主窗口使用 `QMainWindow` 来组织应用的主要结构，包括菜单、工具栏、状态栏和中央区域。视频流的捕获与显示通过 OpenCV (`cv2.VideoCapture`) 完成，实时从摄像头捕捉图像，并将每一帧转换为适合显示的格式。视频流中的每一帧经过机器学习模型处理，识别出图像中的物体并标记其类别，随后使用 `QLabel` 将这些标注信息渲染到 UI 上。`QTimer` 被用来定时刷新显示，确保视频流在用户界面上能够平滑呈现。

```python
self.capture = cv2.VideoCapture(1)
self.timer = QTimer(self)
self.timer.timeout.connect(self.update_frame)
self.timer.start(int(1000 / CAP_FREQ)) # CAP_FREQ = 30
```

UI 控件之间的交互通过信号和槽机制来管理。如果遇到识别出其他相似物品时，用户可以选择点击选择按钮，弹出`SelectWindow` ，允许用户选择商品标签并输入重量。选择标签后，系统会计算价格并更新相应的界面元素，实时展示价格变化。用户输入重量后，程序会重新计算并显示总价格。所有这些界面变化都通过信号与主窗口进行交互，保证 UI 的动态更新与用户的操作同步。

在购物车的管理方面，`QTableWidget` 被用来展示购物车中的物品，用户可以通过操作界面添加、删除物品，或者清空购物车。每当有物品添加或移除时，界面会自动更新，总金额也会重新计算并显示在专门的标签上，所有的这些操作都通过内存中的 `item_list` 进行管理，确保数据与界面状态的一致性。

```python
def accept_information(self):
def remove_item_from_cart(self, cart_index):
```

支付对话框则通过展示二维码和条形码来进行支付相关操作。二维码和条形码的生成依赖于一个外部的 `payment_generator` 模块，该模块将购物车中的信息转化为支付所需的格式，并以图片的形式展示在 UI 上。用户可以选择接受或取消支付，选择接受支付后，支付成功的信号会传递给主窗口，进而清空购物车中的所有物品。

```python
def generate_qrcode(cart_items, total_price):
def generate_barcode(order_id):
```

所有这些功能都依赖于 PyQt6 提供的灵活布局和控件事件管理机制，使得 UI 的响应性和交互性得到了优化。通过适当的信号和槽连接，主窗口、选择窗口和支付窗口之间的逻辑流程紧密联系，共同实现了一个流畅且直观的用户体验。

# **第5章**      测试报告

## 5.1 功能测试

在测试之前，首先需要搭建测试环境。测试环境包括硬件和软件两部分：

- **硬件环境**：树莓派4B、HX711 AD转换模块、形变称重传感器、USB摄像头、显示器。
- **软件环境**：Raspberry Pi OS操作系统、Python 3.12、PyTorch框架、OpenCV库、PyQt6界面库、MySQL数据库。（所有第三方库已在项目根目录的 requirements.txt 中记录）

打开软件后，系统会自动启动主窗口，界面中显示当前摄像头的实时画面。摄像头模块将会调用当前主机连接的摄像设备（如内置或外接摄像头），并将捕捉到的视频流实时展示在软件界面上。视频画面上方或旁边会实时显示模型对物品的自动识别标签，表明当前摄像头捕捉到的物品信息。这些标签是通过训练好的深度学习模型进行物品识别并判断得出的。

<img src="C:\Users\Holme\Pictures\Screenshots\Screenshot 2025-02-27 135508.png" width=60%>

<center>图 2 主界面</center>

在某些情况下，自动识别的标签可能不完全准确，或者操作员希望手动更正物品标签。用户可以直接在界面中看到自动生成的标签信息。如果发现识别错误，操作者可以通过输入框手动输入正确的标签信息，确保商品被正确地添加到购物车中。同时，软件会实时更新购物车状态，显示已经添加的商品以及当前购物车中的物品总数和合计金额。

<img src="C:\Users\Holme\Pictures\Screenshots\Screenshot 2025-02-27 135401.png" width=40%>

<center>图 3 手动输入</center>

当购物完成，用户可以点击“确认交易”按钮，系统会自动读取当前购物车中的所有物品信息。随后，软件会生成相应的二维码和条形码，用户可以选择将这些信息通过打印或显示在手机屏幕上用于后续支付和结算。二维码和条形码会包含购物车的详细信息，确保支付过程的顺利进行，同时方便结账人员快速扫描。

<img src="C:\Users\Holme\Pictures\Screenshots\Screenshot 2025-02-27 135537.png" width=60%>

<center>图 4 支付信息</center>

## 5.2优化与更新

尽管系统已经实现了核心功能，并且在测试中表现良好，但在实际应用中仍存在一些可以进一步优化的地方。以下是针对系统当前存在的不足提出的优化建议和未来更新方向：

### 5.2.1 模型识别优化

1. **增加训练数据量**：当前模型的训练数据集每类果蔬仅有约100张图片，这可能导致模型在实际场景中的识别准确率不如测试集（测试集准确率为96%）。为了提高模型的泛化能力，建议增加每类果蔬的训练图片数量，尤其是现实场景中的多样化图片。通过数据增强技术（如旋转、缩放、色彩变换等），进一步丰富训练数据，帮助模型更好地适应不同的光照、角度和背景条件。
2. **多标签输出**：当前系统在模型识别时，仅输出概率最高的果蔬类别。然而，在实际应用中，模型可能会遇到难以区分的相似果蔬（如不同品种的苹果或梨）。为了减少人工干预的频率，建议将模型输出的前几名概率结果都显示在界面上，供用户选择。例如，当模型无法确定某果蔬的具体种类时，可以在界面上显示“可能是苹果、梨或桃子”，用户可以根据实际情况选择正确的标签。
3. **模型迁移学习与扩展**：当前系统使用的是ResNet-18模型，未来可以尝试使用更复杂的模型（如ResNet-34或ResNet-50）来提高识别精度。通过迁移学习，将模型应用于更多种类的果蔬或其他商品（如生鲜、日用品等），进一步扩展系统的应用场景。

### 5.2.2 用户交互优化

1. **界面友好性提升**：当前系统的用户界面已经具备基本功能，但在用户体验方面仍有提升空间。例如，可以增加更多的视觉提示和操作引导，帮助用户更快上手。在识别结果不明确时，界面可以自动弹出提示框，建议用户重新放置果蔬或调整摄像头角度。
2. **语音提示功能**：为了进一步提升用户体验，可以考虑增加语音提示功能。当系统完成果蔬识别或称重后，通过语音播报果蔬名称、重量和价格，方便用户核对信息。语音提示功能尤其适用于嘈杂环境（如菜市场），能够减少用户对屏幕的依赖。



# **第6章**      应用前景

随着人工智能（AI）、物联网（IoT）和大数据技术的迅猛发展，零售行业正经历深刻的变革。“慧眼识蔬——基于AIoT的果蔬自助智秤系统”作为一款创新的物联网应用，展现出广阔的应用前景。

在传统零售场景中，果蔬称重和结算过程效率低下且繁琐，尤其在高峰时段，消费者需长时间排队等候，严重影响购物体验。本系统通过集成先进的AI识别技术和物联网设备，实现了果蔬的快速识别、称重和结算，显著提升零售运营效率，减少人工操作，降低人力成本，同时为消费者提供无缝的购物体验，增强消费者满意度和忠诚度。

此外，该系统高度自动化，完美契合无人零售和智能超市的发展需求，支持条形码或二维码打印，可与现有无人零售系统无缝对接，为智能超市建设提供有力技术支持。系统还具备数据存储和管理功能，可实时记录商品、价格和结算信息，生成数据报告，助力零售管理者优化库存、调整价格策略、预测市场需求，实现精细化管理，提升企业竞争力。其绿色环保特性减少了纸质标签依赖，降低资源消耗和碳排放，符合可持续发展理念。

系统的核心技术——卷积神经网络（CNN）和物联网（IoT）——具有广泛的适用性和可扩展性，不仅适用于果蔬称重，还可拓展至其他零售商品的自动识别和管理，如生鲜、日用品等，并能轻松集成智能货架、智能推荐系统等模块，为零售行业的数字化转型提供强大支持。

在全球零售行业智能化、自动化的发展趋势下，本系统具备国际化市场潜力，其高效识别能力和便捷结算流程能满足不同国家和地区的需求，有望在全球范围内推广，为国际零售企业提供智能化解决方案，推动全球零售行业的数字化升级。

综上所述，“慧眼识蔬”系统不仅在当前零售市场具有显著应用价值，更为零售行业的未来发展提供了创新思路和技术支持，有望成为零售行业智能化升级的重要标志，引领行业迈向高效、便捷、智能的未来。

# 参考文献

1. Raspberry Pi Foundation. (2022). **Raspberry Pi 4 Model B**. Retrieved from https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
2. PyTorch Team. (2023). **PyTorch Documentation**. Retrieved from https://pytorch.org/docs/stable/
3. OpenCV Documentation. (2023). **OpenCV-Python Tutorials**. Retrieved from https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
4. Kaggle. (2023). **Fruits 360 Dataset**. Retrieved from https://www.kaggle.com/datasets/masoudnickparvar/fruits-360
5. Kaggle. (2023). **Fruit and Vegetable Classification**. Retrieved from https://www.kaggle.com/datasets/awanchad/fruit-vegetable-dataset

