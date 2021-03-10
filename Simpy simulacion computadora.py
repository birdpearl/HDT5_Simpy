import simpy
def compu(env, task, system):
    # arrives at the system
    arrival_time = env.now

    with system.ram.request() as request:
        yield request
        yield env.process(system.getSpace(task))

    with system.procesor.request() as request:
        yield request
        yield env.process(system.funish(task))

    if random.choice([0, 1]):
        with system.decide.request() as request:
            yield request
            yield env.process(system.enviarA(task))

    # task is processed in procesor
    wait_times.append(env.now - arrival_time)
    
env = simpy.Environment()
env.run()