from wraprun import Wraprun


def main():

    mutations = ['e255k', 'e255v']
    drugs = ['nilotinib']
    num_replicas = 25
    root = '/lustre/atlas/scratch/farkaspall/chm126/inspire-data'
    task = "-n 1 serial esmacs --short --root {} --mutation {} --drug {} --replica {:02}"

    job = Wraprun()

    for mutation in mutations:
        for drug in drugs:
            for replica in range(num_replicas):
                job.add_task(task.format(root, mutation, drug, replica))

    job.launch()


if __name__ == '__main__':
    main()
