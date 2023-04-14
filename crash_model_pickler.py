import pickle
from detection import AccidentDetectionModel

mod=AccidentDetectionModel("model_crash.json", 'model_weights.h5')
pickle.dump(mod, open('crash_model.pkl','wb'))
