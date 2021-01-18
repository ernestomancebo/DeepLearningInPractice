import matplotlib.pyplot as plt


def plot_trainig_results(train_history):
    # Train Accuracy
    acc = train_history.history['acc']
    val_acc = train_history.history['val_acc']

    # Validation Accuracy
    loss = train_history.history['loss']
    val_loss = train_history.history['val_loss']

    # Self explanatory
    epochs = range(1, len(acc) + 1)

    # this is the Accuracy metric
    plt.plot(epochs, acc, 'bo', label='Training Acc.')
    plt.plot(epochs, val_acc, 'b', label='Validation Acc.')
    plt.title('Training and Validation Accuracy')

    plt.legend()
    plt.figure()

    # this is the Loss function metric
    plt.plot(epochs, loss, 'bo', label='Training Loss')
    plt.plot(epochs, val_loss, 'b', label='Validation Loss')
    plt.title('Training and Validation Loss')

    plt.legend()
    plt.show()
