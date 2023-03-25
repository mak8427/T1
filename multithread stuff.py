import itertools
import concurrent.futures
import threading
import concurrent.futures
import threading


def buy_product_for_agents_chunk(agents_chunk, product_list):
    out_of_market = 0
    for agent in agents_chunk:
        out_of_market += buy_product_for_agent(agent, product_list)
    return out_of_market

def buy_product_multiprocessed(agent_list, product_list, num_threads=10):
    out_of_market = 0

    chunk_size = len(agent_list) // num_threads
    agent_chunks = [agent_list[i * chunk_size:(i + 1) * chunk_size] for i in range(num_threads)]

    # If agent_list length is not divisible by num_threads, add the remaining agents to the last chunk
    agent_chunks[-1].extend(agent_list[num_threads * chunk_size:])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(buy_product_for_agents_chunk, chunk, product_list) for chunk in agent_chunks]
        out_of_market_values = [future.result() for future in futures]

    for agent in agent_list:
        if agent.agent_10y_history[-1] != -1:
            product_list[agent.agent_10y_history[-1]].number_sold += 1

    out_of_market = sum(out_of_market_values)
    return out_of_market