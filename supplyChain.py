class SupplyChainEntity:
    def __init__(self, name, available_resources):
        self.name = name
        self.available_resources = available_resources

    def negotiate(self, other_entity, requested_resources):
        self_ratio = self.calculate_ratio(requested_resources)
        other_ratio = other_entity.calculate_ratio(requested_resources)

        self_allocation = self.calculate_allocation(self_ratio, requested_resources)
        other_allocation = other_entity.calculate_allocation(other_ratio, requested_resources)

        return self_allocation, other_allocation

    def calculate_ratio(self, requested_resources):
        total_available = sum(self.available_resources)
        return [resource / total_available for resource in requested_resources]

    def calculate_allocation(self, ratio, requested_resources):
        return [ratio[i] * requested_resources[i] for i in range(len(requested_resources))]

def simulate_supply_chain(entity1, entity2, requested_resources):
    allocation1, allocation2 = entity1.negotiate(entity2, requested_resources)

    print(f"{entity1.name} allocation: {allocation1}")
    print(f"{entity2.name} allocation: {allocation2}")

# Example Usage
entityA = SupplyChainEntity("EntityA", [100, 150, 200])
entityB = SupplyChainEntity("EntityB", [120, 180, 150])

requested_resources = [30, 40, 50]

simulate_supply_chain(entityA, entityB, requested_resources)
