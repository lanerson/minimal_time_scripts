import cProfile
import inspect
import os

def profile_decorator(func):
    def wrapper(*args, **kwargs):
        # Determinar o nome do script chamador
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        script_name = os.path.splitext(os.path.basename(caller_file))[0]
        prof_filename = f"{script_name}_profile.prof"
        
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        # Salvar as estatísticas de profiling em um arquivo binário
        profiler.dump_stats(prof_filename)
        
        return result
    return wrapper
    
