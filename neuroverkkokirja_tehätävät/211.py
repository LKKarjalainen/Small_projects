import matplotlib.pyplot as plt
import sklearn.datasets as skd
import sklearn.model_selection as skms
import torch
import random

class Model0(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = torch.nn.Linear(2, 1)
        
    def forward(self, x):
        return self.layer_1(x)

def accuracy(y_pred, y_true):
    correct = 0
    for i in range(len(y_pred)):
        if torch.eq(y_pred[i], y_true[i]):
            correct += 1
    # print(correct, len(y_pred))
    acc = (correct / len(y_pred)) * 100
    return acc

# Random data for testing purposes using rand.
def random_data():
    coords = []
    for i in range(10000):
        x = random.uniform(0.0, 10.0)
        y = random.uniform(0.0, 10.0)
        coords.append((x, y))
    return coords

def plot_data(model, X_train, y_train, X_test, y_test):
    import requests
    from pathlib import Path
    
    if Path("helper_functions.py").is_file():
        print("helper_functions.py already exists, skipping download")
    else:
        print("Downloading helper_functions.py")
        request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
        with open("helper_functions.py", "wb") as f:
            f.write(request.content)

    from helper_functions import plot_predictions, plot_decision_boundary
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Train")
    plot_decision_boundary(model, X_train, y_train)
    plt.subplot(1, 2, 2)
    plt.title("Test")
    plot_decision_boundary(model, X_test, y_test)
    plt.show()
    

def train(model, X_train, y_train, X_test, y_test, device):
    model = model.to(device)
    X_train = X_train.to(device)
    y_train = y_train.to(device)
    X_test = X_test.to(device)
    y_test = y_test.to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    loss_fn = torch.nn.BCEWithLogitsLoss()
    
    for epoch in range(100):
        model.train()
        y_logits = model(X_train).squeeze()
        y_pred = torch.round(torch.sigmoid(y_logits))
        loss = loss_fn(y_logits, y_train.float())
        acc = accuracy(y_pred, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        model.eval()
        with torch.inference_mode():
            test_logits = model(X_test).squeeze()
            test_pred = torch.round(torch.sigmoid(test_logits))
            test_loss = loss_fn(test_logits, y_test.float())
            test_acc = accuracy(test_pred, y_test)
            
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Train Loss: {loss:.2f}, Train Acc: {acc:.2f}%, Test Loss: {test_loss:.2f}, Test Acc: {test_acc:.2f}%")           

# Crude if else to find the most general hypothesis
def find_s_if(coords_and_classes):
    min_x = 11
    min_y = 11
    max_x = -1
    max_y = -1
    for coord in coords_and_classes:
        if coord[1] == 1:
            if coord[0][0] < min_x:
                min_x = coord[0][0]
            if coord[0][1] < min_y:
                min_y = coord[0][1]
            if coord[0][0] > max_x:
                max_x = coord[0][0]
            if coord[0][1] > max_y:
                max_y = coord[0][1]
    print("Most general hypothesis: x >= " + str(min_x) + ", y >= " + str(min_y) + ", x <= " + str(max_x) + ", y <= " + str(max_y))

# Neural network to find the most general hypothesis
def find_s_neuralnetwork(coords, classes):
    
    # Create torch tensors from data and split into train and test data
    X = torch.tensor(coords)
    Y = torch.tensor(classes)
    print(X[:5], Y[:5])
    X_train, X_test, y_train, y_test = skms.train_test_split(X, 
                                                    Y, 
                                                    test_size=0.4,
                                                    random_state=42)
    print(len(X_train), len(X_test), len(y_train), len(y_test))
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Using {} device".format(device))

    X_train, y_train = X_train.to(device), y_train.to(device)
    X_test, y_test = X_test.to(device), y_test.to(device)
    
    model = Model0().to(device)
    print(model)

    untrained_preds = model(X_test)
    print(f"Length of predictions: {len(untrained_preds)}, Shape: {untrained_preds.shape}")
    print(f"Length of test samples: {len(y_test)}, Shape: {y_test.shape}")
    print(f"\nFirst 10 predictions:\n{untrained_preds[:10]}")
    print(f"\nFirst 10 test labels:\n{y_test[:10]}")
    
    
    # Get predictions classes.
    y_pred_probs = torch.sigmoid(untrained_preds)
    print(y_pred_probs[:5], y_train[:5])
    y_pred = torch.round(y_pred_probs)
    print(y_pred[:5], y_train[:5])
    
    # get accuracy before training
    acc = accuracy(y_pred, y_test)
    print(f"Accuracy before training: {acc:.2f}%")
    
    train(model, X_train, y_train, X_test, y_test, device)
    plot_data(model, X_train, y_train, X_test, y_test)
    

def classify_test_data(coords):
    classes = []
    for coord in coords:
        if coord[0] >= 3 and coord[1] >= 3 and coord[0] <= 7 and coord[1] <= 7:
            classes.append(1)
        else:
            classes.append(0)
    return classes


if __name__ == "__main__":
    print(torch.version.cuda)
    print(torch.__version__)
    coords = random_data()
    # test_data = random_data()
    classes = classify_test_data(coords)
    #print(coords)
    #print(classes)
    #print(sum(classes))
    # print(sum(classes)/len(classes))
    coords_and_classes = []
    for i in range(len(coords)):
        coords_and_classes.append((coords[i], classes[i]))
    # print(coords_and_classes)
    x = [coords_and_classes[i][0][0] for i in range(len(coords_and_classes))]
    y = [coords_and_classes[i][0][1] for i in range(len(coords_and_classes))]
    plt.scatter(x=x, y=y, c=[coords_and_classes[i][1] for i in range(len(coords_and_classes))])
    # plt.show()
    # find_s_if(coords_and_classes)
    
    # Create torch tensors from data and split into train and test data
    X = torch.tensor(coords)
    Y = torch.tensor(classes)
    print(X[:5], Y[:5])
    X_train, X_test, y_train, y_test = skms.train_test_split(X, 
                                                    Y, 
                                                    test_size=0.4, # 20% test, 80% train
                                                    random_state=42)
    print(len(X_train), len(X_test), len(y_train), len(y_test))
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Using {} device".format(device))
    
    find_s_neuralnetwork(coords, classes)